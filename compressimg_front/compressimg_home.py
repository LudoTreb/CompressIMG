import streamlit as st
from tools.tools_img import manipulate_img


# titre du site
st.title("compressIMG")

# descriptif du site
st.write(
    """Descriptif du site : Lorem ipsum dolor sit amet consectetur.
    Metus lorem pulvinar quis urna bibendum gravida blandit non sed.
    Orci dui arcu tortor tortor imperdiet tortor hendrerit scelerisque."""
)

# h1 Step 1
st.write("# 📂 Step 1")

# widget drag & drop
uploaded_file = st.file_uploader(
    "Choose an image  file", ["PNG", "JPG", "WEBP"]
)

st.write("---")

# h1 Step 2
st.write("# 🛠️ Step 2")
st.write("Custom your export file")

# 3 colones
col_1, col_2, col_3 = st.columns(3)
# - Name avec widget : st.text_input("You can rename your image compress", "name_file.png")
with col_1:
    st.write("### Name")
    name_img = st.text_input("You can rename your image compress", "name_file")

# - Quality & resize avec widget : st.slider('Resize', 0, 100, (55))
with col_2:
    st.write("### Quality & Resize")

    resize_factor = st.slider('Resize', 0, 100, (55))
    quality_img = st.select_slider(
        "Quality of your image",
        options=["Poor", "Low", "Medium", "Good", "High"],
    )

# - Extension avec widget : st.selectbox("your extension", ("PNG", "JPG", "WEBP"),)
with col_3:
    st.write("### Extension")
    extention_img = st.selectbox(
        "Your extension",
        ("PNG", "JPEG", "WEBP"),
    )

st.write("---")

user_data_input = {
    "img_converted_name": name_img,
    "img_converted_extension": extention_img,
    "img_converted_scale": resize_factor,
    "img_converted_quality": quality_img,
}


# h1 Step 3
st.write("# 🗜️ Step 3")
st.write("Compress & download your compressed image ")
# 3 colones
col_4, col_5, col_6 = st.columns(3)

# - Compress avec widget : st.button("Compress")
with col_4:
    compress_btn = st.button("Compress", use_container_width=True)
    if uploaded_file:
        if compress_btn:
            img_compressed = manipulate_img(uploaded_file, user_data_input)
            st.image(img_compressed)

# - Une fois la compression terminée, le bouton Download apparait  avec widget : st.download_button()

with col_5:
    is_button_true = True

    if compress_btn:
        is_button_true = False
    else:
        is_button_true = True

    download_btn = st.button(
        "Download", disabled=is_button_true, use_container_width=True
    )


# - Une fois le download terminé, un emoji pouce apparait.
with col_6:
    if download_btn:
        st.write("👍")
