import streamlit as st
import base64
import time
from datetime import time

st.set_page_config(
  page_title="Web Absensi",
  page_icon="🗓️",  
)

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("foto/pupuk.jpg")