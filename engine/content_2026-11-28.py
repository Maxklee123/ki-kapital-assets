# -*- coding: utf-8 -*-
# Inhalt 28.11.2026 (Samstag) - Saeule: UNERSETZBAR-FRAMING
# Kernbefund: KI-Kompetenz ist in DACH schon Befoerderungskriterium (71,5 %),
# und es gibt dafuer bereits Definitionen (84,5 %) und standardisierte
# Assessments (81,5 %) - nur hat niemand dem Angestellten das Raster gezeigt.
# Gleichzeitig sehen nur 16,5 % den Arbeitgeber in der Hauptverantwortung.
# Quelle geprueft: HiBob DACH-Whitepaper "Vom KI-Druck zur KI-Kompetenz"
# (26.05.2026, n = 200 DACH-Entscheider), gegengeprueft bei MIDRANGE
# (16.07.2026). Globale Fassung: "2026 report: AI maturity benchmarks"
# (02.06.2026, n = 1.200, Censuswide, Feldzeit 03.02.-12.03.2026) nennt fuer
# die Welt 67 % bei Befoerderung - die 71,5 % sind ausdruecklich der DACH-Wert.
# EHRLICHKEIT: Anbieterstudie (HiBob verkauft HR-Software inkl.
# KI-Kompetenz-Bewertung), n = 200, Selbstauskunft von Entscheidern, keine
# Personalsystemdaten. Steht so in src-Zeile und Caption.
# Abgrenzung zu den Vortagen: 24.11./21.11. waren PwC-Stellenanzeigen
# (Arbeitsmarkt von aussen), 22.11. die Stoppuhr-Probe (Zeitgewinn messen),
# 27.11. die Beschluss-Zeile (nach dem Meeting), 26.11. Aufgaben-Sortierer.
# Heute: KI-Output pruefen UND die Pruefung sichtbar hinterlassen.
DATE = "2026-11-28"
PILLAR = "UNERSETZBAR-FRAMING"

NB = " "  # geschuetztes Leerzeichen haelt Zahl und Einheit zusammen

SRC = ("HiBob, „Vom KI-Druck zur KI-Kompetenz“ (DACH) · 26.05.2026 · "
       "n" + NB + "=" + NB + "200 Entscheider, Selbstauskunft")
SRC2 = ("HiBob/Censuswide 2026 · DACH-Teilstichprobe n" + NB + "=" + NB + "200 · "
        "Anbieterstudie, Selbstauskunft, keine Systemdaten")

TAKT = [0.7, 1.3, 3.4, 3.5, 3.5, 3.6]

# ---------------------------------------------------------------- REEL A 10:00
REEL_A = [
    ("hook",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "white_text": "Du hältst deine KI-Nutzung für Privatsache.",
                "green_text": "Sie wird längst mitgezählt."}),
    ("text",   {"kick": "DER DENKFEHLER",
                "headline": "KI-Kompetenz ist kein Thema für die Bewerbung.",
                "body": "Sie ist ein Thema für die **Beförderung** — und zwar in deiner jetzigen Stelle.",
                "src": SRC}),
    ("number", {"kick": "DIE ZAHL",
                "big": "71,5" + NB + "%",
                "caption": "koppeln Beförderung an KI-Kompetenz",
                "body": "So viele der befragten DACH-Unternehmen verknüpfen KI-Kompetenz **ausdrücklich mit Beförderungskriterien.** Weltweit sind es 67" + NB + "%.",
                "src": SRC}),
    ("text",   {"kick": "UND JETZT DER TEIL, DER WEHTUT",
                "headline": "Es gibt dafür ein Raster. Du hast es nie gesehen.",
                "body": "**84,5" + NB + "%** sagen, sie hätten eine klare Definition starker KI-Kompetenz. **81,5" + NB + "%** haben dafür standardisierte Leitfäden oder Assessments.",
                "src": SRC}),
    ("text",   {"kick": "WER DICH DAHIN BRINGT",
                "headline": "Niemand. Nur 16,5" + NB + "% sehen den Arbeitgeber in der Pflicht.",
                "body": "Bewertet wird nach Raster. Beigebracht wird es dir **nicht.** Das ist keine Drohung — das ist der Vorsprung, der noch frei herumliegt.",
                "src": SRC2}),
    ("cta",    {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "statement": "Jeden Tag ein Workflow, der im Job sichtbar wird.",
                "cta": "FOLGEN"}),
]

# ---------------------------------------------------------------- REEL B 14:00
REEL_B = [
    ("hook",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "white_text": "Du prüfst, was die KI dir ausgibt.",
                "green_text": "Nur sieht das niemand."}),
    ("text",   {"kick": "DIE LÜCKE",
                "headline": "Bezahlt wird nicht das Prompten. Bezahlt wird das Prüfen.",
                "body": "Die Fähigkeit mit dem höchsten Aufschlag ist **nicht** „kennt die Tools“, sondern „erkennt, wann der Output falsch ist“.",
                "src": SRC}),
    ("number", {"kick": "DIE ZAHL",
                "big": "33,5" + NB + "%",
                "caption": "zahlen Aufschlag für Output-Prüfung",
                "body": "So viele DACH-Unternehmen sind bereit, für **das Bewerten und Verbessern von KI-Output** mindestens 10" + NB + "% mehr Gehalt zu zahlen — der Spitzenwert aller abgefragten Fähigkeiten.",
                "src": SRC}),
    ("text",   {"kick": "DIE MECHANIK",
                "headline": "Du prüfst schon. Es bleibt nur nichts davon übrig.",
                "body": "Die Prüfung passiert in deinem Kopf und verschwindet dort. Zwei Zeilen Notiz machen aus derselben Arbeit einen **Nachweis**.",
                "src": SRC}),
    ("steps",  {"kick": "DIE PRÜFSPUR — 4 SCHRITTE",
                "title": "Wenn der Output fast fertig aussieht",
                "steps": [
                    "Schwachstellen erfragen: **„Hier ist deine Antwort und meine Aufgabe dazu. Nenne die drei Stellen, an denen du am ehesten falsch liegst.“**",
                    "Prüfbar machen: **„Sag mir zu jeder Stelle in einem Satz, woran ich erkenne, ob sie stimmt – ohne Fachsprache.“**",
                    "Lücken offenlegen: **„Markiere, was du nicht wissen kannst, weil ich dir die Angabe nicht gegeben habe.“**",
                    "Spur hinterlassen: **„Schreib zwei Zeilen: was ich geprüft habe, was ich geändert habe.“**",
                ],
                "src": SRC}),
    ("save",   {"kick": "DER 15-MINUTEN-VORSPRUNG",
                "headline": "Du brauchst das beim nächsten Output, nicht jetzt.",
                "save_title": "Sicher dir das für die nächste KI-Antwort",
                "save_sub": "Genau dann, wenn sie schon fast fertig aussieht."}),
]

# ---------------------------------------------------------------- STORIES
STORY_1 = ("teaser", {"kick": "SAMSTAG · HEUTE UM 10 UHR",
                      "headline": "7 von 10 koppeln Beförderung an KI-Kompetenz",
                      "body": "71,5" + NB + "% der befragten DACH-Unternehmen tun das **schon jetzt.** Unangenehmer ist die zweite Zahl: 81,5" + NB + "% haben dafür ein standardisiertes Raster — und dir hat es keiner gezeigt. Um 10 Uhr steht, was drin steht.",
                      "src": SRC})

STORY_4 = ("question", {"kick": "EINE FRAGE",
                        "headline": "Weißt du, woran dein Betrieb KI-Kompetenz messen würde?",
                        "sub": "Tippe die Zahl in die DM — ich schicke dir heute Abend die Vorlage dazu.",
                        "options": ["Ja, das ist bei uns schriftlich geregelt",
                                    "Es wird geredet, aber nichts steht fest",
                                    "Keine Ahnung — und gefragt hat mich keiner"],
                        "badge": "81,5 % haben ein Raster für KI-Kompetenz"})

STORY_5 = ("dm", {"kick": "VORLAGE PER DM",
                  "headline": "Die Prüfspur",
                  "keyword": "NACHWEIS",
                  "body": "Vier Zeilen, mit denen du KI-Output prüfst — und am Ende zwei Zeilen hast, die belegen, dass du es getan hast.",
                  "cta": "SCHREIB MIR NACHWEIS"})

# ---------------------------------------------------------------- CAPTIONS
CAP_1 = """7 von 10 DACH-Unternehmen koppeln Beförderung schon heute an KI-Kompetenz.

Genau 71,5 Prozent, in einer Befragung von Entscheidern aus Deutschland, Österreich und der Schweiz.

Die unangenehmere Zahl ist die zweite: 81,5 Prozent haben dafür standardisierte Leitfäden oder Assessments. Es gibt also ein Raster — und dir hat es keiner gezeigt.

Um 10 Uhr steht im Reel, was in diesem Raster steht.

Quelle: HiBob, „Vom KI-Druck zur KI-Kompetenz“, DACH-Auswertung, veröffentlicht am 26.05.2026, n = 200 Fach- und Führungskräfte mit Beteiligung an Einstellungsentscheidungen. Selbstauskunft, Anbieterstudie.

#kiimjob #karriere #15minutenvorsprung"""

CAP_2 = """Du hältst deine KI-Nutzung für Privatsache. Dein Betrieb zählt sie längst mit.

HiBob hat 200 Entscheider aus Deutschland, Österreich und der Schweiz befragt — Leute, die an Einstellungen und an der Bewertung von KI-Kompetenz beteiligt sind. 71,5 Prozent sagen: KI-Kompetenz ist bei uns ausdrücklich mit Beförderungskriterien verknüpft. Weltweit liegt derselbe Wert bei 67 Prozent.

Das allein ist noch keine Nachricht. Die Nachricht sind die beiden Zahlen danach.

84,5 Prozent sagen, sie hätten eine klare Definition davon, was starke KI-Kompetenz ist — eine, die HR und Führungskräfte gemeinsam benutzen. 81,5 Prozent haben dafür standardisierte Leitfäden oder Assessments.

Es wird also nicht nach Gefühl bewertet, sondern nach Raster. Nur hat dieses Raster niemand an dich weitergegeben.

Und dann kommt die Zahl, die alles zusammenhält: nur 16,5 Prozent der Befragten sehen den Arbeitgeber in der Hauptverantwortung dafür, dass diese Kompetenz entsteht. Am häufigsten genannt wird die direkte Führungskraft, mit 26,5 Prozent.

Bewertet wird nach Raster. Beigebracht wird es dir nicht.

Das ist keine Drohung. Das ist ein Vorsprung, der noch frei herumliegt — weil die meisten Kollegen diese Zahlen nicht kennen.

Um 14 Uhr steht hier, welche Fähigkeit in diesem Raster am teuersten bezahlt wird. Es ist nicht die, die du erwartest.

Quelle: HiBob, „Vom KI-Druck zur KI-Kompetenz“, DACH-Auswertung, veröffentlicht am 26.05.2026, n = 200. Globale Fassung „2026 report: AI maturity benchmarks“ vom 02.06.2026, n = 1.200, Feldarbeit Censuswide, 3. Februar bis 12. März 2026. Gegengeprüft bei MIDRANGE vom 16.07.2026. Einordnung: Anbieterstudie — HiBob verkauft HR-Software samt KI-Kompetenz-Bewertung. Alles Selbstauskunft von Entscheidern, keine Personalsystemdaten, kleine Stichprobe.

#kiimjob #karriere #15minutenvorsprung"""

CAP_3 = """Öffne das beim nächsten Mal, wenn eine KI-Antwort fast fertig aussieht — da entscheidet sich, ob man deine Arbeit sieht.

Du prüfst, was die KI dir ausgibt. Nur sieht das niemand.

Die Befragung von HiBob hat Entscheidern eine unangenehm konkrete Frage gestellt: für welche KI-Fähigkeit würdet ihr mindestens zehn Prozent mehr Gehalt zahlen? Der Spitzenwert in DACH ist nicht „kennt die Tools“ und nicht „schreibt gute Prompts“. Es sind 33,5 Prozent für das Bewerten und Verbessern von Output-Qualität.

Das ist die Fähigkeit, die du schon hast. Du setzt sie jeden Tag ein, wenn du eine KI-Antwort liest und merkst, dass die dritte Zahl nicht stimmen kann.

Nur passiert diese Prüfung in deinem Kopf — und verschwindet dort. Was bewertet wird, ist aber nicht das Denken. Es ist das, was danach noch da ist.

Diese vier Zeilen kopierst du, wenn der Output fast fertig aussieht:

1. "Hier ist deine Antwort und meine Aufgabe dazu. Nenne die drei Stellen, an denen du am ehesten falsch liegst."
2. "Sag mir zu jeder Stelle in einem Satz, woran ich erkenne, ob sie stimmt – ohne Fachsprache."
3. "Markiere, was du nicht wissen kannst, weil ich dir die Angabe nicht gegeben habe."
4. "Schreib zwei Zeilen: was ich geprüft habe, was ich geändert habe."

Zeile 2 ist die, die dich besser macht. Sie verlangt ein Prüfkriterium, das du ohne Fachwissen nachvollziehen kannst — und genau daran merkst du, ob du dem Ergebnis trauen darfst.

Zeile 4 ist die, die dich sichtbar macht. Zwei Zeilen unter dem Ergebnis: geprüft wurde das, geändert wurde das. Wer deine Arbeit weiterverwendet, sieht sofort, dass da jemand nachgedacht hat.

Funktioniert in Sachbearbeitung, Projektarbeit, Marketing und HR. Überall dort, wo du KI-Output weitergibst, für den du am Ende einstehst.

Quelle: HiBob, „Vom KI-Druck zur KI-Kompetenz“, DACH-Auswertung, 26.05.2026, n = 200 Entscheider. Anbieterstudie, Selbstauskunft, kleine Stichprobe.

#kiimjob #prompt #15minutenvorsprung"""

CAP_4 = """Weißt du, woran dein Betrieb KI-Kompetenz messen würde?

1 Ja, das ist bei uns schriftlich geregelt
2 Es wird geredet, aber nichts steht fest
3 Keine Ahnung — und gefragt hat mich keiner

Tippe die Zahl in die DM — ich schicke dir heute Abend die Vorlage dazu.

81,5 Prozent der befragten DACH-Unternehmen haben standardisierte Leitfäden oder Assessments für KI-Kompetenz. Nur 16,5 Prozent sehen sich selbst in der Pflicht, sie jemandem beizubringen.

#kiimjob #karriere #15minutenvorsprung"""

CAP_5 = """Die Prüfspur als fertige Vorlage.

Vier Zeilen, mit denen du KI-Output prüfst, bevor du ihn weitergibst — und die am Ende zwei Zeilen hinterlassen, die belegen, dass du es getan hast.

Das ist die Fähigkeit, für die in DACH am ehesten ein Gehaltsaufschlag gezahlt würde: Output bewerten und verbessern, nicht Tools kennen.

Dauert keine zwei Minuten und steht danach schriftlich da.

Schreib mir NACHWEIS als DM, dann schicke ich sie dir.

#kiimjob #prompt #15minutenvorsprung"""

SLOTS = {
    "1": {"time": "09:00", "format": "Story",  "frames": [STORY_1], "caption": CAP_1},
    "2": {"time": "10:00", "format": "Reel A", "frames": REEL_A,    "caption": CAP_2},
    "3": {"time": "14:00", "format": "Reel B", "frames": REEL_B,    "caption": CAP_3},
    "4": {"time": "15:00", "format": "Story",  "frames": [STORY_4], "caption": CAP_4},
    "5": {"time": "20:00", "format": "Story",  "frames": [STORY_5], "caption": CAP_5},
}
