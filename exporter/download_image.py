# exporter/download_image.py

import plotly.express as px
import plotly.io as pio
import io

def download_image(fig, visualization_type):
    """
    Fungsi untuk mengunduh gambar visualisasi.
    """
    if fig is None:
        return None

    # Menyimpan gambar dalam buffer
    img_bytes = io.BytesIO()
    pio.write_image(fig, img_bytes, format='png')
    img_bytes.seek(0)
    return f'<a href="data:image/png;base64,{img_bytes.getvalue().encode("base64")}" download="{visualization_type}.png">Download Image</a>'
