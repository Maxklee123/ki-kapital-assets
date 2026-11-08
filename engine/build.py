# -*- coding: utf-8 -*-
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R
from content import REEL_A, REEL_C, KARUSSELL, STORY_TEASER, STORY_ENGAGE, STORY_DM
from captions import CAPTIONS

DATE = "2026-11-08"
OUT  = os.environ.get("OUTROOT", ".") + "/assets/" + DATE
# Sonntagsplan laut Task-Prompt: 2 Reels + 1 Wochen-Karussell + 3 Stories.
PLAN = {
    1: ("09:00", "Story",     STORY_TEASER),
    2: ("10:00", "Reel A",    REEL_A),
    3: ("12:00", "Karussell", KARUSSELL),
    4: ("15:00", "Story",     STORY_ENGAGE),
    5: ("20:00", "Story",     STORY_DM),
    6: ("21:00", "Reel C",    REEL_C),
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
