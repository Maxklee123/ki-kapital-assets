# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-22 (Sonntag) - Saeule: AENGSTE ENTKRAEFTEN
# Quelle: Federal Reserve Bank of Boston, CPP 26-8, 02.09.2026 (Primaer-PDF
# cpp2608.pdf im Wortlaut geprueft). 21,2 / 6,1 / 6,4 % sind MODELLWERTE aus
# einer Regression mit Kontrollvariablen, keine ausgezaehlten Anteile.
# Nicht wiederholt: IAB +1 %/-3 % (lief am 15.11. in derselben Saeule),
# TU Darmstadt (11.11.), BCG (06.11., anderes Haus als die Boston Fed),
# Goldman Sachs (19.11.), Adecco (20.11.), PwC/HR Works (21.11.).
# Workflow-Abgrenzung: KEIN Aufgaben-Audit (11./15.11.) - heute wird nichts
# sortiert und nichts geschaetzt, sondern EINE Aufgabe EINMAL durchlaufen
# und dabei gemessen, Pruefzeit eingerechnet.

NB = " "

SRC_FED = ("Federal Reserve Bank of Boston, Current Policy Perspectives 26-8, "
           "02.09.2026 · Panel rund 1.300 US-Haushalte, Welle Dez. 2025")
SRC_FED2 = ("US-Befragung, nicht Deutschland · Selbsteinschätzung, nicht "
            "gemessen · Schätzwerte aus einem Modell, kein ausgezählter Anteil")

STORY_1 = [
    {"k": "kicker", "t": "SONNTAG · 09 UHR"},
    {"k": "num", "t": "60" + NB + "%", "s": 195, "c": (77, 212, 200)},
    {"k": "numsub", "t": "erwarten KI-bedingten Stellenabbau – in ihrer Branche.", "s": 50},
    {"k": "body", "t": "Um den eigenen Job fürchtet gut ein Zehntel. Die Angst ist also groß für alle anderen und klein für einen selbst. Es gibt eine dritte Zahl, und die zeigt, wo sie wirklich sitzt."},
    {"k": "src", "t": SRC_FED},
    {"k": "gap", "s": 12},
    {"k": "cta", "t": "Um 10 Uhr steht die dritte Zahl"},
]

REEL_A = [
    [{"k": "kicker", "t": "SONNTAG"},
     {"k": "big", "t": "Du denkst, die Angst vor KI wird kleiner, wenn du Abstand hältst.", "s": 84}],
    [{"k": "kicker", "t": "SIE IST ABER WOANDERS"},
     {"k": "big", "t": "Am größten ist sie bei denen, die KI längst benutzen.", "s": 86}],
    [{"k": "kicker", "t": "GESCHÄTZT"},
     {"k": "num", "t": "21,2" + NB + "%", "s": 150},
     {"k": "numsub", "t": "Jobsorge bei denen, die KI nutzen – und keinen Gewinn davon merken.", "s": 46},
     {"k": "body", "t": "Die US-Notenbank Boston hat Beschäftigte mit KI-Berührung danach sortiert, ob sie sich damit produktiver fühlen. Die Mitte fürchtet am meisten."},
     {"k": "src", "t": SRC_FED}],
    [{"k": "kicker", "t": "UND AM ANDEREN ENDE"},
     {"k": "num", "t": "6,1" + NB + "%", "s": 150, "c": (77, 212, 200)},
     {"k": "numsub", "t": "Jobsorge bei denen, die den Gewinn klar spüren.", "s": 48},
     {"k": "body", "t": "Nicht Abstand zur KI senkt die Angst. Ein Gewinn, den du benennen kannst, senkt sie – dreimal so stark wie gar nichts zu merken."},
     {"k": "src", "t": SRC_FED}],
    [{"k": "kicker", "t": "EHRLICH DAZU"},
     {"k": "big", "t": "Das sind US-Daten und Schätzwerte aus einem Modell.", "s": 76},
     {"k": "body", "t": "Nicht Deutschland, nicht ausgezählt, sondern aus einer Regression mit Kontrollvariablen. Alles Selbsteinschätzung, nichts nachgemessen. Und es ist ein Zusammenhang, keine Ursache: wer sicher im Job sitzt, erlebt KI vielleicht ohnehin gelassener.", "s": 40},
     {"k": "src", "t": SRC_FED2}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Gegen das Gefühl hilft kein Argument. Eine Zahl hilft.", "s": 80},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

REEL_B = [
    [{"k": "kicker", "t": "SONNTAG · 14 UHR"},
     {"k": "big", "t": "Du benutzt KI jede Woche – und könntest nicht sagen, was sie dir bringt.", "s": 80}],
    [{"k": "kicker", "t": "GENAU DA SITZT ES"},
     {"k": "big", "t": "Nicht bei denen, die es gar nicht tun. Bei dir.", "s": 88}],
    [{"k": "kicker", "t": "GESCHÄTZT"},
     {"k": "num", "t": "21,2" + NB + "%", "s": 150},
     {"k": "numsub", "t": "Jobsorge in der Mitte – KI im Einsatz, Gewinn nicht spürbar.", "s": 48},
     {"k": "body", "t": "Bei denen, die den Gewinn klar spüren, sind es 6,1 %. Der Unterschied ist kein weiteres Werkzeug. Es ist eine Zahl, die du hast oder nicht."},
     {"k": "src", "t": SRC_FED}],
    [{"k": "kicker", "t": "DIE MECHANIK"},
     {"k": "big", "t": "Nimm EINE Aufgabe und miss sie ein einziges Mal sauber.", "s": 80},
     {"k": "body", "t": "Nicht schätzen, nicht sortieren, nicht planen. Einmal durchlaufen, mitstoppen – und die Prüfzeit ehrlich dazurechnen."}],
    [{"k": "kicker", "t": "DIE VIER ZEILEN"},
     {"k": "steps", "t": [
         "§1 Diese Aufgabe mache ich jede Woche:",
         "   [beschreiben]. Ohne KI brauche ich",
         "   dafür etwa [Minuten].",
         "§2 Geh sie jetzt mit mir Schritt für",
         "   Schritt durch und markiere, was am",
         "   Ende noch offen bleibt.",
         "§3 Rechne ehrlich: welche Minuten sind",
         "   weg – und welche kommen fürs Prüfen",
         "   und Nacharbeiten dazu?",
         "§4 Schreib das Ergebnis als einen Satz",
         "   mit genau einer Zahl.",
     ], "s": 31},
     {"k": "body", "t": "Zeile 3 ist der Kern. Ein Gewinn, der die Prüfzeit nicht mitrechnet, ist keiner – und genau das hält die Unsicherheit am Leben.", "s": 34}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Einen Satz mit einer Zahl kann dir niemand wegdiskutieren. Auch du dir selbst nicht.", "s": 66},
     {"k": "gap", "s": 10},
     {"k": "save", "t": "Sicher dir das für Montag, 9 Uhr – wenn die erste Aufgabe wieder da ist", "lab": "Lesezeichen", "s": 34}],
]

STORY_2 = [
    {"k": "kicker", "t": "KURZE FRAGE"},
    {"k": "big", "t": "Wo stehst du gerade mit KI im Job?", "s": 84},
    {"k": "gap", "s": 18},
    {"k": "rows", "t": ["Ich nutze sie – und merke den Gewinn",
                        "Ich nutze sie – und merke nichts",
                        "Ich nutze sie kaum"], "s": 36},
    {"k": "gap", "s": 10},
    {"k": "cta", "t": "Antworte mit 1, 2 oder 3"},
]

STORY_3 = [
    {"k": "kicker", "t": "SONNTAGABEND"},
    {"k": "big", "t": "Die Stoppuhr-Probe als fertige Vorlage.", "s": 84},
    {"k": "body", "t": "Vier Zeilen, mit denen du an einer einzigen Aufgabe misst, was KI dir wirklich bringt – die Prüfzeit ehrlich eingerechnet."},
    {"k": "gap", "s": 16},
    {"k": "cta", "t": "Schreib mir STOPPUHR als DM"},
]
