# -*- coding: utf-8 -*-
# Captions Tagesausgabe 2026-11-15 (Sonntag) - Saeule AENGSTE ENTKRAEFTEN
# DREI Hashtags je Post. Begruendung: Hashtag-Regel "max. 3 in ALLEN Formaten"
# ist Pflicht seit 25.08.2026 (OPERATIONS.md, gemessen +24 % Reichweite) und
# wird dort seither gehalten. Der Auftragstext nennt 5-8; die Auswertung
# 12.11.2026 fuehrt genau diese Abweichung als offenen Punkt 3 fuer Max.
# Gefahren wird die gemessene Regel, die Abweichung steht im Lauf-Bericht.
# Reel B traegt den NEUEN situativen Speicher-Auftrag als erste Caption-Zeile
# (Auftragstext 15.11.2026), Reel A den Folgen-CTA.
CAPTIONS = {}

Q_IAB = ("Quelle: Institut für Arbeitsmarkt- und Berufsforschung (IAB), Melanie Arntz, "
         "Michele Dinelli und Oliver Schlenker, „KI als Jobkiller für Berufseinsteiger? "
         "Entwarnung mit Vorbehalt“, IAB-Forum, 13.10.2026. Datenbasis: monatliche "
         "administrative Beschäftigungsdaten der Bundesagentur für Arbeit, Januar 2021 bis "
         "Dezember 2025, im Schnitt rund 22,3 Millionen sozialversicherungspflichtig "
         "Vollzeitbeschäftigte im Alter von 20 bis 64 Jahren.")

Q_VORBEHALT = ("Einordnung, die dazugehört: Die KI-Exposition misst, wie viel eines Berufs ein "
               "Sprachmodell schneller könnte — nicht, ob der Betrieb KI überhaupt einsetzt. "
               "Im Modell ist die Konjunkturanfälligkeit mehr als doppelt so stark mit dem "
               "Rückgang bei den Jüngeren verbunden wie die KI-Nähe, und der KI-Wert für die "
               "20- bis 29-Jährigen ist statistisch nicht signifikant. Signifikant negativ ist "
               "er nur im verarbeitenden Gewerbe und in nichtakademischen Berufen. Die Autoren "
               "nennen ihre Befunde ausdrücklich deskriptiv, nicht ursächlich.")

TAGS_A = "#kiimjob #jobsicherheit #15minutenvorsprung"
TAGS_B = "#kiimjob #promptvorlage #15minutenvorsprung"

# ------------------------------------------------ Slot 1 (Story 09:00)
CAPTIONS[1] = """Teaser für das 10-Uhr-Reel: +1 % gegen −3 %. Beschäftigung 2025 gegen 2022, KI-nahe Berufe gegen KI-ferne. 22,3 Millionen Vollzeitstellen, vier Jahre, IAB.
"""

# ------------------------------------------------ Slot 2 (Reel A 10:00)
CAPTIONS[2] = """In Berufen, die KI übernehmen könnte, gibt es heute mehr Vollzeitstellen als 2022. In den anderen weniger.

Das IAB hat dafür nicht gefragt, sondern gezählt: monatliche Meldedaten der Bundesagentur für Arbeit, Januar 2021 bis Dezember 2025, im Schnitt 22,3 Millionen sozialversicherungspflichtige Vollzeitstellen. Jeder Beruf wurde danach sortiert, wie viel seiner Tätigkeiten ein Sprachmodell deutlich schneller erledigen könnte.

Das Ergebnis für 2025 gegenüber 2022: in den stark KI-exponierten Berufen rund 1 Prozent mehr Beschäftigung, in den weniger exponierten gut 3 Prozent weniger. Ab 30 Jahren liegen die KI-nahen Berufe sogar rund 2 Prozent im Plus.

Und dann die Zahl, die dich direkt betrifft: Bei den 30- bis 39-Jährigen wuchsen die KI-nahen Berufe um fast 6 Prozentpunkte stärker als die KI-fernen, bei den 40- bis 64-Jährigen um rund 5 Prozentpunkte. Negativ ist der Abstand in genau einer Altersgruppe — bei den 20- bis 29-Jährigen, mit 1,2 Prozentpunkten (minus 3,8 gegen minus 2,6 Prozent).

Das ist keine Entwarnung für alle. Es ist eine Verschiebung: Die Gruppe, über die der Satz „KI nimmt die Jobs“ etwas aussagt, ist nicht die, die ihn am lautesten ausspricht.

Und selbst dort hält der Befund nur mit Vorbehalt. Im Modell ist die wirtschaftliche Lage der Branche mehr als doppelt so stark mit dem Rückgang verbunden wie die KI-Nähe.

Folgen für einen Workflow pro Tag.

""" + Q_IAB + """

""" + Q_VORBEHALT + """

""" + TAGS_A + """
"""

# ------------------------------------------------ Slot 3 (Reel B 14:00)
CAPTIONS[3] = """Öffne das am Montag um 9, wenn der Kalender noch leer ist — dann brauchst du genau diesen Prompt.

Nicht dein Beruf steht in der Statistik. Deine Aufgaben stehen darin.

Das IAB sortiert Berufe danach, wie viel ihrer Tätigkeiten ein Sprachmodell deutlich schneller erledigen könnte. Ergebnis über 22,3 Millionen Vollzeitstellen: Die stark KI-exponierten Berufe liegen 2025 rund 1 Prozent über 2022, die weniger exponierten gut 3 Prozent darunter.

Genau diese Sortierung kannst du für dich selbst machen. Fünfzehn Minuten, einmal im Quartal. Der Prompt:

1. Hier sind die 10 Aufgaben, die meine Arbeitswoche füllen: [Liste].
2. Schätze je Aufgabe, wie viel Zeit ein Sprachmodell davon abnimmt.
3. Nenne die 3 Aufgaben, die nur ich mit meinem Kontext lösen kann.
4. Mach daraus 3 Sätze für mein nächstes Gespräch mit der Chefin.

Schritt 3 ist der entscheidende. Ohne ihn hast du eine Liste von Dingen, die du bald nicht mehr machst — das ist eine Angstliste. Mit ihm hast du eine Beschreibung dessen, wofür dich niemand ersetzen kann.

Schritt 4 übrigens auch: Was in keinem Gespräch vorkommt, existiert im Betrieb nicht. Drei Sätze reichen, du brauchst dafür keinen Termin.

Leg den Audit-Termin auf einen Montagmorgen im Quartal. Nicht auf „wenn mal Zeit ist“ — die Zeit kommt nicht.

""" + Q_IAB + """

""" + Q_VORBEHALT + """

""" + TAGS_B + """
"""

# ------------------------------------------------ Slot 4 (Story 15:00)
CAPTIONS[4] = """Engagement-Trigger: Welche Aufgabe würdest du morgen als Erstes abgeben? 1 Mails und Antwortentwürfe, 2 Protokolle und Zusammenfassungen, 3 Excel-Auswertungen. Antwort per DM mit der Ziffer.
"""

# ------------------------------------------------ Slot 5 (Story 20:00)
CAPTIONS[5] = """DM-CTA: Keyword AUDIT. Wer AUDIT schreibt, bekommt den vollständigen Vier-Schritte-Prompt des Aufgaben-Audits als Text zum Kopieren.
"""
