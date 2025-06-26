import os
import streamlit as st

from webartsite.path_config import contents_path
from css_load_utils import (
    load_strada_chiusa_css, set_background_image,
    get_enhanced_button_fix_css, get_enhanced_button_fix_js
)

st.set_page_config(layout="wide")

selected_art_project = "sc25"




# Load CSS
try:
    custom_css = load_strada_chiusa_css(selected_art_project)
    enhanced_button_css = get_enhanced_button_fix_css()
    full_css = custom_css + enhanced_button_css
    st.markdown("<style>" + full_css + "</style>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error loading CSS: {str(e)}")
    # Fallback CSS with button fixes
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, rgba(0,0,0,0.9), rgba(20,20,20,0.95));
        color: white;
        font-family: "Bebas Neue", sans-serif;
    }}

    {get_enhanced_button_fix_css()}
    </style>
    """, unsafe_allow_html=True)

# Add enhanced JavaScript
st.html(get_enhanced_button_fix_js())

# Page navigation structure
pages = {
    "SC25": [
        st.Page("pages/{}/0_1_home.py".format(selected_art_project), title="SC25"),
        st.Page("pages/{}/0_2_lineup.py".format(selected_art_project), title="Lineup"),
        st.Page("pages/{}/0_3_full_schedule.py".format(selected_art_project), title="Programma completo"),
    ],
    "Chi siamo": [
        st.Page("pages/{}/1_1_stradachiusa.py".format(selected_art_project), title="Strada Chiusa"),
        st.Page("pages/{}/1_2_onda.py".format(selected_art_project), title="L'Onda"),
        st.Page("pages/{}/1_3_network.py".format(selected_art_project), title="Rete"),
        st.Page("pages/{}/4_1_history.py".format(selected_art_project), title="Edizioni passate"),
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