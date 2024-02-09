import random
import string

def generate_captcha(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

def main():
    length = int(input("Enter the length of the CAPTCHA: "))
    print(generate_captcha(length))


if __name__ == "__main__":
    main()
