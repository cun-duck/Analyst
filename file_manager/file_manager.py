# file_manager.py
import pandas as pd
import os

UPLOAD_FOLDER = "uploads/"

def handle_upload(uploaded_file):
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Baca data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    
    return file_path, df

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
