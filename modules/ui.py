import streamlit as st

def show_header():
    st.markdown("""
    <div style="
    background:linear-gradient(90deg,#8B5CF6,#EC4899);
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
    ">

    <h1>✨ AI Magic Photo Studio ✨</h1>

    <h4>📸 Upload • 🎨 Transform • 🤖 Generate • 🎤 Create Magic</h4>

    </div>
    """, unsafe_allow_html=True)


def show_footer():
    st.markdown("---")
    st.markdown(
        "<center>💜 Made with ❤️ by <b>Fozia</b> | AI • Computer Vision • Generative AI</center>",
        unsafe_allow_html=True,
    )