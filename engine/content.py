# -*- coding: utf-8 -*-
K = "DER 15-MINUTEN-VORSPRUNG"
SRC_T = "TÜV-Verband, Forsa-Umfrage, 08.04.2026 · 587 Erwerbstätige in Deutschland"
SRC_B = "Bitkom-Beschäftigtenbefragung 2026 · 48 % nutzen KI im Job"

STORY_1 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Fast alle benutzen KI wie eine bessere Suchmaschine.", "s": 62},
    {"k": "num", "t": "10 %", "s": 270},
    {"k": "numsub", "t": "lassen ihre Daten auswerten.", "s": 60},
    {"k": "gap", "s": 22},
    {"k": "body", "t": "Dort liegt die Arbeit, die vorher einen halben Tag gekostet hat.", "s": 46},
    {"k": "src", "t": SRC_T},
    {"k": "gap", "s": 26},
    {"k": "cta", "t": "Heute 10:00: die ganze Verteilung", "s": 42},
]

REEL_A = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du benutzt KI im Job vermutlich als bessere Suchmaschine.", "s": 92},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "587 Erwerbstätige wurden gefragt, wofür genau.", "s": 96},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "78 %", "s": 270},
        {"k": "numsub", "t": "nutzen KI, um nach Informationen zu suchen.", "s": 56},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Datensätze analysieren lassen nur 10 %. Berechnungen durchführen 13 %.", "s": 44},
        {"k": "src", "t": SRC_T},
    ],
    [
        {"k": "kicker", "t": "DIE VERTEILUNG"},
        {"k": "calc", "t": [
            ("Informationen suchen", "78 %", (77, 212, 200)),
            ("Texte verbessern", "46 %", (255, 255, 255)),
            ("Daten auswerten", "10 %", (245, 166, 35)),
        ], "s": 52},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "Die Aufgabe mit dem größten Zeitgewinn ist die am wenigsten besetzte.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "DIE LÜCKE"},
        {"k": "big", "t": "Es hängt nicht am Tool. Es hängt an der Formulierung.", "s": 82},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "88 % der Nutzer sagen das selbst. 55 % bekommen trotzdem Ergebnisse, die zu unkonkret sind.", "s": 44},
        {"k": "src", "t": SRC_T},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Wer Zahlen hineingibt statt Fragen, spielt in einer Liga, in der neun von zehn Kollegen nicht antreten.", "s": 62},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Folgen – ein Workflow pro Tag", "s": 46},
    ],
]

REEL_B = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du klickst deine Monatsauswertung noch durch drei Pivot-Tabellen.", "s": 88},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Dafür brauchst du vier Sätze.", "s": 104},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "10 %", "s": 270},
        {"k": "numsub", "t": "der Erwerbstätigen lassen Datensätze von KI analysieren.", "s": 54},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "78 % suchen damit nur Informationen. Die Auswertung bleibt Handarbeit.", "s": 46},
        {"k": "src", "t": SRC_T},
    ],
    [
        {"k": "kicker", "t": "DIE MECHANIK"},
        {"k": "big", "t": "Die Tabelle hochladen reicht nicht. Die KI braucht die Frage, die dein Chef stellen wird.", "s": 70},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Vier Bausteine. Du tauschst nur die Klammern aus.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "ZUM KOPIEREN"},
        {"k": "steps", "t": [
            "§1 ROLLE: Du bist Controller und",
            "prüfst meine Tabelle.",
            "§2 INPUT: Spalten [Spalten],",
            "Zeitraum [Zeitraum].",
            "§3 FRAGE: Nenne die drei größten",
            "Abweichungen zum Vormonat – je",
            "mit Zahl und möglicher Ursache.",
            "§4 FORMAT: Drei Zeilen, eine je",
            "Abweichung. Keine Aussage ohne Zahl.",
        ], "s": 39},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Baustein 3 entscheidet: ohne die konkrete Frage bekommst du eine Zusammenfassung – keine Auswertung.", "s": 60},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Speicher diesen Prompt, bevor du ihn brauchst – nicht erst beim Monatsabschluss", "s": 38},
    ],
]

STORY_4 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Wofür nutzt du KI im Job am häufigsten?", "s": 70},
    {"k": "gap", "s": 30},
    {"k": "rows", "t": [
        "Informationen suchen",
        "Texte schreiben oder glätten",
        "Zahlen und Tabellen auswerten",
    ], "s": 42},
    {"k": "gap", "s": 26},
    {"k": "body", "t": "Bundesweit: 78 % · 46 % · 10 %.", "s": 46},
    {"k": "src", "t": SRC_T},
    {"k": "gap", "s": 22},
    {"k": "cta", "t": "Antworte mit 1, 2 oder 3", "s": 46},
]

STORY_5 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Der Auswertungs-Prompt für deine Tabellen – vier Bausteine zum Einfügen.", "s": 62},
    {"k": "gap", "s": 26},
    {"k": "body", "t": "Rolle, Input, Frage, Format. Einmal gespeichert, bei jedem Monatsabschluss nutzbar.", "s": 44},
    {"k": "gap", "s": 30},
    {"k": "cta", "t": "Schreib mir STACK als DM", "s": 50},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Keyword in die Direktnachricht – du bekommst die Vorlage zurück.", "s": 40, "c": (150, 152, 178)},
]
