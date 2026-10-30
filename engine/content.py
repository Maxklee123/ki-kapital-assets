# -*- coding: utf-8 -*-
K = "DER 15-MINUTEN-VORSPRUNG"
SRC_N = "YouGov im Auftrag von Notion, Juni 2026 · 2.067 Beschäftigte"
SRC_K = "Konstanzer KI-Studie 2026, Universität Konstanz · 1.105 Befragte"

STORY_1 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Deine KI spart dir diese Woche", "s": 64},
    {"k": "num", "t": "22", "s": 330},
    {"k": "numsub", "t": "Minuten. Netto.", "s": 66},
    {"k": "gap", "s": 22},
    {"k": "body", "t": "2,17 Stunden gespart – 1,81 Stunden für Betreuung zurückgegeben.", "s": 46},
    {"k": "src", "t": SRC_N},
    {"k": "gap", "s": 26},
    {"k": "cta", "t": "Heute 10:00: wo die 2 Stunden verloren gehen", "s": 42},
]

REEL_A = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du glaubst, KI spart dir Zeit.", "s": 112},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Deine Woche sagt etwas anderes.", "s": 104},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "22", "s": 340},
        {"k": "numsub", "t": "Minuten pro Woche. Netto.", "s": 62},
        {"k": "gap", "s": 18},
        {"k": "body", "t": "Das ist der ganze Zeitgewinn, den KI bei Büroangestellten übrig lässt.", "s": 46},
        {"k": "src", "t": SRC_N},
    ],
    [
        {"k": "kicker", "t": "DIE RECHNUNG"},
        {"k": "calc", "t": [
            ("KI spart dir", "2,17 Std.", (77, 212, 200)),
            ("Nutzung + Betreuung", "– 1,81 Std.", (255, 120, 120)),
            ("Bleibt pro Woche", "0,37 Std.", (245, 166, 35)),
        ], "s": 58},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "17,2 Stunden im Jahr. Zwei Arbeitstage – nicht zwei Wochen.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "DER EIGENTLICHE FEHLER"},
        {"k": "big", "t": "Nicht das Tool kostet die Zeit. Das Neu-Formulieren tut es.", "s": 72},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Nur 19 % der täglichen Nutzer wurden je geschult. Alle anderen tippen jeden Prompt neu.", "s": 44},
        {"k": "src", "t": SRC_N},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Wer seine Prompts einmal baut und aufhebt, holt die 1,81 Stunden zurück.", "s": 70},
        {"k": "gap", "s": 24},
        {"k": "cta", "t": "Folgen – ein Workflow pro Tag", "s": 46},
    ],
]

REEL_B = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du tippst denselben Prompt zum zehnten Mal.", "s": 100},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Genau da verschwindet dein Zeitgewinn.", "s": 96},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "1,81", "s": 260},
        {"k": "numsub", "t": "Stunden pro Woche gehen für Nutzung und Nachsteuern drauf.", "s": 56},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "Gespart werden 2,17. Fast alles davon geht wieder weg.", "s": 46},
        {"k": "src", "t": SRC_N},
    ],
    [
        {"k": "kicker", "t": "DIE MECHANIK"},
        {"k": "big", "t": "Ein Prompt, einmal gebaut, braucht kein Nachsteuern mehr.", "s": 76},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Vier feste Bausteine. Du tauschst nur die Klammern aus.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "ZUM KOPIEREN"},
        {"k": "steps", "t": [
            "§1 ROLLE: Du bist mein Assistent",
            "für [Aufgabe, z. B. Protokolle].",
            "§2 INPUT: Hier sind die Rohdaten:",
            "[Text einfügen]",
            "§3 REGELN: Max. 5 Sätze, sachlicher",
            "Ton, keine Floskeln, offene Punkte",
            "ausdrücklich benennen.",
            "§4 FORMAT: Erst das Ergebnis, dann",
            "drei Stichpunkte Begründung.",
        ], "s": 40},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Diesen Prompt tippst du einmal – und danach nie wieder.", "s": 72},
        {"k": "gap", "s": 24},
        {"k": "cta", "t": "Speicher das jetzt – Montag 9:00 brauchst du es", "s": 44},
    ],
]

STORY_4 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Wie oft tippst du denselben Prompt neu?", "s": 72},
    {"k": "gap", "s": 30},
    {"k": "rows", "t": [
        "Jedes Mal komplett neu",
        "Ich scrolle im alten Chat",
        "Ich habe feste Vorlagen",
    ], "s": 44},
    {"k": "gap", "s": 26},
    {"k": "body", "t": "1,81 Stunden pro Woche gehen genau dafür drauf.", "s": 44},
    {"k": "src", "t": SRC_N},
    {"k": "gap", "s": 22},
    {"k": "cta", "t": "Antworte mit 1, 2 oder 3", "s": 46},
]

STORY_5 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Die Prompt-Vorlage von heute – als Text zum Einfügen.", "s": 70},
    {"k": "gap", "s": 26},
    {"k": "body", "t": "Vier Bausteine: Rolle, Input, Regeln, Format. Einmal gespeichert, für jede wiederkehrende Aufgabe nutzbar.", "s": 44},
    {"k": "gap", "s": 30},
    {"k": "cta", "t": "Schreib mir STACK als DM", "s": 50},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Keyword in die Direktnachricht – du bekommst die Vorlage zurück.", "s": 40, "c": (150,152,178)},
]

REEL_C = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du wartest, bis die Firma ein KI-Tool einführt.", "s": 96},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Fast die Hälfte wartet nicht.", "s": 110},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "55 %", "s": 250},
        {"k": "numsub", "t": "der KI-Nutzer sagen: mein wichtigstes Werkzeug kam vom Arbeitgeber.", "s": 54},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "Der Rest hat sich den Einstieg selbst gesucht – ohne Einführung, ohne Schulung.", "s": 44},
        {"k": "src", "t": SRC_K},
    ],
    [
        {"k": "kicker", "t": "WO ES PASSIERT"},
        {"k": "calc", "t": [
            ("Büro- und Wissensarbeit", "49 %", (77, 212, 200)),
            ("Produktionsnahe Arbeit", "25 %", (255, 255, 255)),
            ("Firmen unter 50 mit Schulung", "11 %", (245, 166, 35)),
        ], "s": 50},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "Im Büro nutzt schon jeder Zweite KI. Beigebracht hat es fast keinem jemand.", "s": 44},
        {"k": "src", "t": SRC_K},
    ],
    [
        {"k": "kicker", "t": "DER KARRIERE-TEIL"},
        {"k": "big", "t": "Unersetzbar wird nicht, wer das beste Tool hat. Sondern wer im Meeting erklären kann, warum es das Ergebnis trägt.", "s": 62},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Die 45 % ohne Einführung sind keine Regelbrecher. Sie sind der Vergleichsmaßstab für deine nächste Beurteilung.", "s": 60},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Folgen – ein Workflow pro Tag", "s": 46},
    ],
]
