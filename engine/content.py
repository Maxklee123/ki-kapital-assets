# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-08 (Sonntag) - Saeule: AENGSTE ENTKRAEFTEN
# Thema: Der deutsche KI-Stellenmarkt sucht Anwender, nicht Entwickler.
# Quelle: PwC "2026 AI Jobs Barometer", veroeffentlicht 30.06.2026.

SRC_PWC = ["PwC, 2026 AI Jobs Barometer, 30.06.2026 · Auswertung von über",
           "1 Mrd. Stellenanzeigen aus 27 Ländern, deutsche Zahlen für 2025"]
SRC_PWC1 = ["PwC, 2026 AI Jobs Barometer, 30.06.2026 · deutsche Stellenanzeigen 2025"]

# ---------------------------------------------------------------- Slot 1: Story 09:00
STORY_TEASER = [
    {"k": "kicker", "t": "HEUTE 10 UHR"},
    {"k": "num", "t": "7 : 1", "s": 250},
    {"k": "numsub", "t": "So viele KI-Stellen in Deutschland suchen Anwender – nicht Entwickler."},
    {"k": "body", "t": "109.400 Anzeigen für Leute, die KI benutzen. 15.400 für Leute, die sie bauen."},
    {"k": "src", "t": "PwC, 2026 AI Jobs Barometer, 30.06.2026 · deutsche Stellenanzeigen 2025"},
    {"k": "cta", "t": "Das Reel um 10 Uhr"},
]

# ---------------------------------------------------------------- Slot 2: Reel A 10:00
REEL_A = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer
    [{"k": "kicker", "t": "SONNTAG"},
     {"k": "big", "t": "Du hältst dich für zu untechnisch, um bei KI mitzureden.", "s": 90}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "GEGENPROBE"},
     {"k": "big", "t": "Der deutsche Stellenmarkt sieht das anders.", "s": 86}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "7 : 1", "s": 280},
     {"k": "numsub", "t": "KI-Stellen in Deutschland suchen Anwender, nicht Entwickler."},
     {"k": "body", "t": "109.400 Anwender-Rollen gegen 15.400 Entwickler-Rollen."},
     {"k": "src", "t": SRC_PWC1[0]}],
    # F4 (3,5 s)
    [{"k": "kicker", "t": "WAS DAS HEISST"},
     {"k": "big", "t": "Knapp 88 Prozent aller KI-Jobs wollen keinen Code.", "s": 76},
     {"k": "body", "t": "Sie wollen jemanden, der das Werkzeug im Fachprozess einsetzt. Sachbearbeitung, Projekt, Marketing, HR."}],
    # F5 (3,5 s) - Rehook mit zweiter Zahl
    [{"k": "kicker", "t": "UND NOCH EINE ZAHL"},
     {"k": "num", "t": "0,02", "s": 250},
     {"k": "numsub", "t": "So stark hängt KI in Deutschland mit veränderten Kompetenzen zusammen."},
     {"k": "body", "t": "PwC nennt das nahezu inexistent. Dein Beruf bleibt dein Beruf."},
     {"k": "src", "t": SRC_PWC1[0]}],
    # F6 (3,6 s) - Urteil + genau ein CTA
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Nicht das Studium fehlt dir. Die ersten fünfzehn Minuten fehlen.", "s": 72},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 3: Karussell 12:00
KARUSSELL = [
    # 1 Hook
    [{"k": "kicker", "t": "ZAHLEN DER WOCHE"},
     {"k": "big", "t": "Fünf deutsche Zahlen, die der Angst vor KI widersprechen.", "s": 84},
     {"k": "gap", "s": 18},
     {"k": "body", "t": "Alle aus Erhebungen zum deutschen Arbeitsmarkt. Quelle steht auf jeder Seite."}],
    # 2
    [{"k": "kicker", "t": "01 · WER GESUCHT WIRD"},
     {"k": "num", "t": "7 : 1", "s": 230},
     {"k": "numsub", "t": "KI-Stellen suchen Anwender statt Entwickler."},
     {"k": "body", "t": "109.400 Anwender-Rollen gegen 15.400 Entwickler-Rollen in Deutschland, 2025."},
     {"k": "src", "t": "PwC, 2026 AI Jobs Barometer, 30.06.2026"}],
    # 3
    [{"k": "kicker", "t": "02 · WAS ES BRINGT"},
     {"k": "num", "t": "39 %", "s": 230},
     {"k": "numsub", "t": "Höchster Lohnaufschlag für KI-Kenntnisse."},
     {"k": "body", "t": "In Energie, Versorgung und Rohstoffen. In vielen Branchen liegt er über 20 Prozent."},
     {"k": "src", "t": "PwC, 2026 AI Jobs Barometer, 30.06.2026"}],
    # 4
    [{"k": "kicker", "t": "03 · DIE ANGST"},
     {"k": "num", "t": "9 %", "s": 230},
     {"k": "numsub", "t": "So wenige halten es für wahrscheinlich, dass KI ihren Job in fünf Jahren ersetzt."},
     {"k": "body", "t": "64 Prozent halten es für sehr unwahrscheinlich, weitere 26 Prozent für eher unwahrscheinlich."},
     {"k": "src", "t": "Forsa für Table.Briefings, 17.01.2026, 1.004 Erwerbstätige"}],
    # 5
    [{"k": "kicker", "t": "04 · DER GEWINN"},
     {"k": "num", "t": "67 %", "s": 230},
     {"k": "numsub", "t": "sagen, KI spart ihnen bis zu acht Stunden pro Woche."},
     {"k": "body", "t": "Der häufigste Einsatz ist der banalste: Mails, Berichte, PDFs."},
     {"k": "src", "t": "Adobe Acrobat, 07.08.2026, 1.500 Erwerbstätige in Deutschland"}],
    # 6
    [{"k": "kicker", "t": "05 · WIE FRÜH ES IST"},
     {"k": "num", "t": "1,3 %", "s": 230},
     {"k": "numsub", "t": "aller deutschen Stellenanzeigen sind KI-bezogen."},
     {"k": "body", "t": "2024 waren es rund 1,0 Prozent. Rund 125.000 Anzeigen. Das Feld ist nicht verteilt."},
     {"k": "src", "t": "PwC, 2026 AI Jobs Barometer, 30.06.2026"}],
    # 7 CTA
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Gesucht wird nicht, wer KI baut. Gesucht wird, wer sie benutzt.", "s": 76},
     {"k": "gap", "s": 16},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 4: Story 15:00
STORY_ENGAGE = [
    {"k": "kicker", "t": "KURZE FRAGE"},
    {"k": "big", "t": "Was hält dich ab, KI im Job zu benutzen?", "s": 82},
    {"k": "gap", "s": 22},
    {"k": "rows", "t": ["Keine Zeit, mich einzuarbeiten",
                        "Angst, etwas Falsches abzugeben"], "s": 44},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Schreib mir die 1 oder die 2 als DM. Ich antworte jedem."},
    {"k": "cta", "t": "1 oder 2 – per DM"},
]

# ---------------------------------------------------------------- Slot 5: Story 20:00
STORY_DM = [
    {"k": "kicker", "t": "FREI FÜR DICH"},
    {"k": "big", "t": "Die Vorlage, mit der du deinen eigenen Job durchleuchtest.", "s": 78},
    {"k": "gap", "s": 18},
    {"k": "body", "t": "Ein Prompt. Du setzt deine Position ein und bekommst die fünf Aufgaben, die KI dir morgen abnimmt – und die drei, die dich unersetzbar machen."},
    {"k": "gap", "s": 14},
    {"k": "cta", "t": "Schreib STACK als DM"},
]

# ---------------------------------------------------------------- Slot 6: Reel C 21:00
REEL_C = [
    [{"k": "kicker", "t": "SONNTAGABEND"},
     {"k": "big", "t": "Du wartest darauf, dass dein Arbeitgeber dich schult.", "s": 88}],
    [{"k": "kicker", "t": "DIE RECHNUNG"},
     {"k": "big", "t": "Der Markt zahlt schon heute für das, was du dir selbst beibringst.", "s": 74}],
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "+20 %", "s": 260},
     {"k": "numsub", "t": "Lohnaufschlag für KI-Kenntnisse – in vielen deutschen Branchen."},
     {"k": "body", "t": "In Energie, Versorgung und Rohstoffen sind es bis zu 39 Prozent."},
     {"k": "src", "t": SRC_PWC1[0]}],
    [{"k": "kicker", "t": "WOFÜR GENAU"},
     {"k": "big", "t": "Nicht für Entwickeln. Für Anwenden.", "s": 86},
     {"k": "body", "t": "In der Finanzbranche sind 97,3 Prozent aller KI-Rollen Anwender-Rollen. Der höchste Wert aller Branchen."}],
    [{"k": "kicker", "t": "DAS IST DER PUNKT"},
     {"k": "num", "t": "0,02", "s": 240},
     {"k": "numsub", "t": "So wenig hat KI die geforderten Kompetenzen in Deutschland verschoben."},
     {"k": "body", "t": "Du musst niemand anderes werden. Du musst nur der sein, der es schon benutzt."},
     {"k": "src", "t": SRC_PWC1[0]}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Unersetzbar wird nicht, wer die KI versteht. Sondern wer sie am Montag aufmacht.", "s": 68},
     {"k": "gap", "s": 12},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]
