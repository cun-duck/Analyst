# data_analysis/analyze_data.py

import pandas as pd

def analyze_file(df: pd.DataFrame):
    """
    Fungsi untuk menganalisis file dan memberikan rekomendasi visualisasi.
    """
    # Mengambil informasi dasar tentang data
    data_info = df.describe(include='all')
    return data_info
