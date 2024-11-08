# logger/send_log.py

import requests

def send_log_to_telegram(file_name):
    """
    Kirim log pengunggahan file ke Telegram
    """
    token = '7590725563:AAH0AoLSrT5WatVESyDYPKkgW53UtMWp4XI'
    chat_id = '5217803272'
    message = f'File uploaded: {file_name}'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(url)

def send_log_to_telegram(file_name):
    user_ip = requests.get("https://api64.ipify.org").text  # Mendapatkan IP pengguna
    user_agent = requests.get("https://httpbin.org/user-agent").json()["user-agent"]
    
    message = f"New file uploaded: {file_name}\nIP: {user_ip}\nUser Agent: {user_agent}"
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}")
    
