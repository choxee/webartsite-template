import os
import streamlit as st
from webartsite.path_config import contents_path

st.title("Collabora con noi")

st.info("""
**L'energia di "Strada Chiusa" è alimentata da persone** che, come noi, credono nel potere della cultura e della collaborazione. 

**Ci sono molti modi per unirti a noi e fare la differenza!** 🌟

Che tu sia un artista, un volontario, un commerciante o semplicemente una persona che crede nel nostro progetto, 
c'è un posto anche per te nella famiglia L'Onda.
""")

st.markdown("---")

# Overview delle collaborazioni
st.header("🎯 Come Puoi Collaborare")

overview_col1, overview_col2, overview_col3, overview_col4 = st.columns(4)

with overview_col1:
    st.metric("Volontari Attivi", "60+", delta="Ogni anno")
with overview_col2:
    st.metric("Artisti Coinvolti", "100+", delta="Nelle edizioni")
with overview_col3:
    st.metric("Partner Commerciali", "20+", delta="E crescendo")
with overview_col4:
    st.metric("Proposte Accolte", "90%", delta="Delle candidature")

st.markdown("---")

# Tipologie di Collaborazione
collaboration_tabs = st.tabs([
    "🙋 Volontari",
    "🎨 Artisti",
    "🏪 SCMarket",
    "🍕 Food & Beverage",
    "💡 Proposte Libere"
])

# TAB VOLONTARI
with collaboration_tabs[0]:
    st.header("🙋 Diventa Volontario")
    st.subheader("💪 La Forza di Strada Chiusa: I Nostri Volontari!")

    volunteer_col1, volunteer_col2 = st.columns(2)

    with volunteer_col1:
        st.markdown("""
        ### 👥 Chi Cerchiamo
        **Ogni anno, oltre 60 volontari** dedicano tempo e passione alla realizzazione del festival. 

        **Cerchiamo persone:**
        - 🔥 **Appassionate** di cultura urbana
        - 🤝 **Collaborative** e di spirito di squadra
        - ⚡ **Energiche** e proattive
        - 🎯 **Affidabili** e puntuali
        - 💡 **Creative** e propositive

        **Non servono competenze specifiche**, solo voglia di fare e divertirsi!
        """)

    with volunteer_col2:
        st.markdown("""
        ### 🔧 Aree di Volontariato
        **Setup e Allestimenti:**
        - 🏗️ Montaggio palchi e strutture
        - 🎨 Preparazione aree graffiti
        - 🔌 Supporto tecnico audio/luci

        **Durante l'Evento:**
        - 🎫 Accoglienza e informazioni
        - 🎤 Assistenza artisti
        - 🛡️ Sicurezza e controllo aree
        - 📸 Documentazione fotografica

        **Post-Evento:**
        - 🧹 Pulizia e riordino
        - 📦 Smontaggio strutture
        """)

    st.subheader("🎁 Cosa Offriamo ai Volontari")

    benefits_col1, benefits_col2, benefits_col3 = st.columns(3)

    with benefits_col1:
        st.markdown("""
        **🎪 Esperienza Unica**
        - Vivere il festival da protagonista
        - Dietro le quinte con gli artisti
        - Network con persone fantastiche
        """)

    with benefits_col2:
        st.markdown("""
        **🎁 Benefit Concreti**
        - Kit volontario ufficiale
        - Pasti durante l'evento
        - Gadget esclusivi L'Onda
        """)

    with benefits_col3:
        st.markdown("""
        **🌟 Crescita Personale**
        - Competenze organizzative
        - Leadership e teamwork
        - Certificato di partecipazione
        """)

    st.subheader("📝 Come Candidarsi")

    with st.form("volunteer_form"):
        vol_col1, vol_col2 = st.columns(2)

        with vol_col1:
            vol_name = st.text_input("Nome e Cognome*:")
            vol_email = st.text_input("Email*:")
            vol_phone = st.text_input("Telefono:")
            vol_age = st.number_input("Età:", min_value=16, max_value=99, value=25)

        with vol_col2:
            vol_experience = st.selectbox(
                "Esperienza precedente in eventi:",
                ["Nessuna", "Poca", "Discreta", "Molta", "Professionale"]
            )
            vol_areas = st.multiselect(
                "Aree di interesse:",
                ["Setup/Allestimenti", "Accoglienza pubblico", "Assistenza artisti",
                 "Sicurezza", "Documentazione", "Pulizia", "Tecnico audio/luci", "Altro"]
            )
            vol_availability = st.selectbox(
                "Disponibilità:",
                ["Solo giorno evento", "Setup + evento", "Evento + smontaggio", "Tutto il periodo"]
            )

        vol_motivation = st.text_area("Perché vuoi diventare volontario L'Onda?")
        vol_skills = st.text_area("Competenze particolari che vuoi condividere:")

        if st.form_submit_button("🚀 Candidati come Volontario"):
            st.success("✅ **Candidatura inviata!** Ti contatteremo entro una settimana.")
            st.info("📧 Riceverai una conferma via email e sarai invitato a un incontro conoscitivo.")

# TAB ARTISTI
with collaboration_tabs[1]:
    st.header("🎨 Proponi la Tua Arte a Strada Chiusa")
    st.subheader("🎤 Siamo Sempre alla Ricerca di Nuovi Talenti!")

    artist_col1, artist_col2 = st.columns(2)

    with artist_col1:
        st.markdown("""
        ### 🎵 Discipline Artistiche
        **Accettiamo candidature per:**

        **🎤 Musica:**
        - Rap e hip-hop
        - R&B e soul
        - Reggae e dancehall
        - Beatmaking live

        **🎨 Arte Visiva:**
        - Graffiti e street art
        - Live painting
        - Installazioni urbane
        - Arte digitale

        **🕺 Performance:**
        - Breakdance
        - Street dance
        - Freestyle rap
        - Poetry slam
        """)

    with artist_col2:
        st.markdown("""
        ### 📋 Criteri di Selezione
        **Valutiamo:**
        - 🎯 **Qualità artistica** e tecnica
        - 🔥 **Originalità** e creatività
        - 🎪 **Esperienza live** e stage presence
        - 🤝 **Allineamento** con i valori del festival
        - 🌍 **Impatto** sulla community

        **Privilegiamo:**
        - 🏠 **Artisti locali** e del Sud Italia
        - 👥 **Progetti collaborativi**
        - 🌱 **Nuove promesse** emergenti
        - ♻️ **Messaggi positivi** e sociali
        """)

    st.subheader("📝 Come Candidarsi")

    with st.form("artist_form"):
        art_col1, art_col2 = st.columns(2)

        with art_col1:
            art_name = st.text_input("Nome d'arte / Crew*:")
            art_real_name = st.text_input("Nome reale*:")
            art_email = st.text_input("Email*:")
            art_phone = st.text_input("Telefono:")
            art_city = st.text_input("Città di provenienza:")

        with art_col2:
            art_discipline = st.selectbox(
                "Disciplina principale:",
                ["Rap/Hip-Hop", "R&B/Soul", "Beatmaking", "Graffiti", "Breakdance",
                 "Street Dance", "Poetry Slam", "DJ Set", "Altro"]
            )
            art_experience = st.selectbox(
                "Esperienza live:",
                ["Esordiente", "Alcuni live", "Esperienza media", "Molti live", "Professionista"]
            )
            art_members = st.number_input("Numero membri (se crew):", min_value=1, max_value=20, value=1)

        art_description = st.text_area("Descrivi il tuo progetto artistico*:")
        art_links = st.text_area("Link ai tuoi lavori (Spotify, YouTube, Instagram, etc.):")
        art_requirements = st.text_area("Requisiti tecnici particolari:")

        if st.form_submit_button("🎨 Invia Candidatura Artistica"):
            st.success("🎵 **Candidatura ricevuta!** La valuteremo entro 2 settimane.")
            st.info("📱 Nel frattempo, seguici sui social per aggiornamenti sulla selezione!")

# TAB SCMARKET
with collaboration_tabs[2]:
    st.header("🏪 SCMarket: L'Area Creativa e Commerciale")
    st.subheader("🛍️ Porta la Tua Attività al Festival")

    market_col1, market_col2 = st.columns(2)

    with market_col1:
        st.markdown("""
        ### 🎯 Cos'è SCMarket
        **SCMarket è lo spazio dedicato** ad artigiani, creativi e piccoli commercianti 
        che vogliono proporre i loro prodotti durante Strada Chiusa.

        **Tipologie Accettate:**
        - 👕 **Abbigliamento** urban e streetwear
        - 🎨 **Arte e artigianato** locale
        - 💿 **Musica** e merchandising
        - 📚 **Libri** e fanzine underground
        - 🎮 **Gadget** e accessori creativi
        - ♻️ **Prodotti sostenibili** e upcycling
        """)

    with market_col2:
        st.markdown("""
        ### 📦 Cosa Offriamo
        **Servizi Inclusi:**
        - 🏪 **Spazio espositivo** delimitato
        - ⚡ **Allacciamento elettrico** (se necessario)
        - 🛡️ **Sicurezza** dell'area
        - 📢 **Promozione** sui nostri canali

        **Costi:**
        - 💰 **Tariffa simbolica** per coprire le spese
        - 🤝 **Sconti** per associazioni e giovani
        - 💝 **Gratuito** per progetti sociali
        """)

    st.subheader("📝 Candidatura SCMarket")

    with st.form("market_form"):
        market_col1, market_col2 = st.columns(2)

        with market_col1:
            market_name = st.text_input("Nome attività/brand*:")
            market_owner = st.text_input("Nome titolare*:")
            market_email = st.text_input("Email*:")
            market_phone = st.text_input("Telefono*:")

        with market_col2:
            market_type = st.selectbox(
                "Tipo di attività:",
                ["Artigianato", "Abbigliamento", "Arte", "Musica/Vinili",
                 "Accessori", "Libri/Fanzine", "Food (confezionato)", "Altro"]
            )
            market_space = st.selectbox(
                "Spazio necessario:",
                ["Tavolo piccolo (2m)", "Tavolo grande (4m)", "Stand completo", "Spazio personalizzato"]
            )

        market_products = st.text_area("Descrivi i tuoi prodotti*:")
        market_social = st.text_input("Profili social/sito web:")
        market_experience = st.text_area("Esperienza in mercatini/eventi:")

        if st.form_submit_button("🛍️ Candidati per SCMarket"):
            st.success("🏪 **Candidatura SCMarket inviata!** Ti risponderemo entro 10 giorni.")
            st.info("📋 Riceverai informazioni dettagliate su spazi, costi e modalità.")

# TAB FOOD & BEVERAGE
with collaboration_tabs[3]:
    st.header("🍕 Food & Beverage")
    st.subheader("🚚 Porta la Tua Attività Gastronomica")

    food_col1, food_col2 = st.columns(2)

    with food_col1:
        st.markdown("""
        ### 🍴 Tipologie Ricercate
        **Cerchiamo:**
        - 🚚 **Food truck** mobili e attrezzati
        - 🥪 **Street food** di qualità
        - 🌱 **Proposte vegetariane/vegane**
        - 🏠 **Specialità locali** pugliesi
        - 🌍 **Cucine etniche** e fusion
        - 🧊 **Bevande** fresche e analcoliche

        **Requisiti:**
        - ✅ **Licenze** e autorizzazioni in regola
        - 🧼 **Standard igienico-sanitari** elevati
        - ⚡ **Autonomia energetica** preferibile
        - 💰 **Prezzi accessibili** al pubblico
        """)

    with food_col2:
        st.markdown("""
        ### 🤝 Modalità di Collaborazione
        **Offriamo:**
        - 📍 **Posizionamento strategico** nell'area
        - 🔌 **Supporto elettrico** (dove possibile)
        - 💧 **Accesso ad acqua** e servizi
        - 📢 **Promozione** dedicata

        **Accordi:**
        - 💰 **Quota partecipazione** da concordare
        - 🍽️ **Catering** per staff/artisti (sconto)
        - 📊 **Vendite esclusive** nell'area
        - ⏰ **Orari concordati** con l'organizzazione
        """)

    st.subheader("📝 Candidatura Food & Beverage")

    with st.form("food_form"):
        food_col1, food_col2 = st.columns(2)

        with food_col1:
            food_business = st.text_input("Nome attività*:")
            food_owner = st.text_input("Nome titolare*:")
            food_email = st.text_input("Email*:")
            food_phone = st.text_input("Telefono*:")
            food_piva = st.text_input("P.IVA (se presente):")

        with food_col2:
            food_type = st.selectbox(
                "Tipo di cucina:",
                ["Street food italiano", "Cucina pugliese", "Pizza", "Panini gourmet",
                 "Cucina etnica", "Vegetariano/Vegano", "Dolci", "Bevande", "Altro"]
            )
            food_setup = st.selectbox(
                "Tipo di allestimento:",
                ["Food truck completo", "Rimorchio attrezzato", "Gazebo + attrezzature",
                 "Stand fisso", "Banchetto mobile"]
            )

        food_menu = st.text_area("Descrivi il tuo menu/offerta*:")
        food_experience = st.text_area("Esperienza in eventi e festival:")
        food_requirements = st.text_area("Requisiti particolari (spazio, elettricità, etc.):")

        if st.form_submit_button("🍕 Invia Candidatura F&B"):
            st.success("🚚 **Candidatura Food & Beverage ricevuta!** Ti contatteremo entro una settimana.")
            st.info("📋 Organizzeremo un incontro per definire i dettagli della collaborazione.")

# TAB PROPOSTE LIBERE
with collaboration_tabs[4]:
    st.header("💡 Proposte Libere")
    st.subheader("🌟 Hai un'Idea? Parliamone!")

    ideas_col1, ideas_col2 = st.columns(2)

    with ideas_col1:
        st.markdown("""
        ### 🚀 Tipologie di Proposte
        **Siamo aperti a:**
        - 🎪 **Workshop** innovativi e creativi
        - 🎮 **Attività interattive** per il pubblico
        - 🌱 **Progetti sostenibili** e green
        - 🤝 **Collaborazioni** con altre associazioni
        - 💡 **Tecnologie** e innovazioni
        - 🎯 **Attivazioni** di brand responsabili
        - 📚 **Progetti educativi** e formativi
        - ♻️ **Iniziative sociali** e benefiche
        """)

    with ideas_col2:
        st.markdown("""
        ### 🎯 Criteri di Valutazione
        **Valutiamo proposte che:**
        - 🎪 **Arricchiscono** l'esperienza del festival
        - 🤝 **Coinvolgono** attivamente il pubblico
        - 🌱 **Portano valore** alla community
        - 💡 **Sono innovative** e originali
        - ♻️ **Rispettano** l'ambiente e la sostenibilità
        - ❤️ **Sono coerenti** con i nostri valori

        **Non accettiamo:**
        - 🚫 Proposte commerciali aggressive
        - 🚫 Attività che contrastano con la cultura hip-hop
        - 🚫 Iniziative discriminatorie o offensive
        """)

    st.subheader("📝 Invia la Tua Proposta")

    with st.form("proposal_form"):
        prop_col1, prop_col2 = st.columns(2)

        with prop_col1:
            prop_name = st.text_input("Il tuo nome*:")
            prop_organization = st.text_input("Organizzazione/Associazione:")
            prop_email = st.text_input("Email*:")
            prop_phone = st.text_input("Telefono:")

        with prop_col2:
            prop_category = st.selectbox(
                "Categoria proposta:",
                ["Workshop/Laboratorio", "Attività interattiva", "Progetto sociale",
                 "Collaborazione artistica", "Innovazione tecnologica", "Sostenibilità", "Altro"]
            )
            prop_budget = st.selectbox(
                "Budget richiesto:",
                ["Nessuno (gratuito)", "Rimborso spese", "Budget limitato", "Da discutere"]
            )

        prop_title = st.text_input("Titolo della proposta*:")
        prop_description = st.text_area("Descrivi dettagliatamente la tua idea*:")
        prop_target = st.text_area("Chi coinvolgerebbe? (target, numero partecipanti, etc.)")
        prop_requirements = st.text_area("Di cosa avresti bisogno per realizzarla?")
        prop_experience = st.text_area("Esperienze precedenti in progetti simili:")

        if st.form_submit_button("💡 Invia Proposta"):
            st.success("🌟 **Proposta ricevuta!** La valuteremo con attenzione.")
            st.info("📞 Se interessante, ti contatteremo per un approfondimento.")

st.markdown("---")
