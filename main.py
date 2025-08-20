import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("Car Damage Detection")
st.write("Upload a car image to detect damages")

model = YOLO("runs/detect/train2/weights/best.pt")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    results = model.predict(img, save=False, conf=0.4)
    res_plotted = results[0].plot()
    st.image(res_plotted, caption="Detected Damages", use_container_width=True)
