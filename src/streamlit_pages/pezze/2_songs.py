import os

import streamlit as st

from src.webartsite.path_config import contents_path


st.title("Songs gallery")


def add_song_container(song):
    st.header(song)

    audio_path = "https://storage.googleapis.com/public-static-contents-test-0/webartsite-content-0/contents/pezze/audios/{}.mp3".format(
        song
    ).replace(" ", "%20")
    st.audio(audio_path)


add_song_container("La salut")
add_song_container("Il paese che vorrei")

