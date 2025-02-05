import streamlit as st

st.set_page_config(page_title="📄 Bewerbungsunterlagen", page_icon="📄")

# Einheitliches Sidebar-Design
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

# Anschreiben und Lebenslauf Links
st.markdown("[📜 Anschreiben](https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_faa9926d93864cf5a55f55126daa87f0.pdf)")
st.markdown("[📄 Lebenslauf](https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_ef48180d28274fcaad6ee27d627ec440.pdf)")

# Zeugnisse - Mehrere PDFs
st.subheader("🎓 Zeugnisse")

# Liste der PDF-Dateien mit den entsprechenden Links
pdf_files = {
    "Zeugnis Nr. 1 Fachhochschulreife": "https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_a12066e1c3624309b974a3473609960e.pdf",
    "Zeugnis Nr. 2 Einführung in die gymnasiale Oberstufe": "https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_2ef7591aca5d4618adda0a2ca650b71a.pdf",  # Platzhalter-Link, bitte ersetzen
    "Zeugnis Nr. 3 mit IT Note": "https://f6c82f18-3090-44ca-b3bd-b4593bb23558.filesusr.com/ugd/48e2f2_0d8de98a6c54437fbd2f5de8e3e4ac1e.pdf"   # Platzhalter-Link, bitte ersetzen
}

# Iteriere durch die PDF-Dateien und stelle sie als Links dar
for title, pdf_link in pdf_files.items():
    st.markdown(f"[{title}]({pdf_link})")