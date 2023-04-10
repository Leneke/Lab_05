# Task №1. Implement an application for downloading pictures with cats.
from PIL import Image
from easygui import *
import requests
import sys


def cats_img():
    # Get image and save to file
    response = requests.get("https://cataas.com/cat")
    if response.status_code == 200:
        with open("cats.png", "wb") as img_file:
            img_file.write(response.content)
            img_file.close()

    # Adjusting the image size
    image_path = "cats.png"
    img = Image.open(image_path)
    width = img.size[0]
    height = img.size[1]

    if width > height:
        if width > 500:
            new_width = 500
            new_height = int(new_width * height / width)
            new_img = img.resize((new_width, new_height), Image.LANCZOS)
            new_img.save("cats.png")

    else:
        height > width
        if height > 500:
            new_height = 500
            new_width = int(new_height * width / height)
            new_img = img.resize((new_width, new_height), Image.LANCZOS)
            new_img.save("cats.png")


def see_cats_image():
    # Customizing the graphical interface
    title = "Pictures with cats"
    msg = "Do you want to see pictures with cats?"
    choices = ["Yes, I love cats", "No, I don't want to"]
    reply = ccbox(msg, title, choices)
    try:
        while True:
            if reply:
                cats_img()
                msg = "Cats are so funny! Let's see the following picture?"
                image = "cats.png"
                choices = ["More cats", "No, I'm leaving"]
                result = ccbox(msg, title, choices, image)
                if result:
                    continue
                else:
                    # Какую запись лучше, правильнее использовать: break или sys.exit(0)?
                    sys.exit(0)
                    # break
            else:
                # break
                sys.exit(0)
    except Exception as error:
        print(f'Oops, all the cats have run away, come back later. Error: {error}')


if __name__ == "__main__":
    see_cats_image()
