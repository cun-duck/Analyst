import streamlit as st
from file_manager import handle_upload, delete_file
from visualization import render_visualization
from exporter import download_excel, download_image
from logger import send_log_to_telegram
from ai_training import start_training, analyze_file  # Pastikan untuk mengimpor fungsi analyze_file dari ai_training.py

st.set_page_config(page_title="Automated Data Analysis & Visualization", layout="wide")

st.title("Automated Data Analysis & Visualization Dashboard")
st.write("Upload a CSV or Excel file to generate data visualizations and analyses.")

uploaded_file = st.file_uploader("Choose a file (CSV or XLS, max 3MB)", type=["csv", "xls", "xlsx"])
file_path = None
def analyze_file(df):
    # Cek apakah data mengandung nilai yang hilang
    if df.isnull().any().any():
        st.error("Data contains missing values. Please clean the data.")
        return None
    return df  # Return data jika sudah valid
# Cek ukuran file
if uploaded_file is not None:
    if uploaded_file.size > 3 * 1024 * 1024:  # 3MB = 3 * 1024 * 1024 bytes
        st.error("The file size exceeds the 3MB limit. Please upload a smaller file.")
    else:
        # File diterima, lanjutkan ke proses upload
        file_path, df = handle_upload(uploaded_file)

        if df is not None:
            st.success("File successfully uploaded!")
            st.write("### Data Preview")
            st.dataframe(df.head())

            # Kirim log ke Telegram setiap ada file baru yang diunggah
            send_log_to_telegram(uploaded_file.name)

            # Analisis data oleh agen AI untuk memahami jenis data
            visualizations = analyze_file(df)  # Menambahkan analisis data untuk memahami jenis file

            # Sidebar settings
            st.sidebar.write("## Visualization Settings")
            visualization_type = st.sidebar.selectbox(
                "Choose Visualization Type", 
                ["Bar Chart", "Line Chart", "Pie Chart", "Heatmap", "Scatter Plot"]
            )

            # Render and display visualization
            fig = render_visualization(df, visualization_type, st.sidebar)
            if fig:
                st.plotly_chart(fig, use_container_width=True)
            
            # Download options
            st.write("### Download Options")
            st.markdown(download_image(fig, visualization_type), unsafe_allow_html=True)
            st.markdown(download_excel(df), unsafe_allow_html=True)

            # Mulai pelatihan AI di latar belakang (tidak terlihat oleh pengguna)
            agent = start_training(df)  # Menjalankan pelatihan AI di latar belakang

        else:
            st.error("Failed to process the file.")
else:
    if file_path:
        delete_file(file_path)  # Menghapus file ketika user keluar atau upload baru
