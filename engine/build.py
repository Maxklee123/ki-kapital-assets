# -*- coding: utf-8 -*-
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R
from content import REEL_A, REEL_B, STORY_1, STORY_2, STORY_3
from captions import CAPTIONS

DATE = "2026-11-19"
OUT  = os.environ.get("OUTROOT", ".") + "/assets/" + DATE

# Tagesplan nach Auftragstext (Fassung 15.11.2026, Auswertung 14.11.):
# 2 Reels + 3 Stories. Reel C (21:00) und Karussell (12:00) gestrichen.
# Die Story-Slots sind in OPERATIONS.md am 12.11., 16.11. UND zuvor
# gestrichen (6 von 6 am Posttag gemessenen Slots mit reach 0); der
# Auftragstext fuehrt sie weiter. Fuenfte Auswertung in Folge mit diesem
# Widerspruch - er steht im Lauf-Bericht und in der HINWEIS-Zeile,
# entschieden wird er von Max.
PLAN = {
    1: ("09:00", "Story",  STORY_1),
    2: ("10:00", "Reel A", REEL_A),
    3: ("14:00", "Reel B", REEL_B),
    4: ("15:00", "Story",  STORY_2),
    5: ("20:00", "Story",  STORY_3),
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
