import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    provider="auto",
    api_key=os.getenv("HF_TOKEN")
)

PROMPTS = {
    "🎌 Anime": "Convert this image into beautiful Japanese anime while preserving the person's identity.",
    "🌸 Ghibli": "Transform this image into Studio Ghibli style with soft pastel colors, dreamy lighting while preserving the face.",
    "🧸 Pixar": "Convert this image into Disney Pixar 3D animation style while preserving facial identity.",
    "✏ Sketch": "Convert this image into a realistic pencil sketch."
}


def generate_style(image_path, style):

    prompt = PROMPTS.get(style, "Transform this image.")

    try:

        with open(image_path, "rb") as f:

            image = client.image_to_image(
                image=f,
                prompt=prompt,
                model="Qwen/Qwen-Image-Edit"
            )

        os.makedirs("outputs", exist_ok=True)

        output_path = "outputs/generated.png"

        image.save(output_path)

        return output_path

    except Exception as e:
     import traceback
     traceback.print_exc()
     raise