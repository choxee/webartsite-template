import streamlit as st

pages = {
    "Home": [
        st.Page("webartsite/0_home.py", title="Home - 1"),
    ],
    "Who we are": [
        st.Page("webartsite/1_who_we_are.py", title="Who we are - 1"),
    ],
    "Songs": [
        st.Page("webartsite/2_songs.py", title="Songs - 1"),
    ],
    "Live coding": [
        st.Page("webartsite/3_live_coding.py", title="Live coding - 1"),
    ],
    "Contacts": [
        st.Page("webartsite/4_contacts.py", title="Contacts - 1"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()