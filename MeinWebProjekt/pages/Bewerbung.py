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

st.markdown("[📜 Anschreiben](https://example.com/anschreiben.pdf)")
st.markdown("[📄 Motivationsschreiben](https://example.com/motivationsschreiben.pdf)")
st.markdown("[🎓 Zeugnisse](https://example.com/zeugnisse.pdf)")