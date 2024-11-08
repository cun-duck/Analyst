# app.py
import streamlit as st
import pandas as pd
from file_manager import handle_upload, delete_file
from visualization import render_visualization
from exporter import download_excel, download_image
from logger import send_log_to_telegram
from ai_training import start_training  # Modul pelatihan AI

st.set_page_config(page_title="Automated Data Analysis & Visualization", layout="wide")

st.title("Automated Data Analysis & Visualization Dashboard")
st.write("Upload a CSV or Excel file to generate data visualizations and analyses.")

uploaded_file = st.file_uploader("Choose a file (CSV or XLS, max 3MB)", type=["csv", "xls", "xlsx"])
file_path = None

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

            # Analis data untuk menentukan jenis visualisasi yang relevan
            st.write("### Suggested Visualizations")
            visualizations = analyze_file(df)  # Menambahkan analisis data

            # Tampilkan rekomendasi visualisasi
            st.write("Recommended Visualizations:")
            for viz in visualizations:
                st.write(f"- {viz}")
            
            # Sidebar settings untuk memilih jenis visualisasi
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
        
        else:
            st.error("Failed to process the file.")
else:
    if file_path:
        delete_file(file_path)  # Menghapus file ketika user keluar atau upload baru

# Mulai pelatihan AI di latar belakang (tidak terlihat oleh pengguna)
agent = start_training()

# Fungsi untuk analisis file dan menentukan jenis visualisasi
def analyze_file(dataframe):
    columns = dataframe.columns
    data_types = dataframe.dtypes

    recommended_visualizations = []

    # Tentukan rekomendasi visualisasi berdasarkan tipe data
    for col, dtype in zip(columns, data_types):
        if dtype in ['int64', 'float64']:
            recommended_visualizations.append(f"Histogram for {col}")
        elif dtype == 'object':
            recommended_visualizations.append(f"Bar chart for {col}")

    return recommended_visualizations
