# -*- coding: utf-8 -*-
# Captions Tagesausgabe 2026-11-13 (Freitag) - Saeule JOB-WORKFLOWS
# Drei Hashtags je Post (Hashtag-Regel Pflicht ab 25.08.2026, max. 3 in
# ALLEN Formaten; der Hashtag-Test 20.-23.10. wurde in der Auswertung
# 26.10.2026 fuer ungueltig erklaert).
# Reel B traegt heute den FOLGEN-CTA, nicht den Speicher-Auftrag
# (Anpassung 3 der Auswertung 12.11.2026, gueltig 13.-19.11.2026) - die
# erste Caption-Zeile ist deshalb die Hook-Zeile und kein Speicher-Auftrag.
CAPTIONS = {}

Q_IW = ("Quelle: Institut der deutschen Wirtschaft (IW) Köln, IW-Kurzbericht Nr. 63/2026, "
        "Barbara Engels und Andrea Hammermann, „Schatten-KI: Beschäftigte sind schneller "
        "als ihre Betriebe“. Repräsentative, gewichtete IW-Beschäftigtenbefragung, knapp "
        "5.000 Beschäftigte, Befragung März und April 2026. Basis der Schatten-KI-Werte: "
        "2.793 erwerbstätige KI-Nutzer. Veröffentlicht am 19.09.2026.")

Q_BITKOM = ("Zum Vergleich, im selben Kurzbericht zitiert: laut Bitkom (2025) stellen 23 % der "
            "Unternehmen mit 20 bis 99 Beschäftigten generative KI offiziell bereit, "
            "aber 43 % der Unternehmen ab 500 Beschäftigten.")

TAGS_A = "#kiimjob #schattenki #15minutenvorsprung"
TAGS_B = "#kiimjob #promptvorlage #15minutenvorsprung"

# ------------------------------------------------ Slot 2 (Reel A 10:00)
CAPTIONS[2] = """29,1 % der Beschäftigten, die KI im Job nutzen, tun das mit einem Werkzeug, das ihr Betrieb nie bereitgestellt hat.

Das IW Köln hat knapp 5.000 Beschäftigte befragt und nennt es Schatten-KI. Wichtig für die Einordnung: nicht heimlich, nicht verboten. Nur außerhalb der betrieblichen Kontrolle — der private Chatbot-Zugang, das Tool, von dem die IT nichts weiß.

Die Verteilung sagt mehr als der Durchschnitt. Unter 30 Jahren: 38,4 %. Über 55: 20,7 %. Führungskräfte: 34,6 %, ohne Führungsverantwortung 25,6 %. In Betrieben unter 50 Beschäftigten 33,5 %, ab 250 nur noch 25,5 %. Je weniger der Betrieb anbietet, desto mehr organisieren die Leute sich selbst.

Und dann die Zahl, die man zweimal lesen muss: Beschäftigte, die ein starkes Engagement ihres Arbeitgebers beim Aufbau von KI-Kompetenz wahrnehmen, liegen bei 44,5 % Schatten-KI. Die ohne wahrgenommenes Engagement bei 21,3 %. Im multivariaten Modell bleiben 19,9 Prozentpunkte Effekt übrig, hochsignifikant.

Das ist kein Widerspruch, sondern die eigentliche Botschaft: Ermutigung erzeugt Motivation, nicht Infrastruktur. Wer gesagt bekommt „nutzt KI“, aber kein Werkzeug gestellt bekommt, nimmt eben das nächstbeste.

Für dich im Job heißt das nicht „hör auf damit“. Es heißt: deine Arbeit mit dem Werkzeug existiert betrieblich nicht — und damit zählt sie dir auch nicht. Der Engpass ist nicht dein Können.

Folgen für einen Workflow pro Tag.

""" + Q_IW + """

""" + Q_BITKOM + """

""" + TAGS_A + """
"""

# ------------------------------------------------ Slot 3 (Reel B 14:00)
CAPTIONS[3] = """Du kannst das Werkzeug, das deine Arbeit halbiert, im Betrieb niemandem zeigen. Das kostet dich mehr als du denkst.

29,1 % der beruflichen KI-Nutzer arbeiten mit Tools, die ihr Betrieb nicht bereitstellt — bei Führungskräften 34,6 %, bei den unter 30-Jährigen 38,4 %. Das IW Köln hat dafür knapp 5.000 Beschäftigte befragt. Es ist der Normalfall.

Nicht die Nutzung ist das Problem. Die Unsichtbarkeit ist es. Dein bester Output liegt in einem privaten Chat, und im Jahresgespräch gibt es ihn nicht.

Der Weg heraus ist eine Seite, kein Gespräch. Zwanzig Minuten einmalig, vier Schritte:

1. Ich nutze [Werkzeug] für [Aufgabe]. Schreib eine Seite an meine Chefin.
2. Nenne Zweck, Nutzen in Stunden pro Woche und welche Daten hineingehen.
3. Ergänze zwei Risiken und je eine Maßnahme, die sie entschärft.
4. Schließe mit der Bitte um Freigabe für einen Test über vier Wochen.

Schritt 3 ist der entscheidende. Ohne ihn bist du der Kollege, der eine Ausnahme will. Mit ihm bist du der, der Datenschutz und Fehlerrisiko schon durchdacht hat — und das ist eine andere Rolle im Raum.

Schritt 2 übrigens auch: „spart Zeit“ ist kein Argument, „spart vier Stunden pro Woche bei der Angebotserstellung“ ist eins.

Und wenn die Freigabe nicht kommt, hast du trotzdem gewonnen: dann steht schwarz auf weiß, wer informiert war.

Folgen für einen Workflow pro Tag.

""" + Q_IW + """

""" + TAGS_B + """
"""
