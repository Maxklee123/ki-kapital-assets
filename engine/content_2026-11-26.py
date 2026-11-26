# -*- coding: utf-8 -*-
# Inhalt 26.11.2026 (Donnerstag) - Saeule: AENGSTE ENTKRAEFTEN
# Kernbefund: KI loescht keine Stellen, sie verteilt Aufgaben neu.
DATE = "2026-11-26"
PILLAR = "AENGSTE ENTKRAEFTEN"

SRC_A = "Quelle: Epoch AI / Ipsos, Befragung 10.-19.07.2026, n=1.106 erwerbstätige Erwachsene (USA)"
SRC_B = "Quelle: Epoch AI / Ipsos KnowledgePanel, Befragung 03.-05.03.2026, n=2.021 Erwachsene (USA)"

TAKT = [0.7, 1.3, 3.4, 3.5, 3.5, 3.6]

REEL_A = [
    ("hook",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "white_text": "Du fürchtest um deinen Job.",
                "green_text": "Verteilt wird gerade etwas anderes."}),
    ("text",   {"kick": "DER DENKFEHLER",
                "headline": "Die Kündigung ist das falsche Bild.",
                "body": "Was sich bewegt, ist kleiner. Und es bewegt sich **schon jetzt**.",
                "src": SRC_A}),
    ("number", {"kick": "DIE ZAHL",
                "big": "20 %",
                "caption": "der Beschäftigten in den USA",
                "body": "Bei **jedem Fünften** erledigt KI mindestens eine Aufgabe, die vorher ein **Kollege oder ein Dienstleister** gemacht hat.",
                "src": SRC_A}),
    ("text",   {"kick": "WAS DAS HEISST",
                "headline": "Gestrichen wird keine Stelle. Neu verteilt wird eine Aufgabe.",
                "body": "Niemand sagt dir, dass du eine verloren hast. Es fragt nur irgendwann **keiner mehr bei dir nach**.",
                "src": SRC_A}),
    ("text",   {"kick": "DIE EIGENTLICHE FRAGE",
                "headline": "Nicht: Bleibt die Aufgabe? Sondern: Bei wem landet sie?",
                "body": "Das entscheidet sich an den Aufgaben, die du **als Erster** mit KI übernimmst.",
                "src": SRC_A}),
    ("cta",    {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "statement": "Jeden Tag ein Workflow, damit die Aufgabe bei dir landet.",
                "cta": "FOLGEN"}),
]

REEL_B = [
    ("hook",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "white_text": "Du weißt nicht, was du abgeben sollst.",
                "green_text": "Also gibst du nichts ab."}),
    ("text",   {"kick": "DER SORTIERFEHLER",
                "headline": "Die meisten sortieren nach Lästigkeit.",
                "body": "Abgeben solltest du, was **keine Entscheidung** von dir verlangt.",
                "src": SRC_B}),
    ("number", {"kick": "DIE ZAHL",
                "big": "27 %",
                "caption": "sagen: Aufgaben wurden ersetzt",
                "body": "Gleichzeitig sagen **21 %**, dass durch KI **neue Aufgaben** entstanden sind. Dein Job schrumpft nicht. Er wird umgebaut.",
                "src": SRC_B}),
    ("text",   {"kick": "DIE MECHANIK",
                "headline": "Du brauchst keine Liste aller Aufgaben.",
                "body": "Du brauchst **drei Körbe** — und je Korb eine Entscheidung.",
                "src": SRC_B}),
    ("steps",  {"kick": "DER AUFGABEN-SORTIERER — 4 ZEILEN",
                "title": "Einmal pro Woche einfügen",
                "steps": [
                    "Sortieren: **„Meine wiederkehrenden Aufgaben dieser Woche: [Liste]. Sortiere sie in A, B und C.“**",
                    "Regel geben: **„A = Text, Tabelle, Auswertung ohne Haus-Wissen. B = braucht mein Urteil. C = bringt nichts.“**",
                    "Urteil sichern: **„Nenne für jede B-Aufgabe in einem Satz, wo genau mein Urteil entscheidet.“**",
                    "Eine abgeben: **„Nenne die eine A-Aufgabe für diese Woche — plus den Prompt dafür.“**",
                ],
                "src": SRC_B}),
    ("save",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "headline": "Du brauchst das nicht jetzt. Sondern Montag.",
                "save_title": "Sicher dir das für Montag, 9:00 Uhr",
                "save_sub": "Wenn du dir die Woche sortierst und entscheidest, was du abgibst."}),
]

STORY_1 = ("teaser", {"kick": "HEUTE UM 10 UHR",
                      "headline": "1 von 5 — aber nicht so, wie du denkst",
                      "body": "Bei jedem fünften Beschäftigten erledigt KI schon eine Aufgabe. **Nicht seine eigene.** Woher sie kommt, steht um 10 Uhr.",
                      "src": SRC_A})

STORY_4 = ("question", {"kick": "EINE FRAGE",
                        "headline": "Welche Aufgabe würdest du morgen abgeben?",
                        "sub": "Tippe die Zahl in die DM — ich schicke dir heute Abend die Auswertung.",
                        "options": ["Berichte und Protokolle schreiben",
                                    "Daten sortieren und prüfen",
                                    "Mails und Anfragen beantworten"],
                        "badge": "20 % geben schon eine Aufgabe ab"})

STORY_5 = ("dm", {"kick": "VORLAGE PER DM",
                  "headline": "Der Aufgaben-Sortierer",
                  "keyword": "SORTIEREN",
                  "body": "Vier Zeilen, die deine Woche in drei Körbe teilen — und dir die eine Aufgabe nennen, die du diese Woche abgeben kannst.",
                  "cta": "SCHREIB MIR SORTIEREN"})

CAP_1 = """Bei jedem fünften Beschäftigten erledigt KI schon eine Aufgabe. Nicht seine eigene.

Woher diese Aufgabe kommt, steht um 10 Uhr im Reel.

Quelle: Epoch AI / Ipsos, Befragung 10. bis 19. Juli 2026, n = 1.106 erwerbstätige Erwachsene in den USA.

#kiimjob #zukunftsangst #15minutenvorsprung"""

CAP_2 = """Nicht dein Job verschwindet. Deine Aufgaben wechseln den Besitzer — und zwar schon jetzt.

Die Angst vor KI hängt fast immer am selben Bild: eine Kündigung, eine Abteilung, ein Stichtag. In den Zahlen taucht dieses Bild nicht auf. Ein kleineres taucht auf.

Epoch AI hat zusammen mit dem Institut Ipsos 1.106 erwerbstätige US-Amerikaner befragt. Jeder Fünfte sagt: KI erledigt bei mir inzwischen mindestens eine Aufgabe, die vorher ein Kollege oder ein externer Dienstleister gemacht hat.

Das ist keine Entlassungswelle. Das ist eine Umverteilung — eine Ebene unter der Stelle, auf der Ebene der einzelnen Aufgabe.

Genau deshalb merkst du sie nicht. Niemand teilt dir mit, dass du eine Aufgabe verloren hast. Es fragt nur irgendwann keiner mehr bei dir nach.

Die Frage im Team lautet also nicht, ob eine Aufgabe bleibt. Sie lautet, bei wem sie landet. Und das entscheidet sich an den Aufgaben, die du als Erster mit KI übernimmst — nicht an deinem Lebenslauf.

Hier gibt es jeden Tag einen Workflow, der genau dafür sorgt.

Quelle: Epoch AI / Ipsos, Befragung 10. bis 19. Juli 2026, n = 1.106 erwerbstätige Erwachsene in den USA.

#kiimjob #zukunftsangst #15minutenvorsprung"""

CAP_3 = """Öffne das am Montag um 9, wenn du dir die Woche sortierst — dann brauchst du genau diese vier Zeilen.

Du weißt nicht, welche Aufgabe du abgeben sollst. Also gibst du keine ab.

Die meisten sortieren nach Lästigkeit. Das ist der Fehler. Abgeben solltest du, was keine Entscheidung von dir verlangt — nicht das, was nervt.

In derselben Befragungsreihe sagen 27 Prozent der Beschäftigten mit KI-Nutzung, dass Aufgaben ersetzt wurden. 21 Prozent sagen, dass neue entstanden sind. Dein Job schrumpft nicht. Er wird umgebaut — und wer beim Umbau nicht mitsortiert, bekommt den Rest zugeteilt.

Diese vier Zeilen kopierst du einmal pro Woche in dein KI-Tool:

1. "Meine wiederkehrenden Aufgaben dieser Woche: [Liste]. Sortiere sie in A, B und C."
2. "A = das Ergebnis ist Text, Tabelle oder Auswertung und braucht kein Haus-Wissen. B = braucht mein Urteil über Menschen, Historie oder Risiko. C = KI bringt hier nichts."
3. "Nenne für jede B-Aufgabe in einem Satz, an welcher Stelle genau mein Urteil die Entscheidung ist."
4. "Nenne die eine A-Aufgabe, die ich diese Woche komplett abgeben kann — plus den Prompt dafür."

Zeile 3 ist die wichtige. Sie liefert dir den Satz, mit dem du im Meeting begründest, warum diese Aufgabe bei dir bleibt. Zeile 4 verhindert, dass du dich verzettelst: eine Aufgabe, diese Woche, fertig.

Funktioniert in Sachbearbeitung, Projektarbeit, Marketing und HR. Überall dort, wo Aufgaben im Team verteilt werden.

Quelle: Epoch AI / Ipsos KnowledgePanel, Befragung 3. bis 5. März 2026, n = 2.021 Erwachsene in den USA.

#kiimjob #prompt #15minutenvorsprung"""

CAP_4 = """Welche Aufgabe würdest du morgen abgeben?

1 Berichte und Protokolle schreiben
2 Daten sortieren und prüfen
3 Mails und Anfragen beantworten

Tippe die Zahl in die DM — ich schicke dir heute Abend die Auswertung.

#kiimjob #arbeitsalltag #15minutenvorsprung"""

CAP_5 = """Der Aufgaben-Sortierer als fertige Vorlage.

Vier Zeilen, die deine Woche in drei Körbe teilen — und dir die eine Aufgabe nennen, die du diese Woche komplett abgeben kannst.

Schreib mir SORTIEREN als DM, dann schicke ich sie dir.

#kiimjob #prompt #15minutenvorsprung"""

SLOTS = {
    "1": {"time": "09:00", "format": "Story",  "frames": [STORY_1], "caption": CAP_1},
    "2": {"time": "10:00", "format": "Reel A", "frames": REEL_A,    "caption": CAP_2},
    "3": {"time": "14:00", "format": "Reel B", "frames": REEL_B,    "caption": CAP_3},
    "4": {"time": "15:00", "format": "Story",  "frames": [STORY_4], "caption": CAP_4},
    "5": {"time": "20:00", "format": "Story",  "frames": [STORY_5], "caption": CAP_5},
}
