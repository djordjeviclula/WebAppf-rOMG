import tkinter as tk

# Farben und Fonts
TEXT_COLOR = "white"
BUTTON_COLOR = "white"
BACKGROUND_COLOR = "#B3ABB5"
QUESTION_BACKGROUND = "#373737"
HEADER_BACKGROUND = "black"
BUTTON_FONT = ("Courier", 14, "bold")
LABEL_FONT = ("Courier", 18, "normal")
HEADER_FONT = ("Courier", 30, "bold")

# F&As
fragen_antworten = {
    "Wie viele WPM schaffst du?": "71, blind mit einer Genauigkeit von 89% (gestern getestet).",
    "Welche sind deine Lieblings-Shortcuts?": "OPTION+CMD+>/< – der lässt sich für alles verwenden, beim Texte schreiben oder im Browser. CMD+Z – ein Lebensretter.",
    "Welche Werte sind dir besonders wichtig?": "Auf jeden Fall Zuverlässigkeit und Ehrlichkeit. Sich auf jeden verlassen zu können, ist das Schönste, was es gibt.",
    "Was ist dein Lieblingsessen?": "Das habe ich nicht direkt. Solange kein Rosenkohl drin ist, esse ich alles gerne. Besonders freue ich mich aber auf Abende bei Takumi auf der Immermannstraße.",
    "Wann fühlst du dich am produktivsten?": "Sobald ich meinen Rechner aufklappe. Geh mir weg mit Stift und Zettel.",
    "Welche Schwächen möchtest du verbessern?": "Ich habe mich lange als Perfektionist gesehen, doch nach dem Lesen von Steve Jobs’ Biografie wurde mir klar, dass diese Eigenschaft im Alltag oft hinderlich ist. Mein Ziel ist es, den Fokus mehr auf das große Ganze zu legen und weniger in Details zu verlieren.",
    "Was ist deine Lieblingsapp?": "Nicht unbedingt die, welche ich am häufigsten benutze, aber die, von der ich am wenigsten verzichten wollen würde: Blinkist.",
    "Wie kamst du dazu, programmieren zu wollen?": "Ich habe nach Einführung der Kurzbefehle für Mac angefangen, verrückte Kurzbefehle zu erstellen. Das fand ich so spannend, dass ich nach Recherche auf die CS50-Kurse gestoßen bin. Danach war ich hooked.",
    "Warum Peopleware?": "Während meiner Zeit bei BIRDIE & Co. habe ich intensiv mit Notion und Apicbase gearbeitet, um Arbeitsprozesse zu optimieren. Dabei wurde mir klar, dass diese Tools nicht alle meine Anforderungen abdecken. Bei Peopleware sehe ich die Möglichkeit, meine Erfahrung in der Prozessoptimierung einzubringen und durch die Ausbildung meine Programmierkenntnisse weiter zu vertiefen, um maßgeschneiderte Lösungen zu entwickeln.",
    "Wo siehst du dich in fünf Jahren?": "Als eingeschworenes Teammitglied der Peopleware-Gruppe. Das wäre grandios.",
    "Welches ist dein Lieblingsbuch?": "Neben meinem All-Time-Favorite Harry Potter und der Gefangene von Askaban lese ich gerade Die Abenteuer des Sherlock Holmes von Arthur Conan Doyle. Es ist wie ein Blick in eine vergangene Zeit. Außerdem fasziniert mich der Scharfsinn, mit dem Holmes seine Fälle löst.",
    "Was ist dein Traumjob?": "Ein Job, der mir kreative Freiheit und die Möglichkeit gibt, an innovativen Projekten zu arbeiten, die wirklich etwas verändern.",
    "Wie sieht dein idealer Arbeitstag aus?": "Ich denke, solange ich einen oder zwei Shots Espresso hatte, bin ich für alles offen, was dann kommt.",
    "Welche App ist deine liebste?": "Eine App, die ich nicht am häufigsten benutze, aber auf keinen Fall drauf verzichten möchte: Blinkist.",
    "Lieblingsmusik-Genre": "Ich höre alles, von Barock bis Rock. Bin aber absolut kein Pop- oder Mainstream-Musikhörer. Mein Lieblingsalbum ist Lucifuge von Danzig.",
    "Gibt es eine Fähigkeit, die du lernen willst?": "Klarer kommunizieren und besser präsentieren, um meine Ideen noch überzeugender vermitteln zu können.",
    "Welches Land möchtest du unbedingt besuchen?": "Ein Land, in dem ich schon häufig war, ist Österreich. Ich besuche es immer wieder gerne. Leider war ich noch nie in Wien. Das ist auf jeden Fall ein Vorsatz.",
    "Was zeichnet dich aus?": "Die Fähigkeit und die Motivation, mir immer neue Dinge beizubringen.",
}

# As anzeigen lassen
def zeige_antwort(frage):
    antwort_label.config(text=fragen_antworten[frage])  # Antwort Text aktualisieren

# Fenster erstellen
root = tk.Tk()
root.title("uebermich")
root.attributes("-fullscreen", True) #alles auf Vollbild
root.configure(bg=BACKGROUND_COLOR)

# Header Bereich
header_frame = tk.Frame(root, bg=HEADER_BACKGROUND, height=180)
header_frame.pack(fill="x")  # Header über die ganze Breite

welcome_label = tk.Label(header_frame, text="Hi, schön, dass du hier bist!",
                         fg=TEXT_COLOR, bg=HEADER_BACKGROUND, font=HEADER_FONT, wraplength=900, pady=90)
welcome_label.pack()  # Begrüßungstext in den Header

# Hauptbereich für F&As
frame_main = tk.Frame(root, bg=QUESTION_BACKGROUND)  # Hauptbereich mit Hintergrundfarbe für F&A
frame_main.pack(fill="both", expand=True, padx=0, pady=0)
frame_main.pack_propagate(False)

antwort_label = tk.Label(frame_main, text="Um mehr über mich zu erfahren, wähle bitte eine Frage um die Antwort zu sehen",
                         font=LABEL_FONT, wraplength=700, pady=40, bg=QUESTION_BACKGROUND, fg=TEXT_COLOR)
antwort_label.pack()  # Antwort Text wird im Hauptbereich angezeigt

# Fs als Buttons
grid_frame = tk.Frame(frame_main, bg=QUESTION_BACKGROUND)
grid_frame.pack(fill="both", expand=True, pady=60)

# Fragen als Buttons
row_index = 0
col_index = 0
columns = 3  # Anzahl der Spalten

for frage in fragen_antworten.keys():  # Durch alle Fragen gehen
    # Button für jede Frage erstellen
    btn = tk.Button(grid_frame, text=frage, bg=BUTTON_COLOR, fg="black", font=BUTTON_FONT, width=50, height=2,
                    command=lambda f=frage: zeige_antwort(f))  # Button zeigt die Antwort an bei Klicken
    btn.grid(row=row_index, column=col_index, padx=10, pady=20, sticky="nsew")  # Button in Grid einfügen

    col_index += 1  # Spalte erhöhen
    if col_index >= columns:  # Wenn 3 Spalten erreicht sind, auf die nächste Zeile wechseln
        col_index = 0
        row_index += 1

# Spalten gleichmäßig verteilen
for i in range(columns):  # Jede Spalte gleichmäßig verteilen
    grid_frame.columnconfigure(i, weight=1)  # Spaltengewicht

# Fenster starten
root.mainloop()  # Hauptloop starten (wichtig, damit das Fenster bleibt und interaktiv ist)