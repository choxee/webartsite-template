import os
import streamlit as st
from webartsite.path_config import contents_path

# Titolo principale
# st.title("Strada Chiusa 2025")

# Initialize sidebar state - collapsed by default
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "collapsed"  # or "collapsed" if you want it closed by default

st.markdown("---")

# Call to Action principale
col1, col2 = st.columns(2)
with col1:
    if st.button("Line-up", use_container_width=True):
        st.switch_page("pages/sc25/0_2_lineup.py")

with col2:
    if st.button("Programma Completo", use_container_width=True):
        st.switch_page("pages/sc25/0_2_full_schedule.py")

# Header con locandina principale
st.image("https://storage.googleapis.com/public-static-contents-test-0/locandina_sc25.jpg", use_container_width=True)

st.markdown("---")

# Chi Siamo - Sezione principale
st.header("🌊 Chi Siamo")
st.info("""
**L'Onda** è l'associazione culturale no-profit che dal 2014 porta "Strada Chiusa" ad Acquaviva delle Fonti. 

Siamo un gruppo di giovani che crede nel potere della cultura urbana per rivitalizzare gli spazi e unire la comunità. 

Con **oltre 60 volontari** e **migliaia di partecipanti** ogni anno, continuiamo a celebrare la musica, l'arte e lo sport di strada.

Unisciti a noi!
""")

# Numeri chiave
st.subheader("📊 I Nostri Numeri")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Edizioni", "11+", delta="2025")
with col2:
    st.metric("Volontari", "60+", delta="Sempre in crescita")
with col3:
    st.metric("Partecipanti", "Migliaia", delta="Ogni anno")
with col4:
    st.metric("Anni di Storia", "11", delta="Dal 2014")

st.markdown("---")

# Anteprima Edizioni Passate
st.header("🎭 Le Nostre Edizioni")
st.write("**Dieci anni di storia, musica e cultura.** Rivivi i momenti salienti delle edizioni passate:")

# Highlights delle edizioni passate
highlight_col1, highlight_col2, highlight_col3 = st.columns(3)

with highlight_col1:
    st.subheader("🎤 2016 - ONYX")
    st.write("I pionieri dell'hardcore rap americano ad Acquaviva!")

with highlight_col2:
    st.subheader("🎵 2019 - DAS EFX")
    st.write("Leggende hip-hop direttamente dagli Stati Uniti")

with highlight_col3:
    st.subheader("❤️ 2023 - Edizione X")
    st.write("Tributo a Roberto Surico e raccolta fondi AIRC")

if st.button("📸 Esplora le Edizioni Passate", use_container_width=True):
    st.switch_page("pages/sc25/4_1_history.py")

st.markdown("---")
st.success("**La strada racconta, a chi sa ascoltare...**")