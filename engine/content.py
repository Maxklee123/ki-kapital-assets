# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-15 (Sonntag) - Saeule: AENGSTE ENTKRAEFTEN
#
# Saeulen-Zuordnung: Sonntag = AENGSTE ENTKRAEFTEN (Auftragstext; deckungsgleich
# mit Anpassung 2 der Auswertung 09.11.2026, dort AENGSTE = Mi+Do+So).
# Die Auswertung 12.11.2026 misst fuer AENGSTE die hoechste Reichweite
# (oe 23,8 gegen 5,4 bei JOB-WORKFLOWS).
#
# Slot-Plan heute nach Auftragstext vom 15.11.2026 (Auswertung 14.11.):
#   2 Reels + 3 Stories, Reel C und Karussell gestrichen.
#   ABWEICHUNG zu OPERATIONS.md: dort sind die drei Story-Slots am 12.11.
#   gestrichen (reach 0). Der neuere Auftragstext nimmt sie wieder auf -
#   ihm wird gefolgt, der Konflikt ist im Lauf-Bericht vermerkt.
#   Reel B traegt den NEUEN visuellen Speicher-CTA (Auftragstext 15.11.),
#   der die Folgen-CTA-Frist 13.-19.11. aus der Auswertung 12.11. ersetzt.
#
# Thema: Der Satz "KI frisst die Jobs" hat in den deutschen
#        Beschaeftigtendaten bisher keine Entsprechung - und die Gruppe, die
#        tatsaechlich verliert, ist nicht die Zielgruppe dieses Kontos.
# Quelle: Institut fuer Arbeitsmarkt- und Berufsforschung (IAB),
#         Melanie Arntz, Michele Dinelli, Oliver Schlenker,
#         "KI als Jobkiller fuer Berufseinsteiger? Entwarnung mit Vorbehalt",
#         IAB-Forum, veroeffentlicht 13.10.2026; zugehoerige IAB-Presseinfo
#         "KI bisher kein Jobkiller, aber Berufseinsteiger zunehmend betroffen".
#         Datenbasis: monatliche administrative Beschaeftigungsdaten der
#         Bundesagentur fuer Arbeit, Januar 2021 bis Dezember 2025, im Schnitt
#         rund 22,3 Mio. sozialversicherungspflichtig Vollzeitbeschaeftigte
#         im Alter von 20 bis 64 Jahren (ohne Beamte, Selbstaendige,
#         Minijobber, Azubis). KI-Exposition nach Eloundou et al. (2024),
#         Berufe in Quintile geteilt; Poisson-Regression, Referenz 4. Quartal 2022.
#         Kernzahlen: stark KI-exponierte Berufe 2025 rund +1 % gegenueber 2022,
#         weniger exponierte gut -3 %; ab 30 Jahren in stark exponierten Berufen
#         rund +2 %; Wachstumsabstand stark minus schwach: 30-39 fast
#         +6 Prozentpunkte, 40-64 rund +5 Prozentpunkte, 20-29 -1,2 Prozentpunkte
#         (-3,8 % gegen -2,6 %).
# Gegenprobe (Pflicht, steht in Frame 5 und in beiden Captions):
#         Im Modell je Standardabweichung ist der Zusammenhang mit der
#         Konjunkturanfaelligkeit "mehr als doppelt so stark" wie der mit der
#         KI-Exposition; der KI-Wert fuer die 20- bis 29-Jaehrigen (-1,8 %)
#         ist statistisch NICHT signifikant. Signifikant negativ ist er nur
#         im verarbeitenden Gewerbe und in nichtakademischen Berufen bei den
#         unter 30-Jaehrigen. Die Autoren nennen ihre Befunde rein deskriptiv
#         und ausdruecklich keinen kausalen Nachweis.

NB = " "  # geschuetztes Leerzeichen: haelt Zahl und Einheit zusammen

SRC_IAB  = ("IAB · Arntz/Dinelli/Schlenker, 13.10.2026 · 22,3 Mio. Vollzeitstellen, "
            "BA-Daten 2021–2025")
SRC_IAB2 = ("IAB-Forum, 13.10.2026 · Vollzeitbeschäftigung 2025 gegen 2022, "
            "unbereinigt, Berufe nach KI-Exposition")

# ---------------------------------------------------------------- Slot 1: Story 09:00
STORY_1 = [
    {"k": "kicker", "t": "SONNTAG · 09 UHR"},
    {"k": "num", "t": "+1" + NB + "%", "s": 230, "c": (77, 212, 200)},
    {"k": "numsub", "t": "in Berufen, die KI könnte. Minus 3" + NB + "% in Berufen, die sie nicht könnte.", "s": 54},
    {"k": "body", "t": "Das IAB hat 22,3 Millionen Vollzeitstellen nachgezählt, vier Jahre lang, Monat für Monat. Die Richtung ist nicht die, die du erwartest."},
    {"k": "src", "t": SRC_IAB},
    {"k": "gap", "s": 12},
    {"k": "cta", "t": "Um 10 Uhr kommt die ganze Rechnung"},
]

# ---------------------------------------------------------------- Slot 2: Reel A 10:00
REEL_A = [
    [{"k": "kicker", "t": "SONNTAG"},
     {"k": "big", "t": "Du hältst deinen Beruf für den, den KI als Nächstes kassiert.", "s": 84}],
    [{"k": "kicker", "t": "DAS IAB HAT NACHGEZÄHLT"},
     {"k": "big", "t": "22,3 Millionen Vollzeitstellen. Vier Jahre. Monat für Monat.", "s": 82}],
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "+1 : −3", "s": 185},
     {"k": "numsub", "t": "Prozent Beschäftigung 2025 gegen 2022 – KI-nahe Berufe gegen KI-ferne."},
     {"k": "body", "t": "Nicht die Berufe nah an der KI haben Stellen verloren. Die weit weg davon haben verloren."},
     {"k": "src", "t": SRC_IAB}],
    [{"k": "kicker", "t": "WAS DAS FÜR DICH HEISST"},
     {"k": "big", "t": "Die Jobs, die KI könnte, sind mehr geworden. Die anderen weniger.", "s": 78},
     {"k": "body", "t": "Nähe zur KI war in diesen vier Jahren kein Risiko, sondern der Ort, an dem Stellen entstanden sind. Für den Satz „KI frisst meinen Beruf“ gibt es in den deutschen Daten bisher keine Entsprechung."}],
    [{"k": "kicker", "t": "UND JETZT DIE ZAHL FÜR DICH"},
     {"k": "num", "t": "fast 6", "s": 165},
     {"k": "numsub", "t": "Prozentpunkte Vorsprung hatten die KI-nahen Berufe bei den 30- bis 39-Jährigen."},
     {"k": "body", "t": "Bei den 40- bis 64-Jährigen rund 5 Prozentpunkte. Der einzige Rückstand liegt bei den 20- bis 29-Jährigen: 1,2 Prozentpunkte – und dort hängt er laut Modell stärker an der Konjunktur als an der KI."},
     {"k": "src", "t": SRC_IAB2}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Die Zahl, die dir Angst macht, stammt aus dem Jahrzehnt vor deinem.", "s": 78},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 3: Reel B 14:00
REEL_B = [
    [{"k": "kicker", "t": "SONNTAG · 14 UHR"},
     {"k": "big", "t": "Du kannst nicht sagen, welche deiner Aufgaben KI heute schon schneller kann.", "s": 80}],
    [{"k": "kicker", "t": "UND GENAU DAS ENTSCHEIDET"},
     {"k": "big", "t": "Nicht dein Beruf steht in der Statistik. Deine Aufgaben stehen darin.", "s": 82}],
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "+1 : −3", "s": 185},
     {"k": "numsub", "t": "Prozent Beschäftigung 2025 gegen 2022 – KI-nahe Berufe gegen KI-ferne."},
     {"k": "body", "t": "Das IAB misst einen Beruf über seine Aufgaben: Wie viel davon ginge mit einem Sprachmodell deutlich schneller? Genau diese Frage kannst du heute für dich beantworten."},
     {"k": "src", "t": SRC_IAB}],
    [{"k": "kicker", "t": "DIE MECHANIK"},
     {"k": "big", "t": "Fünfzehn Minuten, einmal im Quartal: das Aufgaben-Audit.", "s": 78},
     {"k": "body", "t": "Du listest, was deine Woche wirklich füllt, und markierst, was ein Sprachmodell schneller könnte. Was übrig bleibt, ist dein Kern – und der gehört in das nächste Gespräch mit deiner Führungskraft, nicht in deinen Kopf."}],
    [{"k": "kicker", "t": "DAS AUFGABEN-AUDIT"},
     {"k": "steps", "t": [
         "§1 Hier sind die 10 Aufgaben, die",
         "   meine Arbeitswoche füllen: [Liste].",
         "§2 Schätze je Aufgabe, wie viel Zeit",
         "   ein Sprachmodell davon abnimmt.",
         "§3 Nenne die 3 Aufgaben, die nur ich",
         "   mit meinem Kontext lösen kann.",
         "§4 Mach daraus 3 Sätze für mein",
         "   nächstes Gespräch mit der Chefin.",
     ], "s": 33},
     {"k": "body", "t": "Schritt 3 ist der, der aus einer Liste eine Position macht.", "s": 38}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Wer seine Aufgaben kennt, wird nicht ersetzt. Er wird umgebaut – und redet mit.", "s": 72},
     {"k": "gap", "s": 10},
     {"k": "save", "t": "Sicher dir das für Montag, 9 Uhr", "lab": "Lesezeichen", "s": 46}],
]

# ---------------------------------------------------------------- Slot 4: Story 15:00
STORY_2 = [
    {"k": "kicker", "t": "KURZE FRAGE"},
    {"k": "big", "t": "Welche Aufgabe würdest du morgen als Erstes abgeben?", "s": 80},
    {"k": "gap", "s": 18},
    {"k": "rows", "t": ["Mails und Antwortentwürfe",
                        "Protokolle und Zusammenfassungen",
                        "Excel-Auswertungen"], "s": 44},
    {"k": "gap", "s": 10},
    {"k": "cta", "t": "Antworte mit 1, 2 oder 3"},
]

# ---------------------------------------------------------------- Slot 5: Story 20:00
STORY_3 = [
    {"k": "kicker", "t": "SONNTAGABEND"},
    {"k": "big", "t": "Das Aufgaben-Audit als fertige Vorlage.", "s": 84},
    {"k": "body", "t": "Vier Schritte, fünfzehn Minuten, keine Technik. Du bekommst den vollständigen Prompt als Text zum Kopieren – heute Abend noch."},
    {"k": "gap", "s": 16},
    {"k": "cta", "t": "Schreib mir AUDIT als DM"},
]
