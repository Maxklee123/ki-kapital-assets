# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-10 (Dienstag) - Saeule: UNERSETZBAR-FRAMING
# Thema: Die Faehigkeit, die ueber deine Karriere entscheidet, bewertet deine
#        Fuehrungsebene deutlich hoeher als du selbst - und niemand schult sie.
# Quelle: IU Internationale Hochschule, "KI in der Arbeitswelt: Wie gelingt der
#         Change?", n=2.000 Arbeitnehmende 16-65 J., Deutschland, repraesentativ
#         nach Alter und Geschlecht, Erhebung 31.03.-14.04.2026, veroeff. 24.09.2026.
# Zweitquelle: KI-Monitor 2026, TU Darmstadt (Fachgebiet Wirtschaftsinformatik,
#         Prof. Dr. Peter Buxmann) mit YouGov, ueber 2.000 Personen, Deutschland,
#         Pressemitteilung 28.08.2026.

SRC_IU  = "IU Internationale Hochschule, KI in der Arbeitswelt, 24.09.2026 · n=2.000, Deutschland"
SRC_IU2 = ["IU Internationale Hochschule, KI in der Arbeitswelt, 24.09.2026",
           "n=2.000 Arbeitnehmende, Deutschland, Erhebung 31.03.-14.04.2026"]
SRC_TUD = "KI-Monitor 2026, TU Darmstadt mit YouGov, 28.08.2026 · ueber 2.000 Befragte"

# ---------------------------------------------------------------- Slot 1: Story 09:00
STORY_TEASER = [
    {"k": "kicker", "t": "HEUTE 10 UHR"},
    {"k": "num", "t": "51 : 38", "s": 190},
    {"k": "numsub", "t": "So unterschiedlich bewerten Führungskräfte und Beschäftigte dieselbe Fähigkeit."},
    {"k": "body", "t": "51,2 % der Führungskräfte halten Prompten für eine Fähigkeit, die wichtiger wird. Ohne Führungsverantwortung: 38,1 %."},
    {"k": "src", "t": SRC_IU},
    {"k": "cta", "t": "Das Reel um 10 Uhr"},
]

# ---------------------------------------------------------------- Slot 2: Reel A 10:00
REEL_A = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer
    [{"k": "kicker", "t": "DIENSTAG"},
     {"k": "big", "t": "Du hältst Prompten für eine Spielerei, die bald wieder weggeht.", "s": 88}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "GEGENPROBE"},
     {"k": "big", "t": "Die Ebene, die über dich entscheidet, hält es für etwas anderes.", "s": 84}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "51 : 38", "s": 210},
     {"k": "numsub", "t": "Führungskräfte gegen Beschäftigte, gefragt nach derselben Fähigkeit."},
     {"k": "body", "t": "51,2 % der Führungskräfte erwarten, dass Prompten wichtiger wird. Ohne Führungsverantwortung sagen das 38,1 %."},
     {"k": "src", "t": SRC_IU}],
    # F4 (3,5 s)
    [{"k": "kicker", "t": "WAS DAS HEISST"},
     {"k": "big", "t": "13 Prozentpunkte Abstand – und dieselbe Lücke ein zweites Mal.", "s": 76},
     {"k": "body", "t": "Beim kritischen Prüfen von KI-Ergebnissen: 49,6 % der Führungskräfte, 38,6 % der Beschäftigten. Zweimal unterschätzt du genau das, was oben gezählt wird."}],
    # F5 (3,5 s) - Rehook mit zweiter Zahl
    [{"k": "kicker", "t": "UND DIE ANDERE SEITE"},
     {"k": "num", "t": "43,9 %", "s": 180},
     {"k": "numsub", "t": "haben in zwölf Monaten keine Minute Arbeitszeit für KI genutzt."},
     {"k": "body", "t": "Fast die Hälfte davon hält es für nicht notwendig. Der Kurs, auf den du wartest, ist nicht geplant."},
     {"k": "src", "t": SRC_IU}],
    # F6 (3,6 s) - Urteil + genau ein CTA
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Unersetzbar wird nicht, wer wartet. Sondern wer die Lücke selbst schließt.", "s": 70},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 3: Reel B 14:00
REEL_B = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer
    [{"k": "kicker", "t": "DIENSTAG · 14 UHR"},
     {"k": "big", "t": "Du gibst KI-Ergebnisse weiter, die du nicht wirklich geprüft hast.", "s": 86}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "DAS PROBLEM DARAN"},
     {"k": "big", "t": "Genau dieses Prüfen ist die Fähigkeit, an der du gemessen wirst.", "s": 82}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "49,6 %", "s": 185},
     {"k": "numsub", "t": "der Führungskräfte erwarten, dass kritisches Prüfen von KI-Ergebnissen wichtiger wird."},
     {"k": "body", "t": "Aber nur 33,6 % der Beschäftigten sagen, dass ihr Betrieb kritisches Denken fördert. Fachwissen: 51,6 %."},
     {"k": "src", "t": SRC_IU}],
    # F4 (3,5 s)
    [{"k": "kicker", "t": "DIE MECHANIK"},
     {"k": "big", "t": "Produzieren kann die KI. Haften musst du.", "s": 82},
     {"k": "body", "t": "Sichtbar wird nicht, wer Text liefert, sondern wer den Fehler vorher findet. Dafür brauchst du vier Fragen – immer dieselben."}],
    # F5 (3,5 s) - Artefakt: ohne Speichern nicht nutzbar
    [{"k": "kicker", "t": "DER PRÜF-PROMPT"},
     {"k": "steps", "t": [
         "§1 Nenne die drei Stellen, an denen",
         "   dieser Text sachlich falsch sein kann.",
         "§2 Welche Zahl darin ist nicht belegt?",
         "§3 Was würde ein Fachkundiger sofort",
         "   bestreiten – und mit welchem Argument?",
         "§4 Was fehlt, das der Empfänger braucht?",
     ], "s": 38},
     {"k": "body", "t": "Darüber dein KI-Ergebnis einfügen. Antworten prüfen, dann weitergeben.", "s": 42}],
    # F6 (3,6 s) - einziger CTA: Speicher-Auftrag
    [{"k": "kicker", "t": "EIN HINWEIS"},
     {"k": "big", "t": "Speicher diesen Prompt, bevor du ihn brauchst.", "s": 82},
     {"k": "body", "t": "Am Donnerstag um 16 Uhr, zwischen Mail und Abgabe, suchst du ihn nicht mehr."},
     {"k": "gap", "s": 10},
     {"k": "cta", "t": "Beitrag speichern"}],
]

# ---------------------------------------------------------------- Slot 4: Story 15:00
STORY_ENGAGE = [
    {"k": "kicker", "t": "KURZE FRAGE"},
    {"k": "big", "t": "Hat deine Firma dich in zwölf Monaten zu KI geschult?", "s": 82},
    {"k": "gap", "s": 16},
    {"k": "rows", "t": [
        "Ja, mit Arbeitszeit dafür",
        "Ja, aber in meiner Freizeit",
        "Nein, war nie ein Thema",
        "Nein, ich habe selbst angefangen",
    ], "s": 44},
    {"k": "gap", "s": 12},
    {"k": "body", "t": "Antworte mit der Zahl. Vergleichswert: 43,9 % haben dafür keine Arbeitszeit genutzt.", "s": 42},
    {"k": "src", "t": SRC_IU},
]

# ---------------------------------------------------------------- Slot 5: Story 20:00
STORY_DM = [
    {"k": "kicker", "t": "VORLAGE ZUM KOPIEREN"},
    {"k": "big", "t": "Der Prüf-Prompt von heute Mittag, als Text.", "s": 84},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Vier Fragen, die du über jedes KI-Ergebnis stellst, bevor es deinen Namen trägt."},
    {"k": "gap", "s": 14},
    {"k": "cta", "t": "Schreib mir PRUEFEN per DM"},
    {"k": "body", "t": "Keine Anmeldung, keine Liste. Du bekommst den Text zurück.", "s": 40},
]
