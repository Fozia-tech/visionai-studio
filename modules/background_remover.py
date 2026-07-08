from rembg import remove
from PIL import Image

def remove_background(image):

    output = remove(image)

    return output