import streamlit as st

# Seiten Konfi
st.set_page_config(page_title="🧠 Mini Quiz", page_icon="🎯")

# Hintergrund
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(-45deg, #242525, #242525, #2b2b2b, #242525);
        background-size: 400% 400%;
    }
    .card {
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #0073ff;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 20px;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        background-color: white !important;
        color: #0073ff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Konfi
st.sidebar.title("📚 Quiz Navigation")
st.sidebar.write("Teste dein Wissen!")

# Quiz Fragen
quiz_fragen = {
    "Wie viele Kontinente gibt es?": ["5", "6", "7", "7"],
    "Größtes Land der Welt?": ["China", "USA", "Russland", "Russland"],
    "Wie viele Zähne hat ein Erwachsener?": ["28", "30", "32", "32"],
    "Welche Farbe ergibt Blau + Gelb?": ["Grün", "Orange", "Lila", "Grün"],
    "❗ Schwer: Welches Land ist nach einer Person benannt?": ["Kolumbien", "Bolivien", "Philippinen", "Philippinen"]
}

# Session State für Antworten
if "antworten" not in st.session_state:
    st.session_state.antworten = {}

st.title("🧠 Mini Quiz")

# Fragen anzeigen
for frage, (a, b, c, richtige_antwort) in quiz_fragen.items():
    with st.container():
        st.markdown(f'<div class="card"><h3>{frage}</h3>', unsafe_allow_html=True)
        st.session_state.antworten[frage] = st.radio("", [a, b, c], key=frage, index=None)
        st.markdown("</div>", unsafe_allow_html=True)

# Senden Button
if st.button("Senden"):
    richtig = sum(1 for frage, (a, b, c, richtige_antwort) in quiz_fragen.items() if st.session_state.antworten.get(frage) == richtige_antwort)
    st.sidebar.subheader("📊 Dein Ergebnis")
    st.sidebar.write(f"🎯 Du hast **{richtig} von {len(quiz_fragen)}** Fragen richtig!")

st.divider()


st.write("Lerne weiter und verbessere dein Wissen! 🚀")