import os
import streamlit as st
from webartsite.path_config import contents_path

st.title("Sostienici")

st.info("""
**"Strada Chiusa" è un evento gratuito**, reso possibile dall'impegno volontario e dal sostegno della nostra comunità. 

**Ogni donazione ci permette di continuare a portare cultura urbana ad Acquaviva delle Fonti!** 🎵
""")

st.markdown("---")

# Perché donare
st.header("❤️ Perché Donare a Strada Chiusa")

why_col1, why_col2 = st.columns(2)

with why_col1:
    st.subheader("🎯 I Tuoi Contributi Servono Per:")
    st.write("""
    - 🎟️ **Garantire l'ingresso libero** al festival
    - 🎤 **Ospitare artisti** di fama nazionale e internazionale
    - 🎨 **Organizzare workshop** educativi e inclusivi
    - 🏗️ **Valorizzare gli spazi urbani** dimenticati
    - 🎓 **Sostenere la Borsa di Studio Roberto Surico**
    - 🔧 **Coprire i costi organizzativi** dell'evento
    """)

with why_col2:
    st.subheader("🌟 L'Impatto delle Tue Donazioni")
    st.write("""
    - 🎪 **Festival sempre gratuito** per tutti
    - 🌍 **Rigenerazione urbana** concreta
    - 👥 **Aggregazione sociale** e culturale
    - 🎓 **Sostegno all'istruzione** superiore
    - ❤️ **Ricerca medica** (collaborazione AIRC)
    - 🌱 **Sviluppo sostenibile** del territorio
    """)

st.success("""
**Il tuo contributo è un investimento nella cultura e nella nostra comunità!** 

Ogni euro donato torna alla collettività sotto forma di eventi, cultura, formazione e progresso sociale.
""")

st.markdown("---")

# Risultati Raggiunti
st.header("🏆 Cosa Abbiamo Già Realizzato Insieme")

st.write("**Grazie alle donazioni ricevute negli anni, abbiamo potuto:**")

results_col1, results_col2, results_col3 = st.columns(3)

with results_col1:
    st.metric("Fondi Raccolti 2023", "€18.523", delta="Record storico")
    st.metric("Donati ad AIRC", "€9.000", delta="Ricerca sul cancro")

with results_col2:
    st.metric("Fondi Raccolti 2024", "€9.576", delta="Obiettivo raggiunto")
    st.metric("Edizioni Gratuite", "11+", delta="Dal 2014")

with results_col3:
    st.metric("Beneficiari Diretti", "Migliaia", delta="Ogni anno")
    st.metric("Volontari Coinvolti", "60+", delta="Community attiva")

# Dettaglio utilizzo fondi
st.subheader("💰 Come Utilizziamo le Donazioni")

usage_tabs = st.tabs(["🎪 Organizzazione Evento", "🎓 Borsa di Studio", "❤️ Cause Sociali", "🏗️ Sviluppo Progetto"])

with usage_tabs[0]:
    st.markdown("""
    ### 🎪 Organizzazione dell'Evento (70%)

    **Costi principali per realizzare Strada Chiusa:**
    - 🎤 **Audio e Luci**: Noleggio attrezzature professionali
    - 🏗️ **Allestimenti**: Palchi, strutture, aree dedicate
    - 🎨 **Materiali Workshop**: Bombolette, tele, strumenti
    - 🚛 **Logistica**: Trasporti, movimentazione, setup
    - 🔒 **Sicurezza**: Servizi di vigilanza e primo soccorso
    - 📢 **Comunicazione**: Stampa locandine, promozione
    """)

with usage_tabs[1]:
    st.markdown("""
    ### 🎓 Borsa di Studio Roberto Surico (15%)

    **In memoria del nostro co-fondatore:**
    - 💰 **Contributo economico** per studenti meritevoli
    - 🏥 **Corso di Medicina** presso Università LUM
    - 📚 **Supporto** per libri e materiali didattici
    - 🎯 **Selezione** basata su merito e necessità
    - ❤️ **Perpetuazione** dello spirito di Roberto
    """)

with usage_tabs[2]:
    st.markdown("""
    ### ❤️ Cause Sociali (10%)

    **Sostegno a progetti di beneficenza:**
    - 🏥 **AIRC**: Ricerca contro il cancro
    - 🎵 **Conservatorio Piccinni**: Borse di studio musicali
    - 🌱 **Progetti locali**: Iniziative per la comunità
    - 👥 **Centri sociali**: Supporto alle attività giovanili
    """)

with usage_tabs[3]:
    st.markdown("""
    ### 🏗️ Sviluppo del Progetto (5%)

    **Investimenti per il futuro:**
    - 📊 **Strumenti organizzativi**: Software e tecnologie
    - 📚 **Formazione team**: Corsi e workshop per volontari
    - 🔍 **Ricerca e sviluppo**: Nuovi format e attività
    - 🌐 **Comunicazione digitale**: Sito web e presenza online
    """)

st.markdown("---")

# Metodi di Donazione
st.header("💳 Come Donare")

st.write("**Sostenere Strada Chiusa è semplice e sicuro. Scegli il metodo che preferisci:**")

donation_methods = st.tabs(["💳 PayPal", "🏦 Bonifico", "🎯 Crowdfunding", "🎁 Donazioni in Natura"])

with donation_methods[0]:
    st.markdown("""
    ### 💳 Dona con PayPal

    **Il metodo più semplice e sicuro:**
    - ⚡ **Immediato**: Donazione processata subito
    - 🔒 **Sicuro**: Protezione PayPal garantita
    - 💳 **Flessibile**: Carta, conto PayPal o bonifico
    - 📧 **Ricevuta**: Conferma automatica via email
    """)

    # PayPal button placeholder
    st.info("""
    🔗 **Link PayPal per donazioni**: 
    *[Sarà inserito il link PayPal ufficiale dell'associazione]*

    **Importi suggeriti**: €10, €25, €50, €100 o importo libero
    """)

    if st.button("💳 Dona con PayPal", use_container_width=True):
        st.success("🔄 **Reindirizzamento a PayPal...** (link da configurare)")

with donation_methods[1]:
    st.markdown("""
    ### 🏦 Bonifico Bancario

    **Per donazioni tramite bonifico bancario:**

    **Intestatario**: Associazione Culturale L'Onda  
    **IBAN**: *[Da inserire IBAN ufficiale]*  
    **Causale**: Donazione Strada Chiusa 2025  
    **BIC/SWIFT**: *[Se necessario per bonifici internazionali]*
    """)

    st.warning("""
    📧 **Importante**: Dopo aver effettuato il bonifico, invia una mail a 
    **ass.cult.onda@gmail.com** con la ricevuta per ricevere conferma e ringraziamenti.
    """)

with donation_methods[2]:
    st.markdown("""
    ### 🎯 Campagne di Crowdfunding

    **Partecipa alle nostre campagne ufficiali:**
    - 🎪 **Campagna Pre-Evento**: Per i costi organizzativi
    - ❤️ **Campagna Benefica**: Per cause sociali specifiche
    - 🎓 **Campagna Borsa di Studio**: Dedicata a Roberto Surico
    """)

    st.info("""
    📢 **Le campagne di crowdfunding vengono lanciate** sui nostri social media 
    e includono rewards speciali per i sostenitori!

    **Segui i nostri canali** per non perdere le prossime campagne.
    """)

with donation_methods[3]:
    st.markdown("""
    ### 🎁 Donazioni in Natura

    **Puoi anche contribuire con beni e servizi:**
    - 🎨 **Materiali**: Bombolette, tele, strumenti musicali
    - 🍕 **Catering**: Cibo e bevande per volontari
    - 🚛 **Servizi**: Trasporti, noleggi, competenze professionali
    - 💡 **Expertise**: Consulenze gratuite in vari settori
    """)

    st.info("""
    📧 **Per donazioni in natura**: Contatta **ass.cult.onda@gmail.com** 
    specificando cosa vuoi donare e in che quantità.

    **Rilasciamo sempre ricevuta** per donazioni aziendali deducibili.
    """)

st.markdown("---")

# Livelli di Donazione
st.header("🌟 Livelli di Sostegno")

support_col1, support_col2 = st.columns(2)

with support_col1:
    st.subheader("🥉 SUPPORTER (€10-25)")
    st.write("""
    - 📧 **Newsletter** esclusiva con aggiornamenti
    - 🎵 **Playlist** ufficiali Strada Chiusa
    - 📱 **Ringraziamento** sui social media
    - 🎫 **Accesso prioritario** alle comunicazioni
    """)

    st.subheader("🥈 ADVOCATE (€25-50)")
    st.write("""
    **Tutto del livello Supporter +**
    - 🎁 **Gadget** ufficiale Strada Chiusa
    - 📸 **Foto** esclusive behind-the-scenes
    - 🎤 **Menzione** speciale durante l'evento
    - 📺 **Accesso** agli aftermovie in anteprima
    """)

with support_col2:
    st.subheader("🥇 CHAMPION (€50-100)")
    st.write("""
    **Tutto dei livelli precedenti +**
    - 👕 **T-shirt** ufficiale dell'edizione
    - 🎪 **Invito** VIP all'evento
    - 📋 **Backstage pass** per incontrare gli artisti
    - 🏆 **Riconoscimento** nell'albo dei sostenitori
    """)

    st.subheader("💎 PATRON (€100+)")
    st.write("""
    **Tutto dei livelli precedenti +**
    - 🎨 **Opera d'arte** originale degli street artist
    - 🍽️ **Cena** con il team organizzativo
    - 📰 **Intervista** sui nostri canali
    - 🌟 **Partnership** personalizzata di ringraziamento
    """)

st.markdown("---")

# Trasparenza e Rendicontazione
st.header("📊 Trasparenza e Rendicontazione")

transparency_col1, transparency_col2 = st.columns(2)

with transparency_col1:
    st.subheader("🔍 Come Garantiamo la Trasparenza")
    st.write("""
    - 📊 **Report annuali** dettagliati sull'utilizzo fondi
    - 📧 **Newsletter** periodiche ai donatori
    - 📱 **Aggiornamenti** sui social media
    - 🎥 **Video** di rendicontazione post-evento
    - 📋 **Bilanci** pubblici dell'associazione
    """)

with transparency_col2:
    st.subheader("📈 Monitoraggio dell'Impatto")
    st.write("""
    - 🎯 **Obiettivi** chiari e misurabili
    - 📊 **Metriche** di successo definite
    - 📸 **Documentazione** fotografica e video
    - 💬 **Feedback** da partecipanti e beneficiari
    - 🏆 **Risultati** condivisi con la community
    """)

st.success("""
**Crediamo nella totale trasparenza** nell'utilizzo delle donazioni. 
Ogni euro ricevuto è tracciato e rendicontato alla nostra community di sostenitori.
""")

st.markdown("---")

# Donazioni Aziendali
st.header("🏢 Donazioni Aziendali e Detrazioni")

corporate_col1, corporate_col2 = st.columns(2)

with corporate_col1:
    st.subheader("💼 Vantaggi per le Aziende")
    st.write("""
    - 📄 **Ricevuta fiscale** per detrazioni
    - 🏷️ **Visibilità** come supporter dell'evento
    - 📊 **CSR Report**: Contributo alla responsabilità sociale
    - 🤝 **Networking**: Connessioni con altre aziende partner
    - 🎯 **Target audience**: Accesso a giovani e famiglie
    """)

with corporate_col2:
    st.subheader("📋 Procedure per Aziende")
    st.write("""
    **Per donazioni aziendali superiori a €100:**
    1. 📧 **Contatto preventivo** via email
    2. 📄 **Invio documentazione** fiscale necessaria
    3. 💰 **Bonifico** con causale specifica
    4. 📋 **Ricevuta ufficiale** entro 7 giorni
    5. 🎁 **Pacchetto** di ringraziamento personalizzato
    """)

st.info("""
📧 **Per donazioni aziendali**: ass.cult.onda@gmail.com  
**Oggetto**: Donazione Aziendale Strada Chiusa 2025

**Include**: Ragione sociale, partita IVA, importo donazione, indirizzo fatturazione
""")

st.markdown("---")

# Donazione Rapida
st.header("⚡ Fai una Donazione Ora")

st.write("**Scegli l'importo e contribuisci subito al successo di Strada Chiusa 2025:**")

# Quick donation buttons
donation_col1, donation_col2, donation_col3, donation_col4 = st.columns(4)

with donation_col1:
    if st.button("💝 €10", use_container_width=True):
        st.info("🔄 Reindirizzamento a PayPal per €10...")

with donation_col2:
    if st.button("💝 €25", use_container_width=True):
        st.info("🔄 Reindirizzamento a PayPal per €25...")

with donation_col3:
    if st.button("💝 €50", use_container_width=True):
        st.info("🔄 Reindirizzamento a PayPal per €50...")

with donation_col4:
    if st.button("💝 €100", use_container_width=True):
        st.info("🔄 Reindirizzamento a PayPal per €100...")

# Custom amount
st.subheader("💰 Importo Personalizzato")

with st.form("custom_donation"):
    col1, col2 = st.columns(2)

    with col1:
        custom_amount = st.number_input("Importo (€):", min_value=5, value=25, step=5)
        donor_email = st.text_input("La tua email (per ricevuta):")

    with col2:
        donor_name = st.text_input("Nome (opzionale):")
        message = st.text_area("Messaggio di sostegno (opzionale):")

    if st.form_submit_button("💝 Dona Ora", use_container_width=True):
        st.success(f"✅ **Preparando donazione di €{custom_amount}**")
        st.info("🔄 Reindirizzamento a PayPal in corso...")
        if message:
            st.write(f"💌 **Il tuo messaggio**: {message}")

st.markdown("---")

# Ringraziamenti
st.header("🙏 Ringraziamenti Speciali")

st.write("**Un grazie di cuore a tutti i sostenitori** che hanno reso possibili le passate edizioni:")

thanks_col1, thanks_col2 = st.columns(2)

with thanks_col1:
    st.subheader("❤️ Donatori Individuali")
    st.write("""
    - 👥 **Centinaia di cittadini** di Acquaviva e provincia
    - 🎵 **Appassionati** di cultura hip-hop da tutta Italia
    - 👨‍👩‍👧‍👦 **Famiglie** che credono nel valore educativo
    - 🌟 **Ex partecipanti** diventati sostenitori
    """)

with thanks_col2:
    st.subheader("🏢 Aziende e Organizzazioni")
    st.write("""
    - 🏪 **Commercianti locali** e artigiani
    - 🏛️ **Istituzioni** pubbliche e private
    - 🎭 **Associazioni** culturali e artistiche
    - 🤝 **Partner** storici del progetto
    """)

st.success("""
**Ogni contributo, grande o piccolo, è fondamentale** per il successo di Strada Chiusa. 

La vostra generosità permette di mantenere vivo questo progetto unico di cultura e rigenerazione urbana.

**GRAZIE di cuore!** ❤️
""")