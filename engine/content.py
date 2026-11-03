# -*- coding: utf-8 -*-
K = "DER 15-MINUTEN-VORSPRUNG"
SRC_R = "Randstad „Age of Augmentation“, 03.06.2026 · 2,4 Mio. Stellenanzeigen in Deutschland"
SRC_D = "KI-Monitor 2026, TU Darmstadt mit YouGov · über 2.000 Befragte"

STORY_1 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Wer KI nachweisbar kann, steigt auf", "s": 62},
    {"k": "num", "t": "3,5x", "s": 290},
    {"k": "numsub", "t": "schneller als die Kollegen.", "s": 62},
    {"k": "gap", "s": 22},
    {"k": "body", "t": "Nicht die Nutzung entscheidet. Der Nachweis entscheidet.", "s": 46},
    {"k": "src", "t": SRC_R},
    {"k": "gap", "s": 26},
    {"k": "cta", "t": "Heute 10:00: woran der Nachweis hängt", "s": 42},
]

REEL_A = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du glaubst, Beförderung hängt an deinen Jahren im Haus.", "s": 92},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "2,4 Millionen Stellenanzeigen sagen etwas anderes.", "s": 92},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "3,5x", "s": 300},
        {"k": "numsub", "t": "schneller steigen Beschäftigte mit nachweisbarer KI-Kompetenz auf.", "s": 56},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Randstad hat 35,8 Mio. Stellenanzeigen aus fünf Jahren ausgewertet, 2,4 Mio. davon in Deutschland.", "s": 44},
        {"k": "src", "t": SRC_R},
    ],
    [
        {"k": "kicker", "t": "WAS DARAN HÄNGT"},
        {"k": "calc", "t": [
            ("Aufstiegstempo", "3,5x", (77, 212, 200)),
            ("Vergütung weltweit", "bis +25 %", (245, 166, 35)),
            ("Dafür nötiges Studium", "keins", (255, 255, 255)),
        ], "s": 54},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "Gefragt ist der Fachbereich mit KI – nicht die Informatik.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "DIE LÜCKE"},
        {"k": "big", "t": "Fast alle benutzen es. Fast keiner kann es belegen.", "s": 82},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "72,3 % haben KI schon genutzt. Nur 21,8 % nennen ihre eigenen Kenntnisse hoch.", "s": 44},
        {"k": "src", "t": SRC_D},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Du musst nicht besser werden als deine Kollegen. Nur der sein, der sagen kann, was es gebracht hat.", "s": 64},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Folgen – ein Workflow pro Tag", "s": 46},
    ],
]

REEL_B = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Im Jahresgespräch fragt dich keiner, welche KI du nutzt.", "s": 92},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Gefragt wird, was dabei herauskam.", "s": 100},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "18,6 %", "s": 210},
        {"k": "numsub", "t": "der Beschäftigten ohne Führungsrolle hatten je ein KI-Training.", "s": 54},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "Bei Führungskräften sind es 35,2 % – fast doppelt so viele.", "s": 46},
        {"k": "src", "t": SRC_D},
    ],
    [
        {"k": "kicker", "t": "DIE MECHANIK"},
        {"k": "big", "t": "Dein Nachweis ist kein Zertifikat. Er ist ein Satz mit einer Zahl darin.", "s": 74},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Vier Bausteine. Du tauschst nur die Klammern aus.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "ZUM KOPIEREN"},
        {"k": "steps", "t": [
            "§1 ROLLE: Du bist mein Coach für",
            "das Jahresgespräch.",
            "§2 INPUT: Diese Aufgabe habe ich",
            "mit KI gelöst: [Aufgabe]",
            "§3 REGELN: Formuliere EINEN Satz.",
            "Mit Zahl (Zeit oder Stück), ohne",
            "Tool-Namen, ohne Fachbegriff.",
            "§4 FORMAT: Erst der Satz, dann drei",
            "Belege für die Nachfrage.",
        ], "s": 40},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Baustein 3 ist der Entscheidende: ohne ihn klingt der Satz nach Angeberei, mit ihm nach Ergebnis.", "s": 62},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Speicher das, bevor du es brauchst – nicht erst am Tag des Gesprächs", "s": 40},
    ],
]

STORY_4 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Wie viele in deinem Team hatten je ein KI-Training?", "s": 68},
    {"k": "gap", "s": 30},
    {"k": "rows", "t": [
        "Keiner – wir machen das selbst",
        "Ein paar – meist die Chefs",
        "Alle, es war verpflichtend",
    ], "s": 42},
    {"k": "gap", "s": 26},
    {"k": "body", "t": "Bundesweit: 18,6 % ohne Führungsrolle, 35,2 % mit.", "s": 44},
    {"k": "src", "t": SRC_D},
    {"k": "gap", "s": 22},
    {"k": "cta", "t": "Antworte mit 1, 2 oder 3", "s": 46},
]

STORY_5 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Der Nachweis-Satz für dein Jahresgespräch – als Prompt zum Einfügen.", "s": 64},
    {"k": "gap", "s": 26},
    {"k": "body", "t": "Vier Bausteine: Rolle, Input, Regeln, Format. Einmal gespeichert, bei jeder Beurteilung nutzbar.", "s": 44},
    {"k": "gap", "s": 30},
    {"k": "cta", "t": "Schreib mir STACK als DM", "s": 50},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Keyword in die Direktnachricht – du bekommst die Vorlage zurück.", "s": 40, "c": (150, 152, 178)},
]
