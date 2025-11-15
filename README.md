# Path of Exile Trade Alert Bot

This tool monitors the *Path of Exile* `Client.txt` log file in real time and sends incoming trade messages directly to Telegram with interactive buttons:

- **Minute** — sends "Wait a few minutes, please..."
- **Away** — sends "Away from PC. I'll contact you later."

Useful when you step away from the PC (food, shower, walk, bathroom) but still want to respond to trade messages quickly without losing deals.

---

## 🔧 Features

- Real-time monitoring of `Client.txt` via watchdog
- Parsing trade messages:
  - standard trade messages: "Hi, I'd like to buy..."
  - bulk-trade messages
- Extracts buyer nickname
- Extracts item and price information
- Sends Telegram notifications through a bot
- Inline buttons for quick replies
- Automatically pastes prepared responses into PoE using `pyautogui`
- Multithreading (main thread + Telegram callback handler)

---

## ⚠ Important

The game **must be active (in focus)** when the automatic response is sent.  
If Path of Exile is minimized, `pyautogui` cannot type into the chat.

---

## 📦 Installation

1. Install Python 3.10+
2. Download the repository:
```bash
git clone https://github.com/pxrnxdxmxn/PoE-Trade-Notification-Bot
cd PoE-Trade-Notification-Bot
```


# Path of Exile Trade Alert Bot

Этот небольшой инструмент отслеживает входящие трейд-сообщения в *Path of Exile* через лог-файл `Client.txt` и отправляет уведомления в Telegram с интерактивными кнопками:

- **Minute** — отправляет игроку сообщение "Wait a few minutes..."
- **Away** — отправляет сообщение "Away from PC..."

Полезно, если вы отошли от ПК (еда, душ, прогулка, туалет), но хотите быстро отвечать трейдерам, чтобы не терять сделки.

---

## 🔧 Возможности

- Мониторинг `Client.txt` в реальном времени (watchdog)
- Парсинг приватных сообщений формата:
  - обычные трейды "Hi, I'd like to buy..."
  - bulk-trade запросы
- Определение ника покупателя
- Извлечение предмета и цены из сообщения
- Уведомления в Telegram через бота
- Inline-кнопки в Telegram для мгновенных ответов
- Автоматическая отправка подготовленного ответа в PoE через `pyautogui`
- Многопоточность (основной поток + поток обработки callback'ов)

---

## ⚠ Важно

Игра **должна быть развернута (в фокусе)** в момент отправки автоматического ответа.  
Если Path of Exile свернута, `pyautogui` не сможет вставить текст в чат.

---

## 📦 Установка

1. Установите Python 3.10+
2. Скачайте репозиторий:
```bash
git clone https://github.com/yourname/poe-trade-alert
cd poe-trade-alert
```
