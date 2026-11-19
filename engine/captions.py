# -*- coding: utf-8 -*-
# Captions Tagesausgabe 2026-11-19 (Donnerstag) - Saeule AENGSTE ENTKRAEFTEN
# DREI Hashtags je Post. Begruendung: Hashtag-Regel "max. 3 in ALLEN
# Formaten" ist Pflicht seit 25.08.2026 (OPERATIONS.md, gemessen +24 %
# Reichweite). Der Auftragstext nennt 5-8; seit 12.10. offener Punkt fuer
# Max. Gefahren wird die gemessene Regel, die Abweichung steht im Bericht.
# Reel B traegt den situativen Speicher-Auftrag als ERSTE Caption-Zeile
# (Auftragstext 15.11.2026), Reel A den Folgen-CTA.
# HARTE LAENGENPRUEFUNG (Anpassung 2 der Auswertung 16.11.2026): jede
# Caption <= 2200 Zeichen, sonst weist Meta den Container mit HTTP 400 ab.
CAPTIONS = {}

TAGS_A = "#kiimjob #arbeitsmarkt #15minutenvorsprung"
TAGS_B = "#kiimjob #arbeitsalltag #15minutenvorsprung"

Q_GS = ("Quelle: Goldman Sachs, Analyse des Ökonomen Pierfrancesco Mei, Note "
        "von Ende Oktober 2026. Grundlage: über 15.000 Beschäftigte, die "
        "zwischen 2016 und 2025 ihren Job verloren haben (Displaced Worker "
        "Supplement der US-Arbeitsmarktstatistik). Berichtet von Fortune "
        "(30.10.2026), TheStreet (01.11.2026) und Axios (03.11.2026). Die "
        "Septemberzahlen stammen aus der US-Statistik JOLTS, zitiert in "
        "Goldmans Ausblick 2027 (16.11.2026).")

Q_EIN = ("Einordnung: Goldman Sachs ist eine Investmentbank, kein unabhängiges "
         "Institut. Keine Statistik fragt Entlassene, ob KI der Grund war — "
         "Goldman schätzt die KI-Nähe aus Beruf, Branchen-Adoption und "
         "gestrichener Stelle und zählt die obersten 30 Prozent als "
         "wahrscheinlich KI-verdrängt. Das ist eine Annahme, keine Messung. "
         "Alles US-Daten, deutsche Werte gibt es dazu nicht. Die Berichte "
         "nennen zwei verschiedene Startjahre (2022 bzw. 2023), und Goldman "
         "erwartet die stärkere Wirkung erst in den Folgejahren: Der Befund "
         "heißt „noch nicht“, nicht „nie“.")

# ------------------------------------------------ Slot 1 (Story 09:00)
CAPTIONS[1] = """Teaser für das 10-Uhr-Reel: Im September wurde 1 Prozent der Beschäftigten gekündigt — ein normaler Monat. Die KI-Entlassungswelle ist 2026 nicht gekommen. Die zweite Zahl steht um 10 Uhr. Quelle: US-Statistik JOLTS, zitiert in Goldmans Ausblick 2027.
"""

# ------------------------------------------------ Slot 2 (Reel A 10:00)
CAPTIONS[2] = """Die große KI-Entlassungswelle ist 2026 nicht gekommen. Das Risiko sitzt an einer anderen Stelle.

Angst vor KI im Job hängt fast immer an einem Bild: der Welle, die irgendwann kommt und ganze Abteilungen mitnimmt. In den Arbeitsmarktzahlen ist sie nicht angekommen. Im September wurde 1 Prozent der Beschäftigten gekündigt, 1,6 Millionen Kündigungen stehen 5,4 Millionen Einstellungen gegenüber, und die Erstanträge auf Arbeitslosengeld lagen bei 200.000 — ein Jahr davor bei 228.000.

Die Zahl, die stattdessen zählt, betrifft den Wiedereinstieg. Wer einen KI-nahen Job verliert, sucht rund einen Monat länger als andere Entlassene: unter 35 drei Wochen, ab 35 fünf Wochen. Und ein Jahr nach dem Jobverlust ist diese Gruppe rund 10 Prozentpunkte häufiger noch ohne Arbeit.

Das verschiebt die Frage. Nicht: Kommt die Welle? Sondern: Wie stehe ich da, wenn ich suchen muss?

""" + Q_GS + """

""" + Q_EIN + """

""" + TAGS_A + """
"""

# ------------------------------------------------ Slot 3 (Reel B 14:00)
CAPTIONS[3] = """Öffne das morgen früh, bevor du auf Senden drückst — dann brauchst du genau diese vier Zeilen.

Du schickst die Unterlage raus und hoffst, dass keiner nachfragt. Fragt dann doch jemand, antwortest du aus dem Stand — und genau das bleibt hängen.

Wer aus einem KI-nahen Job verdrängt wird, sucht rund einen Monat länger als andere Entlassene. Nachgewiesen wird dabei nie, dass du KI benutzt hast, sondern dass dein Urteil über dem Ergebnis stand. Das übt man an eigenen Unterlagen, nicht an Kursen.

Der Trick: Lass die KI nicht deinen Text prüfen. Lass sie drei Leser spielen.

Die vier Zeilen:

1. Hier ist mein Entwurf: [einfügen]. Es liest: [wer entscheidet].
2. Spiele drei Leser: den Skeptiker, den Zahlenmenschen, den Chef mit 2 Minuten.
3. Nenne je den härtesten Einwand — als Frage, die im Termin fällt.
4. Sag, welche zwei ich vorher beantworten muss und welche nicht.

Zeile 2 macht den Unterschied: „Prüfe meinen Entwurf“ bringt Stilhinweise, eine Rolle bringt den Einwand, der wirklich fällt. Zeile 4 bleibt bei dir — die KI sammelt, du entscheidest.

Eine Unterlage, die den härtesten Einwand schon beantwortet, fällt auf.

""" + Q_GS + """

Einordnung: Herausgeber ist eine Investmentbank, die KI-Nähe ist geschätzt und nicht erhoben, alle Werte sind US-Daten.

""" + TAGS_B + """
"""

# ------------------------------------------------ Slot 4 (Story 15:00)
CAPTIONS[4] = """Was macht dir bei KI im Job am meisten Sorge? 1 mein Job fällt irgendwann weg, 2 ich finde dann nichts Neues, 3 ich bleibe hängen, wo ich bin. Antworte mit 1, 2 oder 3.
"""

# ------------------------------------------------ Slot 5 (Story 20:00)
CAPTIONS[5] = """Der Einwand-Vorlauf als fertige Vorlage: vier Zeilen, die deinen Entwurf von drei harten Lesern angreifen lassen — und dir sagen, welche zwei Einwände du vorher beantworten musst. Schreib mir EINWAND als DM, dann bekommst du den vollständigen Text zum Kopieren.
"""

# ------------------------------------------------ Laengenpruefung
for _slot, _txt in CAPTIONS.items():
    if len(_txt) > 2200:
        _cut = _txt[:2200].rsplit("\n\n", 1)[0]
        print("WARNUNG Caption slot-%d gekuerzt: %d -> %d Zeichen"
              % (_slot, len(_txt), len(_cut)))
        CAPTIONS[_slot] = _cut
