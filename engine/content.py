# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-13 (Freitag) - Saeule: JOB-WORKFLOWS
#
# Saeulen-Zuordnung nach Anpassung 2 der Auswertung 09.11.2026:
#   UNERSETZBAR-FRAMING = Di + Sa + Mo, JOB-WORKFLOWS = nur Fr,
#   AENGSTE ENTKRAEFTEN = Mi + Do + So. Freitag ist damit JOB-WORKFLOWS.
#   Anpassung 5 der Auswertung 12.11.2026 haelt die Saeule ausdruecklich:
#   JOB-WORKFLOWS braucht mindestens zwei weitere Messtage, bevor die
#   Verteilung an der Reichweite ausgerichtet wird.
#
# Slot-Plan heute (nach Auswertung 12.11.2026):
#   Anpassung 1: Karussell 12:00 gestrichen.
#   Anpassung 2: Story-Slots 09:00, 15:00 und 20:00 gestrichen (reach 0,
#       replies 0, profile_visits 0 bei der Messung am Posttag 12.11.).
#       Die Streichung soll ausdruecklich in den Produktionslauf.
#   Anpassung 4 der Auswertung 09.11.: 21:00 Reel C wird nicht gebaut.
#   Gebaut werden damit genau zwei Feed-Slots: 10:00 Reel A, 14:00 Reel B.
#
# CTA heute (Anpassung 3 der Auswertung 12.11.2026):
#   Reel B bekommt fuer sieben Tage (13.-19.11.) den FOLGEN-CTA statt des
#   woertlichen Speicher-Auftrags - 3 Saves auf 143 erreichte Accounts im
#   Fenster 06.-12.11. Die nummerierte Schrittliste in Frame 5 bleibt
#   (Reel-Bauform, Pflicht ab 04.09.2026), nur der CTA wechselt.
#
# Thema: Schatten-KI. Knapp drei von zehn Beschaeftigten, die KI beruflich
#        nutzen, arbeiten mit Werkzeugen, die der eigene Betrieb nicht
#        bereitstellt. Fuer die Zielgruppe ist das kein Compliance-Thema,
#        sondern ein Sichtbarkeits-Thema: die eigene beste KI-Arbeit liegt
#        in einem privaten Chat und zaehlt im Job deshalb nicht.
#        Der counterintuitive Befund sitzt im Rehook: wo der Arbeitgeber
#        KI-Kompetenz am staerksten foerdert, ist der Anteil am hoechsten.
# Quelle: Institut der deutschen Wirtschaft (IW) Koeln, IW-Kurzbericht
#         Nr. 63/2026, Barbara Engels und Andrea Hammermann,
#         "Schatten-KI: Beschaeftigte sind schneller als ihre Betriebe".
#         Repraesentative, gewichtete IW-Beschaeftigtenbefragung, knapp
#         5.000 Beschaeftigte, Befragung Maerz und April 2026; Basis der
#         Schatten-KI-Zahlen n = 2.793 erwerbstaetige KI-Nutzer,
#         multivariates Logit-Modell n = 2.618. Veroeffentlicht
#         19.09.2026, DOI 10.67087/19.21441. Neuer Berichtszyklus in der
#         Fachpresse am 13.11.2026.
#         Kernzahlen: 29,1 % Schatten-KI unter beruflichen KI-Nutzern;
#         38,4 % unter 30 gegen 20,7 % ueber 55; 34,6 % bei
#         Fuehrungskraeften gegen 25,6 % ohne Fuehrungsverantwortung;
#         44,5 % bei stark wahrgenommener Foerderung gegen 21,3 % ohne;
#         19,9 Prozentpunkte Effekt im multivariaten Modell (p < 0,001);
#         33,5 % in Betrieben unter 50 gegen 25,5 % ab 250 Beschaeftigten.
# Gegenprobe: Bitkom (2025), zitiert im selben Kurzbericht - 23 % der
#         kleinen Unternehmen (20-99 Beschaeftigte) stellen generative KI
#         offiziell bereit, 43 % der Grossunternehmen ab 500. Die Luecke
#         zwischen Bedarf und Bereitstellung ist also betrieblich, nicht
#         persoenlich.

NB = " "  # geschuetztes Leerzeichen: haelt Zahl und Einheit zusammen

SRC_IW  = ("IW Köln · Kurzbericht 63/2026, knapp 5.000 Beschäftigte, "
           "Befragung März/April 2026")
SRC_IW2 = ("IW Köln, Kurzbericht 63/2026 · Basis 2.793 erwerbstätige "
           "KI-Nutzer, Befragung März/April 2026")
SRC_BITKOM = "Bitkom 2025, zitiert im IW-Kurzbericht 63/2026"

# ---------------------------------------------------------------- Slot 2: Reel A 10:00
REEL_A = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer, keine Zahl
    [{"k": "kicker", "t": "FREITAG"},
     {"k": "big", "t": "Deine beste KI-Arbeit läuft über ein Werkzeug, das dein Betrieb nie freigegeben hat.", "s": 80}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "UND DU BIST NICHT DIE AUSNAHME"},
     {"k": "big", "t": "Das IW Köln hat knapp 5.000 Beschäftigte gefragt, wie sie es wirklich machen.", "s": 78}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "29,1" + NB + "%", "s": 175},
     {"k": "numsub", "t": "der beruflichen KI-Nutzer arbeiten mit Werkzeugen, die der Betrieb nicht bereitstellt."},
     {"k": "body", "t": "Das IW nennt es Schatten-KI. Nicht heimlich, nicht verboten – nur außerhalb der betrieblichen Kontrolle. Knapp drei von zehn."},
     {"k": "src", "t": SRC_IW}],
    # F4 (3,5 s) - Deutung
    [{"k": "kicker", "t": "WAS DAS FÜR DICH HEISST"},
     {"k": "big", "t": "Arbeit, die im Betrieb nicht existiert, zählt dort auch nicht für dich.", "s": 76},
     {"k": "body", "t": "Dein privater Chat kennt dein bestes Ergebnis. Deine Führungskraft kennt es nicht. Genau da entsteht die Lücke zwischen dem, was du kannst, und dem, was dir zugeschrieben wird."}],
    # F5 (3,5 s) - Rehook mit zweiter Zahl, counterintuitiv
    [{"k": "kicker", "t": "UND JETZT DIE ÜBERRASCHUNG"},
     {"k": "num", "t": "44,5 : 21,3", "s": 128},
     {"k": "numsub", "t": "Prozent Schatten-KI – mit starker Förderung durch den Arbeitgeber gegen keine."},
     {"k": "body", "t": "Wo der Betrieb KI-Kompetenz am stärksten fördert, ist der Anteil am höchsten, nicht am niedrigsten: 19,9 Prozentpunkte Effekt im Modell. Die Motivation ist da. Die Freigabe fehlt."},
     {"k": "src", "t": SRC_IW2}],
    # F6 (3,6 s) - Urteil + genau ein CTA
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Der Engpass ist nicht dein Können. Es ist, dass niemand davon weiß.", "s": 76},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 3: Reel B 14:00
REEL_B = [
    # F1 (0,7 s) - Behauptung ueber den Zuschauer
    [{"k": "kicker", "t": "FREITAG · 14 UHR"},
     {"k": "big", "t": "Du kannst das Werkzeug, das deine Arbeit halbiert, niemandem im Betrieb zeigen.", "s": 80}],
    # F2 (1,3 s)
    [{"k": "kicker", "t": "DAS KOSTET DICH ETWAS"},
     {"k": "big", "t": "Nicht die Nutzung ist das Problem. Die Unsichtbarkeit ist es.", "s": 82}],
    # F3 (3,4 s) - harte Zahl
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "29,1" + NB + "%", "s": 175},
     {"k": "numsub", "t": "arbeiten mit KI-Werkzeugen, die der eigene Betrieb nicht bereitstellt."},
     {"k": "body", "t": "Bei Führungskräften sind es 34,6" + NB + "%, bei den unter 30-Jährigen 38,4" + NB + "%. Es ist der Normalfall, nicht die Ausnahme."},
     {"k": "src", "t": SRC_IW}],
    # F4 (3,5 s) - Mechanik
    [{"k": "kicker", "t": "DIE MECHANIK"},
     {"k": "big", "t": "Aus Schatten wird Sichtbarkeit durch eine Seite, nicht durch ein Gespräch.", "s": 74},
     {"k": "body", "t": "Zwanzig Minuten einmalig: ein Einseiter, der dein Werkzeug zur Freigabe vorschlägt. Du kommst damit nicht als Bittsteller, sondern als der Kollege, der das Thema schon gelöst hat."}],
    # F5 (3,5 s) - Artefakt: der vollstaendige Prompt
    [{"k": "kicker", "t": "DIE WERKZEUG-FREIGABE"},
     {"k": "steps", "t": [
         "§1 Ich nutze [Werkzeug] für [Aufgabe].",
         "   Schreib eine Seite an meine Chefin.",
         "§2 Nenne Zweck, Nutzen in Stunden pro",
         "   Woche und welche Daten hineingehen.",
         "§3 Ergänze zwei Risiken und je eine",
         "   Maßnahme, die sie entschärft.",
         "§4 Schließe mit der Bitte um Freigabe",
         "   für einen Test über vier Wochen.",
     ], "s": 33},
     {"k": "body", "t": "Schritt 3 ist der, der aus einer Bitte einen Vorschlag macht.", "s": 38}],
    # F6 (3,6 s) - Urteil + genau ein CTA (Folgen, Anpassung 3 der Auswertung 12.11.2026)
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Freigabe bekommt nicht der, der fragt. Sondern der, der sie vorbereitet hat.", "s": 74},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]
