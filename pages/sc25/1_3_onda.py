import os
import streamlit as st
from webartsite.path_config import contents_path

st.title("🌊 L'Onda")

st.info("""
**L'Onda** è un'associazione culturale no-profit fondata nella primavera del 2014 ad Acquaviva delle Fonti (BA) 
da un gruppo di giovani studenti e lavoratori pugliesi. 

Nata dall'**amicizia** e dalla **passione condivisa** per la cultura urbana! 🎵
""")

st.markdown("---")

# Presentazione dell'Associazione
st.header("🎯 La Nostra Missione")

mission_col1, mission_col2 = st.columns(2)

with mission_col1:
    st.subheader("🌟 Obiettivi Principali")
    st.write("""
    La nostra associazione si propone di **valorizzare il territorio** attraverso eventi che trasformano 
    **spazi urbani inutilizzati** in luoghi di:

    - 🤝 **Incontro** e socializzazione
    - 🎨 **Arte** e creatività
    - 👥 **Partecipazione** attiva
    - 🌱 **Crescita** comunitaria
    """)

with mission_col2:
    st.subheader("🎤 Focus Culturale")
    st.write("""
    L'obiettivo principale è **promuovere la cultura hip hop e urbana**, creando occasioni di:

    - 📚 **Aggregazione** culturale
    - 🎓 **Crescita** personale e collettiva
    - 🌍 **Valorizzazione** della comunità locale
    - 🔗 **Connessione** tra generazioni
    """)

st.markdown("---")

# Storia dell'Associazione
st.header("📚 La Nostra Storia")

st.write("""
**Dal 2014, L'Onda ha percorso un cammino di crescita e consolidamento**, 
trasformando un'idea nata dall'amicizia in un punto di riferimento culturale per la Puglia.
""")

# Timeline dell'evoluzione
timeline_col1, timeline_col2 = st.columns(2)

with timeline_col1:
    st.subheader("🌱 Gli Inizi (2014-2016)")
    st.write("""
    - **2014**: Fondazione dell'associazione
    - **Prima edizione** di Strada Chiusa
    - **Eventi itineranti** per la città
    - **Costruzione** della rete locale
    """)

    st.subheader("🚀 La Crescita (2017-2019)")
    st.write("""
    - **Consolidamento** del format festival
    - **Artisti internazionali** (Onyx, Das EFX)
    - **Espansione** delle attività
    - **Riconoscimento nazionale**
    """)

with timeline_col2:
    st.subheader("💪 La Maturità (2020-2023)")
    st.write("""
    - **Resilienza** durante la pandemia
    - **Edizione X** con tributo a Roberto
    - **€18.523** raccolti per AIRC
    - **Allineamento** con SDGs ONU
    """)

    st.subheader("🔮 Il Futuro (2024-2025)")
    st.write("""
    - **Nuove edizioni** sempre più ambiziose
    - **Espansione** della rete territoriale
    - **Innovazione** nei formati
    - **Sostenibilità** a lungo termine
    """)

st.success("""
**Ogni edizione è stata un passo in avanti**, un'opportunità per espandere il nostro impatto 
e rafforzare il legame con la comunità.
""")

st.markdown("---")

# Il Team
st.header("👥 Il Nostro Team")

st.warning("🔥 **OLTRE 60 VOLONTARI ATTIVI** 🔥")

st.write("""
Siamo un **gruppo eterogeneo** di giovani e meno giovani, tutti uniti dalla passione per la cultura 
e il desiderio di fare la differenza. 

Dagli organizzatori ai volontari, **ogni membro del team L'Onda** contribuisce con la propria energia 
e competenza a rendere Strada Chiusa un evento straordinario.
""")

team_col1, team_col2, team_col3 = st.columns(3)

with team_col1:
    st.subheader("🎯 Organizzatori")
    st.write("""
    - **Direzione artistica**
    - **Coordinamento generale**
    - **Gestione partnership**
    - **Comunicazione**
    """)

with team_col2:
    st.subheader("🔧 Staff Tecnico")
    st.write("""
    - **Allestimenti**
    - **Audio e luci**
    - **Sicurezza**
    - **Logistica**
    """)

with team_col3:
    st.subheader("🤝 Volontari")
    st.write("""
    - **Accoglienza pubblico**
    - **Supporto artisti**
    - **Gestione aree**
    - **Pulizia e ordine**
    """)

# Vuoi unirti?
st.info("""
**🌟 Vuoi far parte del team L'Onda?**

Cerchiamo sempre nuove persone motivate che vogliano contribuire alla realizzazione di Strada Chiusa!

**Contattaci**: ass.cult.onda@gmail.com
""")

st.markdown("---")

# Numeri Principali
st.header("📊 I Nostri Numeri")

# Metriche principali
metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

with metrics_col1:
    st.metric("Volontari Attivi", "60+", delta="Il cuore del festival")
with metrics_col2:
    st.metric("Edizioni Realizzate", "11+", delta="Dal 2014")
with metrics_col3:
    st.metric("Partecipanti", "Migliaia", delta="Ogni anno cresciamo")
with metrics_col4:
    st.metric("Fondi Raccolti", "€28k+", delta="Per cause sociali")

# Statistiche dettagliate
stats_col1, stats_col2 = st.columns(2)

with stats_col1:
    st.subheader("🎪 Impatto Eventi")
    st.write("""
    - **100+ artisti** ospitati negli anni
    - **4000+ mq** di area graffiti
    - **40+ street artist** per edizione
    - **15+ workshop** realizzati annualmente
    """)

with stats_col2:
    st.subheader("💰 Impatto Sociale")
    st.write("""
    - **€18.523** per AIRC (edizione 2023)
    - **€9.576** raccolti nel 2024
    - **Borse di studio** al Conservatorio
    - **Spazi urbani** riqualificati
    """)

st.markdown("---")

# Come ci Finanziamo
st.header("💡 Come ci Finanziamo")

finance_col1, finance_col2 = st.columns(2)

with finance_col1:
    st.subheader("🎯 Principi Fondamentali")
    st.write("""
    **L'Onda è e resterà un'associazione no-profit**, e **Strada Chiusa sarà sempre un evento gratuito**.

    Questo è un **principio cardine** della nostra missione civica, per garantire a tutti:
    - 🎟️ **Libero accesso** alla cultura
    - 🏘️ **Riconoscimento** negli spazi urbani
    - 🌱 **Partecipazione** senza barriere economiche
    """)

with finance_col2:
    st.subheader("🤝 Fonti di Finanziamento")
    st.write("""
    La realizzazione di eventi di tale portata è possibile grazie a:

    - 🏢 **Partner commerciali** e sponsor
    - 🎭 **Realtà artistiche** e culturali
    - 🏃 **Associazioni sportive**
    - 🎲 **Lotterie** e raccolte fondi
    - 💰 **Crowdfunding** comunitario
    """)

# Crowdfunding Success
st.subheader("🎯 Il Successo del Crowdfunding")

st.success("""
**Le nostre campagne di crowdfunding dimostrano il forte legame con la community:**

- 📈 **€18.523** - Edizione 2023 (record storico)
- 📈 **€9.576** - Edizione 2024
- 🎯 **100% obiettivo** raggiunto sempre
- 💪 **Partecipazione attiva** della comunità

**La nostra straordinaria community ci sostiene** perché crede nel progetto!
""")

st.markdown("---")

# Partnerships e Collaborazioni
st.header("🤝 Le Nostre Collaborazioni")

collab_col1, collab_col2 = st.columns(2)

with collab_col1:
    st.subheader("🏛️ Supporto Istituzionale")
    st.write("""
    - **Comune di Acquaviva delle Fonti**
    - **Regione Puglia** (per progetti specifici)
    - **Enti locali** e territoriali
    - **Università** e istituti di formazione
    """)

with collab_col2:
    st.subheader("🎭 Rete Culturale")
    st.write("""
    - **Associazioni culturali** locali
    - **Centri giovanili** e sociali
    - **Realtà artistiche** del territorio
    - **Network hip-hop** nazionale
    """)

st.markdown("---")

# Borsa di Studio Roberto Surico
st.header("🎓 Borsa di Studio Roberto Surico")

st.error("""
**In memoria del nostro co-fondatore Roberto Surico** ❤️

Abbiamo istituito una borsa di studio in collaborazione con l'**Università LUM**. 

Questa iniziativa mira a sostenere i futuri studenti del corso di medicina, 
perpetuando lo spirito di Roberto e il suo impegno per il futuro.
""")

roberto_col1, roberto_col2 = st.columns(2)

with roberto_col1:
    st.subheader("🎯 Obiettivi della Borsa")
    st.write("""
    - **Supporto economico** agli studenti meritevoli
    - **Memoria attiva** di Roberto Surico
    - **Investimento** nel futuro della medicina
    - **Continuità** dei valori dell'associazione
    """)

with roberto_col2:
    st.subheader("💰 Come Contribuire")
    st.write("""
    - **Donazioni** dedicate al progetto
    - **Fundraising** durante gli eventi
    - **Campagne specifiche** di raccolta
    - **Partner** che sostengono l'iniziativa
    """)

st.info("📧 **Per maggiori dettagli sulla borsa di studio**: ass.cult.onda@gmail.com")

st.markdown("---")

# Call to Action
st.header("🚀 Unisciti a L'Onda!")

cta_col1, cta_col2, cta_col3 = st.columns(3)

with cta_col1:
    if st.button("🤲 Diventa Volontario", use_container_width=True):
        st.switch_page("pages/sc25/4_1_collaborate.py")

with cta_col2:
    if st.button("💰 Fai una Donazione", use_container_width=True):
        st.switch_page("pages/sc25/4_1_donations.py")

with cta_col3:
    if st.button("📱 Seguici sui Social", use_container_width=True):
        st.switch_page("pages/sc25/4_1_contacts_social.py")

st.success("""
🌊 **L'Onda è più di un'associazione: è una famiglia che crede nel potere trasformativo della cultura!** 

Insieme, continuiamo a creare onde di cambiamento positivo nella nostra comunità. 🌊
""")