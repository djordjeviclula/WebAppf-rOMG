import streamlit as st

# Konfiguration
st.set_page_config(page_title="👋 Willkommen", page_icon="👋")

# Styling für Sidebar und Logo
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #7C9ED3, #C6DC8B);
        color: black !important;
        padding-top: 20px;
        position: relative;
    }
    [data-testid="stSidebar"] * {
        color: black !important;
    }
    .logo-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .logo-container img {
        max-width: 150px; /* Breite des Logos */
        max-height: 150px; /* Höhe des Logos */
        margin: 0 auto;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo einfügen
st.sidebar.markdown(
    """
    <div class="logo-container">
        <img src="https://static.wixstatic.com/media/48e2f2_9faff59164a343948cc25328031b85fa~mv2.png/v1/fill/w_174,h_176,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/48e2f2_9faff59164a343948cc25328031b85fa~mv2.png" alt="Logo">
    </div>
    """,
    unsafe_allow_html=True
)

# Anfang
st.title("👋 Hey, schön, dass du hier bist!")

st.divider()

st.write("Liebe Frau Kampka, lieber Herr Fernandez, liebes Peopleware-Team,")
st.write(
    "Ich hoffe, euch gefällt es und ich kann damit zeigen, wie viel Spaß ich am Lernen habe. "
    "Gleichzeitig möchte ich meine Begeisterung für IT, Software und digitale Prozesse mit euch teilen!"
)

st.divider()
st.write(
    "Diese gesamte Web-App habe ich mit **Python & Streamlit** erstellt. Weiter unten könnt ihr mehr dazu erfahren.")

st.divider()

# 🖥️ UI Design & Blender
st.subheader("🖥️ UI Design & Blender")
if st.button("➡️ mehr erfahren", use_container_width=True, key="blender"):
    st.switch_page("pages/UI_Design_&_Blender.py")

st.divider()

# ❓ F&As
st.subheader("❓ Fragen & Antworten")
if st.button("➡️ mehr erfahren", use_container_width=True, key="faq"):
    st.switch_page("pages/FAQ.py")

st.divider()

# 📄 Bewerbungsdateien
st.subheader("📄 Bewerbungsunterlagen")
if st.button("➡️ mehr erfahren", use_container_width=True, key="bewerbung"):
    st.switch_page("pages/Bewerbung.py")

st.divider()

# 🐍 Python & Streamlit
st.subheader("🐍 Python & Streamlit")
if st.button("➡️ mehr erfahren", use_container_width=True, key="python"):
    st.switch_page("pages/Python_&_Streamlit.py")

st.divider()

# Abschluss
st.write("Danke fürs Vorbeischauen! 😊")