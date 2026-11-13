# -*- coding: utf-8 -*-
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R
from content import REEL_A, REEL_B
from captions import CAPTIONS

DATE = "2026-11-13"
OUT  = os.environ.get("OUTROOT", ".") + "/assets/" + DATE
# Freitag, Saeule JOB-WORKFLOWS (Anpassung 2 der Auswertung 09.11.2026:
# UNERSETZBAR = Di+Sa+Mo, JOB-WORKFLOWS = nur Fr, AENGSTE = Mi+Do+So;
# Anpassung 5 der Auswertung 12.11.2026 haelt die Saeule noch zwei Messtage).
#
# Gebaut werden genau ZWEI Feed-Slots. Begruendung, alles aus OPERATIONS.md:
#   - Slot 1 (09:00 Story), Slot 4 (15:00 Story), Slot 5 (20:00 Story):
#     gestrichen nach Anpassung 2 der Auswertung 12.11.2026. Die Messung am
#     Posttag 12.11. ergab auf allen drei Slots reach 0, replies 0,
#     profile_visits 0, follows 0. Die Streichung soll ausdruecklich in den
#     Produktionslauf, nicht nur in OPERATIONS.
#   - 12:00 Karussell: gestrichen nach Anpassung 1 derselben Auswertung
#     (reach oe 3,0 gegen oe 23,8 auf dem 14:00-Slot).
#   - Slot 6 (21:00 Reel C): wird seit dem 10.11.2026 nicht gebaut
#     (Anpassung 4 der Auswertung 09.11.2026).
# Die Slot-Nummern 2 und 3 bleiben unveraendert, damit die Pfade
# assets/<DATUM>/slot-2 (10:00) und slot-3 (14:00) zu den Sheet-Zeilen und
# zur Erwartung der Post-Laeufe passen.
PLAN = {
    2: ("10:00", "Reel A", REEL_A),
    3: ("14:00", "Reel B", REEL_B),
}
made = {}
for slot in sorted(PLAN):
    time, fmt, spec = PLAN[slot]
    d = OUT + "/slot-%d" % slot
    os.makedirs(d, exist_ok=True)
    files = []
    if fmt == "Story":
        R.render(spec, d + "/story.jpg", footer=True)
        files.append("story.jpg")
    else:
        frames = []
        for i, fr in enumerate(spec, start=1):
            p = d + "/frame-%d.jpg" % i
            R.render(fr, p, footer=True, dots=(i-1, 6))
            frames.append(p); files.append("frame-%d.jpg" % i)
        R.build_reel(frames, d + "/reel.mp4", "/tmp/seg-%d" % slot)
        files.append("reel.mp4")
    with open(d + "/caption.txt", "w", encoding="utf-8") as fh:
        fh.write(CAPTIONS[slot])
    files.append("caption.txt")
    made[slot] = {"time": time, "format": fmt, "files": files}
    print("slot-%d %s %s: " % (slot, time, fmt) + ", ".join(
        "%s(%dKB)" % (f, os.path.getsize(d+"/"+f)//1024) for f in files))
with open(OUT + "/manifest.json", "w", encoding="utf-8") as fh:
    json.dump(made, fh, indent=1, ensure_ascii=False)
print("DONE", OUT)
