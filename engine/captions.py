# -*- coding: utf-8 -*-
# Captions Tagesausgabe 2026-11-16 (Montag) - Saeule JOB-WORKFLOWS
# DREI Hashtags je Post. Begruendung: Hashtag-Regel "max. 3 in ALLEN Formaten"
# ist Pflicht seit 25.08.2026 (OPERATIONS.md, gemessen +24 % Reichweite) und
# wird dort seither gehalten. Der Auftragstext nennt 5-8; die Auswertung
# 12.11.2026 fuehrt genau diese Abweichung als offenen Punkt 3 fuer Max.
# Gefahren wird die gemessene Regel, die Abweichung steht im Lauf-Bericht.
# Reel B traegt den situativen Speicher-Auftrag als ERSTE Caption-Zeile
# (Auftragstext 15.11.2026), Reel A den Folgen-CTA.
CAPTIONS = {}

Q_NOTION = ("Quelle: YouGov im Auftrag von Notion, Online-Befragung vom 9. bis 19. Juni 2026. "
            "Stichprobe: 2.067 Beschäftigte im deutschen Privatsektor in computergestützten "
            "Positionen, davon 1.554 mit KI-Nutzung für die Arbeit. Berichtete Werte: 2,17 Stunden "
            "Zeitersparnis pro Woche, 1,81 Stunden Aufwand für Nutzung und Betreuung, daraus eine "
            "Netto-Ersparnis von 22 Minuten pro Woche. Gegengeprüft in digitalbusiness-magazin.de "
            "vom 21.09.2026 und bei MIDRANGE vom 15.09.2026 — beide nennen dieselben Zahlen.")

Q_VORBEHALT = ("Einordnung, die dazugehört: Alle Werte sind Selbstauskunft, kein gemessener "
               "Kalender — Beschäftigte schätzen ihre eigene Zeitersparnis, und solche "
               "Schätzungen fallen regelmäßig zu hoch aus. Auftraggeber der Studie ist ein "
               "Anbieter, der selbst KI-Funktionen verkauft; dass Zeit beim Hin- und Herspringen "
               "zwischen Werkzeugen verloren geht, liegt in seinem Interesse. Befragt wurde nur "
               "der Privatsektor in computergestützten Positionen, nicht alle Beschäftigten. Und "
               "die Quelle sagt nicht, ob sich die 2,17 und 1,81 Stunden auf alle 2.067 Befragten "
               "oder nur auf die 1.554 KI-Nutzer beziehen. Die Richtung der Zahlen ist belastbar, "
               "die zweite Dezimalstelle nicht.")

TAGS_A = "#kiimjob #zeitmanagement #15minutenvorsprung"
TAGS_B = "#kiimjob #promptvorlage #15minutenvorsprung"

# ------------------------------------------------ Slot 1 (Story 09:00)
CAPTIONS[1] = """Teaser für das 10-Uhr-Reel: 22 Minuten netto pro Woche. 2,17 Stunden spart KI, 1,81 Stunden kostet das Bedienen und Prüfen. 2.067 Beschäftigte, deutscher Privatsektor, YouGov für Notion, Juni 2026.
"""

# ------------------------------------------------ Slot 2 (Reel A 10:00)
CAPTIONS[2] = """Deine KI spart dir zwei Stunden pro Woche. Netto bleiben 22 Minuten davon übrig.

YouGov hat für diese Befragung beide Seiten der Rechnung abgefragt — und das ist der Unterschied zu allen Zahlen, die du bisher gesehen hast. 2.067 Beschäftigte im deutschen Privatsektor, alle an computergestützten Arbeitsplätzen.

Die eine Seite: 2,17 Stunden pro Woche, die KI an Arbeit abnimmt. Die andere Seite: 1,81 Stunden pro Woche, die das Bedienen kostet — den Prompt formulieren, das Ergebnis lesen, es prüfen, es nachbessern. Übrig bleiben 22 Minuten die Woche.

Das ist keine Nachricht gegen KI. Es ist eine Nachricht darüber, wo der Hebel liegt: nicht im nächsten Tool, sondern in den 1,81 Stunden. Die 2,17 sind dir vom Modell gegeben. Die 1,81 gehören dir.

Wer das Erklären einmalig erledigt statt fünfzigmal, verschiebt die Rechnung — und zwar auf der Seite, die er selbst steuert.

""" + Q_NOTION + """

""" + Q_VORBEHALT + """

""" + TAGS_A + """
"""

# ------------------------------------------------ Slot 3 (Reel B 14:00)
CAPTIONS[3] = """Öffne das morgen um 9, wenn du die erste Mail neu formulierst — dann brauchst du genau diesen Baustein.

Du tippst jeden Prompt neu, als wäre es der erste. Das ist die Stunde, die dir fehlt.

Die Zahl dahinter: 1,81 Stunden pro Woche gehen laut YouGov fürs Bedienen und Prüfen weg — von 2,17 Stunden, die KI an Arbeit abnimmt. Netto bleiben 22 Minuten. Jede Minute, die du beim Erklären einsparst, landet direkt in diesem Rest.

Die Mechanik dagegen ist unspektakulär: Für jede Aufgabe, die du mehr als dreimal im Monat machst, schreibst du den Rahmen ein einziges Mal auf. Danach tauschst du nur noch den Inhalt.

Der Baustein:

1. Du bist [Rolle]. Ziel in einem Satz: [was am Ende rauskommen soll].
2. Kontext: Empfänger [wer], Vorwissen [was bekannt ist], Ton [wie].
3. Format: [Form], maximal [Länge], in dieser Reihenfolge: [1., 2., 3.].
4. Sag am Ende, was du nicht wissen konntest und was ich prüfen muss.

Schritt 4 ist der, auf den es ankommt. Ohne ihn liest du jedes Ergebnis komplett gegen, weil du nicht weißt, wo die Lücken sitzen. Mit ihm prüfst du die zwei Stellen, die das Modell selbst benannt hat — das ist der Teil der 1,81 Stunden, der sofort verschwindet.

Schritt 1 und 3 sparen die zweite Runde: Die meisten Nachbesserungen sind keine Fehler, sondern Formatfragen, die vorher nicht gesagt wurden.

Zehn Minuten für den Baustein. Danach jede Woche länger.

""" + Q_NOTION + """

""" + Q_VORBEHALT + """

""" + TAGS_B + """
"""

# ------------------------------------------------ Slot 4 (Story 15:00)
CAPTIONS[4] = """Engagement-Trigger: Welcher Teil frisst bei dir die gesparte Zeit? 1 den Prompt überhaupt formulieren, 2 das Ergebnis Zeile für Zeile prüfen, 3 nachbessern, bis es rausgehen kann. Antwort per DM mit der Ziffer.
"""

# ------------------------------------------------ Slot 5 (Story 20:00)
CAPTIONS[5] = """DM-CTA: Keyword BAUSTEIN. Wer BAUSTEIN schreibt, bekommt den vollständigen vierzeiligen Prompt-Baustein als Text zum Kopieren.
"""
