# -*- coding: utf-8 -*-
# Captions Tagesausgabe 2026-11-18 (Mittwoch) - Saeule JOB-WORKFLOWS
# DREI Hashtags je Post. Begruendung: Hashtag-Regel "max. 3 in ALLEN
# Formaten" ist Pflicht seit 25.08.2026 (OPERATIONS.md, gemessen +24 %
# Reichweite). Der Auftragstext nennt 5-8; die Auswertung 12.11.2026
# fuehrt genau diese Abweichung als offenen Punkt 3 fuer Max. Gefahren
# wird die gemessene Regel, die Abweichung steht im Lauf-Bericht.
# Reel B traegt den situativen Speicher-Auftrag als ERSTE Caption-Zeile
# (Auftragstext 15.11.2026), Reel A den Folgen-CTA.
# HARTE LAENGENPRUEFUNG (Anpassung 2 der Auswertung 16.11.2026): jede
# Caption muss <= 2200 Zeichen sein, sonst weist Meta den Container mit
# HTTP 400 ab. Ursache des Ausfalls vom 16.11. um 14:00 (2619 Zeichen).
CAPTIONS = {}

TAGS_A = "#kiimjob #arbeitsalltag #15minutenvorsprung"
TAGS_B = "#kiimjob #meetingvorbereitung #15minutenvorsprung"

Q_MS = ("Quelle: Microsoft 2026 Work Trend Index, veröffentlicht am 05.05.2026, "
        "erhoben von Edelman Data x Intelligence. Befragt wurden 20.000 "
        "Wissensarbeitende in 10 Märkten (darunter Deutschland), die KI im Job "
        "bereits nutzen, Februar bis April 2026. Werte: 16 Prozent "
        "Spitzengruppe, 53 gegen 33 Prozent bei der Aufteilung Mensch/KI, "
        "43 gegen 30 Prozent bei bewusst KI-freier Arbeit, 66 Prozent mehr Zeit "
        "für hochwertige Arbeit, 86 Prozent behandeln KI-Output als "
        "Ausgangspunkt. Gegengeprüft bei The Neuron (08.05.2026) und "
        "Fast Company (12.05.2026).")

Q_EIN = ("Einordnung, die dazugehört: Herausgeber ist Microsoft, das genau das "
         "verkauft, was der Bericht empfiehlt. Befragt wurden ausschließlich "
         "Menschen, die KI schon nutzen — wer nie nutzt, wurde herausgefiltert. "
         "Alles ist Selbstauskunft, Zusammenhang statt Ursache. Deutschland ist "
         "einer von zehn Märkten und wird nicht gesondert ausgewiesen.")

# ------------------------------------------------ Slot 1 (Story 09:00)
CAPTIONS[1] = """Teaser für das 10-Uhr-Reel: Nur 16 Prozent der Leute, die KI im Job nutzen, gehören zur Spitzengruppe — bei identischen Werkzeugen. Microsoft Work Trend Index 2026, 20.000 Befragte, Edelman Data x Intelligence.
"""

# ------------------------------------------------ Slot 2 (Reel A 10:00)
CAPTIONS[2] = """Dir fehlt bei KI nicht das Werkzeug. 84 Prozent der Nutzer haben dasselbe — und kommen nicht weiter.

Microsoft hat für den Work Trend Index 2026 20.000 Wissensarbeitende befragen lassen, die KI im Job bereits benutzen. 16 Prozent von ihnen zählt der Bericht zur Spitzengruppe. Die übrigen 84 Prozent sitzen vor denselben Programmen.

Der Unterschied steckt nicht in der Software, sondern in einer Minute vor der Aufgabe: 53 Prozent der Spitzengruppe halten inne und legen fest, was die KI übernimmt und was sie selbst entscheiden. Unter allen befragten KI-Nutzern tun das 33 Prozent. Dieselbe Richtung bei der zweiten Zahl: 43 gegen 30 Prozent erledigen manche Arbeit bewusst ohne KI.

Das ist die ganze Mechanik. Nicht mehr tippen, sondern vorher aufteilen.

""" + Q_MS + """

""" + Q_EIN + """

""" + TAGS_A + """
"""

# ------------------------------------------------ Slot 3 (Reel B 14:00)
CAPTIONS[3] = """Öffne das zehn Minuten vor deinem nächsten Meeting — dann brauchst du genau diese vier Zeilen.

Du überfliegst die Unterlage kurz vorher und sagst im Termin nichts, weil dir keine Frage einfällt, die nicht dumm klingt. Das liegt nicht am Lesen, sondern daran, dass Überfliegen keine Fragen erzeugt.

53 Prozent der KI-Spitzengruppe legen vor der Arbeit fest, was die KI tut und was sie selbst. Unter allen befragten KI-Nutzern sind es 33 Prozent. Genau diese Aufteilung macht aus zehn Minuten Überfliegen zehn Minuten Vorbereitung: Die KI liest. Du entscheidest, was in der Unterlage eine Entscheidung ist.

Die vier Zeilen:

1. Das ist die Unterlage zum Termin: [einfügen].
2. Was wird darin entschieden — und was nur berichtet?
3. Nenne die drei Stellen, die meinen Bereich betreffen: [Bereich].
4. Mach daraus drei Fragen unter 15 Wörtern. Sag, welche zuerst kommt.

Schritt 2 ist der Kern. Ohne die Trennung bekommst du eine Zusammenfassung, und aus Zusammenfassungen entstehen keine Fragen. Schritt 4 begrenzt die Länge, weil eine Frage über 15 Wörter im Meeting als Monolog ankommt.

Eine präzise Frage wirkt länger als jede Wortmeldung danach.

""" + Q_MS + """

Einordnung: Herausgeber ist Microsoft, befragt wurden nur KI-Nutzer, alle Werte sind Selbstauskunft.

""" + TAGS_B + """
"""

# ------------------------------------------------ Slot 4 (Story 15:00)
CAPTIONS[4] = """Woran scheitert dein nächstes Meeting? 1 ich lese die Unterlage zu spät, 2 mir fällt keine gute Frage ein, 3 ich rede, es bleibt nichts hängen. Antworte mit 1, 2 oder 3.
"""

# ------------------------------------------------ Slot 5 (Story 20:00)
CAPTIONS[5] = """Die Meeting-Vorbereitung als fertige Vorlage: vier Zeilen, die aus einer fremden Unterlage drei Fragen machen — und dir sagen, welche du zuerst stellst. Schreib mir MEETING als DM, dann bekommst du den vollständigen Text zum Kopieren.
"""

# ------------------------------------------------ Laengenpruefung
for _slot, _txt in CAPTIONS.items():
    if len(_txt) > 2200:
        _cut = _txt[:2200].rsplit("\n\n", 1)[0]
        print("WARNUNG Caption slot-%d gekuerzt: %d -> %d Zeichen"
              % (_slot, len(_txt), len(_cut)))
        CAPTIONS[_slot] = _cut
