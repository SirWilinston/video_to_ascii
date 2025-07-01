from PIL import Image
from tkinter import filedialog
import os
import pathlib

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]
ASCII_CHARS.reverse()
directorio_jpg = # change this to the name you want for your ascii art directory

def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_heigth = int(new_width * ratio)
    resize_image = image.resize((new_width*2, new_heigth))
    return(resize_image)

def grayify(image):
    greyscale_image = image.convert("L")
    return greyscale_image

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return(characters)

def get_path():
    file_path = filedialog.askdirectory(
            initialdir="./",  # Optional: Set initial directory
            title="Seleccione el directorio de frames",
        )

    current = str(pathlib.Path(__file__).parent.resolve()).replace("\\","/")

    return file_path.replace(str(current + "/"), "")

if __name__ == "__main__":

    path = get_path()

    items = os.listdir(path)

    for item in items:
        imagen = Image.open(f"{path}/{item}")
        
        i = item.split(".")
        item = i[0]

        width = 110

        new_image_data = pixel_to_ascii(grayify(resize_image(imagen, width)))

        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i+(width*2))] for i in range(0, pixel_count, width*2))

        os.makedirs("ascii/" + directorio_jpg, exist_ok=True)

        with open(f"ascii/{directorio_jpg}/{item}.txt", "w") as text_file:
            text_file.write(ascii_image)
