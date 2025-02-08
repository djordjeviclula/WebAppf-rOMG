import streamlit as st

st.set_page_config(page_title="📄 Bewerbungsunterlagen", page_icon="📄")

# Lineal Verlauf
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

st.title("📄 Bewerbungsunterlagen")

st.write("Hier findest du meine Bewerbungsunterlagen als PDF.")

# erste Links
st.markdown("[📜 Anschreiben](https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_faa9926d93864cf5a55f55126daa87f0.pdf)")
st.markdown("[📄 Lebenslauf](https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_ef48180d28274fcaad6ee27d627ec440.pdf)")

# Zeugnisse
st.subheader("🎓 Zeugnisse")

# Links von Zeugnissen
zeugnisse_files = {
    "Zeugnis Übersicht": "https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_98a270e662cd4e51bbc152c4f3139b7a.pdf"
}

# Zeugnisse anzeigen
for title, pdf_link in zeugnisse_files.items():
    st.markdown(f"[{title}]({pdf_link})")

# Auszeichnungen
st.subheader("🏆 Auszeichnungen")

# Links von Auszeichnungen
auszeichnungen_files = {
    "Auszeichnungen Übersicht": "https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_f6ea8a34ee054ef7b04b22ebb764c8a0.pdf"
}

# Auszeichnungen anzeigen
for title, pdf_link in auszeichnungen_files.items():
    st.markdown(f"[{title}]({pdf_link})")