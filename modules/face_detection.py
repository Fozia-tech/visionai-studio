import cv2
import numpy as np

# Load the face detection model
face_cascade = cv2.CascadeClassifier(
    "models/haarcascade_frontalface_default.xml"
)

def detect_faces(image):
    # Convert uploaded image to NumPy array
    img = np.array(image)

    # Convert RGB to BGR (OpenCV format)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Convert back to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img