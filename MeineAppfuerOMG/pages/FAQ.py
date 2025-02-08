import streamlit as st

st.set_page_config(page_title="❓ Fragen & Antworten", page_icon="❓")

# lineal Verlauf
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

st.title("❓ Fragen & Antworten (FAQ)")

st.divider()

st.write("Hier habe ich ein paar Fragen und Antworten vorbereitet. Ich hoffe, sie gefallen euch "
         "und ihr könnt mich dadurch etwas besser kennenlernen!")

fragen_antworten = {
    "Wie viele WPM schaffst du?": "71, blind mit einer Genauigkeit von 89% (gestern getestet).",
    "Welche sind deine Lieblings-Shortcuts?": "OPTION+CMD+>/< – universell einsetzbar, egal ob beim Schreiben oder im Browser. "
                                              "CMD+Z – ein echter Lebensretter!",
    "Welche Werte sind dir besonders wichtig?": "Zuverlässigkeit und Ehrlichkeit. Sich auf andere verlassen zu können, "
                                                "ist für mich unbezahlbar.",
    "Was ist dein Lieblingsessen?": "Ich habe kein festes Lieblingsgericht – solange kein Rosenkohl drin ist, esse ich fast alles gerne! "
                                    "Besonders freue ich mich aber auf Abende bei Takumi auf der Immermannstraße.",
    "Wann fühlst du dich am produktivsten?": "Sobald ich meinen Rechner aufklappe – geh mir weg mit Stift und Zettel.",
    "Welche Schwächen möchtest du verbessern?": "Ich habe mich lange als Perfektionist gesehen, aber nach dem Lesen von Steve Jobs’ Biografie "
                                                "wurde mir klar, dass Perfektionismus oft hinderlich ist. Ich arbeite daran, mich weniger in Details zu verlieren "
                                                "und mehr auf das große Ganze zu fokussieren.",
    "Was ist deine Lieblingsapp?": "Nicht unbedingt die, die ich am häufigsten nutze, aber eine, auf die ich nicht verzichten möchte: **Blinkist**.",
    "Wie kamst du dazu, programmieren zu wollen?": "Ich habe nach der Einführung der Kurzbefehle für Mac angefangen, kreative Workflows zu bauen. "
                                                   "Das fand ich so spannend, dass ich mehr darüber lernen wollte – und so bin ich über Recherchen auf die CS50-Kurse gestoßen. "
                                                   "Seitdem hat mich das Programmieren nicht mehr losgelassen!",
    "Warum die Omnicom Media Group??": "Die Omnicom Media Group vereint zwei Aspekte, die mich besonders ansprechen: Innovation und Zusammenarbeit. Besonders beeindruckt mich, wie "
                                       "OMG mit datengetriebenen Ansätzen und modernster Technologie Markenkommunikation auf ein neues Level hebt. Während meiner bisherigen Tätigkeiten, "
                                       "insbesondere bei BIRDIE & Co., habe ich wertvolle Einblicke in die Prozessoptimierung und digitale Transformation gewonnen. Ich durfte selbst Schulungen organisieren und "
                                       "erleben, wie wichtig eine effektive Vermittlung von Wissen für den Erfolg eines Projekts ist. Bei OMG sehe ich die Möglichkeit, meine technischen Fähigkeiten mit meiner Leidenschaft "
                                       "für klare Kommunikation und innovative Lösungen zu kombinieren. Mich begeistert der Gedanke, aktiv an Projekten mitzuwirken, die Kunden einen messbaren Mehrwert bieten, und gleichzeitig Teil"
                                       "eines dynamischen Teams zu sein, das die Grenzen des Möglichen in der digitalen Kommunikation auslotet.",
    "Wo siehst du dich in fünf Jahren?": "Als fester Bestandteil der Omnicom Media Group, in einem kreativen Team, das Innovationen vorantreibt.",
    "Welches ist dein Lieblingsbuch?": "Neben meinem All-Time-Favorite **Harry Potter und der Gefangene von Askaban** lese ich gerade "
                                       "**Die Abenteuer des Sherlock Holmes** von Arthur Conan Doyle. Es ist faszinierend, wie Holmes seine Fälle löst, "
                                       "und gleichzeitig ein spannender Einblick in eine vergangene Zeit.",
    "Was ist dein Traumjob?": "Ein Job, der mir kreative Freiheit gibt und in dem ich an innovativen Projekten arbeite, die wirklich etwas verändern können.",
    "Wie sieht dein idealer Arbeitstag aus?": "Solange ich einen oder zwei Shots Espresso hatte, bin ich für alles offen, was dann kommt!",
    "Lieblingsmusik-Genre?": "Ich höre alles, von Barock bis Rock. Mainstream-Pop ist nicht mein Ding. Mein Lieblingsalbum ist **Lucifuge** von Danzig.",
    "Gibt es eine Fähigkeit, die du lernen willst?": "Klarer kommunizieren und besser präsentieren, um meine Ideen überzeugender zu vermitteln.",
    "Welches Land möchtest du unbedingt besuchen?": "Ich liebe Österreich und war schon oft dort. Leider war ich noch nie in Wien – das steht definitiv auf meiner Liste.",
    "Was zeichnet dich aus?": "Mein Ehrgeiz und meine Motivation, mir immer wieder neue Dinge beizubringen."
}

frage = st.selectbox("Wähle eine Frage:", list(fragen_antworten.keys()))
st.write(f"**Antwort:** {fragen_antworten[frage]}")

st.divider()

st.write("Du hast noch weitere Fragen? Dann schreibe mir doch einfach!")
st.markdown("📧 **E-Mail:** [djordjevicluka@icloud.com](mailto:djordjevicluka@icloud.com)")