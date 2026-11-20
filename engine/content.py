# -*- coding: utf-8 -*-
# Tagesausgabe 2026-11-20 (Freitag) - Saeule: JOB-WORKFLOWS
#
# Saeulen-Zuordnung: Freitag = JOB-WORKFLOWS nach Auftragstext (Mo/Mi/Fr).
# Anmerkung: Anpassung 1 der Auswertung 16.11.2026 will Fr auf AENGSTE
# ENTKRAEFTEN legen und JOB-WORKFLOWS nur Di/Do. Gefahren wird der
# Auftragstext (Anweisung des Kontoinhabers); die Entscheidung liegt bei Max
# und steht in der HINWEIS-Zeile.
#
# Slot-Plan heute nach Auftragstext: 2 Reels + 3 Stories.
#   Offener Widerspruch, sechste Auswertung in Folge: Anpassung 3 der
#   Auswertung 16.11.2026 streicht die drei Story-Slots endgueltig
#   (6 von 6 am Posttag gemessene Slots mit reach 0) und will die
#   Kapazitaet in einen dritten Reel-Slot um 17:00 geben. Der Auftragstext
#   vom 15.11. fuehrt die Stories weiter - ihm wurde gefolgt.
#
# Thema: Nicht das Werkzeug entscheidet, sondern WO die KI sitzt. Wer sie im
#        Arbeitsschritt hat statt im Chatfenster daneben, spart nach eigenen
#        Angaben 20 % mehr Zeit pro Tag und fuehlt sich siebenmal seltener
#        ueberfordert. Daraus folgt der Workflow des Tages: aus einem
#        wiederkehrenden Handgriff eine stehende Arbeitsanweisung machen,
#        die naechste Woche noch da ist.
#
# Quelle (eine Studie, wie fuer Reel A vorgesehen):
#        Adecco Group, "Global Workforce of the Future", 7. Ausgabe 2026.
#        Vollbericht: "People-powered performance: How to unlock happiness
#        in the hybrid workforce". 40.500 Beschaeftigte, 36 Laender,
#        21 Branchen, Online-Befragung in den Landessprachen, Feldzeit
#        Juni bis Juli 2026, veroeffentlicht 19.11.2026.
#        Kernzahlen (alle Selbstauskunft):
#        - 74 % nutzen KI-Agenten bei der Arbeit (2025: 64 %)
#        - 20 % mehr Zeit pro Tag gespart, wenn die KI gut in die
#          Arbeitsablaeufe eingebettet ist, gegenueber geringer Integration
#        - siebenmal seltener das Gefuehl, mit dem Einsatz der KI-Werkzeuge
#          ueberfordert zu sein
#        - 96 % der an der Neugestaltung ihrer Arbeit Beteiligten sind
#          bereit, sich anzupassen, gegen 29 % der nicht Beteiligten
#        - 93 % der Geschulten berichten eine Produktivitaetssteigerung,
#          gegen 47 % der Ungeschulten (Basis: KI-Nutzer)
#        - Schulungsteilnahme gesunken: 77 % (2025) auf 67 % (2026)
#        - 66 % sagen, KI habe die fuer ihre Arbeit noetigen Kompetenzen
#          veraendert
#
# Gegenprobe (Pflicht, zwei unabhaengig formulierte Berichte):
#        it-boltwise.de vom 19.11.2026 bestaetigt 40.500, 36 Laender,
#        21 Branchen, 74 % / 64 %, die 20 % mehr Zeit pro Tag, "siebenmal
#        seltener", 96 % / 29 %, 92 % / 15 %, 66 %, 77 % / 67 % und
#        93 % / 47 %. spielemagazin.de vom 19.11.2026 bestaetigt 40.500,
#        36 Laender, 74 % / 64 %, "rund 20 %" mit ausdruecklichem Zusatz
#        "nach eigenen Angaben", "siebenmal seltener" und 96 % / 29 %.
#        Keine abweichende Zahl in beiden Berichten.
#
# BEWUSST NICHT VERWENDET, weil nur EINE Quelle sie nennt (stehende Regel
# des Kontos): der deutsche Teilwert "87 % der Befragten in Deutschland
# nutzen KI-Agenten" steht ausschliesslich im Zitat von Peter Blersch in
# Adeccos eigener deutscher Pressemitteilung und in deren wortgleichen
# Syndizierungen (finanznachrichten.de, boerse.de, ad-hoc-news.de, advfn) -
# kein unabhaengig formulierter Bericht fuehrt ihn. Er steht in keinem
# Frame und in keiner Caption. Dasselbe gilt fuer die Fuehrungswerte
# 19 % / 21 % / 39 %, die nur bei it-boltwise auftauchen.
#
# Gegenprobe/Einordnung (Pflicht, steht in Frame 5 von Reel A und in beiden
# Captions):
#        (1) Herausgeber ist ein Personaldienstleister, der Weiterbildung
#            und Workforce-Beratung verkauft - also genau das, was die
#            Studie empfiehlt.
#        (2) Alle Werte sind Selbstauskunft. Niemand hat nachgemessen, wie
#            viel Zeit tatsaechlich gespart wurde.
#        (3) Zusammenhang, nicht Ursache: die Gruppen bilden sich selbst.
#            Wer gut integrierte KI hat, arbeitet vielleicht ohnehin in
#            einem besser organisierten Betrieb.
#        (4) "Gut eingebettet" wird nicht definiert, und die 20 % sind ein
#            RELATIVER Aufschlag ohne genannte Basis - sie lassen sich
#            nicht in Minuten umrechnen.
#        (5) Erhebungsinstitut, Gewichtung, Fehlertoleranz und die deutsche
#            Fallzahl nennt die Mitteilung nicht.
#
# Abgrenzung zu frueheren Ausgaben (Pflicht-Pruefung):
#   - Adecco, "Global Workforce of the Future", 40.500 Befragte und der
#     Begriff KI-Agenten kommen in OPERATIONS.md nirgends vor (gepruefte
#     Volltextsuche ueber alle Auswertungen bis 26.10.2026) und in den
#     Ausgaben 01.-19.11.2026 nicht; dort liefen TU Darmstadt, Randstad,
#     TUEV/Forsa, BCG, IW Koeln, PwC, IU, Civey, IAB, YouGov/Notion,
#     Microsoft und Goldman Sachs.
#   - Abgrenzung zum 18.11. (Microsoft Work Trend Index): dort ging es um
#     die ENTSCHEIDUNG VOR DER ARBEIT, welche Aufgabe die KI uebernimmt
#     (Mensch/KI-Aufteilung, 53 % gegen 33 %). Heute geht es um den ORT:
#     ob die KI im wiederkehrenden Arbeitsschritt steckt oder in einem
#     Chatfenster daneben. Andere Quelle, andere Zahl, anderer Mechanismus.
#   - Workflow-Abgrenzung: kein Faktencheck (10.11.), kein Aufgaben-Audit
#     (11./15.11., welche Aufgaben), keine Marktwert-Saetze (12.11.), keine
#     Freigabe-Anfrage (13.11.), kein Prompt-Baustein (16.11., wie man EINEN
#     Prompt formuliert), kein Lehrplan (17.11.), keine Meeting-Vorbereitung
#     (18.11.), kein Einwand-Vorlauf (19.11.). Heute: ein wiederkehrender
#     Handgriff wird in eine STEHENDE Arbeitsanweisung mit einem festen
#     Pruefpunkt uebersetzt - nicht ein besserer Prompt, sondern ein
#     Arbeitsschritt, der naechste Woche noch da ist.

NB = " "  # geschuetztes Leerzeichen: haelt Zahl und Einheit zusammen

SRC_AD = ("Adecco Group, Global Workforce of the Future 2026 · 40.500 "
          "Beschäftigte, 36 Länder, Juni–Juli 2026")
SRC_AD2 = ("Adecco verkauft Weiterbildung · Selbstauskunft, nicht gemessen "
           "· Zusammenhang, keine Ursache")

# ---------------------------------------------------------------- Slot 1: Story 09:00
STORY_1 = [
    {"k": "kicker", "t": "FREITAG · 09 UHR"},
    {"k": "num", "t": "74" + NB + "%", "s": 195, "c": (77, 212, 200)},
    {"k": "numsub", "t": "arbeiten schon mit KI-Agenten. Letztes Jahr waren es 64.", "s": 50},
    {"k": "body", "t": "Das Werkzeug haben also fast alle. Es gibt eine zweite Zahl, und die trennt die, bei denen es etwas bringt, von allen anderen."},
    {"k": "src", "t": SRC_AD},
    {"k": "gap", "s": 12},
    {"k": "cta", "t": "Um 10 Uhr steht die zweite Zahl"},
]

# ---------------------------------------------------------------- Slot 2: Reel A 10:00
REEL_A = [
    [{"k": "kicker", "t": "FREITAG"},
     {"k": "big", "t": "Du denkst, dir fehlt bei KI noch das richtige Werkzeug.", "s": 88}],
    [{"k": "kicker", "t": "DAS HABEN ABER FAST ALLE"},
     {"k": "big", "t": "Es entscheidet nicht, welches du hast. Es entscheidet, wo es steht.", "s": 80}],
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "74" + NB + "%", "s": 180},
     {"k": "numsub", "t": "arbeiten mit KI-Agenten – ein Jahr davor waren es 64 %."},
     {"k": "body", "t": "40.500 Beschäftigte in 36 Ländern. Das Werkzeug ist damit kein Vorsprung mehr, sondern die Grundausstattung."},
     {"k": "src", "t": SRC_AD}],
    [{"k": "kicker", "t": "DIE ZAHL, DIE TRENNT"},
     {"k": "num", "t": "20" + NB + "%", "s": 155, "c": (77, 212, 200)},
     {"k": "numsub", "t": "mehr Zeit pro Tag – bei denen, deren KI im Arbeitsablauf sitzt statt daneben.", "s": 46},
     {"k": "body", "t": "Dieselbe Gruppe fühlt sich siebenmal seltener überfordert. Nicht mehr Werkzeuge. Derselbe Handgriff, nur eingebaut."},
     {"k": "src", "t": SRC_AD}],
    [{"k": "kicker", "t": "EHRLICH DAZU"},
     {"k": "big", "t": "Das rechnet ein Personaldienstleister, der Weiterbildung verkauft.", "s": 72},
     {"k": "body", "t": "Alles Selbstauskunft, nichts nachgemessen. Die 20 % sind ein Aufschlag ohne genannte Basis, „gut eingebettet“ wird nicht definiert, und wer so arbeitet, sitzt vielleicht ohnehin im besser organisierten Betrieb.", "s": 42},
     {"k": "src", "t": SRC_AD2}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Ein neues Werkzeug ändert deinen Freitag nicht. Ein eingebauter Schritt schon.", "s": 74},
     {"k": "gap", "s": 14},
     {"k": "cta", "t": "Folgen für einen Workflow pro Tag"}],
]

# ---------------------------------------------------------------- Slot 3: Reel B 14:00
REEL_B = [
    [{"k": "kicker", "t": "FREITAG · 14 UHR"},
     {"k": "big", "t": "Du tippst dieselbe Aufgabe jede Woche neu in die KI.", "s": 88}],
    [{"k": "kicker", "t": "UND MONTAG"},
     {"k": "big", "t": "fängst du wieder bei einem leeren Chatfenster an.", "s": 84}],
    [{"k": "kicker", "t": "GEMESSEN"},
     {"k": "num", "t": "20" + NB + "%", "s": 155},
     {"k": "numsub", "t": "mehr Zeit pro Tag haben die, bei denen die KI im Arbeitsablauf steckt.", "s": 48},
     {"k": "body", "t": "Nicht im Chatfenster daneben. Der Unterschied ist kein Werkzeug, sondern ein Schritt, der nächste Woche noch da ist."},
     {"k": "src", "t": SRC_AD}],
    [{"k": "kicker", "t": "DIE MECHANIK"},
     {"k": "big", "t": "Nimm den Handgriff, den du diese Woche dreimal gemacht hast.", "s": 78},
     {"k": "body", "t": "Daraus wird keine bessere Frage, sondern eine stehende Arbeitsanweisung – mit einem festen Punkt, an dem du draufschaust."}],
    [{"k": "kicker", "t": "DIE VIER ZEILEN"},
     {"k": "steps", "t": [
         "§1 Diese Aufgabe mache ich jede Woche:",
         "   [beschreiben]. So sah sie zuletzt aus:",
         "   [einfügen].",
         "§2 Mach daraus eine feste Anweisung:",
         "   was ich reingebe, was du tust,",
         "   wie das Ergebnis aussehen muss.",
         "§3 Nenne den EINEN Punkt, an dem ich",
         "   prüfen muss, bevor es rausgeht.",
         "§4 Schreib sie so, dass ich nächste",
         "   Woche nur die neuen Zahlen tausche.",
     ], "s": 31},
     {"k": "body", "t": "Zeile 3 ist der Kern: ohne festen Prüfpunkt wird aus Zeitersparnis Nachkontrolle. Zeile 4 macht daraus einen Schritt statt eines Versuchs.", "s": 34}],
    [{"k": "kicker", "t": "MEINE EINORDNUNG"},
     {"k": "big", "t": "Montag früh entscheidet sich, ob du KI benutzt oder eingebaut hast.", "s": 72},
     {"k": "gap", "s": 10},
     {"k": "save", "t": "Sicher dir das für Montag, 9 Uhr – wenn die Woche wieder bei Null anfängt", "lab": "Lesezeichen", "s": 34}],
]

# ---------------------------------------------------------------- Slot 4: Story 15:00
STORY_2 = [
    {"k": "kicker", "t": "KURZE FRAGE"},
    {"k": "big", "t": "Welcher Handgriff kommt bei dir jede Woche wieder?", "s": 80},
    {"k": "gap", "s": 18},
    {"k": "rows", "t": ["Derselbe Statusbericht",
                        "Dieselbe Art von Mail",
                        "Dieselbe Tabelle auffrischen"], "s": 40},
    {"k": "gap", "s": 10},
    {"k": "cta", "t": "Antworte mit 1, 2 oder 3"},
]

# ---------------------------------------------------------------- Slot 5: Story 20:00
STORY_3 = [
    {"k": "kicker", "t": "FREITAGABEND"},
    {"k": "big", "t": "Die Wiedervorlage als fertige Vorlage.", "s": 84},
    {"k": "body", "t": "Vier Zeilen, die aus einer wöchentlichen Aufgabe eine stehende Arbeitsanweisung machen – mit dem einen Punkt, an dem du vorher draufschaust."},
    {"k": "gap", "s": 16},
    {"k": "cta", "t": "Schreib mir VORLAGE als DM"},
]
