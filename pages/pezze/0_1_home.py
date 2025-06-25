import os

import streamlit as st

from webartsite.path_config import contents_path

logo_path = os.path.join(contents_path, "pezze/images/pezze_logo.jpeg")
st.image(logo_path, use_container_width=True)

