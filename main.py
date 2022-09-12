import api
import markdown
import os
from alert import Alert, DiscordAlert

from typing import Any, Dict, Tuple
from bs4 import BeautifulSoup


def run(alert: Alert) -> None:
    title = _get_target_title()
    visibility = _get_visibility()
    category_id, category_name = _get_category()
    html = _convert_md_to_html(title)
    tag = _extract_tag(html)

    result = api.post_write(
        title=title,
        content=str(html),
        tag=tag,
        visibility=visibility,
        category_id=category_id,
    )
    if result.get("tistory") is None:
        raise ValueError("Upload failed.")

    _update_directory(category_name)

    alert.send_message(result)


def _get_target_title() -> str:
    # TODO: 추후 복수의 파일도 업로드할 수 있도록 변경예정
    file_arr = os.listdir("upload/.")

    if len(file_arr) > 1:
        raise ValueError("하나의 글만 업로드할 수 있습니다.")

    title = file_arr.pop().rstrip(".md")
    return title


def _get_visibility() -> str:
    visibility = input("공개여부 옵션을 입력해주세요. [0: 비공개, 2: 공개] \n>>> ")
    if visibility not in ["0", "2"]:
        raise ValueError("잘못된 공개여부 옵션입니다.")


def _get_category() -> Tuple[str, str]:
    info = api.get_blog_info()
    categories = sorted(
        (
            (category["id"], category["name"], category["parent"])
            for category in info["categories"]
            if category["parent"] != ""
        ),
        key=lambda x: x[2],
    )
    for i, category in enumerate(categories):
        print(f"{i + 1}: {category[1]}")

    category_input = input("카테고리 번호를 입력해주세요. \n>>> ")
    if not category_input.isdigit():
        raise ValueError("카테고리 번호는 숫자입니다.")

    category_index = int(category_input) - 1
    if int(category_index) >= len(categories):
        raise ValueError("없는 카테고리 번호입니다.")

    targer_category = categories[category_index]
    category_id, category_name = targer_category[0], targer_category[1]

    return category_id, category_name


def _convert_md_to_html(title: str) -> Dict[str, Any]:
    with open(f"upload/{title}.md", "r") as f:
        text = f.read()
        html = markdown.markdown(text, extensions=["fenced_code"])
        return BeautifulSoup(html, "html.parser")


def _extract_tag(html: str) -> str:
    head_tag = [h1.text for h1 in html.find_all("h1")]
    tail_tag = [html.tag.extract().text] if html.tag else []
    tag = ",".join(head_tag + tail_tag)
    return tag


def _update_directory(category_name: str) -> None:
    path = f"/category/{category_name}"
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == "__main__":
    run(DiscordAlert())
