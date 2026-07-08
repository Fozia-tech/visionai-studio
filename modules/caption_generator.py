import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_caption(image_path):
    image = Image.open(image_path)

    response = model.generate_content([
        "You are an AI social media expert. Look at this image and generate:\n"
        "1. One creative Instagram caption.\n"
        "2. Three relevant hashtags.\n"
        "Keep it short and attractive.",
        image
    ])

    return response.text