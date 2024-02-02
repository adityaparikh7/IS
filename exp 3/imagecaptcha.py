from PIL import Image, ImageDraw, ImageFont
import random
import string


def generate_captcha():
    # Generate a random string for the CAPTCHA
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    width, height = 500, 100
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
        x = random.randint(0, width - 15)
        y = random.randint(0, height - 15)
        draw.point((x, y), fill='black')
    for _ in range(5):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([start, end], fill='black')

    image.show()

if __name__ == "__main__":
    generate_captcha()
