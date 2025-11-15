import time
import os
import re
import requests
import pyperclip
import threading
import pyautogui
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

last_trade_nick = None
BOT_TOKEN = 'YOUR BOT TOKEN' # https://t.me/BotFather
CHAT_ID = 'YOUR CHAT ID' # https://t.me/getmyid_bot
LOG_FILE_PATH = r"PATH TO YOUR CLIENT FILE" 

def send_trade_notification_with_buttons(text, nick):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    message = f"@{nick} {text}"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "Minute", "callback_data": "minute"}],
                [{"text": "Away", "callback_data": "away"}]
            ]
        }
    }
    requests.post(url, json=payload)

def extract_message(line):
    from_index = line.find("@From")
    if from_index != -1:
        return line[from_index:]
    return line

def extract_item_info(raw_message):
    try:
        bulk_match = re.search(r"your (.+?) for my (.+?) in", raw_message)
        if bulk_match:
            item = bulk_match.group(1)
            offer = bulk_match.group(2)
            return f"{item} for {offer}"

        normal_match = re.search(r"your (.+?) listed for (\d+)\s*(\w+)", raw_message)
        if normal_match:
            item = normal_match.group(1)
            price = normal_match.group(2)
            currency = normal_match.group(3)
            return f"{item} for {price} {currency}"

    except Exception as e:
        print(f"[Ошибка парсинга] {e}")
    return raw_message


def paste_message_to_poe(message, nick):
    formatted_message = f"@{nick} {message}"
    pyperclip.copy(formatted_message)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    pyautogui.press('enter')

def handle_callbacks():
    last_update_id = None
    while True:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
            if last_update_id:
                url += f"?offset={last_update_id + 1}"

            response = requests.get(url)
            updates = response.json().get("result", [])

            for update in updates:
                last_update_id = update["update_id"]

                if "callback_query" in update:
                    data = update["callback_query"]["data"]
                    user = update["callback_query"]["from"]["first_name"]

                    if data == "minute" and last_trade_nick:
                        paste_message_to_poe("Wait a few minutes please, taking shower.", last_trade_nick)
                    elif data == "away" and last_trade_nick:
                        paste_message_to_poe("Away from PC. I'll contact you later.", last_trade_nick)


        except Exception as e:
            print(f"[Callback Error] {e}")
        time.sleep(2)

def extract_nick(raw_message):
    match = re.search(r"@From <.*?> ([^:]+):", raw_message)
    if match:
        return match.group(1).strip()
    return None

def extract_bulk_nick(raw_message):
    match = re.search(r"@(.+?)(?:\s|$)", raw_message)
    if match:
        return match.group(1).strip()
    return None

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.position = os.path.getsize(file_path)

    def on_modified(self, event):
        if event.src_path.endswith("Client.txt"):
            with open(self.file_path, "r", encoding="utf-8", errors="ignore") as f:
                f.seek(self.position)
                new_lines = f.readlines()
                self.position = f.tell()

            for line in new_lines:
                line = line.strip()

                if "@From" in line and "like to buy your" in line:
                    clean_msg = extract_message(line)
                    nick = extract_nick(clean_msg)
                    formatted = extract_item_info(clean_msg)

                    if nick:
                        global last_trade_nick
                        last_trade_nick = nick
                        send_trade_notification_with_buttons(formatted, nick)




if __name__ == "__main__":
    print("🔍 Ожидание входящих трейдов... (можно свернуть)")
    event_handler = LogFileHandler(LOG_FILE_PATH)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(LOG_FILE_PATH), recursive=False)
    observer.start()

    threading.Thread(target=handle_callbacks, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()