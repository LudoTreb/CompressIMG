import streamlit as st
from PIL import Image

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

    if data_input["img_converted_extension"] == "JPEG":
        extention = "jpg"

        extension_img = extention
        ok_name_img = f"{name_img}.{extension_img}"

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
    ok_name_img = formated_name_img(data_input)

    if img.mode != "RGB":
        img = img.convert("RGB")

    quality_correspondence = {
        "Poor": 10,
        "Low": 30,
        "Medium": 50,
        "Good": 70,
        "High": 90,
    }
    quality = quality_correspondence.get(data_input["img_converted_quality"])
    # print(f"filename : {img.filename}, type: {type(img.filename)}")
    img_compressed = img.copy()
    # print(
    #     f"filename : {img_compressed.filename}, type: {type(img_compressed.filename)}"
    # )
    print(
        f"format : {data_input['img_converted_extension']}, type: {type(data_input['img_converted_extension'])}"
    )
    print(f"name : {ok_name_img}, type: {type(ok_name_img)}")
    img_compressed.save(
        ok_name_img,
        format=data_input["img_converted_extension"],
        optimize=True,
        quality=quality,
    )
    print(f"size : {img_compressed.size}, type: {type(img_compressed.size)}")
    print(
        f"format : {img_compressed.format}, format: {type(img_compressed.format)}"
    )
    # print(
    #     f"filename : {img_compressed.filename}, type: {type(img_compressed.filename)}"
    # )

    return img_compressed


def scale_img(img, data_input):
    """Resize an image. Homothetique.

    Args:
        img (class 'PIL.Image.Image'): image file
        data_input (dict): all data given by the user

    Returns:
         class 'PIL.Image.Image': an resized image
    """
    scale_factor = data_input["img_converted_scale"] / 100
    # print(
    #     f"filename_resizing_img_before : {img.filename}, type: {type(img.filename)}"
    # )
    new_img_width = int(img.width * scale_factor)
    new_img_height = int(img.height * scale_factor)
    resized_img = img.copy()
    resized_img = img.resize((new_img_width, new_img_height))
    # print(
    #     f"filename_resizing_img_after : {resized_img.filename}, type: {type(resized_img.filename)}"
    # )

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
    # print(
    #     f"filename_img_uploaded : {img_uploaded.filename}, type: {type(img_uploaded.filename)}"
    # )

    resized_img = scale_img(img_uploaded, data_input)
    # print(
    #     f"filename_resized_img : {resized_img.filename}, type: {type(resized_img.filename)}"
    # )
    img_compressed = compress_img(resized_img, data_input)

    return img_compressed


img_compressed = manipulate_img(mon_image, user_data_input)

print(type(img_compressed))
