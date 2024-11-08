# exporter/download_excel.py

import pandas as pd
import io

def download_excel(df):
    """
    Fungsi untuk mengekspor data sebagai file Excel.
    """
    if df is None:
        return None

    # Menyimpan dataframe ke dalam buffer Excel
    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{output.getvalue().encode("base64")}" download="data.xlsx">Download Excel</a>'
