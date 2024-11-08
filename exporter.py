# exporter.py
import pandas as pd
from io import BytesIO
import plotly.io as pio
import base64

def download_excel(df):
    towrite = BytesIO()
    df.to_excel(towrite, index=False, engine='xlsxwriter')
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:file/xlsx;base64,{b64}" download="data.xlsx">Download Excel File</a>'
    return href

def download_image(fig, name):
    img_bytes = pio.to_image(fig, format="jpeg", width=1080, height=720)
    b64 = base64.b64encode(img_bytes).decode()
    href = f'<a href="data:image/jpeg;base64,{b64}" download="{name}.jpeg">Download JPEG</a>'
    return href
