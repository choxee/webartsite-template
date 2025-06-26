import os
import streamlit as st
from webartsite.path_config import contents_path

st.title("Un decennio di Strada Chiusa")

st.info("""
**Dal 2014, "Strada Chiusa" è cresciuta** fino a diventare un appuntamento imperdibile per gli appassionati 
di cultura hip hop e urbana. 

Ogni edizione ha portato con sé **nuove esperienze**, artisti di fama nazionale e internazionale, 
e un coinvolgimento sempre maggiore della comunità.

**Rivivi con noi i momenti che hanno fatto la storia del nostro festival!** 🎵
""")

st.markdown("---")

# Timeline Overview
st.header("📅 Timeline delle Edizioni")

# Metrics overview
overview_col1, overview_col2, overview_col3, overview_col4 = st.columns(4)

with overview_col1:
    st.metric("Anni di Storia", "11+", delta="Dal 2014")
with overview_col2:
    st.metric("Edizioni Realizzate", "10+", delta="Sempre crescendo")
with overview_col3:
    st.metric("Artisti Ospitati", "100+", delta="Nazionale e internazionale")
with overview_col4:
    st.metric("Fondi Raccolti", "€28k+", delta="Per cause sociali")

st.markdown("---")

# Edizioni Dettagliate
st.header("🎭 Le Nostre Edizioni")

# Creazione dei tab per ogni edizione
editions = st.tabs([
    "🔟 2023 - Edizione X",
    "🎤 2019 - Das EFX",
    "🎪 2017 - Reunion Nazionale",
    "🇺🇸 2016 - Onyx",
    "📈 2015 - Salto di Qualità",
    "🌱 2014 - L'Inizio"
])

# EDIZIONE 2023 - STRADA CHIUSA X
with editions[0]:
    st.header("🔟 Strada Chiusa X - Edizione 2023")
    st.subheader("❤️ Omaggio a Roberto Surico")

    edition_2023_col1, edition_2023_col2 = st.columns(2)

    with edition_2023_col1:
        st.markdown("""
        ### 🎯 Caratteristiche dell'Edizione
        **Un'edizione memorabile e significativa**, segno della resilienza e della passione della nostra comunità.

        **Punti Salienti:**
        - 🎂 **Celebrazione del decennale** del festival
        - ❤️ **Tributo** al co-fondatore Roberto Surico
        - 🎨 **Murata commemorativa** realizzata
        - 💰 **€18.523** raccolti per la ricerca
        - 🏥 **€9.000** donati all'AIRC
        """)

    with edition_2023_col2:
        st.markdown("""
        ### 🎤 Lineup e Partecipazioni
        **Artisti Principali:**
        - 🎵 Mix di veterani e nuove promesse
        - 🎨 **40+ street artist** partecipanti
        - 🎧 DJ set per tutta la giornata
        - 🕺 Battle di breakdance

        **Attività Speciali:**
        - 🎨 Murata dedicata a Roberto
        - 💬 Dibattiti sulla cultura hip-hop
        - 🏀 Tornei sportivi
        - 👶 Area SC Kids
        """)

    st.success("""
    **L'Edizione X ha rappresentato un momento di maturità** per Strada Chiusa, 
    dimostrando come un festival possa essere contemporaneamente celebrazione, memoria e impegno sociale.
    """)

    st.info("""
    **💰 Risultato Raccolta Fondi**: €18.523 raccolti - il **record storico** del festival!

    **Destinazione**: €9.000 donati all'AIRC per la ricerca contro il cancro
    """)

# EDIZIONE 2019 - DAS EFX E KAOS ONE
with editions[1]:
    st.header("🎤 Strada Chiusa 2019")
    st.subheader("🇺🇸 Das EFX e Kaos One")

    edition_2019_col1, edition_2019_col2 = st.columns(2)

    with edition_2019_col1:
        st.markdown("""
        ### 🌟 Una Tappa Fondamentale
        **Un'altra milestone** con l'arrivo direttamente dagli Stati Uniti dei leggendari **Das EFX**.

        **Headliner Internazionali:**
        - 🇺🇸 **Das EFX** - Leggende del hip-hop anni '90
        - 🇮🇹 **Kaos One** - Icona del rap italiano underground
        - 🎧 **DJ Craim** - Maestro del turntablism

        **Crescita dell'Evento:**
        - 📈 **Partecipazione record** per l'epoca
        - 🌍 **Riconoscimento nazionale** del festival
        - 🎪 **Espansione** delle attività proposte
        """)

    with edition_2019_col2:
        st.markdown("""
        ### 🎭 Lineup Completa 2019
        **Artisti Italiani:**
        - 🎤 **Siberia** (Grezzo, Suarez, DJ Drugo)
        - 🎵 **7peccati**
        - 🎨 **Writer** e street artist nazionali

        **Attività Espanse:**
        - 🛹 **Area skateboard** dedicata
        - 🏀 **Street basketball** tournament
        - 🎨 **Graffiti jam** sul muro ferroviario
        - 🍕 **Street food** ampliato
        """)

    st.success("""
    **Il 2019 ha consolidato Strada Chiusa** come uno dei festival hip-hop più importanti del Sud Italia, 
    capace di attrarre artisti internazionali di primo piano.
    """)

# EDIZIONE 2017 - RIUNIONE NAZIONALE
with editions[2]:
    st.header("🎪 Strada Chiusa 2017")
    st.subheader("🇮🇹 Riunione Nazionale Hip Hop")

    edition_2017_col1, edition_2017_col2 = st.columns(2)

    with edition_2017_col1:
        st.markdown("""
        ### 🏆 Il Format si Consacra
        **Il format di Strada Chiusa si è consacrato** con una lineup di altissimo livello 
        che ha riunito il meglio della scena hip hop italiana **da Nord a Sud**.

        **Innovazioni:**
        - 🎪 **Consolidamento** del format festival
        - 🗺️ **Copertura nazionale** degli artisti
        - 📈 **Upgrade** di tutte le attività
        - 🎯 **Standard** di eccellenza stabiliti
        """)

    with edition_2017_col2:
        st.markdown("""
        ### 🌟 Lineup Stellare 2017
        **Artisti Principali:**
        - 🎤 **La Famiglia** (Napoli)
        - 🎵 **Egreen**
        - 🎭 **Il Turco**
        - 🎪 **Er Costa**
        - 🎯 **Gast**
        - 🎨 **Lucci**
        - 🎧 **Mr.Phil**
        - 🎵 **Do Your Thang Records**
        - 🎤 **Inoki**
        - 🎧 **DJ Zarra**
        - 🎪 **Chapo**
        - 🎭 **Mopashà**
        """)

    st.success("""
    **L'edizione 2017 è stata il momento** in cui Strada Chiusa ha dimostrato di poter competere 
    con i maggiori festival hip-hop italiani per qualità della lineup e organizzazione.
    """)

# EDIZIONE 2016 - ONYX
with editions[3]:
    st.header("🇺🇸 Strada Chiusa 2016")
    st.subheader("🔥 Gli Onyx ad Acquaviva!")

    edition_2016_col1, edition_2016_col2 = st.columns(2)

    with edition_2016_col1:
        st.markdown("""
        ### 🚀 Salto Internazionale
        **Un salto di qualità e internazionalità** epocale. Via Monteschiavo è stata chiusa 
        per ospitare gli **Onyx**, pilastri dell'Hip Hop americano.

        **Milestone Storiche:**
        - 🇺🇸 **Primi ospiti internazionali** di peso
        - 🛣️ **Chiusura di Via Monteschiavo**
        - 🎪 **Espansione location** dell'evento
        - 📈 **Crescita dimensionale** significativa
        """)

    with edition_2016_col2:
        st.markdown("""
        ### 🎤 Lineup 2016
        **Headliner:**
        - 🔥 **ONYX** - Leggende del hardcore rap (NYC)
        - 🎵 **Il Turco**
        - 🎧 **Mr Phil**
        - 🎤 **Inoki**

        **Novità dell'Edizione:**
        - 🍕 **Street food** ufficiale
        - 🎨 **Graffiti Jam** espansa
        - 🏃 **Attività sportive** integrate
        - 🎭 **Festival della Polemica**
        """)

    st.success("""
    **L'edizione 2016 con gli Onyx** ha segnato l'ingresso di Strada Chiusa nell'olimpo 
    dei festival hip-hop italiani, dimostrando la capacità di attrarre artisti leggendari.
    """)

# EDIZIONE 2015 - SALTO DI QUALITÀ
with editions[4]:
    st.header("📈 Strada Chiusa 2015")
    st.subheader("🌟 Un Salto di Qualità")

    edition_2015_col1, edition_2015_col2 = st.columns(2)

    with edition_2015_col1:
        st.markdown("""
        ### 🏗️ Riqualificazione Urbana
        **Il campetto di Via Roma ha ripreso vita** con le rime di artisti di qualità 
        e l'energia della comunità hip-hop.

        **Obiettivi Raggiunti:**
        - 🏘️ **Riqualificazione** area di Via Roma
        - 📈 **Crescita artistica** e contenutistica
        - 🎯 **Standard** di qualità elevati
        - 🌱 **Bases** per future espansioni
        """)

    with edition_2015_col2:
        st.markdown("""
        ### 🎵 Lineup 2015
        **Artisti Principali:**
        - 🎤 **Stokka & Madbuddy**
        - 🎧 **Tenko & Scriba**
        - 🎵 **Uncle Jungle**
        - 🎭 **Cico & MaMaAFRIKA**
        - 🎨 **Antonino Barresi**

        **Focus dell'Edizione:**
        - 🎪 **Salto qualitativo** evidente
        - 🎯 **Curation artistica** migliorata
        - 🏘️ **Impatto urbano** positivo
        """)

    st.info("""
    **Il 2015 ha mostrato subito un salto di qualità** musicale e contenutistico, 
    stabilendo le basi per le future edizioni di successo.
    """)

# EDIZIONE 2014 - L'INIZIO
with editions[5]:
    st.header("🌱 Strada Chiusa 2014")
    st.subheader("✨ L'Inizio di un Sogno")

    edition_2014_col1, edition_2014_col2 = st.columns(2)

    with edition_2014_col1:
        st.markdown("""
        ### 🌱 La Nascita del Progetto
        **La prima edizione**, ancora "in fieri" ma già un successo 
        nel panorama giovanile acquavivese.

        **Caratteristiche Fondative:**
        - 🎯 **Prima sperimentazione** del concept
        - 👥 **Community building** iniziale
        - 🗺️ **Eventi itineranti** per la città
        - 💭 **Vision** ambiziosa per il futuro
        """)

    with edition_2014_col2:
        st.markdown("""
        ### 🎤 Lineup Pioneer 2014
        **Artisti della Prima Ora:**
        - 🎵 **Flash Band**
        - 🎤 **Inoki** - Veterano che ha creduto nel progetto

        **Il Significato:**
        - ✨ **Primo passo** di un viaggio straordinario
        - 🌱 **Semina** per le future edizioni
        - 🤝 **Costruzione** della rete di supporto
        - 💡 **Prototipo** del format attuale
        """)

    st.warning("""
    **Il 2014 ha segnato l'inizio** del nostro entusiasmante viaggio. 
    Da quella prima edizione sperimentale è nato tutto quello che Strada Chiusa rappresenta oggi.
    """)

st.markdown("---")

# Evoluzione del Festival
st.header("📈 L'Evoluzione di Strada Chiusa")

evolution_col1, evolution_col2 = st.columns(2)

with evolution_col1:
    st.subheader("🎪 Crescita Artistica")
    st.write("""
    **Dal 2014 al 2023:**
    - 🎤 **Da eventi locali** a festival nazionale
    - 🌍 **Da artisti regionali** a star internazionali
    - 🎨 **Da piccole jam** a 4000mq di street art
    - 🎯 **Da esperimento** a modello replicabile
    """)

with evolution_col2:
    st.subheader("💪 Impatto Sociale")
    st.write("""
    **Crescita dell'Impatto:**
    - 💰 **€0** → **€28k+** raccolti per beneficenza
    - 👥 **Decine** → **Migliaia** di partecipanti
    - 🏘️ **Una strada** → **Intero quartiere** rivitalizzato
    - 🌱 **Idea locale** → **Modello nazionale**
    """)

# Timeline grafica
st.subheader("📊 Timeline di Crescita")

timeline_data = {
    "Anno": [2014, 2015, 2016, 2017, 2019, 2023],
    "Livello": ["Locale", "Regionale", "Nazionale", "Nazionale+", "Internazionale", "Consolidato"],
    "Highlight": ["Prima edizione", "Via Roma", "Onyx USA", "Lineup stellare", "Das EFX", "Edizione X"]
}

for i, (anno, livello, highlight) in enumerate(
        zip(timeline_data["Anno"], timeline_data["Livello"], timeline_data["Highlight"])):
    if i < len(timeline_data["Anno"]) - 1:
        st.write(f"**{anno}** - {livello}: *{highlight}* ➡️")
    else:
        st.write(f"**{anno}** - {livello}: *{highlight}* 🏆")

st.markdown("---")

# Galleria e Media
st.header("📸 Galleria e Media")

media_tabs = st.tabs(["🎥 Aftermovie", "📸 Foto Gallery", "📋 Locandine Storiche"])

with media_tabs[0]:
    st.subheader("🎥 Aftermovie delle Edizioni")

    st.info("""
    **🎬 Aftermovie 2024**: *Link YouTube da inserire*

    **🎬 Aftermovie 2023**: *Link YouTube da inserire*

    **🎬 Collezione completa**: Disponibile sul nostro canale YouTube [@londa280](https://www.youtube.com/@londa280)
    """)

    if st.button("▶️ Guarda su YouTube", use_container_width=True):
        st.success("🔄 Reindirizzamento al canale YouTube...")

with media_tabs[1]:
    st.subheader("📸 Foto delle Edizioni Passate")

    photo_categories = st.columns(4)

    with photo_categories[0]:
        st.write("**🎤 Artisti**")
        st.write("Performance live e backstage")

    with photo_categories[1]:
        st.write("**🎨 Street Art**")
        st.write("Graffiti e opere realizzate")

    with photo_categories[2]:
        st.write("**🕺 Breakdance**")
        st.write("Battle e workshop")

    with photo_categories[3]:
        st.write("**👥 Pubblico**")
        st.write("Atmosfera e partecipazione")

    st.info("""
    📱 **Segui i nostri social** per vedere tutte le foto delle edizioni passate:
    - **Instagram**: [@stradachiusa](https://www.instagram.com/stradachiusa/)
    - **Facebook**: [Strada Chiusa](https://www.facebook.com/stradachiusablockparty/)
    """)

with media_tabs[2]:
    st.subheader("📋 Locandine delle Edizioni")

    st.write("""
    **Una collezione delle locandine** che hanno annunciato ogni edizione di Strada Chiusa, 
    testimonianza visiva della nostra evoluzione grafica e artistica.
    """)

    poster_col1, poster_col2, poster_col3 = st.columns(3)

    with poster_col1:
        st.write("**2014-2016**")
        st.write("Prime sperimentazioni grafiche")

    with poster_col2:
        st.write("**2017-2019**")
        st.write("Consolidamento dell'identità visiva")

    with poster_col3:
        st.write("**2020-2024**")
        st.write("Maturità e riconoscibilità")

    st.info("🎨 **Collezione completa** disponibile nella galleria del sito")

st.markdown("---")

# Call to Action
st.header("🚀 Il Futuro della Storia")

future_col1, future_col2 = st.columns(2)

with future_col1:
    st.subheader("🔮 Strada Chiusa 2025")
    st.write("""
    **La prossima edizione** si preannuncia ancora più spettacolare, 
    forte dell'esperienza accumulata e del supporto di una community 
    sempre più numerosa e appassionata.
    """)

    if st.button("🎵 Scopri SC25", use_container_width=True):
        st.switch_page("pages/sc25/0_1_home.py")

with future_col2:
    st.subheader("📚 Fai Parte della Storia")
    st.write("""
    **Vuoi essere protagonista** delle prossime edizioni? 
    Unisciti a noi come volontario, partner o semplice 
    sostenitore del progetto!
    """)

    if st.button("🤝 Collabora con Noi", use_container_width=True):
        st.switch_page("pages/sc25/4_1_collaborate.py")

st.success("""
📚 **Ogni edizione di Strada Chiusa è un capitolo** della storia della cultura urbana pugliese. 

Insieme, continuiamo a scrivere questa storia fatta di musica, arte, comunità e impegno sociale. 

**La storia continua... e tu puoi farne parte!** 🎵
""")

with st.expander("🎵 Altri Artisti che Hanno Calcato il Nostro Palco", expanded=True):
    artist_list_col1, artist_list_col2 = st.columns(2)

    with artist_list_col1:
        st.markdown("""
        **Artisti Italiani:**
        - 🎤 **La Famiglia** (Napoli)
        - 🎤 **Stokka & Madbuddy**
        - 🎤 **Egreen**
        - 🎤 **Il Turco**
        - 🎤 **Er Costa**
        - 🎤 **Inoki**
        - 🎤 **Mr. Phil**
        """)

    with artist_list_col2:
        st.markdown("""
        **Producer e DJ:**
        - 🎧 **DJ Craim**
        - 🎧 **DJ Zarra**
        - 🎧 **DJ Drugo**
        - 🎵 **Uncle Jungle**
        - 🎵 **Tenko & Scriba**
        - 🎵 **Flash Band**
        """)