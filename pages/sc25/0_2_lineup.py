import os
import streamlit as st
from webartsite.path_config import contents_path

st.markdown("---")

# Headliners Section
st.header("Lineup")

headliner_col1, headliner_col2 = st.columns(2)

with headliner_col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(220, 38, 38, 0.1); border-radius: 12px; margin-top: 1rem;">
        <h3 style="color: #dc2626; margin-bottom: 0.5rem;">ONYX (Queens, New York)</h3>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://storage.googleapis.com/public-static-contents-test-0/Onyx.png", use_container_width=True)



with headliner_col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(220, 38, 38, 0.1); border-radius: 12px; margin-top: 1rem;">
        <h3 style="color: #dc2626; margin-bottom: 0.5rem;">DOPE D.O.D. ( Groningen, Paesi Bassi)</h3>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://storage.googleapis.com/public-static-contents-test-0/Dope.png", use_container_width=True)


# Italian Artists Section
#st.header("🇮🇹 Artisti Italiani")

# Row 1: Extrapolo & Corveleno
italian_col1, italian_col2 = st.columns(2)

with italian_col1:

    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(239, 68, 68, 0.1); border-radius: 12px; margin-top: 1rem;">
        <h3 style="color: #ef4444; margin-bottom: 0.5rem;">EXTRAPOLO (Napoli/NYC) - Host</h3>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://storage.googleapis.com/public-static-contents-test-0/Polo.png", use_container_width=True)

with italian_col2:

    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(239, 68, 68, 0.1); border-radius: 12px; margin-top: 1rem;">
        <h3 style="color: #ef4444; margin-bottom: 0.5rem;">CORVELENO (Roma)</h3>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://storage.googleapis.com/public-static-contents-test-0/corveleno%20(2).png", use_container_width=True)

# Row 2: No Fang & Ellie Cottino
italian_col3, italian_col4 = st.columns(2)

with italian_col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(248, 113, 113, 0.1); border-radius: 12px; margin-top: 1rem;">
        <h3 style="color: #f87171; margin-bottom: 0.5rem;">NO FANG (Puglia)</h3>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://storage.googleapis.com/public-static-contents-test-0/Nofang.png")

with italian_col4:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(248, 113, 113, 0.1); border-radius: 12px; margin-top: 1rem;">
        <h3 style="color: #f87171; margin-bottom: 0.5rem;">ELLIE COTTINO & SISTA SOFY (Torino)</h3>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://storage.googleapis.com/public-static-contents-test-0/Ellie.png")

st.markdown("---")

# Special Events Section
st.header("Tecniche perfette- Campionato nazionale di freestyle")

st.image("https://storage.googleapis.com/public-static-contents-test-0/Tecniche perfette (2).png", use_container_width=True)

st.header("Altre attività")

special_col1, special_col2 = st.columns(2)


with special_col1:
    st.markdown("""
    ### Arte e sport

    - **Graffiti Area**: 4000+ mq con 40+ street artists
    - **Breaking & Freestyle**: Competizioni e battle
    - **Skate Park**: Esibizioni skate e rollerblade
    - **DJ Set**: Aree dedicate al DJing
    - **Street Basket**: Torneo 3vs3

    """)

with special_col2:

    st.markdown("""
    ### Famiglie ed enogastronomia
    
    - **SC Kids**: Attività per bambini
    - **Food Area**: Tante golosità locali
    - **Bar**: Rinfresco sempre assicurato

    """)

st.markdown("---")

# Call to action per seguire aggiornamenti
st.header("📢 Resta Aggiornato")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📱 Segui i Social
    Per essere il primo a sapere chi si esibirà nel 2025:
    - **Instagram**: [@stradachiusa](https://www.instagram.com/stradachiusa/)
    - **Facebook**: [Strada Chiusa](https://www.facebook.com/stradachiusablockparty/)
    - **YouTube**: [L'Onda](https://www.youtube.com/@londa280)
    """)

with col2:
    st.markdown("""
    ### 🎯 Vuoi esibirti nelle prossime edizioni?
    Sei un artista e vuoi proporre la tua candidatura per Strada Chiusa 2026?

    **Contattaci!** 📧 ass.cult.onda@gmail.com
    """)

# Note finali
st.info("""
**💡 Nota**: La programmazione di Strada Chiusa include sempre un mix equilibrato tra artisti affermati 
e nuove promesse, garantendo sia qualità che scoperta di nuovi talenti.

**Tutti gli spettacoli sono gratuiti e aperti al pubblico!** 🎟️
""")

# Footer quote
st.markdown("""
<div style="text-align: center; padding: 2rem; margin-top: 2rem; font-style: italic; font-size: 1.1rem; color: #dc2626;">
    "La strada racconta, a chi sa ascoltare..." 🌊
</div>
""", unsafe_allow_html=True)
