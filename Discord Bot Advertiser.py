import requests
import time

TOKEN = "" #Insert bot token or your own
CHANNEL_ID = "" #Insert channel ID
MESSAGE = "" #Insert your message here
WAIT_TIME = #Enter a number 1 second bigger than the slow mode timer

headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

def send_message(content):
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    data = {"content": content}
    response = requests.post(url, json=data, headers=headers)
    print(f"[+] Sent message: {response.status_code} - {response.text}")

while True:
    send_message(MESSAGE)
    print(f"[i] Waiting {WAIT_TIME // 60} minutes...")
    time.sleep(WAIT_TIME)