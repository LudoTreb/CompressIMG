import streamlit as st
from tools.tools_img import (
    manipulate_img,
    formated_name_img,
    scale_img,
    open_img,
    quality_img,
    compress_img,
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


uploaded_file = st.file_uploader("", ["PNG", "JPG", "WEBP"])


st.write("---")

st.write("## 🛠️ Custom your export file")

st.write("")


col_1, col_2, col_3 = st.columns(3, gap="medium")

with col_1:
    st.write("### Parameters")
    name_img = st.text_input("You can rename it:", "name_file")

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
    "img_converted_name": name_img,
    "img_converted_extension": extention_img,
    "img_converted_scale": resize_factor,
    "img_converted_quality": quality_img,
}


with col_2:
    st.write("### Preview")
    if uploaded_file:
        img_preview = open_img(uploaded_file)
        img_preview = scale_img(img_preview, user_data_input)

        img_preview_weight_quality = compress_img(img_preview, user_data_input)

        if uploaded_file:
            st.image(img_preview_weight_quality)


with col_3:
    st.write("### Data")
    if uploaded_file:
        data_img = (
            f"**name**: {name_img}  \n"
            f"**format**: {extention_img}  \n"
            f"**width**: {img_preview.size[0]} px  \n"
            f"**height**: {img_preview.size[1]} px  \n"
            f"**weight**: {img_preview_weight_quality.getbuffer().nbytes/100} octets"
        )
        st.write(data_img)

st.write("---")


st.write("## 🗜️ Compress & download")

compress_btn = st.button("Compress", use_container_width=True)

is_button_true = True
img_compressed = uploaded_file

if uploaded_file:
    if compress_btn:
        img_compressed = manipulate_img(uploaded_file, user_data_input)
        is_button_true = False

    st.download_button(
        "Download your image",
        data=img_compressed,
        file_name=formated_name_img(user_data_input),
        mime=f"image/{user_data_input['img_converted_extension'].lower()}",
        use_container_width=True,
        disabled=is_button_true,
    )
