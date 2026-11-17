# -*- coding: utf-8 -*-
# Captions Tagesausgabe 2026-11-17 (Dienstag) - Saeule UNERSETZBAR-FRAMING
# DREI Hashtags je Post. Begruendung: Hashtag-Regel "max. 3 in ALLEN
# Formaten" ist Pflicht seit 25.08.2026 (OPERATIONS.md, gemessen +24 %
# Reichweite) und wird dort seither gehalten. Der Auftragstext nennt 5-8;
# die Auswertung 12.11.2026 fuehrt genau diese Abweichung als offenen
# Punkt 3 fuer Max. Gefahren wird die gemessene Regel, die Abweichung
# steht im Lauf-Bericht.
# Reel B traegt den situativen Speicher-Auftrag als ERSTE Caption-Zeile
# (Auftragstext 15.11.2026), Reel A den Folgen-CTA.
# HARTE LAENGENPRUEFUNG (Anpassung 2 der Auswertung 16.11.2026): jede
# Caption muss <= 2200 Zeichen sein, sonst weist Meta den Container mit
# HTTP 400 ab. Ursache des Ausfalls vom 16.11. um 14:00 (2619 Zeichen).
CAPTIONS = {}

TAGS_A = "#kiimjob #karriere #15minutenvorsprung"
TAGS_B = "#kiimjob #promptvorlage #15minutenvorsprung"

Q_PWC = ("Quelle: PwC AI Jobs Barometer 2026, veröffentlicht am 30.06.2026. "
         "Ausgezählt wurden über eine Milliarde Stellenanzeigen aus 27 Ländern, "
         "davon rund 9 Millionen in Deutschland; Berichtsjahr 2025. Deutsche Werte: "
         "109.400 Anwenderrollen gegen 15.400 Entwicklerrollen, 1,3 Prozent aller "
         "Anzeigen mit KI-Anforderung (rund 125.000), Lohnaufschlag in den meisten "
         "Sektoren über 20 Prozent. Gegengeprüft bei silicon.de vom 30.06.2026 und "
         "bei aktuelle-sozialpolitik.de vom 20.08.2026.")

# ------------------------------------------------ Slot 1 (Story 09:00)
CAPTIONS[1] = """Teaser für das 10-Uhr-Reel: 7 zu 1. In Deutschland stehen 109.400 KI-Anwenderrollen gegen 15.400 Entwicklerrollen. PwC AI Jobs Barometer 2026, über eine Milliarde ausgezählte Stellenanzeigen.
"""

# ------------------------------------------------ Slot 2 (Reel A 10:00)
CAPTIONS[2] = """Die KI-Stellen in Deutschland gehen nicht an Programmierer. Auf eine Entwicklerrolle kommen sieben für Anwender.

PwC hat für das AI Jobs Barometer 2026 über eine Milliarde Stellenanzeigen aus 27 Ländern ausgezählt, rund neun Millionen davon in Deutschland. Das Ergebnis für 2025: 109.400 Anzeigen suchen jemanden, der KI anwendet. 15.400 suchen jemanden, der KI baut.

Das Verhältnis ist die eigentliche Nachricht, nicht die Zahl. Es heißt: Was im deutschen Arbeitsmarkt knapp ist, ist nicht das Programmieren. Knapp ist der Angestellte, der ein Werkzeug sicher benutzt.

Bezahlt wird es auch. Anzeigen, die KI-Kompetenz verlangen, nennen in den meisten Sektoren über 20 Prozent mehr Gehalt, bei Energie und Versorgern bis zu 39 Prozent. In professionellen Dienstleistungen sind es 13 Prozent.

Und die Kehrseite derselben Zahl: Wenn der Vorsprung kein Studium braucht, dann ist er auch für den Kollegen neben dir erreichbar. Genau das macht ihn dringend und nicht beruhigend.

""" + Q_PWC + """

Einordnung, die dazugehört: Gemessen sind Stellenanzeigen, keine gezahlten Gehälter — der Aufschlag steht in Ausschreibungen, nicht auf Lohnzetteln. 1,3 Prozent aller Anzeigen ist ein kleiner Anteil, von einem Massenphänomen kann keine Rede sein. Im Finanzsektor liegt der Aufschlag bei minus 9 Prozent. PwC ist eine Beratung und profitiert von dem Bedarf, den die Studie beschreibt. Und die Quellen widersprechen sich leicht: pwc.de nennt 7 zu 1, silicon.de rund 8 zu 1; die Rohzahlen ergeben 7,1.

""" + TAGS_A + """
"""

# ------------------------------------------------ Slot 3 (Reel B 14:00)
CAPTIONS[3] = """Öffne das zwei Wochen vor deinem Jahresgespräch — dann brauchst du genau diesen Prompt.

Du nutzt KI längst im Job. Belegen könntest du es nicht.

Genau das entscheidet im Jahresgespräch: nicht was du kannst, sondern was du zeigen kannst. PwC hat ausgezählt, dass in stark KI-exponierten Berufen seit 2019 rund 225 neue Kompetenzen dazugekommen sind. Niemand lernt 225 Dinge nach. Aber ein Teil davon steckt längst in deinen letzten vier Wochen Arbeit — nur unaufgeschrieben.

Die Mechanik ist deshalb keine Weiterbildung, sondern eine Übersetzung: Du lässt die KI deine eigenen Aufgaben durchgehen und in Sätze fassen, die ein Vorgesetzter als Ergebnis liest.

Der Nachweis-Prompt:

1. Hier sind 10 Aufgaben aus meinen letzten vier Wochen: [Liste].
2. Markiere, wo KI das Ergebnis messbar verbessert hat: schneller, genauer, mehr Umfang.
3. Schreib je Treffer einen Satz: Aufgabe, Werkzeug, Ergebnis, Zahl.
4. Sag, welcher Satz ohne Zahl nicht überzeugt — und welche Zahl mir fehlt.

Schritt 4 ist der entscheidende. Er sagt dir vorher, welchen Satz dein Chef auseinandernimmt, und du lieferst die Zahl nach, statt im Gespräch zu improvisieren. Schritt 3 verhindert die Floskel: Ohne Zahl ist es eine Behauptung, mit Zahl ein Ergebnis.

Zwanzig Minuten jetzt sind später drei Sätze, die niemand bestreitet.

Quelle: PwC AI Jobs Barometer 2026, 30.06.2026, über eine Milliarde Stellenanzeigen aus 27 Ländern. Rund 225 neue Kompetenzen pro Beruf zwischen 2019 und 2025 in stark KI-exponierten Berufen. Gegengeprüft bei silicon.de vom 30.06.2026 und bei aktuelle-sozialpolitik.de vom 20.08.2026.

Einordnung: Gemessen werden Stellenanzeigen, nicht Beschäftigte — was eine Anzeige zur KI-Anzeige macht, legt PwC nicht offen. Die 225 gelten nur für stark exponierte Berufe, nicht für jeden Job. Und PwC ist eine Beratung, die von diesem Bedarf lebt.

""" + TAGS_B + """
"""

# ------------------------------------------------ Slot 4 (Story 15:00)
CAPTIONS[4] = """Woran würde dein Chef heute sehen, dass du KI nutzt? 1 an einem Ergebnis mit Zahl, 2 daran, dass du schneller fertig bist, 3 an gar nichts. Antworte mit 1, 2 oder 3.
"""

# ------------------------------------------------ Slot 5 (Story 20:00)
CAPTIONS[5] = """Der Nachweis-Prompt als fertige Vorlage: vier Zeilen, die aus vier Wochen Arbeit drei Sätze machen, die im Jahresgespräch bestehen. Schreib mir NACHWEIS als DM, dann bekommst du den vollständigen Text zum Kopieren.
"""

# ------------------------------------------------ Laengenpruefung
for _slot, _txt in CAPTIONS.items():
    if len(_txt) > 2200:
        _cut = _txt[:2200].rsplit("\n\n", 1)[0]
        print("WARNUNG Caption slot-%d gekuerzt: %d -> %d Zeichen"
              % (_slot, len(_txt), len(_cut)))
        CAPTIONS[_slot] = _cut
