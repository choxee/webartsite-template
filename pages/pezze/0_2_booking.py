import os

import streamlit as st

st.title("Booking")

st.info("Text us a summary of your booking request and we will reply as soon as possible!")

with st.form("my_form"):

    st.subheader("Contact form")
    st.text_input("Your name / organisation:")
    st.text_input("Your email")
    st.text_input("Your message:")

    st.form_submit_button('Send booking request')

st.info("You can also send a mail to pezze@pezze.com")
