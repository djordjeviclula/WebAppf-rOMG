import streamlit as st

# Konfiguration der Seite
st.set_page_config(page_title="🐍 Python & Streamlit", page_icon="🐍")

# Sidebar Design und Farbverlauf
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

# Titel der Seite
st.title("🐍 Python & Streamlit – Meine erste Web-App")

# Einleitung
st.markdown(
    """
    <div style="font-size:18px; font-weight:bold;">
    Diese Seite ist entstanden, weil ich mich unbedingt mit Python und Streamlit auseinandersetzen wollte. 
    Ich wollte für diese Bewerbung etwas Besonderes machen und über mich hinauswachsen. 
    Nach einigen Tagen des Experimentierens konnte ich diese Web-App bauen!
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Zitate
st.markdown(
    """
    <div style="
        background-color: #133A4E;
        border-left: 4px solid #0D2533;
        padding: 10px;
        font-style: italic;
        font-size: 18px;
        color: white;">
        Ich bin kein Pro, aber will einer werden.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Beschreibender Text
st.write("Auch wenn das Projekt klein erscheint, habe ich **sehr viel gelernt** "
         "und bin stolz darauf, es mit euch teilen zu können!")

st.divider()

# Unterüberschrift
st.subheader("🚀 Mein Weg zum Projekt")

st.write("Am Anfang hatte ich die Idee, eine **GUI als One-Pager mit Tkinter** zu bauen – "
         "aber das war für meinen Wissensstand eine Nummer zu groß. Nach einiger Recherche habe ich mich für **Streamlit** entschieden, "
         "weil der Einstieg einfacher schien.")

st.write("Doch auch wenn der Start simpel wirkte, war die Umsetzung eine echte Herausforderung. "
         "Ich hatte vor diesem Projekt **kaum Erfahrung im Programmieren** – nur die **Grundlagen von Python** hatte ich mir vorher angeeignet.")

st.write("Also begann ich meine Reise:")

st.markdown("""
✔️ **Viele Stunden YouTube-Tutorials geschaut**  
✔️ **Unzählige Google-Suchen durchgeführt**  
✔️ **Die sehr gute Streamlit-Dokumentation genutzt**  
""")

st.divider()

# Unterüberschrift zu Herausforderungen und Durchbrüchen
st.subheader("⚡ Herausforderungen und Durchbrüche")

st.write("Ich habe wirklich **Tag und Nacht** an diesem Code gesessen. "
         "Auch wenn er für erfahrene Entwickler vielleicht einfach aussieht, war es für mich eine riesige Herausforderung. "
         "Es gab Momente, in denen ich **komplett feststeckte** und nicht weiterwusste – und ja, vielleicht war auch mal ein kleiner **Nervenzusammenbruch** dabei.")

st.write("Doch **aufgeben kam nicht in Frage**. Ich habe mich durchgebissen, gelernt, ausprobiert und Fehler behoben – und jetzt bin ich **stolz auf das Ergebnis**.")

st.divider()

# Abschlusszitat
st.markdown(
    """
    <div style="
        background-color: #133A4E;
        border-left: 4px solid #0D2533;
        padding: 10px;
        font-size: 16px;
        color: white;">
        Noch nie habe ich so viel Arbeit in eine Bewerbung gesteckt. Doch genau das zeigt meinen 
        <strong>Ehrgeiz</strong>, meine <strong>autodidaktischen Fähigkeiten</strong> und meine 
        <strong>brennende Motivation</strong>, von euch zu lernen. Ich hoffe, dass meine Mühe sich lohnt 
        und ich die Chance bekomme, Teil der <strong>Peopleware Gruppe</strong> zu werden.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Ende - Kontinuierliches Lernen
st.subheader("🚀 Kontinuierliches Lernen")

st.write(
    "Dieses Projekt ist nur der Anfang. Ich bin fest entschlossen, mich kontinuierlich weiter zu entwickeln und mich bald auch mit **Django** oder anderen fortgeschrittenen Tools auseinanderzusetzen. Ich glaube, dass ich dadurch meine Fähigkeiten noch weiter ausbauen kann."
)