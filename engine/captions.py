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

TAGS_A = "#kiimjob #weiterbildung #15minutenvorsprung"
TAGS_B = "#kiimjob #promptvorlage #15minutenvorsprung"

Q_TUV = ("Quelle: TÜV Weiterbildungsstudie 2026, erhoben von Forsa für den "
         "TÜV-Verband, veröffentlicht am 28.04.2026. Befragt wurden 500 "
         "Unternehmen ab 20 Mitarbeitenden in Deutschland, Januar bis März 2026. "
         "Werte: 56 Prozent nutzen generative KI im Arbeitsalltag, 27 Prozent "
         "haben jemanden geschult (2024: 12 Prozent), 45 Prozent sehen derzeit "
         "keinen Bedarf, 21 Prozent der Betriebe mit 20 bis 49 Beschäftigten "
         "gegen 49 Prozent ab 250. Gegengeprüft bei silicon.de vom 28.04.2026.")

Q_EINORDNUNG = ("Einordnung, die dazugehört: Befragt wurden Unternehmen, nicht "
                "Beschäftigte — das ist die Sicht der Leitung, keine Messung, wer "
                "wirklich etwas gelernt hat. Auftraggeber ist der TÜV-Verband, "
                "dessen Mitglieder Weiterbildung verkaufen. Und fair dagegen "
                "gehalten: 27 Prozent sind mehr als doppelt so viel wie 2024. Die "
                "Richtung stimmt, das Tempo reicht nur nicht an die Nutzung heran.")

# ------------------------------------------------ Slot 1 (Story 09:00)
CAPTIONS[1] = """Teaser für das 10-Uhr-Reel: 45 Prozent der Unternehmen sehen derzeit keinen Bedarf an KI-Weiterbildung — während 56 Prozent generative KI im Arbeitsalltag nutzen. TÜV Weiterbildungsstudie 2026, Forsa, 500 Unternehmen.
"""

# ------------------------------------------------ Slot 2 (Reel A 10:00)
CAPTIONS[2] = """Deine Firma nutzt KI längst. Beibringen will sie es dir nicht: 56 Prozent nutzen, 27 Prozent schulen.

Forsa hat für den TÜV-Verband 500 Unternehmen ab 20 Mitarbeitenden befragt, und zwar die Geschäftsführung und die Weiterbildungsverantwortlichen selbst. 45 Prozent sehen derzeit keinen Bedarf an KI-Weiterbildung. 9 Prozent planen konkret etwas, 17 Prozent ermitteln gerade erst den Bedarf.

Die Lücke ist das Thema, nicht die einzelne Zahl: Benutzt wird das Werkzeug in mehr als jedem zweiten Betrieb. Beigebracht wird es in gut jedem vierten.

Am längsten wartet, wer in einem kleinen Betrieb sitzt. 21 Prozent bei 20 bis 49 Beschäftigten, 32 Prozent bei 50 bis 249, 49 Prozent ab 250. Dazu kommt das Budget: 29 Prozent geben weniger als 500 Euro pro Mitarbeitendem und Jahr aus — für Weiterbildung insgesamt, nicht für KI.

Daraus folgt nichts Dramatisches, sondern etwas Praktisches: Die Kompetenz, mit der du im Job unersetzbar wirst, wird dir mit hoher Wahrscheinlichkeit nicht angeboten. Du gibst sie dir selbst — und genau das ist der Vorsprung, weil die Kollegen auf dieselbe Schulung warten.

""" + Q_TUV + """

""" + Q_EINORDNUNG + """

""" + TAGS_A + """
"""

# ------------------------------------------------ Slot 3 (Reel B 14:00)
CAPTIONS[3] = """Öffne das am Freitagnachmittag, wenn die erste Stunde ruhig ist — dann brauchst du genau diesen Prompt.

Du weißt nicht, welche KI-Fähigkeit dir in deinem Job überhaupt etwas bringt. Deshalb fängst du gar nicht erst an.

Auf den Kurs der Firma zu warten, ist dabei statistisch keine gute Idee: 27 Prozent der Unternehmen haben überhaupt jemanden im Umgang mit KI geschult. 2024 waren es 12 Prozent — die Zahl hat sich verdoppelt und ist trotzdem die Minderheit. In Betrieben mit 20 bis 49 Beschäftigten sind es 21 Prozent.

Die Mechanik braucht deshalb keinen Kurs. Dein Lehrplan steht schon, er steht in deiner Aufgabenliste: drei Fähigkeiten, die zu den Aufgaben passen, die du ohnehin jede Woche machst.

Der Lehrplan-Prompt:

1. Das sind meine 8 wiederkehrenden Aufgaben im Job: [Liste].
2. Welche drei davon könnte KI heute übernehmen — ohne neues Werkzeug?
3. Nenne je Aufgabe die EINE Fähigkeit, die ich dafür beherrschen muss.
4. Gib mir pro Fähigkeit eine Übung von 20 Minuten, mit Beispiel zum Nachbauen.

Schritt 2 ist die Begrenzung: ohne „ohne neues Werkzeug“ bekommst du eine Tool-Liste statt eines Lehrplans. Schritt 4 macht es umsetzbar — ohne Übung bleibt die Antwort eine Sammlung von Begriffen, die du nach zwei Tagen vergessen hast.

Drei Übungen zu 20 Minuten sind eine Stunde. So lange wartet man sonst auf gar nichts.

""" + Q_TUV + """

Einordnung: Befragt wurden Unternehmen, nicht Beschäftigte. Auftraggeber ist der TÜV-Verband, dessen Mitglieder Weiterbildung verkaufen.

""" + TAGS_B + """
"""

# ------------------------------------------------ Slot 4 (Story 15:00)
CAPTIONS[4] = """Was hält dich davon ab, dir KI selbst beizubringen? 1 keine Zeit neben dem Tagesgeschäft, 2 ich weiß nicht, womit anfangen, 3 Angst, etwas falsch zu machen. Antworte mit 1, 2 oder 3.
"""

# ------------------------------------------------ Slot 5 (Story 20:00)
CAPTIONS[5] = """Der Lehrplan-Prompt als fertige Vorlage: vier Zeilen, die aus deiner Aufgabenliste drei Fähigkeiten und drei Übungen zu je 20 Minuten machen. Schreib mir LEHRPLAN als DM, dann bekommst du den vollständigen Text zum Kopieren.
"""

# ------------------------------------------------ Laengenpruefung
for _slot, _txt in CAPTIONS.items():
    if len(_txt) > 2200:
        _cut = _txt[:2200].rsplit("\n\n", 1)[0]
        print("WARNUNG Caption slot-%d gekuerzt: %d -> %d Zeichen"
              % (_slot, len(_txt), len(_cut)))
        CAPTIONS[_slot] = _cut
