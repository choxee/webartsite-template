import os
import streamlit as st
from webartsite.path_config import contents_path

st.title("🤝 Chi ci supporta")

st.info("""
**Il successo di "Strada Chiusa" è indissolubilmente legato al supporto** di aziende, enti e associazioni 
che condividono la nostra visione e credono nel valore della cultura urbana per la comunità.

**A loro va il nostro più sincero ringraziamento!** ❤️
""")

st.markdown("---")

partnership_col1, partnership_col2 = st.columns(2)

with partnership_col1:
    st.subheader("💰 Sponsorizzazioni Finanziarie")
    st.info("""
    **Main Sponsor**: Visibilità principale
    """)
    st.info("""
    **Title Sponsor**: Naming rights
    """)

    st.markdown("---")

    st.subheader("🔧 Partnership Tecniche")
    st.write("""
    **Supporto con forniture e servizi:**
    - 🎤 **Audio/Video**: Attrezzature professionali
    - 🏗️ **Allestimenti**: Palchi e strutture
    - 🚛 **Logistica**: Trasporti e movimentazione
    - 🔒 **Sicurezza**: Servizi di vigilanza
    """)

with partnership_col2:
    st.subheader("📢 Collaborazioni Mediali")
    st.write("""
    **Promozione attraverso canali:**
    - 📺 **Media Partner**: TV e radio locali
    - 📰 **Press Partner**: Giornali e riviste
    - 📱 **Digital Partner**: Social e web
    - 🎙️ **Podcast Partner**: Audio content
    """)
    st.markdown("---")

    st.subheader("🎁 Sponsorizzazioni In-Kind")
    st.write("""
    **Beni o servizi in cambio di visibilità:**
    - 🍕 **Food & Beverage**: Catering e ristoro
    - 👕 **Merchandising**: Gadget e abbigliamento
    - 🎨 **Materiali**: Forniture per workshop
    - 🏨 **Hospitality**: Alloggi per artisti
    """)

st.markdown("---")

# Sponsor Principali Attuali
st.header("🏆 I Nostri Sponsor Ufficiali 2025")

st.warning("""
**🚧 Sezione in aggiornamento**

La lista completa dei partner e sponsor per Strada Chiusa 2025 sarà pubblicata nei prossimi mesi.

**Segui i nostri canali per tutti gli aggiornamenti!**
""")

# Placeholder per sponsor
st.subheader("🎯 Categorie di Sponsorizzazione")

sponsor_categories = st.tabs(["🥇 Main Partner", "🥈 Technical Partner", "🥉 Media Partner", "🎁 Supporter"])

with sponsor_categories[0]:
    st.write("**Main Partner** - I nostri sponsor principali che rendono possibile l'evento")
    st.info("🔜 **Annunci in arrivo** - Seguici sui social per scoprire chi saranno i Main Partner 2025!")

with sponsor_categories[1]:
    st.write("**Technical Partner** - Aziende che forniscono servizi e attrezzature specializzate")
    st.info("🔧 **Cerchiamo partner tecnici** per audio, video, allestimenti e logistica")

with sponsor_categories[2]:
    st.write("**Media Partner** - Testate giornalistiche e media che promuovono l'evento")
    st.info("📢 **Collaborazioni media** in definizione per una copertura completa")

with sponsor_categories[3]:
    st.write("**Supporter** - Realtà locali e piccole aziende che sostengono la cultura")
    st.info("🤝 **Sempre aperti** a nuove collaborazioni con il territorio")

st.markdown("---")

# Storia dei Partner
st.header("📚 I Partner Storici")

st.write("""
**Negli anni, molte realtà hanno creduto nel progetto Strada Chiusa** e ci hanno sostenuto 
nella crescita del festival:
""")

historical_col1, historical_col2 = st.columns(2)

with historical_col1:
    st.subheader("🏛️ Partner Istituzionali")
    st.write("""
    - **Comune di Acquaviva delle Fonti**
    - **Regione Puglia** (progetti specifici)
    - **Provincia di Bari**
    - **Enti locali** del territorio
    """)

    st.subheader("🎭 Partner Culturali")
    st.write("""
    - **Conservatorio "Niccolò Piccinni"** di Bari
    - **Università LUM** Giuseppe Degennaro
    - **Associazioni culturali** locali
    - **Centri giovanili** e sociali
    """)

with historical_col2:
    st.subheader("🏢 Partner Commerciali")
    st.write("""
    - **Aziende locali** del settore food
    - **Store** di abbigliamento urban
    - **Tech companies** per audio/video
    - **Fornitori** di servizi specializzati
    """)

    st.subheader("📱 Media Partner")
    st.write("""
    - **Radio locali** e web radio
    - **Blog** e magazine specializzati
    - **Influencer** della scena hip-hop
    - **Piattaforme digitali** emergenti
    """)

st.markdown("---")

# Vantaggi per i Partner
st.header("🌟 Vantaggi per i Partner")

benefits_col1, benefits_col2, benefits_col3 = st.columns(3)

with benefits_col1:
    st.subheader("📈 Visibilità")
    st.write("""
    - **Logo** su tutti i materiali
    - **Menzioni** sui social media
    - **Spazio espositivo** all'evento
    - **Presenza** negli aftermovie
    """)

with benefits_col2:
    st.subheader("🎯 Target")
    st.write("""
    - **Giovani 15-35 anni**
    - **Appassionati** di cultura urbana
    - **Famiglie** (area SC Kids)
    - **Turisti** culturali
    """)

with benefits_col3:
    st.subheader("💡 Valori")
    st.write("""
    - **Innovazione** e creatività
    - **Sostenibilità** sociale
    - **Inclusione** e diversità
    - **Autenticità** culturale
    """)

# Pacchetti di Sponsorizzazione
st.subheader("📦 Pacchetti di Sponsorizzazione")

packages = st.tabs(["🥇 PLATINUM", "🥈 GOLD", "🥉 SILVER", "💎 BRONZE"])

with packages[0]:
    st.markdown("""
    ### 🥇 PACCHETTO PLATINUM
    **Il massimo della visibilità e del coinvolgimento**

    **Benefici inclusi:**
    - 🎯 **Logo principale** su tutti i materiali
    - 🎤 **Spazio dedicato** per brand activation
    - 🎥 **Presenza** in tutti i video ufficiali
    - 📱 **Menzioni social** prioritarie
    - 🎁 **Hospitality** per ospiti aziendali
    - 📊 **Report** dettagliato post-evento
    """)

with packages[1]:
    st.markdown("""
    ### 🥈 PACCHETTO GOLD
    **Visibilità di alto livello con ottimo ROI**

    **Benefici inclusi:**
    - 🏷️ **Logo** su materiali principali
    - 🏪 **Stand** espositivo standard
    - 📹 **Menzioni** nei video recap
    - 📱 **Post social** dedicati
    - 🎟️ **Accrediti** per staff aziendale
    """)

with packages[2]:
    st.markdown("""
    ### 🥉 PACCHETTO SILVER
    **Supporto efficace per aziende locali**

    **Benefici inclusi:**
    - 🏷️ **Logo** su materiali selezionati
    - 📱 **Menzioni social** regolari
    - 🎪 **Presenza** nell'area sponsor
    - 📧 **Newsletter** dedicate
    """)

with packages[3]:
    st.markdown("""
    ### 💎 PACCHETTO BRONZE
    **Sostegno base con visibilità garantita**

    **Benefici inclusi:**
    - 🏷️ **Logo** nei ringraziamenti
    - 📱 **Menzione social** di ringraziamento
    - 🎫 **Inviti** all'evento
    - 🤝 **Networking** con altri partner
    """)

st.markdown("---")

# Come Diventare Partner
st.header("🚀 Come Diventare Partner")

steps_col1, steps_col2 = st.columns(2)

with steps_col1:
    st.subheader("📝 Step per la Partnership")
    st.write("""
    **1. Contatto Iniziale**
    - Invia una mail a **ass.cult.onda@gmail.com**
    - Specifica il tipo di collaborazione
    - Descrivi la tua azienda/organizzazione

    **2. Incontro Conoscitivo**
    - Chiamata o meeting per discutere
    - Presentazione del progetto
    - Definizione degli obiettivi comuni

    **3. Proposta Personalizzata**
    - Pacchetto su misura per le tue esigenze
    - Timeline e deliverable chiari
    - Contratto di sponsorizzazione
    """)

with steps_col2:
    st.subheader("💼 Cosa Valutare")
    st.write("""
    **Per l'Azienda:**
    - Allineamento con i **valori** del brand
    - **Target demografico** e geografico
    - **ROI** e metriche di successo
    - **Budget** disponibile

    **Per L'Onda:**
    - **Coerenza** con la missione
    - **Qualità** dell'azienda/servizio
    - **Valore aggiunto** per il pubblico
    - **Sostenibilità** della partnership
    """)

# Testimonianze (placeholder)
st.subheader("💬 Cosa Dicono i Nostri Partner")

testimonial_col1, testimonial_col2 = st.columns(2)

with testimonial_col1:
    st.info("""
    **"Collaborare con L'Onda e Strada Chiusa ci ha permesso di entrare in contatto 
    con una community autentica e appassionata. Un investimento che ha portato 
    visibilità e valore al nostro brand."**

    *- Partner storico*
    """)

with testimonial_col2:
    st.info("""
    **"L'organizzazione professionale e la passione del team L'Onda rendono 
    questa partnership non solo un investimento commerciale, ma un contributo 
    concreto alla crescita culturale del territorio."**

    *- Sponsor istituzionale*
    """)

st.markdown("---")

# Opportunità Speciali
st.header("✨ Opportunità Speciali 2025")

special_col1, special_col2 = st.columns(2)

with special_col1:
    st.subheader("🎂 11° Anniversario")
    st.write("""
    **Celebrazioni speciali per l'undicesima edizione:**
    - 🎉 **Eventi commemorativi** e retrospettive
    - 📚 **Documentario** sulla storia del festival
    - 🏆 **Riconoscimenti** ai partner storici
    - 🎁 **Pacchetti** anniversario esclusivi
    """)

with special_col2:
    st.subheader("🌱 Sostenibilità")
    st.write("""
    **Focus su partnership sostenibili:**
    - 🌍 **Green sponsor** per iniziative eco-friendly
    - ♻️ **Economia circolare** e riuso
    - 🌱 **Impact partnership** per cause sociali
    - 📊 **Reporting** di sostenibilità
    """)

st.markdown("---")

# Call to Action Finale
st.header("📞 Contattaci Oggi")

contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.subheader("📧 Informazioni Generali")
    st.write("""
    **Email**: ass.cult.onda@gmail.com
    **Oggetto**: Partnership Strada Chiusa 2025

    **Includi nella tua email:**
    - Nome azienda/organizzazione
    - Tipo di partnership interessata
    - Budget orientativo
    - Contatti per approfondimenti
    """)

with contact_col2:
    st.subheader("📱 Seguici sui Social")
    st.write("""
    **Instagram**: [@stradachiusa](https://www.instagram.com/stradachiusa/)
    **Facebook**: [Strada Chiusa](https://www.facebook.com/stradachiusablockparty/)
    **YouTube**: [L'Onda](https://www.youtube.com/@londa280)

    **Rimani aggiornato** sui partner e le novità!
    """)

# Modulo contatto veloce
st.subheader("⚡ Contatto Rapido")

with st.form("partner_contact"):
    col1, col2 = st.columns(2)

    with col1:
        company = st.text_input("Nome Azienda/Organizzazione:")
        email = st.text_input("Email di contatto:")

    with col2:
        partnership_type = st.selectbox(
            "Tipo di partnership:",
            ["Sponsorizzazione Finanziaria", "Partnership Tecnica", "Media Partner", "In-Kind", "Altro"]
        )
        budget = st.selectbox(
            "Budget orientativo:",
            ["< €1.000", "€1.000 - €5.000", "€5.000 - €10.000", "> €10.000", "Da discutere"]
        )

    message = st.text_area("Messaggio (opzionale):")

    if st.form_submit_button("📨 Invia Richiesta Partnership"):
        st.success("✅ **Richiesta inviata!** Ti contatteremo entro 48 ore.")
        st.info("📧 Riceverai una conferma all'indirizzo email fornito.")

st.success("""
🤝 **Diventa parte della famiglia Strada Chiusa!** 

Insieme possiamo creare un impatto positivo sulla comunità e promuovere la cultura urbana 
in Puglia e oltre. 🌟
""")