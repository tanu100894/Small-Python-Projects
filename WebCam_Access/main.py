# Build a webapp that can access the web camera and browse a photo from your computer and convert it to greyscale.

import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera_image and convert it to grey scale
    cam_img = Image.open(camera_image)
    grey_img = cam_img.convert("L")
    st.image(grey_img)

if uploaded_image:
    # Supply the uploaded image by the user and convert it to grey scale
    upl_img = Image.open(uploaded_image)
    grey_img = upl_img.convert("L")
    st.image(grey_img)