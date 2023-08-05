import streamlit as st

# titre du site
st.title("compressIMG")

# descriptif du site
st.write(
    "Descriptif du site : Lorem ipsum dolor sit amet consectetur. Metus lorem pulvinar quis urna bibendum gravida blandit non sed. Orci dui arcu tortor tortor imperdiet tortor hendrerit scelerisque."
)

# h1 Step 1
# title
st.write("# 📂 Step 1")

# widget drag & drop
uploaded_file = st.file_uploader(
    "Choose an image  file", ["PNG", "JPG", "WEBP"]
)

st.write("---")

# h1 Step 2
# title
st.write("# 🛠️ Step 2")
st.write("Custom your export file")

# 3 colones
col_1, col_2, col_3 = st.columns(3)
# - Name avec widget : st.text_input("You can rename your image compress", "name_file.png")
with col_1:
    st.write("### Name")
    st.text_input("You can rename your image compress", "name_file")

# - Quality & resize avec widget : st.slider('Resize', 0, 100, (55))
with col_2:
    st.write("### Quality & Resize")

    st.slider('Resize', 0, 100, (55))
    st.select_slider(
        "Quality of your image",
        options=["Poor", "Low", "Medium", "Good", "High"],
    )

# - Extension avec widget : st.selectbox("your extension", ("PNG", "JPG", "WEBP"),)
with col_3:
    st.write("### Extension")
    st.selectbox(
        "Your extension",
        ("PNG", "JPG", "WEBP"),
    )

st.write("---")

# h1 Step 3
# title
st.write("# 🗜️ Step 3")
st.write("Compress & download your compressed image ")
# 3 colones
col_4, col_5, col_6 = st.columns(3)

# - Compress avec widget : st.button("Compress")
with col_4:
    compress_btn = st.button("Compress", use_container_width=True)

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
