import requests
import orjson

from typing import Any, Dict, Optional
from config import ACCESS_TOKEN, BLOG_NAME, DISCORD_WEBHOOK_URL

API_URL = "https://www.tistory.com/apis"

common_params = {"access_token": ACCESS_TOKEN, "output": "json", "blogName": BLOG_NAME}


def get_blog_info() -> Dict[str, Any]:
    res = requests.get(
        f"{API_URL}/category/list?",
        params={**common_params},
    )
    return orjson.loads(res.text)["tistory"]["item"]


def get_post_list(page: Optional[int] = 1) -> Dict[str, Any]:
    res = requests.get(
        f"{API_URL}/post/list?",
        params={"page": page, **common_params},
    )
    return orjson.loads(res.text)


def get_post_read(post_id: str):
    res = requests.get(
        f"{API_URL}/post/read?",
        params={"postId": post_id, **common_params},
    )
    return orjson.loads(res.text)


def post_write(
    title: str,
    content: str,
    tag: Optional[str] = None,
    slogan: Optional[str] = None,
    password: Optional[str] = None,
    published: Optional[int] = None,
    visibility: Optional[int] = 3,
    category_id: Optional[int] = 0,
    accept_comment: Optional[int] = 1,
) -> Dict[str, Any]:
    option_params = _check_options(
        tag,
        slogan,
        password,
        published,
        visibility,
        category_id,
        accept_comment,
    )
    res = requests.post(
        f"{API_URL}/post/write?",
        params={
            "title": title,
            "content": content,
            **option_params,
            **common_params,
        },
    )
    return orjson.loads(res.text)


def post_modify(
    post_id: str,
    title: str,
    content: str,
    tag: Optional[str] = None,
    slogan: Optional[str] = None,
    password: Optional[str] = None,
    published: Optional[int] = None,
    visibility: Optional[int] = 3,
    category_id: Optional[int] = 0,
    accept_comment: Optional[int] = 1,
) -> Dict[str, Any]:
    option_params = _check_options(
        tag,
        slogan,
        password,
        published,
        visibility,
        category_id,
        accept_comment,
    )
    res = requests.post(
        f"{API_URL}/post/modify?",
        params={
            "postId": post_id,
            "title": title,
            "content": content,
            **option_params,
            **common_params,
        },
    )
    return orjson.loads(res.text)


def _check_options(
    tag: Optional[str],
    slogan: Optional[str],
    password: Optional[str],
    published: Optional[int],
    visibility: Optional[int],
    category_id: Optional[int],
    accept_comment: Optional[int],
):
    option_params = {}
    if tag:  # ??????(',' ??? ??????)
        option_params.update({"tag": tag})
    if slogan:  # ?????? ??????
        option_params.update({"slogan": slogan})
    if password:  # ????????? ????????????
        option_params.update({"password": password})
    if published:  # ????????????(TIMESTAMP ?????? ????????? ????????? ?????? ?????? ??????. ?????????: ????????????)
        option_params.update({"published": published})
    if visibility:  # ????????????(0: ????????? - ?????????, 1: ??????, 3: ??????)
        option_params.update({"visibility": visibility})
    if category_id:  # ???????????? ?????????(?????????: 0)
        option_params.update({"category": category_id})
    if accept_comment:  # ?????? ??????(0, 1 - ?????????)
        option_params.update({"acceptComment": accept_comment})
    return option_params


def send_message_to_discord(message: Dict[str, Any]) -> None:
    if DISCORD_WEBHOOK_URL:
        requests.post(DISCORD_WEBHOOK_URL, data=message)
    else:
        print(f"??????????????? ???????????? ????????? ???????????????.\n'DISCORD_WEBHOOK_URL'??? ??????????????????.")
