# -*- coding: utf-8 -*-
import os, json, math, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
BG      = (26, 26, 46)
BG2     = (14, 14, 28)
WHITE   = (255, 255, 255)
MUTED   = (150, 152, 178)
ACCENT  = (245, 166, 35)
ACCENT2 = (77, 212, 200)
CARD    = (36, 37, 62)

FONTDIR = os.environ.get("FONTDIR", "fonts")
def _f(name, size):
    return ImageFont.truetype(os.path.join(FONTDIR, name), size)
def BOLD(s):  return _f("Poppins-Bold.ttf", s)
def MED(s):   return _f("Poppins-Medium.ttf", s)
def REG(s):   return _f("Poppins-Regular.ttf", s)

SAFE_TOP, SAFE_BOT = 230, 250
PAD = 86

def bg():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(BG[i] + (BG2[i]-BG[i]) * (t**1.4)) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    glow = Image.new("RGB", (W, H), (0,0,0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-320, -520, 760, 420], fill=(46, 44, 86))
    glow = glow.filter(ImageFilter.GaussianBlur(180))
    img = Image.composite(Image.blend(img, glow, 0.45), img, Image.new("L", (W, H), 90))
    return img

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def tracked(d, xy, text, font, fill, track):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + track

def measure(items, scale=1.0):
    dummy = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    total, blocks = 0, []
    for it in items:
        k = it["k"]
        if k == "kicker":
            f = BOLD(int(27*scale)); h = int(34*scale); gap = int(46*scale)
            blocks.append((it, f, [it["t"]], h, gap))
        elif k == "big":
            f = BOLD(int(it.get("s", 92)*scale)); lh = int(f.size*1.14)
            ls = wrap(dummy, it["t"], f, W-2*PAD)
            blocks.append((it, f, ls, lh, int(40*scale)))
        elif k == "num":
            f = BOLD(int(it.get("s", 300)*scale)); lh = int(f.size*1.0)
            blocks.append((it, f, [it["t"]], lh, int(14*scale)))
        elif k == "numsub":
            f = BOLD(int(it.get("s", 58)*scale)); lh = int(f.size*1.2)
            ls = wrap(dummy, it["t"], f, W-2*PAD)
            blocks.append((it, f, ls, lh, int(40*scale)))
        elif k == "body":
            f = MED(int(it.get("s", 50)*scale)); lh = int(f.size*1.4)
            ls = wrap(dummy, it["t"], f, W-2*PAD)
            blocks.append((it, f, ls, lh, int(34*scale)))
        elif k == "src":
            f = REG(int(26*scale)); lh = int(34*scale)
            ls = wrap(dummy, it["t"], f, W-2*PAD)
            blocks.append((it, f, ls, lh, int(30*scale)))
        elif k == "steps":
            f = MED(int(it.get("s", 41)*scale)); lh = int(f.size*1.42)
            ls = it["t"]
            blocks.append((it, f, ls, lh, int(36*scale)))
        elif k == "rows":
            f = MED(int(it.get("s", 46)*scale)); lh = int(f.size*1.9)
            blocks.append((it, f, it["t"], lh, int(34*scale)))
        elif k == "calc":
            f = BOLD(int(it.get("s", 54)*scale)); lh = int(f.size*1.55)
            blocks.append((it, f, it["t"], lh, int(36*scale)))
        elif k == "cta":
            f = BOLD(int(it.get("s", 46)*scale)); lh = int(f.size*1.3)
            ls = wrap(dummy, it["t"], f, W-2*PAD-80)
            blocks.append((it, f, ls, lh + int(46*scale), int(34*scale)))
        elif k == "gap":
            blocks.append((it, None, [], int(it.get("s", 30)*scale), 0))
    for it, f, ls, lh, gap in blocks:
        total += (lh * max(1, len(ls)) if it["k"] != "cta" else lh) + gap
    return total - (blocks[-1][4] if blocks else 0), blocks

def render(items, out, footer=True, dots=None):
    img = bg(); d = ImageDraw.Draw(img)
    scale = 1.0
    avail = H - SAFE_TOP - SAFE_BOT
    for _ in range(26):
        th, blocks = measure(items, scale)
        if th <= avail: break
        scale -= 0.035
    th, blocks = measure(items, scale)
    y = SAFE_TOP + int(max(0, (avail - th)) * 0.42)

    for it, f, ls, lh, gap in blocks:
        k = it["k"]
        if k == "gap":
            y += lh; continue
        if k == "kicker":
            tracked(d, (PAD, y), it["t"], f, it.get("c", ACCENT), int(5*scale))
            d.line([(PAD, y+lh+16), (PAD+int(96*scale), y+lh+16)], fill=it.get("c", ACCENT), width=5)
            y += lh + gap; continue
        if k == "num":
            col = it.get("c", ACCENT)
            d.text((PAD-6, y - int(f.size*0.14)), it["t"], font=f, fill=col)
            y += lh + gap; continue
        if k == "calc":
            for row in it["t"]:
                lab, val, col = row
                fl = MED(int(f.size*0.74))
                d.text((PAD, y + (f.size-fl.size)//2), lab, font=fl, fill=MUTED)
                vw = d.textlength(val, font=f)
                d.text((W-PAD-vw, y), val, font=f, fill=col if col else WHITE)
                y += lh
            y += gap; continue
        if k == "rows":
            for i, row in enumerate(it["t"]):
                bx0, by0, bx1, by1 = PAD, y, W-PAD, y+lh-int(18*scale)
                d.rounded_rectangle([bx0, by0, bx1, by1], radius=int(22*scale), fill=CARD)
                nf = BOLD(int(f.size*1.0))
                d.text((bx0+int(34*scale), by0+(by1-by0-nf.size*1.3)//2), str(i+1), font=nf, fill=ACCENT)
                d.text((bx0+int(92*scale), by0+(by1-by0-f.size*1.3)//2), row, font=f, fill=WHITE)
                y += lh
            y += gap; continue
        if k == "steps":
            box_h = lh*len(ls) + int(52*scale)
            d.rounded_rectangle([PAD-14, y-int(26*scale), W-PAD+14, y-int(26*scale)+box_h],
                                radius=int(26*scale), fill=CARD, outline=ACCENT, width=3)
            for i, line in enumerate(ls):
                if line.startswith("§"):
                    nf = BOLD(f.size)
                    d.text((PAD+int(14*scale), y), line[1], font=nf, fill=ACCENT)
                    d.text((PAD+int(56*scale), y), line[2:].strip(), font=f, fill=WHITE)
                else:
                    d.text((PAD+int(56*scale), y), line, font=f, fill=(206,208,230))
                y += lh
            y += int(26*scale) + gap; continue
        if k == "cta":
            bh = f.size*1.3*len(ls) + int(46*scale)
            d.rounded_rectangle([PAD-14, y, W-PAD+14, y+bh], radius=int(26*scale),
                                fill=it.get("bg", ACCENT))
            yy = y + int(23*scale)
            for line in ls:
                tw = d.textlength(line, font=f)
                d.text(((W-tw)//2, yy), line, font=f, fill=it.get("c", (20,20,36)))
                yy += int(f.size*1.3)
            y += bh + gap; continue
        col = {"big": WHITE, "numsub": WHITE, "body": (214,216,236), "src": MUTED}[k]
        col = it.get("c", col)
        for line in ls:
            d.text((PAD, y), line, font=f, fill=col)
            y += lh
        y += gap

    if footer:
        hf = MED(27)
        d.text((PAD, H-SAFE_BOT+98), "@ki_innovation_biz", font=hf, fill=(176,178,204))
        sx = PAD + d.textlength("@ki_innovation_biz", font=hf) + 16
        d.text((sx, H-SAFE_BOT+98), "·  Der 15-Minuten-Vorsprung", font=REG(27), fill=(104,106,134))
    if dots:
        i, n = dots
        cx = W - PAD - (n*30 - 12)
        for k2 in range(n):
            x = cx + k2*30
            r = 7
            c = ACCENT if k2 == i else (74, 76, 104)
            d.ellipse([x-r, H-SAFE_BOT+104-r, x+r, H-SAFE_BOT+104+r], fill=c)
    img.save(out, "JPEG", quality=84, optimize=True, progressive=True)
    return out

DUR = [0.7, 1.3, 3.4, 3.5, 3.5, 3.6]
FPS = 30

def ffmpeg_bin():
    import shutil
    w = shutil.which("ffmpeg")
    if w: return w
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()

def build_reel(frames, out, workdir):
    FF = ffmpeg_bin()
    os.makedirs(workdir, exist_ok=True)
    segs = []
    for i, (img, dur) in enumerate(zip(frames, DUR)):
        n = int(round(dur*FPS))
        seg = os.path.join(workdir, "seg%d.mp4" % i)
        zexpr = "1+0.075*on/%d" % max(1, n-1)
        vf = ("zoompan=z='" + zexpr + "':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              ":d=%d:s=%dx%d:fps=%d,format=yuv420p" % (n, W, H, FPS))
        cmd = [FF, "-y", "-loop", "1", "-i", img, "-vf", vf, "-frames:v", str(n),
               "-c:v", "libx264", "-preset", "medium", "-crf", "26",
               "-pix_fmt", "yuv420p", "-r", str(FPS), seg]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError("ffmpeg seg%d: %s" % (i, r.stderr[-900:]))
        segs.append(seg)
    lst = os.path.join(workdir, "list.txt")
    with open(lst, "w") as fh:
        for s in segs: fh.write("file '%s'\n" % os.path.abspath(s))
    cmd = [FF, "-y", "-f", "concat", "-safe", "0", "-i", lst,
           "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
           "-shortest", "-c:v", "libx264", "-preset", "slow", "-tune", "stillimage", "-crf", "33",
           "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "32k",
           "-movflags", "+faststart", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("ffmpeg concat: %s" % r.stderr[-900:])
    return out
