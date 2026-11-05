# -*- coding: utf-8 -*-
K = "DER 15-MINUTEN-VORSPRUNG"
SRC = "KI-Monitor 2026, TU Darmstadt mit YouGov, 28.08.2026 · über 2.000 Befragte ab 16 Jahren in Deutschland"

ACCENT2 = (77, 212, 200)
ACCENT = (245, 166, 35)
WHITE = (255, 255, 255)

STORY_1 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Fast 60 % der Erwerbstätigen erwarten, dass KI in vielen Berufen Arbeitsplätze ersetzt.", "s": 60},
    {"k": "num", "t": "15,7 %", "s": 250},
    {"k": "numsub", "t": "sagen das über ihren eigenen Arbeitsplatz.", "s": 58},
    {"k": "gap", "s": 22},
    {"k": "body", "t": "Die Angst ist groß – und hat keine Adresse. Genau deshalb bringt sie nichts.", "s": 46},
    {"k": "src", "t": SRC},
    {"k": "gap", "s": 26},
    {"k": "cta", "t": "Heute 10:00: wer die Zahl nach oben zieht", "s": 42},
]

REEL_A = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du hältst Jobverluste durch KI für wahrscheinlich – nur nicht bei dir.", "s": 92},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Über 2.000 Menschen in Deutschland wurden genau das gefragt.", "s": 94},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "59,7 %", "s": 250},
        {"k": "numsub", "t": "der Erwerbstätigen erwarten, dass KI in fünf Jahren Jobs in vielen Berufen ersetzt.", "s": 52},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Für den eigenen Arbeitsplatz sagen das 15,7 %.", "s": 46},
        {"k": "src", "t": SRC},
    ],
    [
        {"k": "kicker", "t": "DIE LÜCKE"},
        {"k": "calc", "t": [
            ("In vielen Berufen", "59,7 %", ACCENT2),
            ("Der eigene Job", "15,7 %", WHITE),
            ("Je in einer KI-Schulung", "15 %", ACCENT),
        ], "s": 52},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "44 Punkte zwischen Sorge und Selbstbezug. Und keiner davon ist Handlung.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "DIE ÜBERRASCHUNG"},
        {"k": "big", "t": "Wer sich mit KI am besten auskennt, nennt 42,8 %. Wer sie kaum kennt: 6,2.", "s": 76},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Nicht die Ahnungslosen haben Angst. Die Informierten haben sie.", "s": 44},
        {"k": "src", "t": SRC},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Die 42,8 % sind nicht schlechter dran. Sie sind die Einzigen, die benennen können, welche Aufgabe geht.", "s": 60},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Folgen – ein Workflow pro Tag", "s": 46},
    ],
]

REEL_B = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du weißt nicht, welche deiner Aufgaben eine KI zuerst übernimmt.", "s": 88},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Vier Sätze bringen die Liste auf den Tisch.", "s": 100},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "15 %", "s": 270},
        {"k": "numsub", "t": "waren je in einer KI-Weiterbildung.", "s": 56},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "Bei Erwerbstätigen 23,2 %. Alle anderen schätzen – und Schätzen ist der Grund, warum die Sorge bleibt.", "s": 44},
        {"k": "src", "t": SRC},
    ],
    [
        {"k": "kicker", "t": "DIE MECHANIK"},
        {"k": "big", "t": "Frag nicht, ob KI deinen Job kann. Zerlege deine Woche in Aufgaben – dann ist es prüfbar.", "s": 70},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Vier Bausteine. Du füllst nur die Klammern.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "ZUM KOPIEREN"},
        {"k": "steps", "t": [
            "§1 ROLLE: Du bist Arbeitsanalyst",
            "und kennst meinen Job nicht.",
            "§2 INPUT: Meine Woche in Aufgaben:",
            "[Aufgabe – Stunden], [Aufgabe – Stunden].",
            "§3 FRAGE: Sortiere in drei Gruppen –",
            "heute von KI erledigbar, nur mit mir",
            "zusammen, nur von mir. Je ein Satz warum.",
            "§4 FORMAT: Drei Listen mit Stundensumme.",
            "Keine Einordnung ohne Begründung.",
        ], "s": 37},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Gruppe 3 ist deine Jobbeschreibung für die nächsten fünf Jahre. Die kennt niemand, der nur Angst hat.", "s": 60},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Speicher das – du brauchst es, bevor dein Chef die Frage stellt", "s": 38},
    ],
]

STORY_4 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Hast du schon mal durchgerechnet, welche deiner Aufgaben KI übernehmen könnte?", "s": 64},
    {"k": "gap", "s": 30},
    {"k": "rows", "t": [
        "Ja – ich kenne meine Liste",
        "Angefangen, nie fertig",
        "Nein – nur ein ungutes Gefühl",
    ], "s": 42},
    {"k": "gap", "s": 26},
    {"k": "body", "t": "Bundesweit waren 15 % je in einer KI-Weiterbildung.", "s": 46},
    {"k": "src", "t": SRC},
    {"k": "gap", "s": 22},
    {"k": "cta", "t": "Antworte mit 1, 2 oder 3", "s": 46},
]

STORY_5 = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Der Aufgaben-Check für deinen Job – vier Bausteine zum Einfügen.", "s": 62},
    {"k": "gap", "s": 26},
    {"k": "body", "t": "Rolle, Input, Frage, Format. Einmal ausgefüllt: drei Listen statt einer Sorge.", "s": 44},
    {"k": "gap", "s": 30},
    {"k": "cta", "t": "Schreib mir LISTE als DM", "s": 50},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Keyword in die Direktnachricht – du bekommst die Vorlage zurück.", "s": 40, "c": (150, 152, 178)},
]
