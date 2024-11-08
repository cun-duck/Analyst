# ai_training/train_agent.py

import pandas as pd

def start_training(df: pd.DataFrame):
    """
    Fungsi untuk melatih agen AI dengan menganalisis struktur dan tipe data
    """
    # Deteksi jenis data, misalnya kolom numerik, kategorikal, dll.
    data_info = df.dtypes
    recommendations = {}

    for column, dtype in data_info.items():
        if dtype in ['int64', 'float64']:
            recommendations[column] = 'Numerical Data - Suitable for line chart, scatter plot'
        else:
            recommendations[column] = 'Categorical Data - Suitable for bar chart, pie chart'

    return recommendations
