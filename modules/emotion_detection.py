from deepface import DeepFace
import numpy as np


def detect_emotion(image):

    img = np.array(image)

    try:

        result = DeepFace.analyze(
            img_path=img,
            actions=["emotion"],
            enforce_detection=False,
            silent=True
        )

        # DeepFace may return a list or a dict
        if isinstance(result, list):
            result = result[0]

        emotion = result.get("dominant_emotion", "Unknown")

        return emotion.capitalize()

    except Exception:
        return "No Face Detected"