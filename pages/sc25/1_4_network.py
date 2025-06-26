import os
import streamlit as st
from webartsite.path_config import contents_path

st.title("🕸️ La Rete")

st.info("""
La forza del nostro progetto risiede nella **rete di collaborazioni** che abbiamo costruito negli anni 
con realtà culturali, artistiche e sociali che condividono i nostri valori e la nostra visione.
""")

st.markdown("---")

# Introduzione alla rete
st.header("Una Rete di Valori Condivisi")

st.write("""
**Strada Chiusa** è il risultato di un **ecosistema collaborativo** che include:
- **Associazioni culturali** del territorio
- **Istituzioni** locali e regionali  
- **Collettivi artistici** e creativi
- **Realtà sportive** e giovanili
- **Partner commerciali** sensibili alla cultura
""")

st.markdown("---")

# Istituzioni e Enti
st.header("🏛️ Partner Istituzionali")

institutional_col1, institutional_col2 = st.columns(2)

with institutional_col1:
    st.subheader("🏛️ Comune di Acquaviva delle Fonti")
    st.write("""
    **Supporto fondamentale:**
    - 🏗️ **Patrocinio** ufficiale
    - 🚧 **Concessioni** per spazi pubblici
    - 🚨 **Coordinamento** sicurezza
    - 💡 **Supporto logistico**
    """)

    st.subheader("🎓 Istituzioni Educative")
    st.write("""
    **Collaborazioni accademiche:**
    - **Conservatorio "Niccolò Piccinni"** di Bari
    - **Università LUM** (Borsa Roberto Surico)
    - **Scuole superiori** del territorio
    - **Centri di formazione** professionale
    """)

with institutional_col2:
    st.subheader("🌍 Enti Regionali")
    st.write("""
    **Supporto territoriale:**
    - 🏛️ **Regione Puglia**
    - 🎭 **Assessorati** alla Cultura
    - 🌱 **Progetti** di sviluppo locale
    - 💰 **Bandi** e finanziamenti
    """)

    st.subheader("🎯 Organizzazioni Sociali")
    st.write("""
    **Partnership benefiche:**
    - ❤️ **AIRC** (ricerca sul cancro)
    - 🏥 **Strutture sanitarie** locali
    - 👥 **Centri sociali** e giovanili
    - 🏃 **Associazioni sportive**
    """)

st.markdown("---")

# Rete Hip-Hop Nazionale
st.header("🎤 Network Hip-Hop Nazionale")

hiphop_col1, hiphop_col2 = st.columns(2)

with hiphop_col1:
    st.subheader("🏆 Tecniche Perfette")
    st.write("""
    **Connessione con il freestyle nazionale:**
    - 🎯 **Torneo nazionale** di freestyle
    - 🌟 **Scoperta** di nuovi talenti
    - 🤝 **Scambio** di artisti e culture
    - 📈 **Crescita** della scena italiana
    """)

with hiphop_col2:
    st.subheader("🎭 Collettivi Regionali")
    st.write("""
    **Rete sud-italiana:**
    - 🎵 **Crew** campane (La Famiglia, etc.)
    - 🎨 **Collettivi** pugliesi (No Fang, etc.)
    - 🔥 **Scene locali** interconnesse
    - 📡 **Promozione** reciproca
    """)

# Artisti e Mentor
st.subheader("🌟 Artisti e Mentor Storici")

st.info("""
**Figure che hanno contribuito alla crescita di Strada Chiusa:**

- 🎤 **Extrapolo** (host e mentor napoletano)
- 🎵 **Onyx** (collaborazione internazionale)
- 🎭 **Kaos One** (icon del rap italiano)
- 🎨 **Writer** e artisti della scena
- 🎧 **DJ** e producer veterani
""")

st.markdown("---")

# Come Funziona la Rete
st.header("⚙️ Come Funziona la Nostra Rete")

network_col1, network_col2, network_col3 = st.columns(3)

with network_col1:
    st.subheader("🔄 Reciprocità")
    st.write("""
    - **Scambio** di risorse
    - **Promozione** incrociata
    - **Condivisione** di competenze
    - **Supporto** reciproco
    """)

with network_col2:
    st.subheader("🎯 Sinergie")
    st.write("""
    - **Progetti** congiunti
    - **Eventi** collaborativi
    - **Workshop** condivisi
    - **Comunicazione** coordinata
    """)

with network_col3:
    st.subheader("🌱 Crescita")
    st.write("""
    - **Espansione** territoriale
    - **Nuove** collaborazioni
    - **Innovazione** nei formati
    - **Sostenibilità** a lungo termine
    """)
