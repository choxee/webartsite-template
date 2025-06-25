import os
import streamlit as st

from webartsite.path_config import contents_path
from css_load_utils import load_strada_chiusa_css, set_background_image

st.set_page_config(layout="wide")

selected_art_project = "sc25"

# Function to set background image (optional usage)
def set_custom_background_image(image_url):
    """Update the background image URL in the CSS template"""
    # This function can be used to dynamically change the background image
    # Example usage: set_custom_background_image("https://your-domain.com/path-to-your-background-image.jpg")
    pass

# Example usage: uncomment and modify the URL to set your background image
# set_custom_background_image("https://your-domain.com/path-to-your-background-image.jpg")

# Load all CSS using the utility function
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
        st.Page("pages/{}/1_2_stradachiusa.py".format(selected_art_project), title="Strada Chiusa"),
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