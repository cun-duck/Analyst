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
