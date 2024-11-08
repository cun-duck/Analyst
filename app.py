# app.py

import streamlit as st
from file_manager.handle_upload import handle_upload
from data_analysis.analyze_data import analyze_file
from exporter.download_image import download_image
from exporter.download_excel import download_excel
from ai_training.train_agent import start_training
from logger.send_log import send_log_to_telegram

st.set_page_config(page_title="Automated Data Analysis & Visualization", layout="wide")

st.title("Automated Data Analysis & Visualization Dashboard")
st.write("Upload a CSV or Excel file to generate data visualizations and analyses.")

uploaded_file = st.file_uploader("Choose a file (CSV or XLS, max 3MB)", type=["csv", "xls", "xlsx"])
file_path = None

# Cek ukuran file
if uploaded_file is not None:
    file_path, df = handle_upload(uploaded_file)
    
    if df is not None:
        st.success("File successfully uploaded!")
        st.write("### Data Preview")
        st.dataframe(df.head())
        
        # Kirim log ke Telegram setiap ada file baru yang diunggah
        send_log_to_telegram(uploaded_file.name)

        # Mulai pelatihan AI untuk mendeteksi jenis data
        agent = start_training(df)

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
    
    else:
        st.error("Failed to process the file.")
else:
    if file_path:
        delete_file(file_path)  # Menghapus file ketika user keluar atau upload baru
