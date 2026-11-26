# -*- coding: utf-8 -*-
import os, sys, json, subprocess, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.environ.get("BRAND", HERE)
OUT = os.environ.get("OUT", os.path.join(HERE, "out"))
FFMPEG = os.environ.get("FFMPEG", "ffmpeg")

sys.path.insert(0, HERE)
os.environ["BRAND"] = BRAND
import render_v3 as R

spec = importlib.util.spec_from_file_location("content", os.path.join(HERE, "content_2026-11-26.py"))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)

MAKERS = {"hook": R.f_hook, "text": R.f_text, "number": R.f_number, "steps": R.f_steps,
          "save": R.f_save, "cta": R.f_cta, "teaser": R.f_teaser,
          "question": R.f_question, "dm": R.f_dm}

def render_all():
    man = {}
    for slot, s in sorted(C.SLOTS.items()):
        dst = os.path.join(OUT, "slot-%s" % slot)
        os.makedirs(dst, exist_ok=True)
        files = []
        if len(s["frames"]) == 1:
            kind, kw = s["frames"][0]
            im = MAKERS[kind](**kw)
            p = os.path.join(dst, "story.jpg")
            R.save(im, p); files.append("story.jpg")
            print("slot %s story.jpg %d B" % (slot, os.path.getsize(p)))
        else:
            for i, (kind, kw) in enumerate(s["frames"], 1):
                im = MAKERS[kind](**kw)
                p = os.path.join(dst, "frame-%d.jpg" % i)
                R.save(im, p); files.append("frame-%d.jpg" % i)
                print("slot %s frame-%d.jpg %d B" % (slot, i, os.path.getsize(p)))
            files.append("reel.mp4")
        open(os.path.join(dst, "caption.txt"), "w").write(s["caption"])
        files.append("caption.txt")
        man[slot] = {"time": s["time"], "format": s["format"], "files": files}
    json.dump(man, open(os.path.join(OUT, "manifest.json"), "w"), indent=1, ensure_ascii=False)
    return man

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(cmd[-1] + "\n" + r.stderr[-1500:])

def seg(src, dst, dur, zoom_from, zoom_to):
    n = max(1, int(round(dur * 30)))
    vf = ("scale=1620:2880,zoompan=z='%.5f+(%.5f)*on/%d':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          ":d=%d:s=1080x1920:fps=30,format=yuv420p" % (zoom_from, zoom_to - zoom_from, n, n))
    run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-i", src, "-vf", vf,
         "-frames:v", str(n), "-r", "30", "-c:v", "libx264", "-preset", "veryfast",
         "-crf", "26", "-pix_fmt", "yuv420p", dst])

def build_reel(slot):
    dst = os.path.join(OUT, "slot-%s" % slot)
    segs = []
    for i, dur in enumerate(C.TAKT, 1):
        s = os.path.join(dst, "seg-%d.mp4" % i)
        z0 = 1.0 + 0.012 * (i - 1)
        seg(os.path.join(dst, "frame-%d.jpg" % i), s, dur, z0, z0 + 0.055)
        segs.append(s)
    lst = os.path.join(dst, "segs.txt")
    open(lst, "w").write("".join("file '%s'\n" % s for s in segs))
    vonly = os.path.join(dst, "_v.mp4")
    run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
         "-c", "copy", vonly])
    out = os.path.join(dst, "reel.mp4")
    run([FFMPEG, "-y", "-loglevel", "error", "-i", vonly,
         "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
         "-shortest", "-c:v", "copy", "-c:a", "aac", "-b:a", "64k",
         "-movflags", "+faststart", out])
    for f in segs + [lst, vonly]:
        os.remove(f)
    return out

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    render_all()
    if "--frames-only" not in sys.argv:
        for slot in ("2", "3"):
            p = build_reel(slot)
            r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                "format=duration,size", "-of", "default=nw=1", p],
                               capture_output=True, text=True)
            print("slot %s reel.mp4 ->" % slot, r.stdout.strip().replace("\n", " "))
