import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# สร้าง dropdown
selected_option = st.selectbox("Select option", ["Data Table", "Graph"])

# ตรวจสอบตัวเลือกที่ผู้ใช้เลือก
if selected_option == "Data Table":
    st.write("นี่คือตารางข้อมูล")
    excel_file = r'C:\Users\A_R_T\Desktop\sampel.xlsx'  # แก้ไขชื่อไฟล์ตามที่คุณใช้งานจริง
    sheet_name = 'Demo'
    data = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='A:B')
    st.dataframe(data)
elif selected_option == "Graph":
    st.write("นี่คือกราฟ")
    excel_file = r'C:\Users\A_R_T\Desktop\sampel.xlsx'  # แก้ไขชื่อไฟล์ตามที่คุณใช้งานจริง
    sheet_name = 'Demo'
    data = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='A:B')
    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=data.iloc[:, 0], y=data.iloc[:, 1])
    ax.set_xlabel('Month')
    ax.set_ylabel('(BOD)mg/L')
    ax.grid(True)
    plt.title("Graph BOD Average")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig)
