import os
import streamlit as st
from webartsite.path_config import contents_path

#st.title("🛣️ Strada Chiusa: La Storia del Festival")

st.markdown("---")

st.info("""
**Strada Chiusa** è molto più di un semplice festival musicale. 

Si configura come un **progetto culturale poliedrico** che celebra la cultura hip-hop e funge da catalizzatore 
per la **rigenerazione urbana** e l'**impegno sociale** ad Acquaviva delle Fonti, Puglia.
""")

st.markdown("---")

# Identità e Mission
st.header("Identità e Missione")

mission_col1, mission_col2 = st.columns(2)

with mission_col1:
    st.subheader("La Nostra Visione")
    st.write("""
    Strada Chiusa è esplicitamente concepito come una **celebrazione della cultura hip-hop** 
    e, in modo ancora più significativo, come un **catalizzatore per la rigenerazione urbana** 
    e l'impegno sociale.

    La nostra identità non risiede solo nella line-up musicale, ma nel nostro **profondo radicamento 
    nel tessuto comunitario** e nella nostra ambizione di produrre un **impatto tangibile e positivo** sul territorio.
    """)

with mission_col2:
    st.subheader("Un Festival Olistico")
    st.write("""
    Il programma del festival dimostra un **impegno olistico** verso gli elementi fondanti 
    della cultura hip-hop, andando ben oltre il modello del concerto tradizionale.

    Ogni edizione include **tutte le discipline** della cultura urbana, creando un'esperienza 
    completa e autentica per i partecipanti.
    """)

st.markdown("---")

# I Quattro Pilastri
st.header("I Quattro Pilastri della Cultura Hip-Hop")

st.write("Strada Chiusa celebra integralmente i quattro elementi fondamentali della cultura hip-hop:")

pillar_col1, pillar_col2 = st.columns(2)

with pillar_col1:
    st.subheader("🎤 1. MCing (Rap)")
    st.write("""
    - **Concerti live** di artisti nazionali e internazionali
    - **Freestyle battle** e competizioni di improvvisazione
    - **Nuove promesse** e artisti affermati
    """)

    st.subheader("🎧 2. DJing")
    st.write("""
    - **DJ set** durante tutto l'evento
    - **Turntablism** e tecniche avanzate
    - **Spazi dedicati** al DJing
    """)

with pillar_col2:
    st.subheader("🖌️ 3. Graffiti/Street Art")
    st.write("""
    - **Oltre 4000 mq** dedicati ai graffiti
    - **40+ street artist** partecipanti
    - **Workshop interattivi** per tutti i livelli
    """)

    st.subheader("🕺 4. Breaking (Breakdance)")
    st.write("""
    - **Competizioni** tra i migliori breaker
    - **Workshop** e masterclass
    - **Cypher spontanee** durante la giornata
    """)

st.markdown("---")

# Attività complementari
st.header("Oltre i Quattro Pilastri")

extra_col1, extra_col2, extra_col3 = st.columns(3)

with extra_col1:
    st.subheader("🛹 Skate Culture")
    st.write("""
    - **Area skate** dedicata
    - **Esibizioni** di skate e rollerblade
    - **Mini contest** e demo
    """)

with extra_col2:
    st.subheader("Street Sports")
    st.write("""
    - **Torneo** di street basket
    - **Attività sportive** urbane
    - **Calisthenics** e parkour
    """)

with extra_col3:
    st.subheader("SC Kids")
    st.write("""
    - **Attività per bambini**
    - **Laboratori creativi**
    - **Area famiglia** sicura
    """)

st.markdown("---")

# Impegno Sociale
st.header("La Vocazione Sociale")

st.warning("""
**La caratteristica più qualificante di Strada Chiusa è la sua esplicita missione sociale.**

Il progetto persegue attivamente la **"riqualificazione di spazi urbani non valorizzati da troppo tempo"**, 
trasformando aree trascurate in centri vibranti di attività culturale.
""")

social_col1, social_col2 = st.columns(2)

with social_col1:
    st.subheader("Rigenerazione Urbana")
    st.write("""
    **Obiettivi concreti:**
    - Riqualificazione di **spazi urbani dimenticati**
    - Creazione di **centri di aggregazione** giovanile
    - **Rivitalizzazione** di aree della città
    - **Recupero** di spazi pubblici inutilizzati
    """)

with social_col2:
    st.subheader("Raccolta Fondi")
    st.write("""
    **Cause sostenute:**
    - **Ricerca sul cancro** (AIRC)
    - **Borse di studio** al Conservatorio "Niccolò Piccinni" di Bari
    - **Progetti sociali** locali
    - **Supporto** alla comunità
    """)

# SDGs ONU
st.subheader("Allineamento con gli SDGs ONU")

st.info("""
**Strada Chiusa è allineato con gli Obiettivi di Sviluppo Sostenibile delle Nazioni Unite:**

**🎯 SDG 8**: Lavoro dignitoso e crescita economica  
**🎯 SDG 10**: Ridurre le disuguaglianze  
**🎯 SDG 16**: Pace, giustizia e istituzioni forti

Questa strategia eleva il festival, posizionandolo all'interno di un quadro globale di sviluppo sostenibile.
""")

st.markdown("---")

# Modello di Finanziamento
st.header("Modello di Finanziamento Sostenibile")

finance_col1, finance_col2 = st.columns(2)

with finance_col1:
    st.subheader("Crowdfunding Comunitario")
    st.write("""
    **Numeri delle campagne passate:**
    - **€18.523** raccolti per la decima edizione
    - **€9.576** raccolti per l'edizione 2024
    - **Coinvolgimento diretto** della comunità
    """)

with finance_col2:
    st.subheader("Partnership Strategiche")
    st.write("""
    **Tipologie di supporto:**
    - **Sponsor** commerciali locali
    - **Partner istituzionali**
    - **Collaborazioni** con associazioni
    - **Sostegno** del Comune di Acquaviva
    """)

st.success("""
**Il modello di finanziamento rafforza l'identità di iniziativa comunitaria**, 
dove i sostenitori investono direttamente non solo nell'intrattenimento, 
ma nel **benessere collettivo** e nel **progresso sociale**.
""")

st.markdown("---")

# Connessione Generazionale
st.header("Ponte Tra le Generazioni")

st.write("""
**Strada Chiusa crea un dialogo costante tra le generazioni del hip-hop italiano.**

La scelta curatoriale di avere **veterani della scena** come host e ospiti non è casuale, 
ma un atto di grande significato simbolico che:
""")

generation_col1, generation_col2 = st.columns(2)

with generation_col1:
    st.markdown("""
    ### Onora il Passato
    - **Tributo** alle icone storiche
    - **Preservazione** della memoria culturale
    - **Trasmissione** del sapere
    """)

with generation_col2:
    st.markdown("""
    ### Coltiva il Futuro
    - **Piattaforma** per nuovi talenti
    - **Continuità** della tradizione
    - **Evoluzione** culturale
    """)

st.info("""
**Esempio**: La presenza di **Extrapolo** come host dell'edizione 2024 ha creato un ponte visibile 
tra la generazione pionieristica dell'hip-hop napoletano e il movimento contemporaneo radicato nel Sud.
""")

st.markdown("---")

# Impatto e Riconoscimenti
st.header("Impatto e Riconoscimenti")

impact_col1, impact_col2, impact_col3 = st.columns(3)

with impact_col1:
    st.metric("Anni di Storia", "11", delta="Dal 2014")
    st.metric("Volontari Attivi", "60+", delta="In crescita")

with impact_col2:
    st.metric("Artisti Ospitati", "100+", delta="Nazionale e internazionale")
    st.metric("Partecipanti", "Migliaia", delta="Ogni edizione")

with impact_col3:
    st.metric("Fondi Raccolti", "€28k+", delta="Per cause sociali")
    st.metric("Mq di Street Art", "4000+", delta="Area graffiti")

st.markdown("---")

# Call to Action
st.header("Unisciti al Movimento")

cta_col1, cta_col2 = st.columns(2)

with cta_col1:
    if st.button("Scopri L'Onda", use_container_width=True):
        st.switch_page("pages/sc25/1_2_onda.py")

with cta_col2:
    if st.button("📸 Edizioni Passate", use_container_width=True):
        st.switch_page("pages/sc25/4_1_history.py")

st.success("""
**Strada Chiusa esemplifica una fase matura e pienamente evoluta della cultura hip-hop**, 
in cui l'ethos del "rappresentare la comunità" viene tradotto in un'impresa sociale strutturata, 
misurabile e sostenibile. 🎵
""")