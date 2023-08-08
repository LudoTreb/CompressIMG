import streamlit as st
from tools.tools_img import manipulate_img, formated_name_img


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
# 3 colones
col_4, col_5, col_6 = st.columns(3)

# - Compress avec widget : st.button("Compress")
with col_4:
    st.write("Oginal data image")
    # TODO ajouter une preview de limage originale + différent info

with col_5:
    st.write("Preview data compressed image")
    # TODO ajouter une preview de l'image compressée + différentes info size, name... si possible une evalution du poid de l'image


# - Une fois la compression terminée, le bouton Download apparait  avec widget : st.download_button()
with col_6:
    st.write("Compress & download")
    compress_btn = st.button("Compress", use_container_width=True)
    is_button_true = True

    if uploaded_file:
        if compress_btn:
            img_compressed = manipulate_img(uploaded_file, user_data_input)

            is_button_true = False

            # FIXME Probleme de nom fichier quand on choisit PNG ou WEBP et que le fichier d'origine est en png. il met "streamlit_download" au lieu du nom rentré ?
            # FIXME Faire apparaitre le bouton dowload mais pas cliquable. Devient cliquable si compress est cliqué.
            download_btn = st.download_button(
                "Download your image",
                data=img_compressed,
                file_name=formated_name_img(user_data_input),
                mime=f"image/{user_data_input['img_converted_extension'].lower()}",
                use_container_width=True,
                disabled=is_button_true,
            )
