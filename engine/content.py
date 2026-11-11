# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-11 (Mittwoch) - Saeule: AENGSTE ENTKRAEFTEN
#
# Saeulen-Zuordnung nach Anpassung 2 der Auswertung 09.11.2026:
#   UNERSETZBAR-FRAMING = Di + Sa + Mo, JOB-WORKFLOWS = nur Fr.
#   Damit fallen Mi + Do + So an AENGSTE ENTKRAEFTEN. Mittwoch ist also
#   ab heute kein JOB-WORKFLOWS-Tag mehr.
# Slot-Plan nach Anpassung 1 der Auswertung 09.11.2026:
#   Karussell 12:00 wieder gestrichen, Stories 09:00 und 15:00 dauerhaft.
#   Slot 6 (21:00 Reel C) wird nach Anpassung 4 nicht mehr gebaut.
#
# Thema: Die Angst vor KI gilt zu einem grossen Teil den Jobs anderer Leute.
#        Dieselbe Studie fragt beides - allgemein und ueber den eigenen Job -
#        und bekommt zwei voellig verschiedene Zahlen.
# Quelle: KI-Monitor 2026, TU Darmstadt (Fachgebiet Wirtschaftsinformatik,
#         Prof. Dr. Peter Buxmann) mit YouGov, ueber 2.000 Befragte in
#         Deutschland, veroeffentlicht 28.08.2026. Erhebungszeitraum von der
#         Quelle nicht ausgewiesen - wird deshalb nirgends behauptet.

SRC_TUD  = "KI-Monitor 2026, TU Darmstadt mit YouGov, 28.08.2026 · über 2.000 Befragte, Deutschland"
SRC_TUD2 = "KI-Monitor 2026, TU Darmstadt (Prof. Buxmann) mit YouGov, veröffentlicht 28.08.2026"

# ---------------------------------------------------------------- Slot 1: Story 09:00
STORY_TEASER = [
    {"k": "kicker", "t": "HEUTE 10 UHR"},
    {"k": "num", "t": "59,7 : 15,7", "s": 128},
    {"k": "numsub", "t": "Dieselbe Studie, dieselben Menschen, zwei Fragen."},
    {"k": "body", "t": "59,7 % der Erwerbstätigen halten es für wahrscheinlich, dass KI in vielen Berufen Arbeit ersetzt. Gefragt nach dem eigenen Arbeitsplatz: 15,7 %."},
    {"k": "src", "t": SRC_TUD},
    {"k": "cta", "t": "Was das bedeutet: 10 Uhr"},
]

# ---------------------------------------------------------------- Slot 2: Reel A 10:00
REEL_A = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer, keine Zahl
    [{"k": "kicker", "t": "MITTWOCH"},
     {"k": "big", "t": "Du hast Angst, dass KI deinen Job übernimmt.", "s": 90}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "GEGENPROBE"},
     {"k": "big", "t": "Dieselbe Studie hat beides gefragt. Allgemein – und über dich.", "s": 84}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "59,7 : 15,7", "s": 140},
     {"k": "numsub", "t": "Prozent. Zwei Fragen an dieselben Erwerbstätigen."},
     {"k": "body", "t": "59,7 % halten es für wahrscheinlich, dass KI in vielen Berufen menschliche Arbeit ersetzt. Für den eigenen Arbeitsplatz sagen das 15,7 %."},
     {"k": "src", "t": SRC_TUD}],
    # F4 (3,5 s) - Deutung
    [{"k": "kicker", "t": "WAS DA PASSIERT"},
     {"k": "big", "t": "Die Angst wächst mit der Entfernung.", "s": 86},
     {"k": "body", "t": "Für fremde Jobs reicht eine Schlagzeile. Für deinen kennst du die Ausnahmen, die Rückfragen, die Zuständigkeit. Deshalb bricht die Zahl um drei Viertel ein."}],
    # F5 (3,5 s) - Rehook mit zweiter Zahl
    [{"k": "kicker", "t": "UND DIE GEGENPROBE"},
     {"k": "num", "t": "43 %", "s": 190},
     {"k": "numsub", "t": "der Befragten mit sehr gutem KI-Wissen rechnen damit, dass KI ihre Arbeit übernimmt."},
     {"k": "body", "t": "Es ist also nicht Angst gegen Mut. Es ist Vermutung gegen Prüfung – und eine geprüfte Sorge kannst du beantworten."},
     {"k": "src", "t": SRC_TUD}],
    # F6 (3,6 s) - Urteil + genau ein CTA
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Nicht die Angst ist das Problem, sondern dass sie unkonkret bleibt.", "s": 72},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 3: Reel B 14:00
REEL_B = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer
    [{"k": "kicker", "t": "MITTWOCH · 14 UHR"},
     {"k": "big", "t": "Du weißt nicht, welche deiner Aufgaben KI heute schon kann.", "s": 86}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "DAS PROBLEM DARAN"},
     {"k": "big", "t": "Solange du das nicht weißt, bleibt die Sorge unbeantwortbar.", "s": 84}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "50,4 %", "s": 185},
     {"k": "numsub", "t": "sorgen sich um den Verlust eigener Fähigkeiten."},
     {"k": "body", "t": "Um den Arbeitsplatz sorgen sich 15,7 %. Die größere Sorge ist also nicht der Job – es ist das Verlernen."},
     {"k": "src", "t": SRC_TUD}],
    # F4 (3,5 s) - Mechanik
    [{"k": "kicker", "t": "DIE MECHANIK"},
     {"k": "big", "t": "Eine Liste schlägt ein Gefühl.", "s": 90},
     {"k": "body", "t": "Dreißig Minuten einmalig: deine Woche in drei Stapel. Was abgeben, was behalten, was keiner sieht. Danach streitest du nicht mehr mit einer Vermutung."}],
    # F5 (3,5 s) - Artefakt: ohne Speichern nicht nutzbar
    [{"k": "kicker", "t": "DAS AUFGABEN-AUDIT"},
     {"k": "steps", "t": [
         "§1 Hier sind meine Aufgaben einer",
         "   normalen Arbeitswoche: [Liste].",
         "§2 Sortiere sie in: KI kann das heute /",
         "   KI kann es halb / nur ich kann es.",
         "§3 Begründe jede Einordnung in einem Satz.",
         "§4 Nenne die drei Aufgaben, bei denen",
         "   mein Urteil den Unterschied macht.",
     ], "s": 36},
     {"k": "body", "t": "Stapel drei ist deine Jobbeschreibung für die nächsten Jahre.", "s": 42}],
    # F6 (3,6 s) - einziger CTA: Speicher-Auftrag
    [{"k": "kicker", "t": "EIN HINWEIS"},
     {"k": "big", "t": "Speicher das Audit, bevor du es brauchst.", "s": 84},
     {"k": "body", "t": "Du machst es nicht heute. Du machst es an dem Abend, an dem die Sorge wieder hochkommt – und dann findest du es nicht."},
     {"k": "gap", "s": 10},
     {"k": "cta", "t": "Beitrag speichern"}],
]

# ---------------------------------------------------------------- Slot 4: Story 15:00
STORY_ENGAGE = [
    {"k": "kicker", "t": "KURZE FRAGE"},
    {"k": "big", "t": "Welche der beiden Sorgen trifft dich eher?", "s": 84},
    {"k": "gap", "s": 16},
    {"k": "rows", "t": [
        "Mein Job fällt weg",
        "Ich verlerne, was ich kann",
        "Beide gleich stark",
        "Keine von beiden",
    ], "s": 44},
    {"k": "gap", "s": 12},
    {"k": "body", "t": "Antworte mit der Zahl. Vergleichswert aus der Studie: 15,7 % gegen 50,4 %.", "s": 42},
    {"k": "src", "t": SRC_TUD},
]

# ---------------------------------------------------------------- Slot 5: Story 20:00
STORY_DM = [
    {"k": "kicker", "t": "VORLAGE ZUM KOPIEREN"},
    {"k": "big", "t": "Das Aufgaben-Audit von heute Mittag, als Text.", "s": 84},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Vier Schritte, die deine Arbeitswoche in drei Stapel sortieren – abgeben, halb, nur du."},
    {"k": "gap", "s": 14},
    {"k": "cta", "t": "Schreib mir AUDIT per DM"},
    {"k": "body", "t": "Keine Anmeldung, keine Liste. Du bekommst den Text zurück.", "s": 40},
]
