# logger/send_log.py

import requests

def send_log_to_telegram(file_name):
    """
    Kirim log pengunggahan file ke Telegram
    """
    token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    message = f'File uploaded: {file_name}'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(url)
