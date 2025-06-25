import os
import streamlit as st
from webartsite.path_config import contents_path

st.title("📞 Contattaci: Siamo Qui per Te!")

st.info("""
**Hai domande, suggerimenti o vuoi semplicemente salutarci?** 

Siamo sempre felici di sentire dalla nostra community! Ecco tutti i modi per rimanere in contatto con L'Onda 
e seguire le novità di Strada Chiusa. 📱✨
""")

st.markdown("---")

# Social Media Principali
st.header("📱 I Nostri Social Media")

st.write("**Seguici sui nostri canali ufficiali** per restare sempre aggiornato!")

# Instagram
st.subheader("Contatti")
instagram_col1, instagram_col2 = st.columns(2)

with instagram_col1:
    st.markdown("""
    **ass.cult.onda@gmail.com**
    """)

    st.markdown("""
    **[Instagram](https://www.instagram.com/stradachiusa/)**

    """)
    st.markdown("""
    **[Facebook](https://www.facebook.com/stradachiusablockparty/?locale=it_IT)**

    """)
    st.markdown("""
    **[Youtube](https://www.youtube.com/@londa280)**

    """)
    #
    # Il nostro canale principale per:
    # - 📸 **Foto esclusive** dai backstage
    # - 📹 **Stories** in tempo reale durante gli eventi
    # - 🎨 **Artwork** e contenuti creativi
    # - 📢 **Annunci** in anteprima
    # - 🎵 **Playlist** e raccomandazioni musicali
# with instagram_col2:
#     st.info("""
#     **🔥 Contenuti che trovi:**
#     - Preparativi e allestimenti
#     - Performance degli artisti
#     - Opere dei graffiti artist
#     - Momenti della community
#     - Dietro le quinte dell'organizzazione
#
#     **👀 Stories highlights** con i momenti migliori di ogni edizione!
#     """)

st.markdown("---")

# Contatti Diretti
st.header("📧 Contatti Diretti")

contacts_col1, contacts_col2 = st.columns(2)

with contacts_col1:
    st.subheader("📮 Email Ufficiale")
    st.markdown("""
    **ass.cult.onda@gmail.com**

    **Usala per:**
    - 🤝 Proposte di collaborazione
    - 🎤 Candidature artistiche
    - 🙋 Richieste di volontariato
    - 💰 Informazioni su sponsorizzazioni
    - 💝 Donazioni e beneficenza
    - ❓ Domande generali

    **⏰ Rispondiamo entro 48 ore** (giorni lavorativi)
    """)

with contacts_col2:
    st.subheader("📍 Dove Siamo")
    st.markdown("""
    **Sede dell'Associazione Culturale L'Onda**

    📍 **Acquaviva delle Fonti (BA)**  
    Puglia, Italia

    *Per incontri in presenza, contattaci via email per fissare un appuntamento*

    🏛️ **Supporto istituzionale**:  
    Comune di Acquaviva delle Fonti
    """)

st.markdown("---")

# Modulo di Contatto
st.header("📝 Contattaci Direttamente")

st.write("**Compila il modulo qui sotto** e ti risponderemo il prima possibile:")

with st.form("contact_form"):
    contact_col1, contact_col2 = st.columns(2)

    with contact_col1:
        name = st.text_input("Nome e Cognome*:")
        email = st.text_input("Email*:")
        phone = st.text_input("Telefono (opzionale):")

    with contact_col2:
        subject = st.selectbox(
            "Oggetto*:",
            [
                "Informazioni generali",
                "Proposta di collaborazione",
                "Candidatura artistica",
                "Volontariato",
                "Partnership/Sponsorizzazione",
                "Donazioni",
                "Richiesta stampa/media",
                "Altro"
            ]
        )
        urgency = st.selectbox(
            "Urgenza:",
            ["Normale", "Urgente", "Non urgente"]
        )

    message = st.text_area("Messaggio*:", height=120)

    # Privacy checkbox
    privacy = st.checkbox("Accetto il trattamento dei dati personali secondo la privacy policy*")

    if st.form_submit_button("📨 Invia Messaggio"):
        if privacy:
            st.success("✅ **Messaggio inviato con successo!**")
            st.info("📧 Ti risponderemo all'indirizzo email fornito entro 48 ore.")
            st.warning(f"📋 **Riepilogo**: {name} - {subject}")
        else:
            st.error("❌ È necessario accettare il trattamento dei dati per inviare il messaggio.")

st.markdown("---")
