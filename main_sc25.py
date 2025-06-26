import os
import streamlit as st

from webartsite.path_config import contents_path
from css_load_utils import load_strada_chiusa_css, set_background_image

st.set_page_config(layout="wide", page_icon="https://storage.googleapis.com/public-static-contents-test-0/logo_sc_photo_background.jpeg")

selected_art_project = "sc25"

try:
    custom_css = load_strada_chiusa_css(selected_art_project)
    st.markdown("<style>" + custom_css + "</style>", unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error loading CSS: {str(e)}")
    # Fallback: load basic styling
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, rgba(0,0,0,0.9), rgba(20,20,20,0.95));
        color: white;
        font-family: "Bebas Neue", sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)


# Page navigation structure
pages = {
    "SC25": [
        st.Page("pages/{}/0_1_home.py".format(selected_art_project), title="SC25"),
        st.Page("pages/{}/0_2_lineup.py".format(selected_art_project), title="Lineup"),
        st.Page("pages/{}/0_3_full_schedule.py".format(selected_art_project), title="Programma completo"),
    ],
    "Chi siamo": [
        st.Page("pages/{}/1_1_stradachiusa.py".format(selected_art_project), title="Strada Chiusa"),
        st.Page("pages/{}/1_2_history.py".format(selected_art_project), title="Edizioni passate"),
        st.Page("pages/{}/1_3_onda.py".format(selected_art_project), title="L'Onda"),
        st.Page("pages/{}/1_4_network.py".format(selected_art_project), title="Rete"),
    ],
    "Partners": [
        st.Page("pages/{}/4_1_partners.py".format(selected_art_project), title="Partners"),
        st.Page("pages/{}/4_1_donations.py".format(selected_art_project), title="Donazioni"),
    ],
    "Contatti": [
        st.Page("pages/{}/4_1_collaborate.py".format(selected_art_project), title="Collabora"),
        st.Page("pages/{}/4_1_contacts_social.py".format(selected_art_project), title="Social"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()