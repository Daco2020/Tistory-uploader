from typing import Any, Dict, Optional
import requests
import orjson

from config import ACCESS_TOKEN, BLOG_NAME, API_URL


common_params = {"access_token": ACCESS_TOKEN, "output": "json"}


def get_blog_info() -> Dict[str, Any]:
    res = requests.get(
        f"{API_URL}/blog/info?",
        params=common_params,
    )
    return orjson.loads(res.text)


def get_post_list(page: Optional[int] = 1) -> Dict[str, Any]:
    res = requests.get(
        f"{API_URL}/post/list?",
        params={"blogName": BLOG_NAME, "page": page, **common_params},
    )
    return orjson.loads(res.text)


def get_post_read(post_id: str):
    res = requests.get(
        f"{API_URL}/post/read?",
        params={"blogName": BLOG_NAME, "postID": post_id, **common_params},
    )
    return orjson.loads(res.text)
