import streamlit as st

from processor import GenerateDescription

generator = GenerateDescription()

st.set_page_config(page_title="Image Caption Generator")

st.title("Image Caption Generator")


image = st.file_uploader("Upload your Image: ")

if image:
    st.image(image)
    caption = generator.generate(image)
    caption = caption.strip("start")
    caption = caption.strip("end")
    caption = caption.strip()
    caption = caption.capitalize()
    caption += "."


    st.header(caption)
