# -*- coding: utf-8 -*-
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R
from content import REEL_A, REEL_B, KARUSSELL, STORY_DM
from captions import CAPTIONS

DATE = "2026-11-06"
OUT  = os.environ.get("OUTROOT", ".") + "/assets/" + DATE
# Slotplan nach OPERATIONS (Auswertung 05.11.2026, Anpassung 1 + Entscheidung 02.11.2026):
#   21:00 Reel C gestrichen (Ursache D), 09:00- und 15:00-Story gestrichen,
#   12:00-Karussell an Mi/Fr/So wieder produziert.
PLAN = {
    1: ("10:00", "Reel A",    REEL_A),
    2: ("12:00", "Karussell", KARUSSELL),
    3: ("14:00", "Reel B",    REEL_B),
    4: ("20:00", "Story",     STORY_DM),
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
    elif fmt == "Karussell":
        R.W, R.H = 1080, 1350
        R.SAFE_TOP, R.SAFE_BOT = 165, 180
        try:
            for i, sl in enumerate(spec, start=1):
                R.render(sl, d + "/slide-%d.jpg" % i, footer=True, dots=(i-1, len(spec)))
                files.append("slide-%d.jpg" % i)
        finally:
            R.W, R.H = 1080, 1920
            R.SAFE_TOP, R.SAFE_BOT = 230, 250
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
