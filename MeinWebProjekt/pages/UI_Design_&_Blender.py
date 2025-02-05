import streamlit as st

# Titel
st.set_page_config(page_title="🌍 UI Design & Blender", page_icon="🌍")

# lieneal Verlauf
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

# Titel
st.title("🌍 UI Design & Blender")

st.divider()

# Website-Link
st.markdown("[➡️ Hier geht's zur Forest and Frame Website](https://www.forestandframe.com)")
st.write("Diese Website habe ich in den letzten 12 Monaten in meiner Freizeit erstellt.")
st.write("Alle Bilder wurden mit **Blender** erstellt – ohne Vorkenntnisse!")

# Bild
st.image("https://static.wixstatic.com/media/48e2f2_8b51a14f25b94daea3e696ffbd1c299a~mv2.jpg/v1/fill/w_1200,h_342,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/48e2f2_8b51a14f25b94daea3e696ffbd1c299a~mv2.jpg",
         caption="Finales Rendering", use_container_width=True)

st.divider()

# 📌 Renderings und Blender
st.subheader("📌 Renderings und Blender")

st.write(
    "Mein erstes Konzept habe ich am iPad mit **Shapr3D** erstellt. "
    "Hier konnte ich bereits auf erste Erfahrungen aus dem 3D-Druck zurückgreifen, "
    "da ich zuvor einige Modelle mit dieser Software entwickelt hatte. "
    "Dennoch war es ein völlig neuer Bereich für mich, da ich mich noch nie mit fotorealistischen Renderings auseinandergesetzt hatte."
)

# Bild
st.image("https://static.wixstatic.com/media/48e2f2_914116ac05d34acabff09c9df5ab6035~mv2.png",
         caption="Mein erstes 3D-Konzept", use_container_width=True)

st.write(
    "💡 **Herausforderung:**\n"
    "Ich wollte professionelle und hochwertige Produktbilder erstellen, aber ohne das Budget für aufwendige Fotografie oder physische Prototypen. "
    "Deshalb war für mich die einzig sinnvolle Lösung, mich in **Blender** einzuarbeiten und mir das nötige Wissen komplett selbst beizubringen.\n\n"
    "Doch der Einstieg in **Blender** war alles andere als einfach. Die unzähligen Funktionen und komplexen Workflows wirkten zunächst überwältigend. "
    "Aber anstatt mich davon entmutigen zu lassen, habe ich monate lang recherchiert, YouTube-Tutorials geschaut und unzählige Fehler gemacht**, "
    "bis ich endlich erste brauchbare Ergebnisse hatte. Dieses autodidaktische Lernen hat mich begeistert und mir gezeigt, "
    "dass ich durch Ausdauer und Neugier fast jedes Problem lösen kann."
)

st.divider()

# 📌 Finales Rendering
st.subheader("📌 Finales Rendering")

st.write("Es hat **ca. 4 Monate** gedauert, bis ich das nötige Skillset aufgebaut hatte, um hochqualitative Renderings zu erstellen.")

# Bild
st.image("https://static.wixstatic.com/media/48e2f2_f1260fcdaa1f44d1b6669978160bcf83~mv2.jpeg",
         caption="Finales Rendering", use_container_width=True)

st.write(
    "🎯 **Technische Herausforderung:**\n"
    "Obwohl mein MacBook M1 eine leistungsstarke CPU besitzt, war die **GPU-Leistung nicht ausreichend**, "
    "um die hochauflösenden Renderings effizient zu berechnen. Nach mehreren Stunden Wartezeit und einigen Abstürzen wurde mir klar, "
    "dass ich eine externe Lösung brauchte. Ich entschied mich für den Online-Render-Service **GarageFarm**, "
    "wo ich meine Bilder für ein paar Cent pro Rendering berechnen lassen konnte."
)

st.write(
    "👉 **Fazit:**\n"
    "Dieser gesamte Prozess war eine der größten Herausforderungen, denen ich mich je gestellt habe – "
    "von den ersten, groben Entwürfen bis hin zu professionellen Renderings. Doch genau das hat mir unglaublich viel Freude bereitet: "
    "**neue Technologien zu meistern, Probleme eigenständig zu lösen und meine Fähigkeiten kontinuierlich zu verbessern.**"
)

st.divider()

# 📌 Die Website
st.subheader("📌 Die Website")

st.write(
    "Nachdem die Renderings fertig waren, wollte ich sie in einer hochwertigen **Webseite** präsentieren. "
    "Ich habe mich für **Wix Studio** entschieden, da ich bereits Erfahrung mit Website-Baukästen hatte. "
    "Doch die **Komplexität dieses Projekts** mit über **50 Unterseiten, zahlreichen Verknüpfungen und Shop-Management** "
    "stellte mich vor völlig neue Herausforderungen."
)

st.write(
    "🌍 **Meine Learnings:**\n"
    "- Ich musste mich intensiv mit **UI/UX-Design** beschäftigen, um eine ansprechende und intuitive Benutzeroberfläche zu gestalten.\n"
    "- Durch die Arbeit mit **Wix Studio** habe ich ein besseres Verständnis für Webstrukturen und responsives Design gewonnen.\n"
    "- **Figma** war mein Tool der Wahl für das Grafikdesign – ein Bereich, in dem ich bereits fortgeschrittene Kenntnisse besitze, "
    "aber durch dieses Projekt noch weiter vertiefen konnte."
)

st.write(
    "👉 **Herausforderung angenommen!**\n"
    "Die Website ist sicher nicht perfekt, und an einigen Stellen müsste die **Responsivität** noch optimiert werden. "
    "Doch insgesamt bin ich **sehr stolz auf das Ergebnis**. Dieses Projekt hat mir gezeigt, dass es **keine Grenze gibt, "
    "wenn man bereit ist, sich neues Wissen anzueignen und sich durch Herausforderungen durchzukämpfen.**"
)

st.divider()

# ende
st.write(
    "### **Zusammenfassung:**\n"
    "✅ Von **Null Erfahrung mit Blender** bis hin zu fotorealistischen Renderings.\n"
    "✅ Von **Webdesign-Anfänger** zu einer komplexen, gut strukturierten Website.\n"
    "✅ Von **Herausforderungen überwältigt** zu einem fertigen Projekt, auf das ich stolz bin.\n\n"
    "Dieses Projekt war eine der größten autodidaktischen Herausforderungen, die ich je gemeistert habe. **Und ich bin bereit, noch weiterzugehen!** 💡🔥"
)