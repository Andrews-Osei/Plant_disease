import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import json
import time

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="LeafVisio · Plant Intelligence",
    page_icon="🍃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# GLOBAL CSS — Dark botanical theme with editorial flair
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

/* ══════════════════════════════════════════
   FULL-SCREEN DARK TAKEOVER
   ══════════════════════════════════════════ */

/* Kill the white Streamlit toolbar */
header[data-testid="stHeader"] {
    background-color: #071209 !important;
    border-bottom: 1px solid #1a3020 !important;
}

/* Hide deploy menu & footer watermark */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }

/* Root */
html, body {
    background-color: #0d1a0f !important;
    margin: 0; padding: 0;
}

/* Every Streamlit wrapper layer */
.stApp,
.stApp > div,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="block-container"],
.main, .main > div {
    background-color: #0d1a0f !important;
    color: #e8f0e9;
}

/* Reduce top gap under toolbar */
[data-testid="stAppViewBlockContainer"] {
    padding-top: 1.2rem !important;
}

/* ── Base font ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div {
    background: linear-gradient(180deg, #071209 0%, #0d1a0f 100%) !important;
    border-right: 1px solid #1e3320 !important;
}

section[data-testid="stSidebar"] * {
    color: #c6ddc9 !important;
}

/* ── Header banner ── */
.leafvisio-header {
    position: relative;
    padding: 3rem 2.5rem 2.5rem;
    background: linear-gradient(135deg, #0a2e10 0%, #112b14 40%, #0d1a0f 100%);
    border-radius: 18px;
    margin-bottom: 2rem;
    overflow: hidden;
    border: 1px solid #1f3d22;
}

.leafvisio-header::before {
    content: "";
    position: absolute;
    top: -40px; right: -40px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(74,188,74,0.12) 0%, transparent 70%);
    border-radius: 50%;
}

.leafvisio-header::after {
    content: "✦";
    position: absolute;
    bottom: 18px; right: 28px;
    font-size: 1rem;
    color: rgba(74,188,74,0.3);
    letter-spacing: 8px;
}

.leafvisio-logo {
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: -1px;
    line-height: 1;
    margin-bottom: 0.3rem;
}

.leafvisio-logo span {
    color: #4abc4a;
}

.leafvisio-tagline {
    font-size: 0.85rem;
    font-weight: 300;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #7aad7a;
    margin-bottom: 1rem;
}

.leafvisio-desc {
    font-size: 1rem;
    color: #9bbf9e;
    max-width: 520px;
    line-height: 1.7;
}

/* ── Section labels ── */
.section-label {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #4abc4a;
    margin-bottom: 0.6rem;
}

/* ── Upload zone ── */
.upload-wrapper {
    background: #101f12;
    border: 1.5px dashed #2a4d2d;
    border-radius: 16px;
    padding: 1.5rem 1.5rem 0.8rem;
    transition: border-color 0.3s;
}

.upload-wrapper:hover {
    border-color: #4abc4a;
}

/* ── File uploader widget ── */
[data-testid="stFileUploader"] {
    background: transparent !important;
}

[data-testid="stFileUploader"] label {
    color: #9bbf9e !important;
    font-size: 0.9rem !important;
}

[data-testid="stFileUploaderDropzone"] {
    background: #0d1a0f !important;
    border: 1px solid #1e3320 !important;
    border-radius: 10px !important;
}

/* ── Image display ── */
.img-frame {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #1e3320;
    background: #101f12;
}

/* ── Result card ── */
.result-card {
    background: linear-gradient(135deg, #101f12 0%, #0e1c10 100%);
    border: 1px solid #1e3320;
    border-radius: 16px;
    padding: 2rem 1.8rem;
    margin-top: 0;
}

.result-card.healthy {
    border-color: #2a6b2a;
    background: linear-gradient(135deg, #0a2010 0%, #0d1f0e 100%);
}

.result-card.diseased {
    border-color: #6b2a2a;
    background: linear-gradient(135deg, #200a0a 0%, #1f0d0d 100%);
}

.plant-species {
    font-size: 0.72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #7aad7a;
    margin-bottom: 0.25rem;
}

.condition-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 1.2rem;
}

.condition-title.healthy { color: #5dd65d; }
.condition-title.diseased { color: #e06060; }

.confidence-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 0.5rem;
}

.confidence-label {
    font-size: 0.78rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #7aad7a;
    white-space: nowrap;
}

.confidence-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #ffffff;
}

/* ── Progress bar ── */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #2a7a2a, #4abc4a) !important;
    border-radius: 4px !important;
}

.stProgress > div > div {
    background: #1a2e1c !important;
    border-radius: 4px !important;
    height: 6px !important;
}

/* ── Alert / info boxes ── */
.stSuccess, .stError, .stInfo, .stWarning {
    border-radius: 10px !important;
    border: none !important;
}

/* ── Primary button ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #2a7a2a, #3da83d) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.5px !important;
    padding: 0.65rem 1rem !important;
    transition: all 0.2s ease !important;
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #3da83d, #52c452) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(74,188,74,0.25) !important;
}

/* ── Sidebar steps ── */
.step-item {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    margin-bottom: 1rem;
}

.step-num {
    width: 24px; height: 24px;
    background: #1e3a20;
    border: 1px solid #2a5a2d;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.7rem;
    font-weight: 600;
    color: #4abc4a;
    flex-shrink: 0;
    margin-top: 2px;
}

.step-text {
    font-size: 0.88rem;
    color: #9bbf9e;
    line-height: 1.5;
}

/* ── Divider ── */
hr {
    border-color: #1e3320 !important;
}

/* ── Stat chips ── */
.stat-chips {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 1.2rem;
}

.chip {
    background: #1a2e1c;
    border: 1px solid #2a4d2d;
    border-radius: 30px;
    padding: 4px 14px;
    font-size: 0.75rem;
    color: #7aad7a;
    letter-spacing: 0.5px;
}

/* ── Footer ── */
.leafvisio-footer {
    text-align: center;
    padding: 2rem 0 1rem;
    color: #3a5a3d;
    font-size: 0.78rem;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# LOAD MODEL & METADATA
# ---------------------------------------------------------
@st.cache_resource
def load_model_and_classes():
    import os

    # Always resolve paths relative to THIS script's location,
    # so it works regardless of which directory you launch Streamlit from.
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    model_path = os.path.join(BASE_DIR, "plant_disease_cnn_model.keras")
    json_path  = os.path.join(BASE_DIR, "class_names.json")

    # ── Load model ───────────────────────────────────────────────────────────
    # Works for BOTH:
    #   • a single .keras archive file
    #   • a .keras *folder* (SavedModel format — contains model.weights.h5)
    if not os.path.exists(model_path):
        st.error(
            f"⚠️ Model not found at:\n\n`{model_path}`\n\n"
            "Make sure **plant_disease_cnn_model.keras** (the file or folder) "
            "sits in the same directory as `app.py`."
        )
        return None, None

    try:
        model = tf.keras.models.load_model(model_path)
    except Exception as e:
        st.error(f"⚠️ Model found but could not be loaded. Details: {e}")
        return None, None

    # ── Load class names ─────────────────────────────────────────────────────
    if not os.path.isfile(json_path):
        st.error(
            f"⚠️ `class_names.json` not found at:\n\n`{json_path}`\n\n"
            "Place it in the same folder as `app.py`."
        )
        return None, None

    try:
        with open(json_path, "r") as f:
            class_names = json.load(f)
    except Exception as e:
        st.error(f"⚠️ Could not read `class_names.json`. Details: {e}")
        return None, None

    return model, class_names

model, class_names = load_model_and_classes()


# ---------------------------------------------------------
# HELPERS
# ---------------------------------------------------------
def preprocess_image(image):
    image = image.convert('RGB')
    image = image.resize((224, 224))
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(image, model, class_names):
    processed = preprocess_image(image)
    preds = model.predict(processed)
    idx = np.argmax(preds[0])
    confidence = float(preds[0][idx])
    class_name = class_names[idx]
    return class_name, confidence


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="padding: 1.2rem 0 0.5rem;">
            <div style="font-family:'Playfair Display',serif; font-size:1.6rem; font-weight:900; color:#ffffff;">
                Leaf<span style="color:#4abc4a;">Visio</span>
            </div>
            <div style="font-size:0.65rem; letter-spacing:3px; text-transform:uppercase; color:#4abc4a; margin-top:2px;">
                Plant Intelligence
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown('<div style="font-size:0.7rem;letter-spacing:2.5px;text-transform:uppercase;color:#4abc4a;margin-bottom:1rem;">How It Works</div>', unsafe_allow_html=True)

    steps = [
        ("Upload", "Take or select a clear photo of a plant leaf — full surface, good lighting."),
        ("Analyze", "Click the scan button to send the image through our CNN model."),
        ("Diagnose", "Receive an instant classification with a confidence score."),
        ("Act", "Review recommendations and take timely action if disease is detected."),
    ]

    for i, (title, desc) in enumerate(steps, 1):
        st.markdown(f"""
            <div class="step-item">
                <div class="step-num">{i}</div>
                <div class="step-text"><b style="color:#c6ddc9;">{title}</b><br>{desc}</div>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
        <div style="background:#101f12; border:1px solid #1e3320; border-radius:10px; padding:1rem 1.1rem;">
            <div style="font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;color:#4abc4a;margin-bottom:0.5rem;">Pro Tip</div>
            <div style="font-size:0.84rem;color:#9bbf9e;line-height:1.6;">
                Images with a plain background and sharp focus yield the most accurate diagnoses. Avoid blurry or low-light photos.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-top:2rem;">
            <div style="font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;color:#3a5a3d;margin-bottom:0.6rem;">Model Info</div>
            <div style="font-size:0.8rem;color:#4a7a4d;line-height:1.7;">
                Architecture: CNN (Custom)<br>
                Input size: 224 × 224 px<br>
                Format: Keras (.keras)
            </div>
        </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# MAIN CONTENT
# ---------------------------------------------------------

# ── Hero Header ──
st.markdown("""
    <div class="leafvisio-header">
        <div class="leafvisio-logo">Leaf<span>Visio</span></div>
        <div class="leafvisio-tagline">AI-Powered · Leaf Diagnostics</div>
        <div class="leafvisio-desc">
            Upload a leaf photograph and let our convolutional neural network instantly
            identify disease conditions — across dozens of crop species — with clinical-grade confidence scoring.
        </div>
        <div class="stat-chips">
            <div class="chip">🌱 38 Disease Classes</div>
            <div class="chip">⚡ Real-Time Inference</div>
            <div class="chip">🔬 CNN-Powered</div>
            <div class="chip">🌍 14+ Plant Species</div>
        </div>
    </div>
""", unsafe_allow_html=True)

if model is None or class_names is None:
    st.stop()

# ── Upload Zone ──
st.markdown('<div class="section-label">01 — Upload Specimen</div>', unsafe_allow_html=True)
st.markdown('<div class="upload-wrapper">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Drop a leaf image here, or click to browse  ·  JPG · JPEG · PNG",
    type=["jpg", "jpeg", "png"],
    label_visibility="visible"
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

# ── Two-column layout ──
col1, col2 = st.columns([1, 1], gap="large")

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    with col1:
        st.markdown('<div class="section-label">02 — Leaf Specimen</div>', unsafe_allow_html=True)
        st.markdown('<div class="img-frame">', unsafe_allow_html=True)
        st.image(image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div style="margin-top:0.7rem; display:flex; gap:10px; align-items:center;">
                <div style="font-size:0.75rem;color:#4a7a4d;">📁 {uploaded_file.name}</div>
                <div style="font-size:0.75rem;color:#3a5a3d;">·</div>
                <div style="font-size:0.75rem;color:#4a7a4d;">{image.size[0]} × {image.size[1]} px</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-label">03 — AI Diagnosis</div>', unsafe_allow_html=True)

        if st.button("🔬 Run Diagnostic Scan", type="primary", use_container_width=True):
            with st.spinner("Scanning leaf patterns through the neural network…"):
                time.sleep(1.2)
                predicted_class, confidence = predict(image, model, class_names)

            parts = predicted_class.split('___')
            plant_name = parts[0].replace("_", " ")
            condition = parts[1].replace("_", " ") if len(parts) > 1 else predicted_class
            is_healthy = "healthy" in condition.lower()

            status_class = "healthy" if is_healthy else "diseased"
            status_icon  = "✦" if is_healthy else "⚠"
            condition_display = condition.title()

            st.markdown(f"""
                <div class="result-card {status_class}">
                    <div class="plant-species">{status_icon} &nbsp; {plant_name}</div>
                    <div class="condition-title {status_class}">{condition_display}</div>
                    <div class="confidence-row">
                        <div class="confidence-label">Confidence</div>
                        <div class="confidence-value">{confidence*100:.1f}%</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
            st.progress(confidence)

            st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

            if is_healthy:
                st.success("✅ **Healthy specimen confirmed.** No signs of disease were detected. Continue your current care routine and monitor regularly.")
            else:
                conf_tier = "High" if confidence > 0.85 else "Moderate" if confidence > 0.60 else "Low"
                st.error(f"⚠️ **{condition_display} detected** with **{conf_tier} confidence**. Prompt treatment is advised. Research targeted fungicides, pesticides, or cultural practices specific to *{condition_display}*.")

                with st.expander("📋 What to do next"):
                    st.markdown(f"""
                        - Isolate the affected plant from healthy specimens immediately.
                        - Research treatment options specifically for **{condition_display}**.
                        - Consult your local agricultural extension service if symptoms persist.
                        - Monitor neighboring plants for early signs of spread.
                        - Document the progression with dated photos for tracking.
                    """)
        else:
            st.markdown("""
                <div style="background:#101f12; border:1px dashed #1e3320; border-radius:14px;
                            padding:2.5rem 1.8rem; text-align:center; margin-top:0;">
                    <div style="font-size:2rem; margin-bottom:0.8rem;">🔬</div>
                    <div style="font-family:'Playfair Display',serif; font-size:1.1rem; color:#c6ddc9; margin-bottom:0.5rem;">
                        Ready to Diagnose
                    </div>
                    <div style="font-size:0.85rem; color:#4a7a4d; line-height:1.6;">
                        Click the button above to run the<br>deep learning diagnostic scan.
                    </div>
                </div>
            """, unsafe_allow_html=True)

else:
    with col1:
        st.markdown("""
            <div style="background:#101f12; border:1px dashed #1e3320; border-radius:14px;
                        padding:3rem 2rem; text-align:center; min-height:280px;
                        display:flex; flex-direction:column; align-items:center; justify-content:center;">
                <div style="font-size:3rem; margin-bottom:1rem; opacity:0.4;">🌿</div>
                <div style="font-size:0.8rem; letter-spacing:2px; text-transform:uppercase;
                            color:#3a5a3d;">Awaiting specimen upload</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background:#101f12; border:1px dashed #1e3320; border-radius:14px;
                        padding:3rem 2rem; text-align:center; min-height:280px;
                        display:flex; flex-direction:column; align-items:center; justify-content:center;">
                <div style="font-size:3rem; margin-bottom:1rem; opacity:0.4;">📊</div>
                <div style="font-size:0.8rem; letter-spacing:2px; text-transform:uppercase;
                            color:#3a5a3d;">Diagnosis results will appear here</div>
            </div>
        """, unsafe_allow_html=True)

# ── Footer ──
st.markdown("""
    <div class="leafvisio-footer">
        LEAFVISIO · Plant Intelligence System &nbsp;·&nbsp; Powered by TensorFlow & Streamlit
    </div>
""", unsafe_allow_html=True)