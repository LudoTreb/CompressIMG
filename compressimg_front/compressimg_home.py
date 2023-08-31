import io
import zipfile

import streamlit as st
from tools.tools_img import (
    compress_img,
    formated_name_img,
    get_filename_without_extension,
    manipulate_img,
    open_img,
    quality_img,
    scale_img,
)

st.markdown(
    "<h1 style='font-size: 5em;text-align: center; border: solid #2B1B3D; border-radius: 10px;'>CompressIMG</h1>",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

st.write(
    """👋 Welcome to CompressIMG. Your image compression tool!
    CompressIMG is a user-friendly web application designed to
    help you optimize and compress your images effortlessly.
    In just three easy steps, you can have your image
    ready for use on the web."""
)

st.write("---")

st.write("## 📂 Choose an image  file")


upload_files = st.file_uploader(
    "", ["PNG", "JPG", "WEBP"], accept_multiple_files=True
)

if 'a_counter' not in st.session_state:
    st.session_state['a_counter'] = 0

st.write("---")

st.write("## 🛠️ Custom your export file")

st.write("")


col_1, col_2, col_3 = st.columns(3, gap="medium")


# dictionary to store data input by user


with col_1:
    st.write("### Preview")

    if len(upload_files) == 0:
        st.markdown(
            """
    <style>
    [data-testid="stImage"]{
    border: 2px solid #D5D7DC;
    border-radius: 8px;
    opacity: 0.3;
    
    }
    </style>
    """,
            unsafe_allow_html=True,
        )

        img_url_3 = "https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png"
        st.image(
            img_url_3,
            caption="No image",
            width=200,
        )


with col_2:
    st.write("### Settings")
    seq_img_btn = st.checkbox("Image sequence")
    if not seq_img_btn:
        st.write(
            "Check the box if you want same settings for all your images and compress them at once."
        )
    else:
        st.write("Choose your settings and compress all yours images")

    if len(upload_files) == 0:
        img_name_default = "name_file"
        img_name_choosed = st.text_input("Rename:", img_name_default)

        extention_img = st.selectbox(
            "Convert in:",
            ("PNG", "JPEG", "WEBP"),
        )

        resize_factor = st.slider(
            'Resize',
            1,
            100,
            50,
            key="slider",
        )
        quality_img = st.select_slider(
            "Quality",
            options=["Poor", "Low", "Medium", "Good", "High"],
            value="Medium",
        )

with col_3:
    st.write("### Compress")
    if len(upload_files) == 0:
        data_img_waiting = (
            f"**name**: none  \n"
            f"**format**: none  \n"
            f"**width**: none px  \n"
            f"**height**: none px  \n"
            f"**weight**: none octets"
        )
        st.write(data_img_waiting)


if upload_files:
    if not seq_img_btn:
        with col_3:
            if st.session_state['a_counter'] < len(upload_files) - 1:
                if st.button(
                    "Next",
                    use_container_width=True,
                ):
                    st.session_state['a_counter'] += 1
        with col_2:
            img_name_default = get_filename_without_extension(
                upload_files[st.session_state['a_counter']].name
            )

            img_name_choosed = st.text_input("Rename:", img_name_default)

            extention_img = st.selectbox(
                "Convert in:",
                ("PNG", "JPEG", "WEBP"),
            )

            resize_factor = st.slider(
                'Resize',
                1,
                100,
                50,
                key="slider",
            )
            quality_img = st.select_slider(
                "Quality",
                options=["Poor", "Low", "Medium", "Good", "High"],
                value="Medium",
            )

        user_data_input = {
            "img_converted_name": img_name_choosed,
            "img_converted_extension": extention_img,
            "img_converted_scale": resize_factor,
            "img_converted_quality": quality_img,
        }

        with col_1:
            img_preview = open_img(upload_files[st.session_state['a_counter']])
            img_preview = scale_img(img_preview, user_data_input)

            img_preview_weight_quality = compress_img(
                img_preview, user_data_input
            )
            st.image(img_preview_weight_quality)
            number_image = f"image {st.session_state['a_counter'] + 1}/{len(upload_files)}"
            st.write(number_image)

            with col_3:
                data_img = (
                    f"**name**: {img_name_choosed}  \n"
                    f"**format**: {extention_img}  \n"
                    f"**width**: {img_preview.size[0]} px  \n"
                    f"**height**: {img_preview.size[1]} px  \n"
                    f"**weight**: {img_preview_weight_quality.getbuffer().nbytes/100} octets"
                )

                compress_btn = st.button(
                    "Compress",
                    use_container_width=True,
                )

                if compress_btn:
                    img_preview = upload_files[st.session_state['a_counter']]
                    img_preview = open_img(img_preview)
                    img_preview = scale_img(img_preview, user_data_input)

                    img_compressed = manipulate_img(
                        upload_files[st.session_state['a_counter']],
                        user_data_input,
                    )

                    st.download_button(
                        "Download your image",
                        data=img_compressed,
                        file_name=formated_name_img(user_data_input),
                        mime=f"image/{user_data_input['img_converted_extension'].lower()}",
                        use_container_width=True,
                    )

                st.write(data_img)

    else:
        with col_2:
            img_name_default = get_filename_without_extension(
                upload_files[st.session_state['a_counter']].name
            )

            img_name_choosed = st.text_input("Rename:", img_name_default)

            extention_img = st.selectbox(
                "Convert in:",
                ("PNG", "JPEG", "WEBP"),
            )

            resize_factor = st.slider(
                'Resize',
                1,
                100,
                50,
                key="slider",
            )
            quality_img = st.select_slider(
                "Quality",
                options=["Poor", "Low", "Medium", "Good", "High"],
                value="Medium",
            )

        user_data_input = {
            "img_converted_name": img_name_choosed,
            "img_converted_extension": extention_img,
            "img_converted_scale": resize_factor,
            "img_converted_quality": quality_img,
        }

        with col_1:
            img_preview = open_img(upload_files[st.session_state['a_counter']])
            img_preview = scale_img(img_preview, user_data_input)

            img_preview_weight_quality = compress_img(
                img_preview, user_data_input
            )
            st.image(img_preview_weight_quality)
            number_image = f"image {st.session_state['a_counter'] + 1}/{len(upload_files)}"
            st.write(number_image)

        with col_3:
            compress_btn = st.button(
                "Compress",
                use_container_width=True,
            )
            if compress_btn:
                compressed_images = []
                for index, image in enumerate(upload_files):
                    img_compressed = manipulate_img(image, user_data_input)
                    compressed_images.append(
                        {
                            "name": user_data_input["img_converted_name"]
                            + "_"
                            + str(index)
                            + "."
                            + user_data_input[
                                "img_converted_extension"
                            ].lower(),
                            "data": img_compressed,
                        }
                    )
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(
                    zip_buffer, 'x', zipfile.ZIP_DEFLATED, False
                ) as myzip:
                    for compressed_image in compressed_images:
                        myzip.writestr(
                            compressed_image["name"], compressed_image["data"]
                        )
                myzip.printdir()
                st.download_button(
                    "Download all images",
                    data=zip_buffer.getvalue(),
                    file_name="compressed_images.zip",
                    use_container_width=True,
                )
