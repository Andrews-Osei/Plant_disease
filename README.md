# 🍃 LeafVisio — AI-Powered Plant Disease Detection

![LeafVisio Banner](https://img.shields.io/badge/LeafVisio-Plant%20Intelligence-2d8a2d?style=for-the-badge&logo=leaf&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18.0-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Diagnose your plant's health instantly using Deep Learning.**  
> Upload a leaf photograph and let our Convolutional Neural Network identify disease conditions across dozens of crop species — with clinical-grade confidence scoring.

---

## 🌐 Live Demo

### 👉 [Launch LeafVisio App](https://plantdisease-nfekpkghoyxsk8wdayvpma.streamlit.app)

> _Click the link above to access the live app — no installation required._

---

## 📸 App Preview

| Upload Screen | Diagnosis Result |
|---|---|
| Upload a clear leaf image | Instant AI diagnosis with confidence score |

---

## ✨ Features

- 🔬 **Real-Time CNN Inference** — Results in under 2 seconds
- 🌱 **38 Disease Classes** — Covers healthy and diseased states
- 🌍 **14+ Plant Species** — Including tomato, potato, apple, corn and more
- 📊 **Confidence Scoring** — Visual progress bar with percentage accuracy
- 💡 **Actionable Advice** — Treatment recommendations for detected diseases
- 🎨 **Dark Botanical UI** — Professional, modern interface built for clarity
- 📱 **Responsive Layout** — Works on desktop and mobile browsers

---

## 🌿 Supported Plant Species & Diseases

| Plant | Conditions Detected |
|---|---|
| 🍎 Apple | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| 🫐 Blueberry | Healthy |
| 🍒 Cherry | Powdery Mildew, Healthy |
| 🌽 Corn (Maize) | Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| 🍇 Grape | Black Rot, Esca, Leaf Blight, Healthy |
| 🍊 Orange | Haunglongbing (Citrus Greening) |
| 🍑 Peach | Bacterial Spot, Healthy |
| 🫑 Pepper | Bacterial Spot, Healthy |
| 🥔 Potato | Early Blight, Late Blight, Healthy |
| 🍓 Strawberry | Leaf Scorch, Healthy |
| 🍅 Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy |

---

## 🚀 Getting Started Locally

### Prerequisites
- Python 3.11
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/andrews-osei/plant_disease.git
cd plant_disease
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Ensure model files are present**
```
plant_disease/
├── app.py
├── class_names.json
├── requirements.txt
├── runtime.txt
├── plant_disease_cnn_model.keras
└── .streamlit/
    └── config.toml
```

**4. Run the app**
```bash
streamlit run app.py
```

**5. Open your browser**
```
http://localhost:8501
```

---

## 🧠 Model Architecture

| Property | Detail |
|---|---|
| Architecture | Convolutional Neural Network (CNN) |
| Input Size | 224 × 224 × 3 (RGB) |
| Output | 38 disease/health classes |
| Framework | TensorFlow / Keras |
| Format | `.keras` (SavedModel) |
| Training Data | PlantVillage Dataset |

### How It Works

```
📷 Leaf Image Upload
        ↓
🔄 Preprocessing (Resize → 224×224, Normalize)
        ↓
🧠 CNN Forward Pass (38-class softmax output)
        ↓
📊 Argmax → Predicted Class + Confidence Score
        ↓
💊 Display Diagnosis + Treatment Advice
```

---

## 🗂️ Project Structure

```
plant_disease/
│
├── app.py                          # Main Streamlit application
├── class_names.json                # 38 class labels from training
├── plant_disease_cnn_model.keras   # Trained CNN model
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python version pin (3.11)
│
└── .streamlit/
    └── config.toml                 # Dark theme configuration
```

---

## 📦 Dependencies

```txt
streamlit>=1.28.0
tensorflow-cpu==2.18.0
pillow>=9.0.0
numpy>=1.23.0
protobuf>=3.20.0
h5py>=3.9.0
```

---

## 🖥️ How to Use the App

1. **Visit** the [live app](https://plantdisease-nfekpkghoyxsk8wdayvpma.streamlit.app)
2. **Upload** a clear photo of a plant leaf (JPG, JPEG, or PNG)
3. **Click** the **"Run Diagnostic Scan"** button
4. **Review** the AI diagnosis — plant name, condition, and confidence score
5. **Act** on the treatment recommendations if a disease is detected

> 💡 **Tip:** Use well-lit, focused images with the full leaf surface visible for the most accurate results.

---

## ☁️ Deployment

This app is deployed on **Streamlit Community Cloud**.

| Property | Value |
|---|---|
| Platform | Streamlit Community Cloud |
| Python Version | 3.11 |
| Repository | `andrews-osei/plant_disease` |
| Branch | `main` |
| Entry Point | `app.py` |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a **Pull Request**

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 👨‍💻 Author

**Andrews Osei**  
GitHub: [@andrews-osei](https://github.com/andrews-osei)

---

## 🙏 Acknowledgements

- [PlantVillage Dataset](https://plantvillage.psu.edu/) — training data source
- [TensorFlow](https://tensorflow.org) — deep learning framework
- [Streamlit](https://streamlit.io) — app framework and cloud hosting

---

<div align="center">
  <sub>Built with 🍃 by Andrews Osei · Powered by TensorFlow & Streamlit</sub>
</div>
