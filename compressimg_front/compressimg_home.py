import streamlit as st
from tools.tools_img import (
    manipulate_img,
    formated_name_img,
    scale_img,
    open_img,
    quality_img,
    compress_img,
    get_filename_without_extension,
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


with col_2:
    st.write("### Parameters")
    img_name_default = "name_file"
    if upload_files:
        img_name_default = get_filename_without_extension(
            upload_files[st.session_state['a_counter']].name
        )

    img_name_choosed = st.text_input("You can rename it:", img_name_default)

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
# dictionary to store data input by user
user_data_input = {
    "img_converted_name": img_name_choosed,
    "img_converted_extension": extention_img,
    "img_converted_scale": resize_factor,
    "img_converted_quality": quality_img,
}

with col_1:
    st.write("### Preview")

with col_3:
    st.write("### Compress")

    if upload_files:
        if st.session_state['a_counter'] < len(upload_files) - 1:
            if st.button("Next"):
                st.session_state['a_counter'] += 1
        with col_1:
            img_preview = open_img(upload_files[st.session_state['a_counter']])
            img_preview = scale_img(img_preview, user_data_input)

            img_preview_weight_quality = compress_img(
                img_preview, user_data_input
            )
            st.image(img_preview_weight_quality)

            with col_3:
                data_img = (
                    f"**name**: {img_name_choosed}  \n"
                    f"**format**: {extention_img}  \n"
                    f"**width**: {img_preview.size[0]} px  \n"
                    f"**height**: {img_preview.size[1]} px  \n"
                    f"**weight**: {img_preview_weight_quality.getbuffer().nbytes/100} octets"
                )
                st.write(data_img)
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

        with col_1:
            number_image = f"image {st.session_state['a_counter'] + 1}/{len(upload_files)}"
            st.write(number_image)
            img_preview = upload_files[st.session_state['a_counter']]
            img_preview = open_img(img_preview)
            img_preview = scale_img(img_preview, user_data_input)
