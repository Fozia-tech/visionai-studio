import cv2
import numpy as np

def cartoonify(image):

    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        8
    )

    color = img

    for _ in range(2):
        color = cv2.bilateralFilter(color, 7, 120, 120)

    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)

    return cartoon