import streamlit as st

# Seiten-Konfiguration
st.set_page_config(page_title="👋 Willkommen", page_icon="👋")

# Sidebar-Hintergrund mit Farbverlauf + schwarze Schrift
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #7C9ED3, #C6DC8B);
        color: black !important;
    }
    [data-testid="stSidebar"] * {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Begrüßungstext
st.title("👋 Hey, schön, dass du hier bist!")

st.divider()

st.write("Liebes peopleware Team, hier habe ich dir ein paar Dinge vorbereitet.")
st.write(
    "Ich hoffe, dir gefällt es, und ich kann dir meinen Ehrgeiz und meine Motivation zeigen, "
    "neue Dinge zu lernen und meine Begeisterung für IT und Software demonstrieren.")

st.divider()
st. write("Diese gesamte Webiste habe ich mit Python und Streamlit erstellt. Weiter unten kannst du mehr dazu erfahren.")

st.divider()

# 🖥️ UI Design & Blender
st.subheader("🖥️ UI Design & Blender")
if st.button("➡️ mehr erfahren", use_container_width=True, key="blender"):
    st.switch_page("pages/UI_Design_&_Blender.py")

st.divider()

# ❓ Fragen & Antworten (FAQ)
st.subheader("❓ Fragen & Antworten")
if st.button("➡️ mehr erfahren", use_container_width=True, key="faq"):
    st.switch_page("pages/FAQ.py")

st.divider()

# 📄 Bewerbungsunterlagen
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