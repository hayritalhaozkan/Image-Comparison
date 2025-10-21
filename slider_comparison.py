# sar_slider_comparison_app.py
import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image

st.set_page_config(page_title="SAR Image Comparison", layout="wide")
st.title("Image Comparison")

st.markdown(
    """
    This tool allows you to compare images taken on two different dates by sliding the mouse.
    The **left** image represents the earlier period, and the **right** image represents the later period.
    """
)

# Input fields for customizing labels
st.sidebar.header("Customize Labels")
label1_default = "Previous Period"
label2_default = "Later Period"

custom_label1 = st.sidebar.text_input("Left Image Label:", value=label1_default)
custom_label2 = st.sidebar.text_input("Right Image Label:", value=label2_default)

# Upload images
col1, col2 = st.columns(2)
with col1:
    uploaded_img1 = st.file_uploader("📂 Upload First Image ", type=["png", "jpg", "jpeg", "tif", "tiff"])
with col2:
    uploaded_img2 = st.file_uploader("📂 Upload Second Image ", type=["png", "jpg", "jpeg", "tif", "tiff"])

# Show comparison slider if images are uploaded
if uploaded_img1 and uploaded_img2:
    try:
        # Convert uploaded file objects to PIL Image objects
        img1_pil = Image.open(uploaded_img1)
        img2_pil = Image.open(uploaded_img2)

        st.markdown("###  Slide the center line with your mouse to observe the changes:")
        image_comparison(
            img1=img1_pil,
            img2=img2_pil,
            label1=custom_label1,
            label2=custom_label2,
            width=900,
            starting_position=50,  # Starts at 50% (middle)
            show_labels=True,
        )
    except Exception as e:
        st.error(f"An error occurred while processing the image: {e}")
        st.warning("Please ensure you have uploaded valid image files.")
else:
    st.info("Start by uploading two images.")