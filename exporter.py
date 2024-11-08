# exporter.py
import pandas as pd
from io import BytesIO
import plotly.io as pio
import base64

def download_excel(df):
    """
    Menghasilkan tautan untuk mengunduh DataFrame dalam format Excel.
    """
    towrite = BytesIO()
    df.to_excel(towrite, index=False, engine='xlsxwriter')
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:file/xlsx;base64,{b64}" download="data.xlsx">Download Excel File</a>'
    return href

def download_image(fig, name):
    """
    Menghasilkan tautan untuk mengunduh gambar visualisasi dalam format JPEG.
    """
    if fig is None:
        return "No figure available to download."
    
    try:
        img_bytes = pio.to_image(fig, format="jpeg", width=1080, height=720, engine="kaleido")
        b64 = base64.b64encode(img_bytes).decode()
        href = f'<a href="data:image/jpeg;base64,{b64}" download="{name}.jpeg">Download JPEG</a>'
        return href
    except Exception as e:
        return f"Error generating image: {str(e)}"
