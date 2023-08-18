from PIL import Image
from pathlib import Path
import io


def get_filename_without_extension(filename: str, suffix="_compress"):
    """Get the name of the file without his extension and add an suffix.
    By default suffix is '_compress' Example: flower.png -> flower_compress

    Args:
        filename (str): the filename complete
        suffix (str, optional): Defaults to "_compress".

    Returns:
        str: concatenation of new filename and suffix
    """
    return Path(filename).stem + suffix


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


def quality_img(data_input):
    """Convert from dictionary the input string from the user into an integer.
     This integer is the reduce quality factor.

    Args:
        data_input (dict):  all data given by the user

    Returns:
        int: This integer is the reduce quality factor
    """

    quality_correspondence = {
        "Poor": 10,
        "Low": 30,
        "Medium": 50,
        "Good": 70,
        "High": 90,
    }

    quality = quality_correspondence.get(data_input["img_converted_quality"])

    return quality


def compress_img(img, data_input):
    """Save an image with some parameter
    like quality to reduce the weight.

    Args:
        img (class 'PIL.Image.Image'): image file
        data_input (dict): all data given by the user

    Returns:
        class '_io.BytesIO': output_buffer an compressed data byte
    """

    if img.mode != "RGB":
        img = img.convert("RGB")

    quality = quality_img(data_input)

    output_buffer = io.BytesIO()

    img.save(
        output_buffer,
        format=data_input["img_converted_extension"],
        optimize=True,
        quality=quality,
    )

    return output_buffer


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


def open_img(img_path):
    """open an image from is location path.

    Args:
        img_path (str): the location path of the image.

    Returns:
         class 'PIL.Image.Image': the image uploaded.
    """
    img_uploaded = Image.open(img_path)

    return img_uploaded


def manipulate_img(img_path, data_input):
    """The function use all the other to compress an image.
    Reduce the quality, resize, rename, convert & save.

    Args:
        img_path (str): image file
        data_input (dict): all data given by the user

    Returns:
        class 'PIL.Image.Image': a compressed image
    """

    img_uploaded = open_img(img_path)

    resized_img = scale_img(img_uploaded, data_input)

    img_compressed = compress_img(resized_img, data_input)

    return img_compressed.getvalue()
