import json
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv()


def get_telegram_base_uri() -> str:
    return f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}"


def get_telegram_file_uri() -> str:
    return f"https://api.telegram.org/file/bot{os.getenv('TELEGRAM_TOKEN')}"


def make_request(method: str, **kwargs) -> dict:
    json_data = json.dumps(kwargs).encode('utf-8')

    request = urllib.request.Request(
        method='POST',
        url=f"{get_telegram_base_uri()}/{method}",
        data=json_data,
        headers={
            'Content-Type': 'application/json',
        },
    )

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode('utf-8')
        response_json = json.loads(response_body)
        assert response_json["ok"] == True
        return response_json["result"]

def get_updates(**kwargs) -> dict:
    return make_request("getUpdates", **kwargs)

def send_message(chat_id: int, text: str, **kwargs) -> dict:
    return make_request("sendMessage", chat_id=chat_id, text=text, **kwargs)

def get_file(file_id: str) -> dict:
    return make_request("getFile", file_id=file_id)

def sendPhoto(chat_id: int, photo: str, **kwargs) -> dict:
    return make_request("sendPhoto", chat_id=chat_id, photo=photo, **kwargs)

def answer_callback_query(callback_query_id: str, **kwargs) -> dict:
    return make_request("answerCallbackQuery", callback_query_id=callback_query_id, **kwargs)

def delete_message(chat_id: int, message_id: int) -> dict:
    return make_request("deleteMessage", chat_id=chat_id, message_id=message_id)