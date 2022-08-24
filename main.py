import api
import markdown
import os

from typing import Any, Dict
from bs4 import BeautifulSoup


def run() -> None:
    title = _get_target_title()
    html = _convert_md_to_html(title)
    tag = _extract_tag(html)
    result = api.post_write(title=title, content=str(html), tag=tag, visibility=0)
    send_message(result)


def _get_target_title() -> str:
    # TODO: 추후 복수의 파일도 업로드할 수 있도록 변경예정
    file_arr = os.listdir("upload/.")
    if len(file_arr) > 1:
        raise ValueError("There must be only one upload article")
    title = file_arr.pop().split(".")[0]
    return title


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


def send_message(result: Dict[str, Any]) -> None:
    """
    개인 메신저로 업로드 결과를 보내줍니다.
    (추후 구현 예정입니다)
    """
    print(result)
    ...


if __name__ == "__main__":
    run()
