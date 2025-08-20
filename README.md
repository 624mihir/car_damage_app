# 🚗 Car Damage Detection App

This project is an **AI-powered Streamlit web app** that detects car damages from uploaded images using a **YOLOv8 model**.  
It provides real-time **object detection** and can be extended to show **segmentation masks** for more detailed damage inspection.

---

## ✨ Features
- Upload any car image (`.jpg`, `.jpeg`, `.png`)
- Detect visible damages using a trained YOLOv8 model
- Visualize detections directly in the browser
- Simple, clean Streamlit interface
- Ready to deploy on **Streamlit Cloud**, **Render**, or any cloud VM

---

## 🎥 Demo
[![Watch the video](https://github.com/624mihir/car_damage_app/issues/1#issue-3336868101)


## ⚡ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/car_damage_app.git
cd car_damage_app
```

### 2️⃣ Create a virtual environment
```bash
conda create -n cardamage python=3.10 -y
conda activate cardamage
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
streamlit run main.py
```

