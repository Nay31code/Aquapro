import streamlit as st
from PIL import Image
import base64
import os
print(os.getcwd())

#set icon 
st.set_page_config(
    page_title="Waste water predictor",
    page_icon="🌊", 
    layout="wide", 
)
#set background 
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True) 

image_path = 'C:/Users/A_R_T/Desktop/Project/Aquapro/Project/plant.JPG'
set_background(image_path)
# set titile 
st.markdown(
    """
    <style>
        .centered-title {
            display: flex;
            justify-content: center;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# ใส่ content ใน div ที่มี class centered-title
st.markdown("<h1 style='text-align: center; color: white; font-size: 60px;'>Aqua Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 40px;'>This web application can show retrospective data and can predict this data</h1>", unsafe_allow_html=True)
