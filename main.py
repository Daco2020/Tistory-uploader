from typing import Any, Dict
import api
import markdown


def run() -> None:
    title = copy_target_article()
    html = get_article_html()
    result = api.post_write(title=title, content=html)
    send_message(result)


def copy_target_article() -> str:
    """
    새로 추가된 md파일을 target.md로 복사하고 title 정보를 가져옵니다.
    (구현중입니다)
    """
    ...
    title = "TEST"
    return title


def get_article_html() -> Dict[str, Any]:
    """
    md 파일을 html 형식으로 바꾸어 반환합니다.
    """
    with open("target.md", "r") as f:
        text = f.read()
        return markdown.markdown(text, extensions=["fenced_code"])


def send_message(result: Dict[str, Any]) -> None:
    """
    개인 메신저로 업로드 결과를 보내줍니다.
    (추후 구현 예정입니다)
    """
    print(result)
    ...


if __name__ == "__main__":
    run()
