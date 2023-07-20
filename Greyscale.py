import streamlit as st
from PIL import Image

st.title("Colour to Greyscale Converter")

# File uploader allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    # Open camera and take image
    camera_image = st.camera_input("Camera")

if uploaded_image:
    # Open file using PIL(Pillow)
    img = Image.open(uploaded_image)

    # Turn image into greyscale
    gray_uploaded_img = img.convert("L")

    # Display image
    st.image(gray_uploaded_img)

if camera_image:
    # Open file using PIL(Pillow)
    img = Image.open(camera_image)

    # Turn image into greyscale
    gray_img = img.convert("L")

    # Display image
    st.image(gray_img)