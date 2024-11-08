# file_manager/handle_upload.py

import pandas as pd
import os
class HandleUpload
def handle_upload(uploaded_file):
    """
    Fungsi untuk menangani upload file, validasi ukuran, dan membaca data
    """
    if uploaded_file.size > 3 * 1024 * 1024:  # 3MB
        return None, "File size exceeds the 3MB limit."
    
    file_path = f"temp/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Membaca file ke dalam dataframe
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    
    return file_path, df
