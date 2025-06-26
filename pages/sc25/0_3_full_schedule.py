import os
import streamlit as st
from webartsite.path_config import contents_path

# st.title("📅 Strada Chiusa 2025: Programma Completo")

# Informazioni principali evento

st.markdown("---")

st.header("Programma completo")

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.subheader("📅 Data")
    st.write("**Da definire** - Estate 2025")
    st.write("*(Segui i social per aggiornamenti)*")

    st.subheader("🕐 Orari")
    st.write("**Apertura**: Ore 15:00")
    st.write("**Chiusura**: Ore 24:00")

with info_col2:
    st.subheader("📍 Dove")
    st.write("**Acquaviva delle Fonti (BA)**")
    st.write("Via Monteschiavo e aree limitrofe")

    st.subheader("🎟️ Ingresso")
    st.success("**GRATUITO** per tutti!")

st.markdown("---")

# Le Attività principali
st.header("🎭 Le Attività di Strada Chiusa 2025")
st.write(
    "**Strada Chiusa è molto più di un festival musicale!** Immergiti nella cultura urbana con un programma ricco di esperienze uniche.")

# Griglia delle attività
st.subheader("🎵 MUSICA E PERFORMANCE")

music_col1, music_col2 = st.columns(2)

with music_col1:
    st.markdown("""
    ### 🎤 Concerti Live
    - **Artisti nazionali** e internazionali
    - **Nuove promesse** della scena rap
    - **Performance acustiche** e con backing track

    ### 🔥 Freestyle Battle
    - **Sfide di improvvisazione** tra MC
    - **Tornei** con giuria qualificata
    - **Premi** per i vincitori
    """)

with music_col2:
    st.markdown("""
    ### 🎧 DJ Set
    - **Mix old school** e nuove tendenze
    - **Producer** emergenti
    - **Musica continua** per tutto l'evento

    ### 🎵 Live Beatmaking
    - **Sessioni** di produzione dal vivo
    - **Workshop** aperti al pubblico
    - **Collaborazioni** artista-producer
    """)

st.markdown("---")

# Arte e Creatività
st.subheader("🎨 ARTE E CREATIVITÀ")

art_col1, art_col2 = st.columns(2)

with art_col1:
    st.markdown("""
    ### 🖌️ Graffiti Area
    - **Oltre 4000 mq** dedicati alla street art
    - **40+ street artist** partecipanti
    - **Workshop** di graffiti per principianti
    - **Muro libero** per tutti
    """)

with art_col2:
    st.markdown("""
    ### 🎨 Workshop Creativi
    - **Tecniche di spray** e lettering
    - **Design urbano** e stencil
    - **Arte digitale** e graphic design
    - **Materiali forniti** dall'organizzazione
    """)

st.markdown("---")

# Sport e Movimento
st.subheader("⚡ SPORT E MOVIMENTO")

sport_col1, sport_col2 = st.columns(2)

with sport_col1:
    st.markdown("""
    ### 🕺 Breakdance Battle
    - **Competizioni** tra i migliori breaker
    - **Workshop** per imparare i passi base
    - **Cypher spontanee** durante la giornata
    - **Giuria internazionale**
    """)

with sport_col2:
    st.markdown("""
    ### 🛹 Skate Area
    - **Sessioni libere** per tutti i livelli
    - **Dimostrazioni** di skate e rollerblade
    - **Mini contest** per i più audaci
    - **Area sicura** e attrezzata
    """)

# Sport aggiuntivi
sport_extra_col1, sport_extra_col2 = st.columns(2)

with sport_extra_col1:
    st.markdown("""
    ### 🏀 Street Basketball
    - **Torneo 3vs3** aperto a tutti
    - **Campo regolamentare** allestito
    - **Premi** per le squadre vincitrici
    """)

with sport_extra_col2:
    st.markdown("""
    ### 🏃 Altre Discipline
    - **Parkour** e freerunning
    - **Calisthenics** e street workout
    - **Dimostrazioni** e mini corsi
    """)

st.markdown("---")

# Gastronomia
st.subheader("🍕 STREET FOOD GOURMET")

food_col1, food_col2 = st.columns(2)

with food_col1:
    st.markdown("""
    ### 🌮 Sapori di Strada
    Le migliori proposte di street food ti aspettano:
    - **Specialità locali** pugliesi
    - **Sapori internazionali**
    - **Opzioni vegetariane** e vegane
    - **Food truck** selezionati
    """)

with food_col2:
    st.markdown("""
    ### 🥤 Bevande e Ristoro
    - **Bevande fresche** e analcoliche
    - **Caffetteria** mobile
    - **Idratazione gratuita** (fontanelle)
    - **Area relax** ombreggiata
    """)

st.markdown("---")

# Dialoghi e Cultura
st.subheader("💭 DIALOGHI E CULTURA")

culture_col1, culture_col2 = st.columns(2)

with culture_col1:
    st.markdown("""
    ### 🗣️ Dialoghi Urbani
    - **Dibattiti** sull'impatto sociale dell'hip-hop
    - **Tavole rotonde** con esperti
    - **Testimonianze** di artisti
    - **Q&A** con il pubblico
    """)

with culture_col2:
    st.markdown("""
    ### 📚 Esposizioni
    - **Mostra fotografica** delle edizioni passate
    - **Exhibit** di street art
    - **Corner dedicati** alla storia hip-hop
    - **Merchandising** ufficiale
    """)

st.markdown("---")

# Attività per famiglie
st.subheader("👶 SC KIDS - PER I PIÙ PICCOLI")

st.info("""
**Strada Chiusa è anche family-friendly!** 

**SC Kids** è la sezione dedicata ai bambini e alle famiglie:
- 🎨 **Laboratori creativi** per bambini
- 🎵 **Mini workshop musicali**
- 🏃 **Giochi** e attività ricreative
- 👨‍👩‍👧‍👦 **Area famiglia** dedicata e sicura
""")

st.markdown("---")

# Informazioni pratiche
st.header("ℹ️ Informazioni Pratiche")

practical_col1, practical_col2 = st.columns(2)

with practical_col1:
    st.subheader("🚗 Come Arrivare")
    st.markdown("""
    **In Auto:**
    - Uscita Acquaviva delle Fonti dalla SS16
    - Parcheggi gratuiti nelle zone limitrofe

    **Mezzi Pubblici:**
    - Autobus da Bari (linee FSE)
    - Treno Bari-Acquaviva delle Fonti
    """)

with practical_col2:
    st.subheader("🛡️ Norme di Sicurezza")
    st.markdown("""
    - **Accesso libero** ma regolamentato
    - **Sicurezza** garantita in tutte le aree
    - **Primo soccorso** sempre presente
    - **Rispetto** per l'ambiente urbano
    """)

# Mappa e orientamento
st.subheader("🗺️ Mappa dell'Evento")
st.info("""
**La mappa dettagliata dell'evento sarà disponibile più vicino alla data.**

Include: palchi, aree attività, punti ristoro, servizi, parcheggi e percorsi di accesso.
""")

st.markdown("---")

# Call to action finale
st.header("📲 Resta Aggiornato")

final_col1, final_col2 = st.columns(2)

with final_col1:
    if st.button("📱 Seguici sui Social", use_container_width=True):
        st.switch_page("pages/sc25/4_1_contacts_social.py")

with final_col2:
    if st.button("🤝 Collabora con Noi", use_container_width=True):
        st.switch_page("pages/sc25/4_1_collaborate.py")


st.warning("""
**⏰ Save the Date**: Le date ufficiali saranno annunciate presto sui nostri canali social.

**#StradaChiusa2025 #StayTuned** 👀
""")

st.success("""
🎵 **Non perdere l'opportunità di vivere Strada Chiusa 2025!** 

Un'intera giornata di cultura urbana, completamente gratuita, nel cuore della Puglia. 🎵
""")

st.info("""

Un evento che si preannuncia ancora più grande e coinvolgente. Acquaviva delle Fonti si animerà con performance live, 
workshop interattivi, tornei sportivi, esposizioni di street art e un'irresistibile offerta di street food gourmet.

""")
