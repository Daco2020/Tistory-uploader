import datetime
from typing import Any, Dict
import api
from abc import ABC, abstractmethod


class Alert(ABC):
    def init(self):
        self._now = datetime.datetime.now()

    @abstractmethod
    def send_message(self, result: Dict[str, Any]) -> None:
        ...


class DiscordAlert(Alert):
    def send_message(self, result: Dict[str, Any]) -> None:
        message = {
            "content": f"시간 : {self.now.strftime('%Y-%m-%d %H:%M:%S')} \n결과 : {result['tistory'].get('url')}"
        }
        api.send_message_to_discord(message)
