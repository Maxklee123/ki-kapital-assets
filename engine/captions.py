# -*- coding: utf-8 -*-
# Captions 2026-11-22 (Sonntag) - AENGSTE ENTKRAEFTEN. DREI Hashtags je Post
# (OPERATIONS-Regel seit 25.08.2026, +24 % Reichweite). Harte Laengenpruefung
# <= 2200 Zeichen (Ausfallursache 16.11.2026, HTTP 400).
CAPTIONS = {}
TAGS_A = "#kiimjob #zukunftsangst #jobsicherheit #karriere #15minutenvorsprung"
TAGS_B = "#kiimjob #produktivitaet #arbeitsalltag #prompt #15minutenvorsprung"

Q_FED = ("Quelle: Federal Reserve Bank of Boston, Current Policy Perspectives "
         "26-8, „Workers' Perspectives on Artificial Intelligence: "
         "Productivity Gains and Job-loss Fears“, Anat Bracha, Rees Hagler "
         "und Jenny Tang, veröffentlicht am 02.09.2026. Sondermodul des "
         "Survey of Consumer Expectations der Federal Reserve Bank of New "
         "York, Wellen Dezember 2024 und Dezember 2025, rotierendes Panel "
         "von rund 1.300 US-Haushaltsvorständen.")

E_FED = ("Einordnung: US-Daten, nicht Deutschland. Alle Werte sind "
         "Selbsteinschätzung — niemand hat Produktivität nachgemessen. Die "
         "21,2, 6,1 und 6,4 Prozent sind Schätzwerte aus einer Regression "
         "mit Kontrollvariablen, keine ausgezählten Anteile. Und es ist ein "
         "Zusammenhang, keine Ursache: Wer ohnehin sicher im Job sitzt, "
         "erlebt KI vielleicht entspannter. Eine Fallzahl je Welle nennt "
         "die Studie nicht.")

CAPTIONS[1] = (
    "60 Prozent erwarten Stellenabbau durch KI — in ihrer Branche. "
    "Um den eigenen Job fürchtet gut ein Zehntel.\n\n"
    "Die Angst gilt also immer den anderen. Es gibt eine dritte Zahl, "
    "und die zeigt, wo sie wirklich sitzt.\n\n"
    "Um 10 Uhr steht sie.\n\n" + TAGS_A)

CAPTIONS[2] = (
    "Die Angst vor KI ist nicht bei denen am größten, die sie meiden.\n\n"
    "60 Prozent der Befragten erwarten KI-bedingten Stellenabbau in ihrer "
    "Branche. Um den eigenen Job fürchtet nur gut ein Zehntel. Die Sorge "
    "gilt also immer den anderen.\n\n"
    "Interessanter ist, wo sie wirklich sitzt. Die US-Notenbank Boston hat "
    "Beschäftigte mit KI-Berührung danach sortiert, ob sie sich mit KI "
    "produktiver fühlen. Bei denen in der Mitte — KI im Einsatz, Gewinn "
    "nicht spürbar — liegt die geschätzte Jobsorge bei 21,2 Prozent. Bei "
    "denen, die den Gewinn klar spüren, bei 6,1 Prozent.\n\n"
    "Die Angst sitzt also nicht am Rand, sondern in der Mitte. Nicht "
    "Abstand zur KI macht ruhig. Ein Gewinn, den du benennen kannst, macht "
    "ruhig.\n\n"
    "Und die unbequeme Hälfte der Nachricht: Nur 6 Prozent der Befragten "
    "gehören überhaupt zu der Gruppe mit den stärksten gefühlten Gewinnen. "
    "Die beruhigende Gruppe ist klein — und sie füllt sich nicht von "
    "allein.\n\n"
    "Um 14 Uhr kommen die vier Zeilen, mit denen du an einer einzigen "
    "Aufgabe misst, was KI dir wirklich bringt.\n\n"
    + Q_FED + "\n\n" + E_FED + "\n\n"
    "Folgen für einen Workflow pro Tag.\n\n" + TAGS_A)

CAPTIONS[3] = (
    "Öffne das am Montag um 9, wenn die erste Aufgabe wieder vor dir "
    "liegt — dann brauchst du genau diese vier Zeilen.\n\n"
    "Du benutzt KI jede Woche und könntest trotzdem nicht sagen, was sie "
    "dir bringt.\n\n"
    "Genau da sitzt die Unsicherheit. Unter Beschäftigten mit "
    "KI-Berührung liegt die geschätzte Jobsorge bei 21,2 Prozent, wenn sie "
    "keinen Gewinn spüren — und bei 6,1 Prozent, wenn sie ihn klar spüren. "
    "Nicht Abstand zur KI trennt die beiden Gruppen. Eine Zahl trennt sie.\n\n"
    "Die bekommst du an einem einzigen Nachmittag. Nicht schätzen, nicht "
    "sortieren: eine Aufgabe, einmal durchlaufen, mitgestoppt.\n\n"
    "Die vier Zeilen:\n\n"
    "1. Diese Aufgabe mache ich jede Woche: [beschreiben]. Ohne KI brauche "
    "ich dafür etwa [Minuten].\n"
    "2. Geh sie jetzt mit mir Schritt für Schritt durch und markiere, was "
    "am Ende noch offen bleibt.\n"
    "3. Rechne ehrlich: Welche Minuten sind weg — und welche kommen fürs "
    "Prüfen und Nacharbeiten dazu?\n"
    "4. Schreib das Ergebnis als einen Satz mit genau einer Zahl.\n\n"
    "Zeile 3 ist der Kern. Ein Gewinn, der die Prüfzeit nicht mitrechnet, "
    "ist keiner — und genau das hält die Unsicherheit am Leben. Zeile 4 "
    "macht aus einem Gefühl etwas, das du am Dienstag noch sagen kannst.\n\n"
    "Einen Satz mit einer Zahl kann dir niemand wegdiskutieren. Auch du "
    "dir selbst nicht.\n\n"
    + Q_FED + "\n\n"
    "Einordnung: US-Daten, nicht Deutschland. Selbsteinschätzung, nicht "
    "gemessen. Die Prozentwerte sind Schätzwerte aus einer Regression mit "
    "Kontrollvariablen und zeigen einen Zusammenhang, keine Ursache.\n\n"
    + TAGS_B)

CAPTIONS[4] = (
    "Wo stehst du gerade mit KI im Job?\n\n"
    "1 — Ich nutze sie und merke den Gewinn\n"
    "2 — Ich nutze sie und merke nichts\n"
    "3 — Ich nutze sie kaum\n\n"
    "Antworte mit 1, 2 oder 3. Gruppe 2 ist die größte — und die "
    "unruhigste.\n\n" + TAGS_A)

CAPTIONS[5] = (
    "Die Stoppuhr-Probe als fertige Vorlage.\n\n"
    "Vier Zeilen, mit denen du an einer einzigen Aufgabe misst, was KI dir "
    "wirklich bringt — die Prüfzeit ehrlich eingerechnet.\n\n"
    "Schreib mir STOPPUHR als DM, dann schicke ich sie dir.\n\n" + TAGS_B)

for _slot, _txt in CAPTIONS.items():
    if len(_txt) > 2200:
        _cut = _txt[:2200].rsplit("\n\n", 1)[0]
        print("WARNUNG Caption slot-%d gekuerzt: %d -> %d" % (_slot, len(_txt), len(_cut)))
        CAPTIONS[_slot] = _cut
