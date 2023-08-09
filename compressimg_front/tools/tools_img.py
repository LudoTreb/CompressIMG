import streamlit as st
from PIL import Image
import io

# données pour faire des essais
mon_image = "flower.png"
user_data_input = {
    "img_converted_name": "flower_compress",
    "img_converted_extension": "JPEG",
    "img_converted_scale": 50,
    "img_converted_quality": "Medium",
}


def formated_name_img(data_input):
    """format the complete name of the img file.
    Concatenation of name + extension.

    Args:
        data_input (dict): all data given by the user

    Returns:
        str: name file + extension
    """

    name_img = data_input["img_converted_name"].lower()
    extension_img = data_input["img_converted_extension"]

    if extension_img == "JPEG":
        extention = "jpg"

        extension_img = extention
        ok_name_img = f"{name_img}.{extension_img}"

    else:
        ok_name_img = f"{name_img}.{extension_img.lower()}"

    return ok_name_img


def compress_img(img, data_input):
    """Save an image with some parameter
    like quality to reduce the weight.

    Args:
        img (class 'PIL.Image.Image'): image file
        data_input (dict): all data given by the user

    Returns:
        class 'PIL.Image.Image': an compressed image
    """

    quality_correspondence = {
        "Poor": 10,
        "Low": 30,
        "Medium": 50,
        "Good": 70,
        "High": 90,
    }

    if img.mode != "RGB":
        img = img.convert("RGB")

    quality = quality_correspondence.get(data_input["img_converted_quality"])

    output_buffer = io.BytesIO()

    img.save(
        output_buffer,
        format=data_input["img_converted_extension"],
        optimize=True,
        quality=quality,
    )

    return output_buffer.getvalue()


def scale_img(img, data_input):
    """Resize an image. Homothetique.

    Args:
        img (class 'PIL.Image.Image'): image file
        data_input (dict): all data given by the user

    Returns:
         class 'PIL.Image.Image': an resized image
    """

    scale_factor = data_input["img_converted_scale"] / 100

    new_img_width = int(img.width * scale_factor)
    new_img_height = int(img.height * scale_factor)
    resized_img = img.copy()
    resized_img = img.resize((new_img_width, new_img_height))

    return resized_img


def manipulate_img(img_path, data_input):
    """The function use all the other to compress an image.
    Reduce the quality, resize, rename, convert & save.

    Args:
        img_path (str): image file
        data_input (dict): all data given by the user

    Returns:
        class 'PIL.Image.Image': a compressed image
    """

    img_uploaded = Image.open(img_path)

    resized_img = scale_img(img_uploaded, data_input)

    img_compressed = compress_img(resized_img, data_input)

    return img_compressed
