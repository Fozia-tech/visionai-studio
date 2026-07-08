import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from PIL import Image

from modules.face_detection import detect_faces
from modules.cartoon import cartoonify
from modules.caption_generator import generate_caption
from modules.image_enhancer import enhance_image
from modules.background_remover import remove_background
from modules.emotion_detection import detect_emotion

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="VisionAI Studio",
    page_icon="📸",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

def load_css():
    if os.path.exists("assets/style.css"):
        with open("assets/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ---------------- HEADER ---------------- #

st.markdown("""
<h1 style='text-align:center;'>✨ VisionAI Studio ✨</h1>

<p style='text-align:center;
font-size:20px;
color:gray;'>

📸 Upload • 🎨 Edit • 🤖 Analyze • 💜 Create Magic

</p>
""", unsafe_allow_html=True)

# ---------------- DASHBOARD ---------------- #

st.markdown("## 📊 VisionAI Dashboard")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🎨 AI Features", "10")

with c2:
    st.metric("📸 Images", "Unlimited")

with c3:
    st.metric("⚡ Speed", "<5 sec")

with c4:
    st.metric("🤖 AI Models", "6")

st.divider()

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🎀 VisionAI Studio")

style = st.sidebar.selectbox(
    "Choose AI Feature",
    [
        "🖼 Original",
        "😀 Face Detection",
        "🎨 Cartoon",
        "✨ Enhance Image",
        "🪄 Remove Background",
        "😊 Emotion Detection",
        "🎌 Anime (Coming Soon 🚀)",
        "🌸 Ghibli (Coming Soon 🚀)",
        "🧸 Pixar (Coming Soon 🚀)",
        "✏ Sketch (Coming Soon 🚀)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("🤖 AI Ready")
st.sidebar.info("📸 Upload an Image")
st.sidebar.write("💜 Made by Fozia")

# ---------------- WELCOME ---------------- #

st.info("""
👋 **Welcome to VisionAI Studio**

✨ Upload any image and explore powerful AI features.

✅ Face Detection

✅ Cartoon Effect

✅ AI Caption Generator

✅ Background Removal

✅ Image Enhancement

🚀 AI Style Transfer (Coming Soon)
""")

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📂 Upload your Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    image_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    col1, col2 = st.columns(2)

    # ---------------- ORIGINAL ---------------- #

    if style == "🖼 Original":

        with col1:
            st.subheader("📷 Original Image")
            st.image(
                image,
                use_container_width=True
            )

    # ---------------- FACE DETECTION ---------------- #

    elif style == "😀 Face Detection":

        result = detect_faces(image)

        with col1:
            st.image(
                image,
                caption="Original",
                use_container_width=True
            )

        with col2:
            st.image(
                result,
                caption="Detected Faces",
                use_container_width=True
            )

        st.success("🎉 Face Detection Completed!")
        st.balloons()

    # ---------------- CARTOON ---------------- #

    elif style == "🎨 Cartoon":

        cartoon = cartoonify(image)

        with col1:
            st.image(
                image,
                caption="Original",
                use_container_width=True
            )

        with col2:
            st.image(
                cartoon,
                caption="Cartoon Effect",
                use_container_width=True
            )
    # ---------------- IMAGE ENHANCER ---------------- #

    elif style == "✨ Enhance Image":

        enhanced = enhance_image(image)

        with col1:
            st.image(
                image,
                caption="Original",
                use_container_width=True
            )

        with col2:
            st.image(
                enhanced,
                caption="Enhanced Image",
                use_container_width=True
            )

        st.success("✨ Image Enhanced Successfully!")

    # ---------------- BACKGROUND REMOVER ---------------- #

    elif style == "🪄 Remove Background":

        bg = remove_background(image)

        with col1:
            st.image(
                image,
                caption="Original",
                use_container_width=True
            )

        with col2:
            st.image(
                bg,
                caption="Background Removed",
                use_container_width=True
            )

        st.success("🪄 Background Removed Successfully!")

    # ---------------- EMOTION DETECTION ---------------- #

    elif style == "😊 Emotion Detection":

        emotion = detect_emotion(image)

        with col1:
            st.image(
                image,
                caption="Original",
                use_container_width=True
            )

        with col2:

            st.subheader("🤖 AI Emotion Analysis")

            emoji = {
                "Happy": "😄",
                "Sad": "😢",
                "Angry": "😠",
                "Fear": "😨",
                "Surprise": "😲",
                "Neutral": "😐",
                "Disgust": "🤢",
                "Unknown": "❓",
                "No Face Detected": "🚫"
            }

            st.metric(
                "Detected Emotion",
                f"{emoji.get(emotion,'😊')} {emotion}"
            )

            if emotion == "Happy":
                st.success("Looks like you're having a great day! 🌸")

            elif emotion == "Sad":
                st.info("Hope everything gets better soon 💙")

            elif emotion == "Angry":
                st.warning("Take a short break 😌")

            elif emotion == "Fear":
                st.warning("Stay calm and take a deep breath 💜")

            elif emotion == "Surprise":
                st.success("Wow! Something surprised you 😄")

            elif emotion == "Neutral":
                st.info("You look calm and relaxed 😌")

            elif emotion == "Disgust":
                st.warning("Interesting expression detected 🤔")

            elif emotion == "No Face Detected":
                st.error("No clear face detected in the image.")

    # ---------------- COMING SOON ---------------- #

    elif style in [
        "🎌 Anime (Coming Soon 🚀)",
        "🌸 Ghibli (Coming Soon 🚀)",
        "🧸 Pixar (Coming Soon 🚀)",
        "✏ Sketch (Coming Soon 🚀)"
    ]:

        with col1:
            st.image(
                image,
                caption="📷 Original Image",
                use_container_width=True
            )

        with col2:

            st.info("🚀 Coming Soon")

            st.markdown("""

# 🎨 AI Style Transfer

These premium AI features will be released in **Version 2.0**

### Upcoming Features

- 🎌 Anime Style
- 🌸 Studio Ghibli Style
- 🧸 Pixar 3D Style
- ✏ Pencil Sketch

Stay tuned for exciting updates! 💜

""")

            st.success("Version 2.0 is under development.")
                # ---------------- AI CAPTION GENERATOR ---------------- #

    st.divider()

    st.subheader("✨ AI Caption Generator")

    if st.button("💜 Generate AI Caption"):

        with st.spinner("🤖 AI is writing a creative caption..."):

            try:

                caption = generate_caption(image_path)

                st.success("✅ Caption Generated!")

                st.info(caption)

            except Exception as e:

                st.error("❌ Caption Generation Failed")

                st.code(str(e))

    # ---------------- DOWNLOAD IMAGE ---------------- #

    st.divider()

    st.subheader("📥 Download")

    with open(image_path, "rb") as file:

        st.download_button(
            label="📥 Download Uploaded Image",
            data=file,
            file_name=uploaded_file.name,
            mime="image/png"
        )

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
    """
<div style="
text-align:center;
padding:30px;
background:#f5f7ff;
border-radius:18px;
margin-top:25px;
">

<h2>✨ VisionAI Studio</h2>

<p style="font-size:18px;">

😀 Face Detection &nbsp; | &nbsp;
🎨 Cartoon Effect &nbsp; | &nbsp;
🪄 Background Removal &nbsp; | &nbsp;
😊 Emotion Detection &nbsp; | &nbsp;
✨ Image Enhancement &nbsp; | &nbsp;
🤖 AI Caption Generator

</p>

<br>

<p style="font-size:17px;">

🚀 Built with Python • Streamlit • OpenCV • DeepFace • Google Gemini

</p>

<br>

<p style="color:gray;">

Version 1.0

</p>

<br>

<b>Made with ❤️ by Fozia</b>

</div>
""",
    unsafe_allow_html=True
)