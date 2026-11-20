# -*- coding: utf-8 -*-
# Captions Tagesausgabe 2026-11-20 (Freitag) - Saeule JOB-WORKFLOWS
# DREI Hashtags je Post. Begruendung: Hashtag-Regel "max. 3 in ALLEN
# Formaten" ist Pflicht seit 25.08.2026 (OPERATIONS.md, gemessen +24 %
# Reichweite), bestaetigt in Anpassung 1 der Auswertung 22.10.2026. Der
# Auftragstext nennt 5-8; seit 12.10. offener Punkt fuer Max.
# Reel B traegt den situativen Speicher-Auftrag als ERSTE Caption-Zeile
# (Auftragstext 15.11.2026), Reel A den Folgen-CTA.
# HARTE LAENGENPRUEFUNG (Anpassung 2 der Auswertung 16.11.2026): jede
# Caption <= 2200 Zeichen, sonst weist Meta den Container mit HTTP 400 ab
# (Ausfallursache 16.11. 14:00).
CAPTIONS = {}

TAGS_A = "#kiimjob #arbeitsalltag #15minutenvorsprung"
TAGS_B = "#kiimjob #produktivitaet #15minutenvorsprung"

Q_AD = ("Quelle: Adecco Group, „Global Workforce of the Future“ 2026 "
        "(7. Ausgabe), veröffentlicht am 19.11.2026. 40.500 Beschäftigte in "
        "36 Ländern und 21 Branchen, Online-Befragung Juni bis Juli 2026. "
        "Zahlen gegengeprüft in den unabhängig formulierten Berichten von "
        "it-boltwise.de und spielemagazin.de, beide vom 19.11.2026.")

Q_EIN = ("Einordnung: Herausgeber ist ein Personaldienstleister, der "
         "Weiterbildung und Workforce-Beratung verkauft — also genau das, "
         "was die Studie empfiehlt. Alle Werte sind Selbstauskunft, niemand "
         "hat nachgemessen. Die 20 Prozent sind ein relativer Aufschlag ohne "
         "genannte Basis und lassen sich nicht in Minuten umrechnen, „gut "
         "eingebettet“ wird nicht definiert, und die Gruppen bilden sich "
         "selbst: Wer so arbeitet, sitzt vielleicht ohnehin im besser "
         "organisierten Betrieb. Erhebungsinstitut, Gewichtung und deutsche "
         "Fallzahl nennt die Mitteilung nicht.")

# ------------------------------------------------ Slot 1 (Story 09:00)
CAPTIONS[1] = """Teaser für das 10-Uhr-Reel: 74 Prozent der Befragten arbeiten mit KI-Agenten, ein Jahr davor waren es 64. Das Werkzeug ist damit Grundausstattung, kein Vorsprung. Die Zahl, die trennt, steht um 10 Uhr. Quelle: Adecco Group, Global Workforce of the Future 2026, 40.500 Beschäftigte in 36 Ländern.
"""

# ------------------------------------------------ Slot 2 (Reel A 10:00)
CAPTIONS[2] = """Das Werkzeug haben jetzt fast alle. Es entscheidet nicht mehr, welches du hast — sondern wo es steht.

74 Prozent der Befragten arbeiten mit KI-Agenten, im Jahr davor waren es 64. Wer also darauf wartet, endlich das richtige Werkzeug zu finden, wartet auf etwas, das die Kollegen schon haben.

Die Zahl, die stattdessen trennt: 20 Prozent mehr Zeit pro Tag — bei denen, deren KI im Arbeitsablauf sitzt statt in einem Chatfenster daneben. Dieselbe Gruppe fühlt sich siebenmal seltener überfordert, mit den Werkzeugen umzugehen.

Das ist der ganze Unterschied: nicht mehr Werkzeuge, sondern derselbe Handgriff, nur eingebaut. Zwei weitere Zahlen aus derselben Studie zeigen, woran das hängt: 96 Prozent derjenigen, die ihre Arbeit selbst mitgestalten durften, sind bereit, sich anzupassen — gegen 29 Prozent der übrigen. Und unter den KI-Nutzern berichten 93 Prozent der Geschulten eine Produktivitätssteigerung, gegen 47 Prozent der Ungeschulten. Die Schulungsteilnahme ist im selben Zeitraum von 77 auf 67 Prozent gefallen.

Ein neues Werkzeug ändert deinen Freitag nicht. Ein eingebauter Schritt schon.

""" + Q_AD + """

""" + Q_EIN + """

""" + TAGS_A + """
"""

# ------------------------------------------------ Slot 3 (Reel B 14:00)
CAPTIONS[3] = """Öffne das am Montag um 9, wenn die Woche wieder bei Null anfängt — dann brauchst du genau diese vier Zeilen.

Du tippst dieselbe Aufgabe jede Woche neu in die KI. Montag sitzt du wieder vor einem leeren Chatfenster und formulierst alles von vorn. Das ist der Punkt, an dem Zeitersparnis verschwindet.

Gemessen wurde das so: 20 Prozent mehr Zeit pro Tag haben die Befragten, bei denen die KI im Arbeitsablauf steckt — nicht daneben. Der Unterschied ist kein Werkzeug, sondern ein Schritt, der nächste Woche noch da ist.

Nimm also den Handgriff, den du diese Woche dreimal gemacht hast. Daraus wird keine bessere Frage, sondern eine stehende Arbeitsanweisung.

Die vier Zeilen:

1. Diese Aufgabe mache ich jede Woche: [beschreiben]. So sah sie zuletzt aus: [einfügen].
2. Mach daraus eine feste Anweisung: was ich reingebe, was du tust, wie das Ergebnis aussehen muss.
3. Nenne den EINEN Punkt, an dem ich prüfen muss, bevor es rausgeht.
4. Schreib sie so, dass ich nächste Woche nur die neuen Zahlen tausche.

Zeile 3 ist der Kern: Ohne festen Prüfpunkt wird aus Zeitersparnis Nachkontrolle. Zeile 4 macht aus einem Versuch einen Schritt — du legst die Anweisung dorthin, wo die Aufgabe liegt, und tauschst nächste Woche nur die Zahlen.

Montag früh entscheidet sich, ob du KI benutzt oder eingebaut hast.

""" + Q_AD + """

Einordnung: Herausgeber ist ein Personaldienstleister, der Weiterbildung verkauft. Alle Werte sind Selbstauskunft, die 20 Prozent sind ein Aufschlag ohne genannte Basis, und die Gruppen bilden sich selbst.

""" + TAGS_B + """
"""

# ------------------------------------------------ Slot 4 (Story 15:00)
CAPTIONS[4] = """Welcher Handgriff kommt bei dir jede Woche wieder? 1 derselbe Statusbericht, 2 dieselbe Art von Mail, 3 dieselbe Tabelle auffrischen. Antworte mit 1, 2 oder 3.
"""

# ------------------------------------------------ Slot 5 (Story 20:00)
CAPTIONS[5] = """Die Wiedervorlage als fertige Vorlage: vier Zeilen, die aus einer wöchentlichen Aufgabe eine stehende Arbeitsanweisung machen — mit dem einen Punkt, an dem du vorher draufschaust, damit aus Zeitersparnis keine Nachkontrolle wird. Schreib mir VORLAGE als DM, dann bekommst du den vollständigen Text zum Kopieren.
"""

# ------------------------------------------------ Laengenpruefung
for _slot, _txt in CAPTIONS.items():
    if len(_txt) > 2200:
        _cut = _txt[:2200].rsplit("\n\n", 1)[0]
        print("WARNUNG Caption slot-%d gekuerzt: %d -> %d Zeichen"
              % (_slot, len(_txt), len(_cut)))
        CAPTIONS[_slot] = _cut
