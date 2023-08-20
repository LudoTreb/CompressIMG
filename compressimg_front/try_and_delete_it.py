import streamlit as st
from tools.tools_img import scale_img, open_img


st.title("test")

# st.session_state

liste = ["a", "b", "c"]


upfiles = st.file_uploader(
    "", ["PNG", "JPG", "WEBP"], accept_multiple_files=True
)


# st.session_state

if 'a_counter' not in st.session_state:
    st.session_state['a_counter'] = 0


number_image = "number of image: it is the first one"

if upfiles:
    next_image = st.button("Next Image")
    if st.session_state['a_counter'] < len(upfiles) - 1:
        if next_image:
            number_image = f"number of image: {st.session_state['a_counter'] + 2}/{len(upfiles)}"
            st.session_state['a_counter'] += 1
            # st.session_state
    else:
        number_image = "number of image: it was the last one"
        button_restart = st.button("restart")
        if button_restart:
            st.session_state['a_counter'] = 0

    st.write(number_image)


col_1, col_2, col_3 = st.columns(3, gap="medium")


with col_2:
    resize_factor = st.slider(
        'Resize',
        1,
        100,
        50,
        key="slider",
    )

img_name_choosed = "test"
extention_img = "jpg"
quality_img = 80

user_data_input = {
    "img_converted_name": img_name_choosed,
    "img_converted_extension": extention_img,
    "img_converted_scale": resize_factor,
    "img_converted_quality": quality_img,
}

with col_1:
    if upfiles:
        img_preview = upfiles[st.session_state['a_counter']]
        img_preview = open_img(img_preview)
        img_preview = scale_img(img_preview, user_data_input)
        st.image(img_preview)
