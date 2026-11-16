# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-16 (Montag) - Saeule: JOB-WORKFLOWS
#
# Saeulen-Zuordnung: Montag = JOB-WORKFLOWS (Auftragstext: Mo/Mi/Fr).
# Vorbehalt aus der Auswertung 12.11.2026, Anpassung 5: JOB-WORKFLOWS lag
# dort bei oe 5,4 Reichweite gegen oe 23,8 bei AENGSTE ENTKRAEFTEN - die
# beiden JOB-WORKFLOWS-Tage waren aber genau die zwei reichweitenschwaechsten
# Tage des Fensters, ein Kalendereffekt ist nicht auszuschliessen. Die
# Auswertung verlangt ausdruecklich zwei weitere Messtage, bevor umgestellt
# wird. Heute ist einer davon.
#
# Slot-Plan heute nach Auftragstext vom 15.11.2026 (Auswertung 14.11.):
#   2 Reels + 3 Stories, Reel C (21:00) und Karussell (12:00) gestrichen.
#   ABWEICHUNG zu OPERATIONS.md: dort sind die drei Story-Slots am 12.11.
#   gestrichen (reach 0, replies 0, profile_visits 0). Der neuere
#   Auftragstext nimmt sie wieder auf - ihm wird gefolgt, der Konflikt
#   steht im Lauf-Bericht.
#   Reel B traegt den visuellen + situativen Speicher-CTA (Auftragstext
#   15.11.), der die Folgen-CTA-Frist 13.-19.11. aus der Auswertung
#   12.11.2026 ersetzt. Reel A behaelt den Folgen-CTA.
#
# Thema: Die Zeit, die KI im Buero spart, wird vom Bedienen und Nachpruefen
#        fast vollstaendig wieder aufgefressen. Netto bleiben 22 Minuten pro
#        Woche. Der Hebel ist deshalb nicht ein weiteres Tool, sondern ein
#        wiederverwendbarer Prompt-Baustein, der das Nachbessern kuerzt.
#
# Quelle: YouGov im Auftrag von Notion, Online-Befragung 9.-19.06.2026,
#         2.067 Beschaeftigte im deutschen Privatsektor in computergestuetzten
#         Positionen, davon 1.554 mit KI-Nutzung fuer die Arbeit.
#         Kernzahlen: Bruttozeitersparnis 2,17 Stunden pro Woche,
#         Aufwand fuer Nutzung und Betreuung (Prompting, Pruefen der
#         Ergebnisse) 1,81 Stunden pro Woche, Netto-Ersparnis 22 Minuten
#         pro Woche bzw. 17,2 Stunden im Jahr.
#         Weitere Werte derselben Studie: 21 % der Agenten-Nutzer sehen einen
#         hoeheren Mehrwert fuer ihr Unternehmen, unter taeglichen Nutzern
#         35 %; 59 % der taeglichen Nutzer haben ihren Verantwortungsbereich
#         erweitert; 34 % sehen bessere Karriereaussichten; 45 % sagen, die
#         taeglich benoetigten Faehigkeiten wandeln sich grundlegend;
#         22 % aller KI-Nutzer bekommen keine wirksame Schulung.
#         Gegengeprueft in zwei unabhaengigen Fachmedien:
#         digitalbusiness-magazin.de, 21.09.2026 (alle Kernzahlen woertlich
#         bestaetigt) und MIDRANGE, 15.09.2026.
#
# Gegenprobe (Pflicht, steht in Frame 5 von Reel A und in beiden Captions):
#         (1) Alle Werte sind SELBSTAUSKUNFT, nicht gemessene Arbeitszeit.
#         (2) Auftraggeber Notion verkauft selbst KI-Funktionen in einem
#             Workspace-Produkt - ein Ergebnis "Zeit geht beim Hin- und
#             Herspringen verloren" liegt im Interesse des Auftraggebers.
#         (3) Die Stichprobe deckt nur den Privatsektor in computergestuetzten
#             Positionen ab, nicht alle Beschaeftigten.
#         (4) Die Quelle sagt nicht, ob sich 2,17 h und 1,81 h auf alle 2.067
#             Befragten oder nur auf die 1.554 KI-Nutzer beziehen.
#         (5) Die Jahresangabe 17,2 Stunden ist nicht hergeleitet: 0,36 h mal
#             52 Wochen ergibt 18,7 h; 17,2 h passen zu rund 48 Arbeitswochen.
#             Deshalb steht in den Bildern die Wochenzahl, nicht die Jahreszahl.

NB = " "  # geschuetztes Leerzeichen: haelt Zahl und Einheit zusammen

SRC_NOTION = ("YouGov für Notion, 9.–19.06.2026 · 2.067 Beschäftigte, "
              "deutscher Privatsektor · Selbstauskunft")
SRC_NOTION2 = ("YouGov/Notion, Befragung Juni 2026 · brutto 2,17" + NB + "h minus "
               "1,81" + NB + "h Bedienung = netto")

# ---------------------------------------------------------------- Slot 1: Story 09:00
STORY_1 = [
    {"k": "kicker", "t": "MONTAG · 09 UHR"},
    {"k": "num", "t": "22" + NB + "Min.", "s": 205, "c": (77, 212, 200)},
    {"k": "numsub", "t": "bleiben pro Woche übrig, wenn man beide Seiten der KI-Rechnung abfragt.", "s": 52},
    {"k": "body", "t": "YouGov hat 2.067 Beschäftigte nicht nur gefragt, was KI ihnen spart — sondern auch, was das Bedienen und Prüfen kostet. Die Differenz ist die ganze Geschichte."},
    {"k": "src", "t": SRC_NOTION},
    {"k": "gap", "s": 12},
    {"k": "cta", "t": "Um 10 Uhr kommt die ganze Rechnung"},
]

# ---------------------------------------------------------------- Slot 2: Reel A 10:00
REEL_A = [
    [{"k": "kicker", "t": "MONTAG"},
     {"k": "big", "t": "Du bist sicher, dass dir KI jede Woche zwei Stunden spart.", "s": 86}],
    [{"k": "kicker", "t": "YOUGOV HAT NACHGERECHNET"},
     {"k": "big", "t": "Diesmal wurde auch die andere Seite der Rechnung abgefragt.", "s": 82}],
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "22" + NB + "Min.", "s": 178},
     {"k": "numsub", "t": "netto pro Woche – nicht pro Tag. 2.067 Beschäftigte, deutscher Privatsektor."},
     {"k": "body", "t": "2,17 Stunden spart die KI. 1,81 Stunden kostet es, sie zu bedienen und ihre Ergebnisse zu prüfen. Übrig bleiben 22 Minuten."},
     {"k": "src", "t": SRC_NOTION}],
    [{"k": "kicker", "t": "WAS DAS FÜR DICH HEISST"},
     {"k": "big", "t": "Dein Zeitgewinn ist echt. Er wird nur an der Tastatur wieder aufgebraucht.", "s": 76},
     {"k": "body", "t": "Nicht das Tool ist das Problem. Das Neuschreiben jedes Prompts und das Nachbessern jedes Ergebnisses ist es — und genau dieser Teil ist der, den du selbst in der Hand hast."}],
    [{"k": "kicker", "t": "UND DAS GEHÖRT DAZU"},
     {"k": "num", "t": "1,81" + NB + "h", "s": 158},
     {"k": "numsub", "t": "Bedienen und Prüfen pro Woche. Das ist die Stellschraube, nicht die 2,17."},
     {"k": "body", "t": "Ehrlich dazu: alles Selbstauskunft, kein gemessener Kalender. Auftraggeber der Studie ist ein Anbieter, der selbst KI verkauft. Befragt wurde nur der Privatsektor am Schreibtisch."},
     {"k": "src", "t": SRC_NOTION2}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Wer die 1,81 Stunden halbiert, gewinnt mehr als jeder Tool-Wechsel bringt.", "s": 76},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 3: Reel B 14:00
REEL_B = [
    [{"k": "kicker", "t": "MONTAG · 14 UHR"},
     {"k": "big", "t": "Du tippst jeden Prompt neu, als wäre es der erste.", "s": 88}],
    [{"k": "kicker", "t": "GENAU DAS KOSTET DIE ZEIT"},
     {"k": "big", "t": "Nicht die KI ist langsam. Das Erklären und Nachbessern ist es.", "s": 82}],
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "1,81" + NB + "h", "s": 170},
     {"k": "numsub", "t": "pro Woche gehen fürs Bedienen und Prüfen weg – von 2,17 gesparten."},
     {"k": "body", "t": "Netto bleiben 22 Minuten die Woche. Jede Minute, die du beim Erklären und Nachbessern einsparst, landet direkt in diesem Rest."},
     {"k": "src", "t": SRC_NOTION}],
    [{"k": "kicker", "t": "DIE MECHANIK"},
     {"k": "big", "t": "Einmal einen Baustein bauen statt fünfzigmal einen Prompt.", "s": 80},
     {"k": "body", "t": "Für jede Aufgabe, die du mehr als dreimal im Monat machst, schreibst du den Rahmen ein einziges Mal auf: Rolle, Kontext, Format, Prüffrage. Danach tauschst du nur noch den Inhalt."}],
    [{"k": "kicker", "t": "DER BAUSTEIN"},
     {"k": "steps", "t": [
         "§1 Du bist [Rolle]. Ziel in einem Satz:",
         "   [was am Ende rauskommen soll].",
         "§2 Kontext: Empfänger [wer], Vorwissen",
         "   [was bekannt ist], Ton [wie].",
         "§3 Format: [Form], maximal [Länge],",
         "   in dieser Reihenfolge: [1., 2., 3.].",
         "§4 Sag am Ende, was du nicht wissen",
         "   konntest und was ich prüfen muss.",
     ], "s": 33},
     {"k": "body", "t": "Schritt 4 ist der, der das Nachbessern kürzt: Du prüfst nicht mehr alles, sondern die zwei Stellen, die genannt werden.", "s": 36}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Der Baustein ist in zehn Minuten geschrieben und spart jede Woche länger.", "s": 72},
     {"k": "gap", "s": 10},
     {"k": "save", "t": "Sicher dir das für morgen, 9 Uhr", "lab": "Lesezeichen", "s": 40}],
]

# ---------------------------------------------------------------- Slot 4: Story 15:00
STORY_2 = [
    {"k": "kicker", "t": "KURZE FRAGE"},
    {"k": "big", "t": "Welcher Teil frisst bei dir die gesparte Zeit?", "s": 84},
    {"k": "gap", "s": 18},
    {"k": "rows", "t": ["Den Prompt überhaupt formulieren",
                        "Das Ergebnis Zeile für Zeile prüfen",
                        "Nachbessern, bis es rausgehen kann"], "s": 42},
    {"k": "gap", "s": 10},
    {"k": "cta", "t": "Antworte mit 1, 2 oder 3"},
]

# ---------------------------------------------------------------- Slot 5: Story 20:00
STORY_3 = [
    {"k": "kicker", "t": "MONTAGABEND"},
    {"k": "big", "t": "Der Prompt-Baustein als fertige Vorlage.", "s": 84},
    {"k": "body", "t": "Vier Zeilen, einmal ausgefüllt, für jede Aufgabe wiederverwendbar. Du bekommst den vollständigen Text zum Kopieren — heute Abend noch."},
    {"k": "gap", "s": 16},
    {"k": "cta", "t": "Schreib mir BAUSTEIN als DM"},
]
