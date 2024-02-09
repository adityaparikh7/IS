import random
import string
from PIL import Image, ImageDraw, ImageFont


def generate_image_captcha():
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    width, height = 500, 100
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 40)

    #printing text on image
    for i in range(len(captcha_text)):
        x = i * (width // len(captcha_text)) + 10
        y = 10
        draw.text((x, y), captcha_text[i], font=font, fill='black')

    # adding noise to the image  
    for _ in range(100):
        x = random.randint(0, width - 15)
        y = random.randint(0, height - 15)
        draw.point((x, y), fill='black')
    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill='black', width=2)

    image.show()

if __name__ == "__main__":
    generate_image_captcha()
