import streamlit as st
from tools.tools_img import (
    manipulate_img,
    formated_name_img,
    scale_img,
    open_img,
    quality_img,
)

with open("style.css") as style:
    st.markdown(f"<style>{style.read}</style>", unsafe_allow_html=True)

# titre du site
st.title("CompressIMG")

# descriptif du site
st.write(
    """Descriptif du site : Lorem ipsum dolor sit amet consectetur.
    Metus lorem pulvinar quis urna bibendum gravida blandit non sed.
    Orci dui arcu tortor tortor imperdiet tortor hendrerit scelerisque."""
)

# h1 Step 1
st.write("# 📂 Choose an image  file")

# widget drag & drop
uploaded_file = st.file_uploader("", ["PNG", "JPG", "WEBP"])

st.write("---")

# h1 Step 2
st.write("# 🛠️ Custom your export file")

st.write("")

# 3 colones
col_1, col_2, col_3 = st.columns(3, gap="medium")

with col_1:
    st.write("#### Parameters")
    name_img = st.text_input("You can rename it:", "name_file")

    extention_img = st.selectbox(
        "Convert in:",
        ("PNG", "JPEG", "WEBP"),
    )

    resize_factor = st.slider('Resize', 0, 100, (50))
    quality_img = st.select_slider(
        "Quality",
        options=["Poor", "Low", "Medium", "Good", "High"],
        value="Medium",
    )

user_data_input = {
    "img_converted_name": name_img,
    "img_converted_extension": extention_img,
    "img_converted_scale": resize_factor,
    "img_converted_quality": quality_img,
}


with col_2:
    st.write("#### Preview")

    img_preview = open_img(uploaded_file)
    img_preview = scale_img(img_preview, user_data_input)

    if uploaded_file:
        st.image(img_preview)

# - Extension avec widget : st.selectbox("your extension", ("PNG", "JPG", "WEBP"),)
with col_3:
    st.write("#### Data")
    data_img = f"**name**: {name_img}  \n**format**: {extention_img}  \n**width**: {img_preview.size[0]}px  \n**height**: {img_preview.size[1]}px  \n**mode**: {img_preview.mode}"
    st.write(data_img)

st.write("---")


# h1 Step 3
st.write("# 🗜️ Compress & download")

# - Compress avec widget : st.button("Compress")

# - Une fois la compression terminée, le bouton Download apparait  avec widget : st.download_button()

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
