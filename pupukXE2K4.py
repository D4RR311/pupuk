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

img = get_img_as_base64("pupuk.jpg")

bg_web = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
}}

[data-testid="stHeader"] {{
background-color: rgba(0, 0, 0, 0);
}}

[data-testid="stToolbar"] {{
right: 1rem;
}}

[data-testid="collapsedControl"] {{
left: 1rem;
}}

</style>
"""

st.title("Web Pupuk Organik Dari Sampah Organik")
st.markdown(bg_web, unsafe_allow_html=True)