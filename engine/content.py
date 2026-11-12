# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-12 (Donnerstag) - Saeule: AENGSTE ENTKRAEFTEN
#
# Saeulen-Zuordnung nach Anpassung 2 der Auswertung 09.11.2026:
#   UNERSETZBAR-FRAMING = Di + Sa + Mo, JOB-WORKFLOWS = nur Fr.
#   Damit fallen Mi + Do + So an AENGSTE ENTKRAEFTEN.
# Slot-Plan nach Anpassung 1 der Auswertung 09.11.2026:
#   Karussell 12:00 gestrichen, Stories 09:00 und 15:00 dauerhaft.
#   Slot 6 (21:00 Reel C) wird nach Anpassung 4 nicht gebaut (Entscheidung
#   02.11.2026, bisher sieben verlorene Produktionen - offen fuer Max).
#
# Thema: Die Angst zeigt auf die falsche Stelle. Dieselbe Befragung trennt
#        zwei Sorgen - den aktuellen Arbeitsplatz (14 %) und die Frage, ob man
#        im eigenen Berufsfeld noch eine neue Anstellung findet (19 %). Die
#        groessere Sorge gilt dem Markt, nicht dem Schreibtisch. Gegen die
#        Vortagsausgabe (TU Darmstadt) ist das eine andere Quelle und eine
#        andere Zahl - bewusst, damit sich die Saeule nicht wiederholt.
# Quelle: Civey im Auftrag der WEB.DE-Redaktion, je 5.000 Erwerbstaetige ab
#         18 Jahren, online, Befragungszeitraum 14.08.-30.09.2026, Stand der
#         Veroeffentlichung 08.10.2026, statistischer Fehler 2,5 Prozentpunkte.
#         Fragewortlaut aktueller Job: "Wie gross ist Ihre Sorge, Ihren
#         aktuellen Arbeitsplatz aufgrund des Einsatzes von Kuenstlicher
#         Intelligenz zu verlieren?" - Zukunft: "... in Ihrem Berufsfeld in
#         Zukunft keine neue Anstellung zu finden?"
# Gegenprobe: Forsa fuer Table.Briefings, 1.004 Erwerbstaetige,
#         veroeffentlicht 17.01.2026 - 9 % halten es fuer hoch oder sehr hoch,
#         dass KI ihren Job in fuenf Jahren ersetzt.

NB = " "  # geschuetztes Leerzeichen: haelt Zahl und Einheit zusammen

SRC_CIVEY  = ("Civey für die WEB.DE-Redaktion · 5.000 Erwerbstätige, "
              "Befragung 14.08.–30.09.2026")
SRC_CIVEY2 = ("Civey im Auftrag der WEB.DE-Redaktion, je 5.000 Erwerbstätige ab 18, "
              "Befragung 14.08.–30.09.2026")
SRC_FORSA  = "Forsa für Table.Briefings · 1.004 Erwerbstätige, 17.01.2026"

# ---------------------------------------------------------------- Slot 1: Story 09:00
STORY_TEASER = [
    {"k": "kicker", "t": "HEUTE 10 UHR"},
    {"k": "num", "t": "14 : 19", "s": 150},
    {"k": "numsub", "t": "Zwei Sorgen, getrennt gemessen. Die kleinere ist die, von der alle reden."},
    {"k": "body", "t": "14" + NB + "% der Erwerbstätigen sorgen sich, ihren aktuellen Arbeitsplatz an KI zu verlieren. 19" + NB + "% sorgen sich, im eigenen Berufsfeld keine neue Anstellung mehr zu finden."},
    {"k": "src", "t": SRC_CIVEY},
    {"k": "cta", "t": "Was das heißt: 10 Uhr"},
]

# ---------------------------------------------------------------- Slot 2: Reel A 10:00
REEL_A = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer, keine Zahl
    [{"k": "kicker", "t": "DONNERSTAG"},
     {"k": "big", "t": "Du hast Angst, dass KI deinen Schreibtisch überflüssig macht.", "s": 88}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "GEGENPROBE"},
     {"k": "big", "t": "Dieselbe Befragung hat zwei Sorgen getrennt gemessen.", "s": 86}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "14 : 19", "s": 160},
     {"k": "numsub", "t": "Prozent. Aktueller Arbeitsplatz gegen neue Anstellung."},
     {"k": "body", "t": "14" + NB + "% sorgen sich um den eigenen Arbeitsplatz. 19" + NB + "% sorgen sich, im eigenen Berufsfeld keine neue Stelle mehr zu finden."},
     {"k": "src", "t": SRC_CIVEY}],
    # F4 (3,5 s) - Deutung
    [{"k": "kicker", "t": "WAS DA STEHT"},
     {"k": "big", "t": "Die größere Sorge gilt nicht deinem Job. Sondern dem danach.", "s": 78},
     {"k": "body", "t": "Dein Stuhl ist sicherer, als die Schlagzeilen sagen: 73" + NB + "% halten die Sorge um den aktuellen Arbeitsplatz für gering. Unsicher ist der Markt außerhalb davon."}],
    # F5 (3,5 s) - Rehook mit zweiter Zahl
    [{"k": "kicker", "t": "UND NOCH EINE ZAHL"},
     {"k": "num", "t": "24 → 13", "s": 150},
     {"k": "numsub", "t": "Prozent. Sorge um den aktuellen Job, 30–39 gegen 40–49."},
     {"k": "body", "t": "Die Angst halbiert sich mit der Berufserfahrung. Nicht weil die KI schwächer wird, sondern weil man irgendwann weiß, welcher Teil der eigenen Arbeit ein Urteil ist."},
     {"k": "src", "t": SRC_CIVEY}],
    # F6 (3,6 s) - Urteil + genau ein CTA
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Nicht dein Platz ist das Risiko, sondern deine Austauschbarkeit außerhalb davon.", "s": 68},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 3: Reel B 14:00
REEL_B = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer
    [{"k": "kicker", "t": "DONNERSTAG · 14 UHR"},
     {"k": "big", "t": "Du kannst nicht belegen, was du mit KI schon kannst.", "s": 90}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "DAS PROBLEM DARAN"},
     {"k": "big", "t": "Genau das ist die Sorge, die in der Umfrage die größere ist.", "s": 82}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "19" + NB + "%", "s": 185},
     {"k": "numsub", "t": "sorgen sich, im eigenen Berufsfeld keine neue Anstellung zu finden."},
     {"k": "body", "t": "Um den aktuellen Arbeitsplatz sorgen sich 14" + NB + "%. Die größere Sorge gilt also deinem Marktwert, nicht deinem Schreibtisch."},
     {"k": "src", "t": SRC_CIVEY}],
    # F4 (3,5 s) - Mechanik
    [{"k": "kicker", "t": "DIE MECHANIK"},
     {"k": "big", "t": "Marktwert besteht aus Belegen, nicht aus Gefühl.", "s": 84},
     {"k": "body", "t": "Zwanzig Minuten einmalig: drei Sätze, die zeigen, was du mit KI geliefert hast – Aufgabe, Ergebnis und die Entscheidung, die du getroffen hast und nicht das Werkzeug."}],
    # F5 (3,5 s) - Artefakt: ohne Speichern nicht nutzbar
    [{"k": "kicker", "t": "DIE DREI MARKTWERT-SÄTZE"},
     {"k": "steps", "t": [
         "§1 Hier sind drei Aufgaben, die ich mit",
         "   KI gelöst habe: [deine Liste].",
         "§2 Formuliere je einen Satz aus Aufgabe,",
         "   Werkzeug und messbarem Ergebnis.",
         "§3 Ergänze pro Satz die Entscheidung,",
         "   die ich getroffen habe – nicht die KI.",
         "§4 Kürze jeden Satz auf 20 Wörter,",
         "   gesprächs- und bewerbungstauglich.",
     ], "s": 34},
     {"k": "body", "t": "Schritt 3 ist der Teil, den die KI nicht über sich selbst sagen kann.", "s": 40}],
    # F6 (3,6 s) - einziger CTA: Speicher-Auftrag
    [{"k": "kicker", "t": "EIN HINWEIS"},
     {"k": "big", "t": "Speicher diesen Prompt, bevor du ihn brauchst.", "s": 82},
     {"k": "body", "t": "Du brauchst ihn nicht heute. Du brauchst ihn im Jahresgespräch, im Bewerbungsgespräch, am Tag der Umstrukturierung – und dann suchst du ihn."},
     {"k": "gap", "s": 10},
     {"k": "cta", "t": "Beitrag speichern"}],
]

# ---------------------------------------------------------------- Slot 4: Story 15:00
STORY_ENGAGE = [
    {"k": "kicker", "t": "KURZE FRAGE"},
    {"k": "big", "t": "Welche der beiden Sorgen ist bei dir größer?", "s": 82},
    {"k": "gap", "s": 16},
    {"k": "rows", "t": [
        "Mein aktueller Arbeitsplatz",
        "Keine neue Stelle zu finden",
        "Beide gleich stark",
        "Keine von beiden",
    ], "s": 42},
    {"k": "gap", "s": 12},
    {"k": "body", "t": "Antworte mit der Zahl. Vergleichswert aus der Umfrage: 14" + NB + "% gegen 19" + NB + "%.", "s": 42},
    {"k": "src", "t": SRC_CIVEY},
]

# ---------------------------------------------------------------- Slot 5: Story 20:00
STORY_DM = [
    {"k": "kicker", "t": "VORLAGE ZUM KOPIEREN"},
    {"k": "big", "t": "Die drei Marktwert-Sätze von heute Mittag, als Text.", "s": 82},
    {"k": "gap", "s": 14},
    {"k": "body", "t": "Vier Schritte, die aus deiner KI-Arbeit drei belegbare Sätze machen – für das Jahresgespräch und für die Bewerbung, die du hoffentlich nie brauchst."},
    {"k": "gap", "s": 14},
    {"k": "cta", "t": "Schreib mir MARKTWERT per DM"},
    {"k": "body", "t": "Keine Anmeldung, keine Liste. Du bekommst den Text zurück.", "s": 40},
]
