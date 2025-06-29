import os
import streamlit as st

from src.webartsite.path_config import contents_path

st.set_page_config(layout="wide")

selected_art_project = "pezze"


pages = {
    "Home": [
        st.Page("src/streamlit_pages/{}/0_1_home.py".format(selected_art_project), title="Home"),
        st.Page("src/streamlit_pages/{}/0_2_booking.py".format(selected_art_project), title="Bookings"),
    ],
    "About": [
        st.Page("src/streamlit_pages/{}/1_1_band.py".format(selected_art_project), title="Band"),
        st.Page("src/streamlit_pages/{}/1_2_people.py".format(selected_art_project), title="People"),
        st.Page("src/streamlit_pages/{}/1_3_network.py".format(selected_art_project), title="Network"),

    ],
    "Songs": [
        st.Page("src/streamlit_pages/{}/2_songs.py".format(selected_art_project), title="Songs"),
    ],
    "Live coding": [
        st.Page("src/streamlit_pages/{}/3_1_live_coding_music.py".format(selected_art_project), title="Music"),
        st.Page("src/streamlit_pages/{}/3_2_live_coding_visuals.py".format(selected_art_project), title="Visuals"),
        st.Page("src/streamlit_pages/{}/3_3_live_coding_choreography.py".format(selected_art_project), title="Choreography"),
    ],
    "Contacts": [
        st.Page("src/streamlit_pages/{}/4_1_contacts_social.py".format(selected_art_project), title="Social"),
        st.Page("src/streamlit_pages/{}/4_2_contacts_booking.py".format(selected_art_project), title="Booking"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()