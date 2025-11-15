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
