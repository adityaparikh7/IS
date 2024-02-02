from PIL import Image, ImageDraw, ImageFont
import random
import string


def generate_captcha():
    # Generate a random string for the CAPTCHA
    captcha_text = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=6))

    # Set the width and height of the image
    width, height = 500, 100

    # Create a new image with a white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Choose a font (you may need to adjust the path based on your system)
    font = ImageFont.truetype("arial.ttf", 40)

    # Randomly rotate the characters for additional complexity
    for i in range(len(captcha_text)):
        rotation = random.randint(-30, 30)
        draw.text((i * (width // len(captcha_text)) + 10, 10),
                  captcha_text[i], font=font, fill='black', angle=rotation)

    # Add some noise (random pixels) to the image
    for _ in range(100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill='black')

    # Save or display the image
    image.show()
    # image.save('captcha.png')


if __name__ == "__main__":
    generate_captcha()
