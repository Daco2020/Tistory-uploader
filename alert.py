import datetime
from typing import Any, Dict
import api
from abc import ABC, abstractmethod


class Alert(ABC):
    @abstractmethod
    def send_message(self, result: Dict[str, Any]) -> None:
        ...


class DiscordAlert(Alert):
    def send_message(self, result: Dict[str, Any]) -> None:
        now = datetime.datetime.now()
        message = {
            "content": f"시간 : {now.strftime('%Y-%m-%d %H:%M:%S')} \n결과 : {result['tistory'].get('url')}"
        }
        api.send_message_to_discord(message)
