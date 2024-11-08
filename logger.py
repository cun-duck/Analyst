# logger.py
import requests

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_log_to_telegram(file_name):
    user_ip = requests.get("https://api64.ipify.org").text  # Mendapatkan IP pengguna
    user_agent = requests.get("https://httpbin.org/user-agent").json()["user-agent"]
    
    message = f"New file uploaded: {file_name}\nIP: {user_ip}\nUser Agent: {user_agent}"
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}")
