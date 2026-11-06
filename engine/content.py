# -*- coding: utf-8 -*-
K = "DER 15-MINUTEN-VORSPRUNG"
SRC_A = "Adobe Acrobat mit 3Gem, Befragung April 2026 \u00b7 1.500 Erwerbst\u00e4tige in Deutschland"
SRC_B = "BCG, KI am Arbeitsplatz 2026, ver\u00f6ffentlicht 02.07.2026"
SRC_C = "Indeed-Befragung, 501 Angestellte in Deutschland, ver\u00f6ffentlicht 17.09.2025"

ACCENT2 = (77, 212, 200)
ACCENT = (245, 166, 35)
WHITE = (255, 255, 255)
MUTED = (150, 152, 178)

# ---------------- REEL A  10:00  Schneller Beweis, EINE Studie ----------------
REEL_A = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du sparst mit KI Zeit. Sagen kannst du nicht, wo sie hingeht.", "s": 92},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "1.500 Erwerbst\u00e4tige in Deutschland wurden genau das gefragt.", "s": 94},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "67 %", "s": 270},
        {"k": "numsub", "t": "sparen mit KI bis zu acht Stunden Arbeitszeit pro Woche.", "s": 54},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Gleiche Erhebung: 26 % nutzen bei der Arbeit gar kein KI-Werkzeug.", "s": 44},
        {"k": "src", "t": SRC_A},
    ],
    [
        {"k": "kicker", "t": "WOF\u00dcR GENAU"},
        {"k": "calc", "t": [
            ("Sparen bis zu 8 h/Woche", "67 %", ACCENT2),
            ("Mails, Berichte, PDFs", "29 %", WHITE),
            ("Nutzen gar keine KI", "26 %", ACCENT),
        ], "s": 52},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "Der h\u00e4ufigste Einsatz ist der banalste \u2013 und der, den jeder im B\u00fcro hat.", "s": 44},
    ],
    [
        {"k": "kicker", "t": "DIE \u00dcBERRASCHUNG"},
        {"k": "big", "t": "Wirtschaft und Beratung: 46 %. Finanzbranche: 36 %. Gleiche Dokumente, zehn Punkte Abstand.", "s": 66},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Der Unterschied liegt nicht am Beruf. Er liegt daran, wer angefangen hat.", "s": 44},
        {"k": "src", "t": SRC_A},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Acht gesparte Stunden, die keiner sieht, sind im Jahresgespr\u00e4ch null Stunden.", "s": 64},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Folgen \u2013 ein Workflow pro Tag", "s": 46},
    ],
]

# ---------------- REEL B  14:00  Mechanik, Prompt in Frame 5 ----------------
REEL_B = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Du schreibst dieselbe Mail dreimal: Rohfassung, Umbau, Ton.", "s": 90},
    ],
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "Vier Bausteine machen daraus einen Durchlauf.", "s": 100},
    ],
    [
        {"k": "kicker", "t": "GEMESSEN"},
        {"k": "num", "t": "29 %", "s": 270},
        {"k": "numsub", "t": "nutzen KI f\u00fcr Mails, Berichte und PDFs.", "s": 56},
        {"k": "gap", "s": 14},
        {"k": "body", "t": "H\u00e4ufigster Einsatz im B\u00fcro \u2013 und der, bei dem die meisten nach der Rohfassung aufh\u00f6ren.", "s": 42},
        {"k": "src", "t": SRC_A},
    ],
    [
        {"k": "kicker", "t": "DIE MECHANIK"},
        {"k": "big", "t": "Gib der KI nicht deinen Text. Gib ihr Empf\u00e4nger, Entscheidung und Einwand.", "s": 70},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Vier Bausteine. Du f\u00fcllst nur die Klammern.", "s": 46},
    ],
    [
        {"k": "kicker", "t": "ZUM KOPIEREN"},
        {"k": "steps", "t": [
            "\u00a71 ROLLE: Du schreibst eine Mail",
            "an [Empf\u00e4nger, seine Rolle].",
            "\u00a72 ZIEL: Er soll [eine Entscheidung]",
            "treffen. Mehr nicht.",
            "\u00a73 EINWAND: Sein wahrscheinlichster",
            "Einwand ist [Einwand]. Nimm ihn in",
            "Satz zwei vorweg.",
            "\u00a74 FORMAT: Max. 120 W\u00f6rter, Betreff",
            "mit der Entscheidung, letzte Zeile",
            "eine Frage. Dazu drei Betreff-Varianten.",
        ], "s": 36},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Baustein 3 ist der, den alle weglassen \u2013 und genau er entscheidet, ob die Mail durchgeht.", "s": 60},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Speicher das \u2013 Montag um 8 brauchst du es", "s": 42},
    ],
]

# ---------------- KARUSSELL  12:00  7 Slides 1080x1350 ----------------
KARUSSELL = [
    [
        {"k": "kicker", "t": K},
        {"k": "big", "t": "42 % sparen mit KI einen Arbeitstag pro Woche.", "s": 78},
        {"k": "gap", "s": 18},
        {"k": "numsub", "t": "66 % bekommen nicht gesagt, was sie mit der Zeit tun sollen.", "s": 50, "c": ACCENT},
        {"k": "src", "t": SRC_B},
    ],
    [
        {"k": "kicker", "t": "WO DIE ZEIT LANDET"},
        {"k": "calc", "t": [
            ("Aufgaben ohne Mehrwert", "~50 %", ACCENT),
            ("Verwaltungsarbeit", "~25 %", WHITE),
            ("Zus\u00e4tzliche Pausen", "20,8 %", WHITE),
            ("Meetings", "7 %", MUTED),
        ], "s": 46},
        {"k": "gap", "s": 12},
        {"k": "body", "t": "Die Zeit kommt an. Sie kommt nur nirgendwo an, wo jemand sie sieht.", "s": 40},
        {"k": "src", "t": SRC_C},
    ],
    [
        {"k": "kicker", "t": "DER STILLE FEHLER"},
        {"k": "num", "t": "23 %", "s": 220},
        {"k": "numsub", "t": "verschweigen ihre Effizienzgewinne bewusst.", "s": 48},
        {"k": "gap", "s": 12},
        {"k": "body", "t": "Aus Angst vor mehr Arbeit. Das Ergebnis ist mehr Arbeit \u2013 nur ohne Anerkennung.", "s": 40},
        {"k": "src", "t": SRC_C},
    ],
    [
        {"k": "kicker", "t": "DER UMSCHLAGPUNKT"},
        {"k": "big", "t": "Wo KI offen gef\u00f6rdert wird, sparen 18 % mehr als sechs Stunden pro Woche.", "s": 62},
        {"k": "gap", "s": 14},
        {"k": "numsub", "t": "57,6 % stecken die Zeit in Weiterbildung oder eigene Projekte.", "s": 44, "c": ACCENT2},
        {"k": "src", "t": SRC_C},
    ],
    [
        {"k": "kicker", "t": "ZUM KOPIEREN"},
        {"k": "steps", "t": [
            "\u00a71 ROLLE: Du bist mein Chef und",
            "hast drei Minuten.",
            "\u00a72 INPUT: Diese Woche mit KI erledigt:",
            "[Aufgabe \u2013 gesparte Zeit], [Aufgabe \u2013 Zeit].",
            "\u00a73 FRAGE: Was davon ist f\u00fcr die Firma",
            "sichtbar wertvoll, was nur f\u00fcr mich",
            "bequem? Trenne hart.",
            "\u00a74 FORMAT: Drei S\u00e4tze, die ich im",
            "Jahresgespr\u00e4ch sagen kann. Mit Zahlen,",
            "ohne Floskeln.",
        ], "s": 33},
    ],
    [
        {"k": "kicker", "t": "MONTAG ANDERS"},
        {"k": "rows", "t": [
            "Eine Zahl notieren, nicht sch\u00e4tzen",
            "Eine gesparte Stunde sichtbar einsetzen",
            "Einen Satz sagen, nicht warten",
        ], "s": 40},
        {"k": "gap", "s": 16},
        {"k": "body", "t": "Drei Minuten Arbeit. Mehr Wirkung als acht gesparte Stunden, von denen keiner wei\u00df.", "s": 40},
    ],
    [
        {"k": "kicker", "t": "MEINE EINORDNUNG"},
        {"k": "big", "t": "Unersetzbar wird man nicht durch gesparte Zeit, sondern dadurch, was man mit ihr zeigt.", "s": 60},
        {"k": "gap", "s": 22},
        {"k": "cta", "t": "Folgen \u2013 ein Workflow pro Tag", "s": 44},
    ],
]

# ---------------- STORY  20:00  DM-CTA ----------------
STORY_DM = [
    {"k": "kicker", "t": K},
    {"k": "big", "t": "Die Mail-Vorlage aus dem 14:00-Reel \u2013 vier Bausteine zum Einf\u00fcgen.", "s": 62},
    {"k": "gap", "s": 24},
    {"k": "body", "t": "Rolle, Ziel, Einwand, Format. Einmal ausgef\u00fcllt: eine Fassung statt drei.", "s": 44},
    {"k": "gap", "s": 28},
    {"k": "cta", "t": "Schreib mir ENTWURF als DM", "s": 48},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Keyword in die Direktnachricht \u2013 du bekommst die Vorlage zur\u00fcck.", "s": 40, "c": MUTED},
]
