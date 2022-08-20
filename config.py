from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")  # TODO: 추후 자동업데이트 필요
BLOG_NAME = "daco2020"
API_URL = "https://www.tistory.com/apis"
