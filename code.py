import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Cool vs. Warm Prediction
def predict_cool_vs_warm(image):
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = image_hsv[:, :, 0]
    warm_mask = (hue >= 0) & (hue <= 60)
    cool_mask = (hue >= 90) & (hue <= 180)
    warm_percentage = np.sum(warm_mask) / hue.size * 100
    cool_percentage = np.sum(cool_mask) / hue.size * 100
    prediction = "Warm" if warm_percentage > cool_percentage else "Cool"
    return prediction, warm_percentage, cool_percentage

# Dull vs. Bright Prediction
def predict_dull_vs_bright(image):
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation = image_hsv[:, :, 1]
    value = image_hsv[:, :, 2]
    dull_saturation_threshold = 80
    dull_value_threshold = 100
    dull_mask = (saturation < dull_saturation_threshold) & (value < dull_value_threshold)
    dull_percentage = np.sum(dull_mask) / saturation.size * 100
    prediction = "Dull" if dull_percentage > 50 else "Bright"
    return prediction, dull_percentage

# Streamlit App
st.title("Image Tone and Brightness Prediction")

# File Uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Predictions
    cool_warm_prediction, warm_percentage, cool_percentage = predict_cool_vs_warm(image)
    dull_bright_prediction, dull_percentage = predict_dull_vs_bright(image)
    
    # Display Results
    st.write(f"**Cool vs. Warm Prediction:** The image is predicted to have a **{cool_warm_prediction}** tone.")
    st.write(f"- Warm Percentage: **{warm_percentage:.2f}%**")
    st.write(f"- Cool Percentage: **{cool_percentage:.2f}%**")
    
    st.write(f"**Dull vs. Bright Prediction:** The image is predicted to be **{dull_bright_prediction}**.")
    st.write(f"- Bright Pixels Percentage: **{100-dull_percentage:.2f}%**")
