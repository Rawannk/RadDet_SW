import streamlit as st
import cv2
import numpy as np
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('ai2.png')

basic_img= cv2.imread('basic b.jpg')
st.title("RadDet")
st.text("jklkjj")
# st.markdown("This is **RAd** ##Det##")

uploaded_file = st.file_uploader("Upload your Image here...", type=['png', 'jpeg', 'jpg'])

if uploaded_file:
 st.image(uploaded_file)
 uploaded_img= cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
if st.button('Start Detecting'):
    if basic_img.shape==uploaded_img.shape:
        st.write('There is Brain Tumour (Type: Glioma)')
    else:
        st.write('There is No Tumour')