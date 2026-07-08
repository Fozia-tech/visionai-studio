from PIL import ImageEnhance, ImageFilter

def enhance_image(image):

    # Increase Sharpness
    sharp = ImageEnhance.Sharpness(image)
    image = sharp.enhance(2.5)

    # Increase Contrast
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(1.4)

    # Increase Color
    color = ImageEnhance.Color(image)
    image = color.enhance(1.3)

    # Increase Brightness
    bright = ImageEnhance.Brightness(image)
    image = bright.enhance(1.1)

    # Final Sharpen Filter
    image = image.filter(ImageFilter.SHARPEN)

    return image