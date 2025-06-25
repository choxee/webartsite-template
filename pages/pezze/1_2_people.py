import os

import streamlit as st

from webartsite.path_config import contents_path

st.title("People")

st.warning("PEZZE IN RANDOM ORDER")

columns = st.columns((1, 1, 1, 1, 1))

def add_member_container(member_name, st_container):
    st_container.header(member_name)


def load_members():
    member_names = {"Joe Cagnaccio", "Choxee", "Addome", "Enrico Barnetto", "San Gohan"}
    member_names = list(set(member_names))
    return member_names

for i in range(len(load_members())):
    member_name = load_members()[i]
    add_member_container(member_name, columns[i])

