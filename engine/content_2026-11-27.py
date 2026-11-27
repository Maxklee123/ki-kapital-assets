# -*- coding: utf-8 -*-
# Inhalt 27.11.2026 (Freitag) - Saeule: JOB-WORKFLOWS
# Kernbefund: Die Zeit geht nicht in der Besprechung verloren, sondern in den
# fuenf Minuten danach - Aktionspunkte werden nicht festgehalten.
# Quelle im Primaer-PDF geprueft (AKAD_Studie_Arbeitswelten_2026.pdf, Stand 29.04.2026).
# NICHT verwendet wurden die Pressemitteilungs-Zahlen (94 %, 6 von 8 Stunden,
# 39/40 % Beschluesse, 76/78 % Suchzeiten) - sie stehen so NICHT im PDF.
# Abgrenzung zu den Vortagen: 18.11. war ein Prompt VOR dem Meeting
# (Vorbereitung), 16./19.11. waren Mail-Formulierung, 26.11. Aufgaben-Sortierer.
# Heute: die fuenf Minuten NACH der Besprechung.
DATE = "2026-11-27"
PILLAR = "JOB-WORKFLOWS"

NB = " "  # geschuetztes Leerzeichen haelt Zahl und Einheit zusammen

SRC = ("AKAD University / Büro-Kaizen, „Arbeitswelten im Wandel 2026“ · "
       "Online-Befragung Mitte Januar bis Mitte März 2026, n" + NB + "=" + NB + "1.260")
SRC2 = ("AKAD-Studie 2026, S." + NB + "34 · überwiegend Deutschland, "
        "nicht repräsentativ")

TAKT = [0.7, 1.3, 3.4, 3.5, 3.5, 3.6]

# ---------------------------------------------------------------- REEL A 10:00
REEL_A = [
    ("hook",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "white_text": "Du sitzt zu viel in Besprechungen.",
                "green_text": "Das ist nicht dein Problem."}),
    ("text",   {"kick": "DER DENKFEHLER",
                "headline": "Die Zeit geht nicht im Meeting verloren.",
                "body": "Sie geht **danach** verloren. In den fünf Minuten, in denen alle aufstehen.",
                "src": SRC}),
    ("number", {"kick": "DIE ZAHL",
                "big": "19" + NB + "%",
                "caption": "sitzen die halbe Arbeitszeit in Meetings",
                "body": "2022 waren es **unter 10" + NB + "%.** Der Anteil hat sich in vier Jahren verdoppelt — und mit ihm die Zahl der Zusagen, die niemand mitschreibt.",
                "src": SRC}),
    ("text",   {"kick": "WAS DABEI PASSIERT",
                "headline": "Nur gut die Hälfte der Besprechungen wird überhaupt protokolliert.",
                "body": "Von den vereinbarten Aktionspunkten werden **nicht einmal zwei Drittel** umgesetzt.",
                "src": SRC2}),
    ("text",   {"kick": "WARUM DAS DICH BETRIFFT",
                "headline": "Was nicht aufgeschrieben ist, hat niemand zugesagt.",
                "body": "Und wenn später gefragt wird, wer es übernehmen sollte, erinnert sich jeder **anders**.",
                "src": SRC}),
    ("cta",    {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "statement": "Jeden Tag ein Workflow, der im Job sichtbar wird.",
                "cta": "FOLGEN"}),
]

# ---------------------------------------------------------------- REEL B 14:00
REEL_B = [
    ("hook",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "white_text": "Du schreibst nach dem Meeting kein Protokoll.",
                "green_text": "Niemand sonst auch."}),
    ("text",   {"kick": "DIE LÜCKE",
                "headline": "Du brauchst kein Protokoll. Du brauchst vier Zeilen.",
                "body": "Ein Protokoll liest keiner. Eine Liste mit **Name und Datum** liest jeder.",
                "src": SRC}),
    ("number", {"kick": "DIE ZAHL",
                "big": "2" + NB + "von" + NB + "3",
                "caption": "nicht einmal so viele Aktionspunkte",
                "body": "Etwas mehr als die Hälfte der Besprechungen wird protokolliert. Von den vereinbarten Aktionspunkten werden **nicht einmal zwei Drittel** umgesetzt.",
                "src": SRC2}),
    ("text",   {"kick": "DIE MECHANIK",
                "headline": "Deine Notizen reichen. Auch die krakeligen.",
                "body": "Du tippst ab, was du mitgeschrieben hast, und lässt die KI daraus **Zusagen** machen — nicht Zusammenfassung.",
                "src": SRC}),
    ("steps",  {"kick": "DIE BESCHLUSS-ZEILE — 4 SCHRITTE",
                "title": "Direkt nach der Besprechung",
                "steps": [
                    "Rohmaterial rein: **„Hier meine Notizen aus der Besprechung: [abtippen]. Mach daraus nur die Zusagen.“**",
                    "Form vorgeben: **„Jede Zeile: Was – wer – bis wann. Keine Zusammenfassung, keine Höflichkeit.“**",
                    "Lücken zeigen: **„Markiere jede Zusage, bei der Name oder Datum fehlt, mit OFFEN.“**",
                    "Rückfrage bauen: **„Formuliere eine Nachricht, die nur die OFFEN-Punkte klärt – höchstens drei Sätze.“**",
                ],
                "src": SRC}),
    ("save",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "headline": "Du brauchst das nicht jetzt. Sondern in fünf Minuten.",
                "save_title": "Sicher dir das für deine nächste Besprechung",
                "save_sub": "Direkt danach, solange die Notizen noch vor dir liegen."}),
]

# ---------------------------------------------------------------- STORIES
STORY_1 = ("teaser", {"kick": "FREITAG · HEUTE UM 10 UHR",
                      "headline": "Jeder Fünfte sitzt die halbe Arbeitszeit in Meetings",
                      "body": "2022 war es **noch nicht einmal jeder Zehnte.** Das Problem ist aber nicht die Zeit darin — es sind die fünf Minuten danach. Um 10 Uhr steht, was dort verloren geht.",
                      "src": SRC})

STORY_4 = ("question", {"kick": "EINE FRAGE",
                        "headline": "Was passiert bei dir nach der Besprechung?",
                        "sub": "Tippe die Zahl in die DM — ich schicke dir heute Abend die Vorlage dazu.",
                        "options": ["Jemand schreibt ein Protokoll, das keiner liest",
                                    "Jeder notiert sich selbst irgendwas",
                                    "Nichts — und beim nächsten Mal fragt jemand nach"],
                        "badge": "nicht einmal 2 von 3 Zusagen werden umgesetzt"})

STORY_5 = ("dm", {"kick": "VORLAGE PER DM",
                  "headline": "Die Beschluss-Zeile",
                  "keyword": "BESCHLUSS",
                  "body": "Vier Zeilen, die aus deinen Notizen eine Liste machen: was, wer, bis wann — und wo noch ein Name fehlt.",
                  "cta": "SCHREIB MIR BESCHLUSS"})

# ---------------------------------------------------------------- CAPTIONS
CAP_1 = """Jeder Fünfte sitzt die halbe Arbeitszeit in Besprechungen. 2022 war es noch nicht einmal jeder Zehnte.

Das Problem ist aber nicht die Zeit darin. Es sind die fünf Minuten danach.

Um 10 Uhr steht im Reel, was in diesen fünf Minuten verloren geht.

Quelle: AKAD University / Büro-Kaizen, „Arbeitswelten im Wandel 2026“, Online-Befragung Mitte Januar bis Mitte März 2026, n = 1.260, überwiegend Deutschland, nicht repräsentativ.

#kiimjob #meetings #15minutenvorsprung"""

CAP_2 = """Du sitzt zu viel in Besprechungen. Das ist nicht dein Problem — das ist nur das, was du merkst.

Die AKAD University hat mit Büro-Kaizen 1.260 Büroarbeitende befragt, zwischen Mitte Januar und Mitte März 2026. Ein Wert sticht heraus: 19 Prozent verbringen die Hälfte ihrer Arbeitszeit oder mehr in Besprechungen. 2022 waren es unter 10 Prozent. Der Anteil hat sich in vier Jahren verdoppelt.

Spannend wird es bei der zweiten Zahl. Nur etwas mehr als die Hälfte der Besprechungen wird überhaupt protokolliert. Und von den Aktionspunkten, die darin vereinbart werden, werden nicht einmal zwei Drittel umgesetzt.

Daraus folgt etwas Unangenehmes: die Zeit geht nicht in der Besprechung verloren. Sie geht danach verloren. In den fünf Minuten, in denen alle aufstehen und keiner mitschreibt, wer was bis wann übernimmt.

Was nicht aufgeschrieben ist, hat niemand zugesagt. Und wenn zwei Wochen später gefragt wird, wer es machen sollte, erinnert sich jeder anders — meistens zu deinen Lasten, wenn du der Jüngste im Raum warst.

Genau diese fünf Minuten sind der Hebel. Nicht die Besprechung selbst.

Um 14 Uhr steht hier, wie du sie in vier Zeilen schließt.

Quelle: AKAD University / Büro-Kaizen, „Arbeitswelten im Wandel 2026“, Online-Befragung Mitte Januar bis Mitte März 2026, n = 1.260, überwiegend Deutschland, nicht repräsentativ. Die Zahlen sind dem Studien-PDF entnommen, nicht der Pressemitteilung.

#kiimjob #meetings #15minutenvorsprung"""

CAP_3 = """Öffne das direkt nach deiner nächsten Besprechung — in den fünf Minuten, in denen die Notizen noch vor dir liegen.

Du schreibst nach dem Meeting kein Protokoll. Niemand sonst auch.

Das ist keine Nachlässigkeit, das ist die Regel: etwas mehr als die Hälfte der Besprechungen wird protokolliert, und von den vereinbarten Aktionspunkten werden nicht einmal zwei Drittel umgesetzt.

Der Fehler ist der Anspruch. Ein Protokoll ist zu viel Arbeit, also entsteht gar nichts. Du brauchst aber kein Protokoll. Du brauchst vier Zeilen, in denen steht: was, wer, bis wann.

Deine krakeligen Notizen reichen dafür. Du tippst ab, was du mitgeschrieben hast, und lässt die KI daraus Zusagen machen — ausdrücklich keine Zusammenfassung.

Diese vier Zeilen kopierst du direkt nach der Besprechung in dein KI-Tool:

1. "Hier meine Notizen aus der Besprechung: [abtippen]. Mach daraus nur die Zusagen."
2. "Jede Zeile: Was – wer – bis wann. Keine Zusammenfassung, keine Höflichkeit."
3. "Markiere jede Zusage, bei der Name oder Datum fehlt, mit OFFEN."
4. "Formuliere eine Nachricht, die nur die OFFEN-Punkte klärt – höchstens drei Sätze."

Schritt 3 ist der wichtige. Er macht sichtbar, was im Raum nur nach Einigkeit geklungen hat: eine Aufgabe ohne Namen ist keine Aufgabe, ein Termin ohne Datum ist keiner.

Schritt 4 ist der, der dich sichtbar macht. Du schickst keine Zusammenfassung, die keiner liest, sondern drei Sätze mit den offenen Punkten — zwanzig Minuten nach der Besprechung. Das fällt auf, und zwar bei genau den Leuten, bei denen es auffallen soll.

Funktioniert in Sachbearbeitung, Projektarbeit, Marketing und HR. Überall dort, wo in Besprechungen Aufgaben verteilt werden.

Quelle: AKAD University / Büro-Kaizen, „Arbeitswelten im Wandel 2026“, S. 34, Online-Befragung Mitte Januar bis Mitte März 2026, n = 1.260, überwiegend Deutschland, nicht repräsentativ.

#kiimjob #prompt #15minutenvorsprung"""

CAP_4 = """Was passiert bei dir nach der Besprechung?

1 Jemand schreibt ein Protokoll, das keiner liest
2 Jeder notiert sich selbst irgendwas
3 Nichts — und beim nächsten Mal fragt jemand nach

Tippe die Zahl in die DM — ich schicke dir heute Abend die Vorlage dazu.

Nicht einmal zwei Drittel der vereinbarten Aktionspunkte werden umgesetzt.

#kiimjob #meetings #15minutenvorsprung"""

CAP_5 = """Die Beschluss-Zeile als fertige Vorlage.

Vier Zeilen, die aus deinen Notizen eine Liste machen: was, wer, bis wann — und wo noch ein Name oder ein Datum fehlt.

Dauert nach der Besprechung keine zwei Minuten und ersetzt das Protokoll, das sowieso keiner schreibt.

Schreib mir BESCHLUSS als DM, dann schicke ich sie dir.

#kiimjob #prompt #15minutenvorsprung"""

SLOTS = {
    "1": {"time": "09:00", "format": "Story",  "frames": [STORY_1], "caption": CAP_1},
    "2": {"time": "10:00", "format": "Reel A", "frames": REEL_A,    "caption": CAP_2},
    "3": {"time": "14:00", "format": "Reel B", "frames": REEL_B,    "caption": CAP_3},
    "4": {"time": "15:00", "format": "Story",  "frames": [STORY_4], "caption": CAP_4},
    "5": {"time": "20:00", "format": "Story",  "frames": [STORY_5], "caption": CAP_5},
}
