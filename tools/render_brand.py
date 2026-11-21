#!/usr/bin/env python3
# Renderer @ki_innovation_biz - Markenlayout, rekonstruiert aus den Frames vom 20.11.2026
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts")

AMBER = (245, 166, 35)
TEAL  = (76, 212, 200)
WHITE = (255, 255, 255)
BODY  = (206, 208, 233)
GREY  = (150, 152, 176)
FGREY = (173, 174, 192)
BOX   = (36, 38, 63)
BOXLN = (72, 74, 108)

MARGIN = 84
CW = W - 2 * MARGIN
FOOT_Y = 1778

def F(name, size):
    return ImageFont.truetype(os.path.join(FD, "Poppins-%s.ttf" % name), size)

def tw(d, txt, font, track=0.0):
    if not track:
        return d.textlength(txt, font=font)
    return sum(d.textlength(c, font=font) for c in txt) + track * max(0, len(txt) - 1)

def tracked(d, xy, txt, font, fill, track):
    x, y = xy
    for c in txt:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textlength(c, font=font) + track

def wrap(d, txt, font, maxw):
    out = []
    for para in txt.split("\n"):
        words, cur = para.split(" "), ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if d.textlength(t, font=font) <= maxw or not cur:
                cur = t
            else:
                out.append(cur); cur = w_
        out.append(cur)
    return out

def bg():
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = (y / (H - 1)) ** 0.92
        c = (int(28 + (12 - 28) * t), int(29 + (12 - 29) * t), int(50 + (22 - 50) * t))
        d.line([(0, y), (W, y)], fill=c)
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-520, -820, 760, 560], fill=46)
    glow = glow.filter(ImageFilter.GaussianBlur(220))
    lift = Image.new("RGB", (W, H), (46, 48, 78))
    return Image.composite(lift, im, glow)

def kicker(im, txt, y=None):
    d = ImageDraw.Draw(im)
    f = F("SemiBold", 27)
    y = y if y is not None else 430
    tracked(d, (MARGIN, y), txt.upper(), f, AMBER, 6.0)
    wdt = tw(d, txt.upper(), f, 6.0)
    d.rounded_rectangle([MARGIN, y + 46, MARGIN + min(wdt, 190), y + 50], radius=2, fill=AMBER)
    return y + 74

def footer(im, dot=None, dots=6):
    d = ImageDraw.Draw(im)
    fh = F("SemiBold", 27)
    fr = F("Regular", 26)
    d.text((MARGIN, FOOT_Y), "@ki_innovation_biz", font=fh, fill=(236, 237, 247))
    x = MARGIN + d.textlength("@ki_innovation_biz", font=fh) + 16
    d.text((x, FOOT_Y + 1), "·  Der 15-Minuten-Vorsprung", font=fr, fill=FGREY)
    if dot:
        cx = W - MARGIN - 8
        for i in range(dots, 0, -1):
            col = AMBER if i == dot else (62, 63, 88)
            r = 8 if i == dot else 7
            d.ellipse([cx - r, FOOT_Y + 14 - r, cx + r, FOOT_Y + 14 + r], fill=col)
            cx -= 30

def f_hook(kick, headline, dot=None, size=80):
    im = bg(); d = ImageDraw.Draw(im)
    fh = F("Bold", size)
    lines = wrap(d, headline, fh, CW)
    lh = int(size * 1.26)
    ky = 960 - (len(lines) * lh) // 2 - 110
    y = kicker(im, kick, ky) + 18
    for ln in lines:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += lh
    footer(im, dot); return im

def f_text(kick, headline, body, dot=None, size=62):
    im = bg(); d = ImageDraw.Draw(im)
    fh = F("Bold", size); fb = F("Regular", 42)
    hl = wrap(d, headline, fh, CW)
    bd = wrap(d, body, fb, CW) if body else []
    lh, lb = int(size * 1.26), 58
    total = 74 + len(hl) * lh + (30 + len(bd) * lb if bd else 0)
    y = kicker(im, kick, 920 - total // 2) + 10
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += lh
    y += 30
    for ln in bd:
        d.text((MARGIN, y), ln, font=fb, fill=BODY); y += lb
    footer(im, dot); return im

def f_stat(kick, big, claim, body, source, cta=None, dot=None, bigsize=150):
    im = bg(); d = ImageDraw.Draw(im)
    fn = F("ExtraBold", bigsize); fc = F("Bold", 42)
    fb = F("Regular", 42); fs = F("Regular", 25)
    cl = wrap(d, claim, fc, CW)
    bd = wrap(d, body, fb, CW) if body else []
    sr = wrap(d, source, fs, CW) if source else []
    nh = int(bigsize * 1.08)
    total = (74 + nh + 16 + len(cl) * 54 + (30 + len(bd) * 58 if bd else 0)
             + (26 + len(sr) * 34 if sr else 0) + (34 + 100 if cta else 0))
    y = kicker(im, kick, max(300, 930 - total // 2)) + 6
    d.text((MARGIN - 6, y - int(bigsize * 0.14)), big, font=fn, fill=TEAL)
    y += nh + 16
    for ln in cl:
        d.text((MARGIN, y), ln, font=fc, fill=WHITE); y += 54
    if bd:
        y += 30
        for ln in bd:
            d.text((MARGIN, y), ln, font=fb, fill=BODY); y += 58
    if sr:
        y += 26
        for ln in sr:
            d.text((MARGIN, y), ln, font=fs, fill=GREY); y += 34
    if cta:
        y += 34
        d.rounded_rectangle([MARGIN, y, W - MARGIN, y + 100], radius=14, fill=AMBER)
        fcta = F("Bold", 40)
        d.text(((W - d.textlength(cta, font=fcta)) / 2, y + 26), cta, font=fcta, fill=(24, 20, 10))
    footer(im, dot); return im

def f_steps(kick, steps, note, dot=None):
    im = bg(); d = ImageDraw.Draw(im)
    fnum = F("Bold", 36); fs = F("SemiBold", 37); fnote = F("Regular", 40)
    cards = [wrap(d, s, fs, CW - 150) for s in steps]
    inner = sum(len(c) * 46 for c in cards) + 22 * (len(cards) - 1) + 56
    nt = wrap(d, note, fnote, CW) if note else []
    total = 74 + inner + (34 + len(nt) * 54 if nt else 0)
    y = kicker(im, kick, max(300, 930 - total // 2)) + 8
    top = y
    d.rounded_rectangle([MARGIN, top, W - MARGIN, top + inner], radius=18,
                        fill=(29, 30, 52), outline=AMBER, width=3)
    ty = top + 28
    for i, c in enumerate(cards, 1):
        d.text((MARGIN + 30, ty - 2), str(i), font=fnum, fill=AMBER)
        for j, ln in enumerate(c):
            d.text((MARGIN + 76 + (0 if j == 0 else 26), ty), ln, font=fs, fill=WHITE)
            ty += 46
        ty += 22
    y = top + inner
    if nt:
        y += 34
        for ln in nt:
            d.text((MARGIN, y), ln, font=fnote, fill=BODY); y += 54
    footer(im, dot); return im

def f_save(kick, headline, savetext, dot=None):
    im = bg(); d = ImageDraw.Draw(im)
    fh = F("Bold", 62)
    hl = wrap(d, headline, fh, CW)
    fsv = F("Bold", 36)
    sv = wrap(d, savetext, fsv, CW - 210)
    box_h = max(104, len(sv) * 44 + 54)
    total = 74 + len(hl) * 78 + 38 + box_h + 150
    y = kicker(im, kick, max(300, 900 - total // 2)) + 10
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 78
    y += 38
    bt = y
    d.rounded_rectangle([MARGIN, bt, W - MARGIN, bt + box_h], radius=14,
                        fill=(30, 31, 54), outline=AMBER, width=3)
    ix, iy = MARGIN + 34, bt + (box_h - 76) // 2
    d.polygon([(ix, iy), (ix + 54, iy), (ix + 54, iy + 76), (ix + 27, iy + 52), (ix, iy + 76)], fill=AMBER)
    ty = bt + (box_h - len(sv) * 44) // 2
    for ln in sv:
        d.text((MARGIN + 118, ty), ln, font=fsv, fill=WHITE); ty += 44
    ay = bt + box_h + 18
    pts = [(MARGIN + 36 + i * 16, ay + int(((i / 46.0) ** 2.4) * 132)) for i in range(47)]
    d.line(pts, fill=AMBER, width=6, joint="curve")
    ex, ey = pts[-1]
    d.polygon([(ex + 16, ey + 18), (ex - 18, ey - 4), (ex + 4, ey - 22)], fill=AMBER)
    fl = F("SemiBold", 30); lbl = "Lesezeichen"
    d.text((ex - d.textlength(lbl, font=fl) / 2 - 6, ey + 36), lbl, font=fl, fill=TEAL)
    footer(im, dot); return im

def f_question(kick, headline, options, cta):
    im = bg(); d = ImageDraw.Draw(im)
    fh = F("Bold", 62); fo = F("SemiBold", 40)
    hl = wrap(d, headline, fh, CW)
    cards = [wrap(d, o, fo, CW - 150) for o in options]
    hs = [len(c) * 48 + 52 for c in cards]
    total = 74 + len(hl) * 78 + 46 + sum(hs) + 22 * (len(cards) - 1) + 40 + 100
    y = kicker(im, kick, max(300, 920 - total // 2)) + 10
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 78
    y += 46
    for i, (c, hgt) in enumerate(zip(cards, hs)):
        d.rounded_rectangle([MARGIN, y, W - MARGIN, y + hgt], radius=16, fill=BOX, outline=BOXLN, width=2)
        d.text((MARGIN + 34, y + (hgt - 48) // 2 - 2), chr(65 + i), font=F("ExtraBold", 44), fill=AMBER)
        ty = y + (hgt - len(c) * 48) // 2
        for ln in c:
            d.text((MARGIN + 110, ty), ln, font=fo, fill=WHITE); ty += 48
        y += hgt + 22
    y += 40
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + 100], radius=14, fill=AMBER)
    fc = F("Bold", 40)
    d.text(((W - d.textlength(cta, font=fc)) / 2, y + 26), cta, font=fc, fill=(24, 20, 10))
    footer(im); return im

def f_dm(kick, headline, keyword, body, cta):
    im = bg(); d = ImageDraw.Draw(im)
    fh = F("Bold", 62); fb = F("Regular", 42)
    hl = wrap(d, headline, fh, CW)
    bd = wrap(d, body, fb, CW)
    total = 74 + len(hl) * 78 + 44 + 150 + 36 + len(bd) * 58 + 40 + 100
    y = kicker(im, kick, max(300, 910 - total // 2)) + 10
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 78
    y += 44
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + 150], radius=16, fill=(30, 31, 54), outline=AMBER, width=3)
    fk = F("ExtraBold", 76)
    tracked(d, ((W - tw(d, keyword, fk, 8.0)) / 2, y + 32), keyword, fk, AMBER, 8.0)
    y += 186
    for ln in bd:
        d.text((MARGIN, y), ln, font=fb, fill=BODY); y += 58
    y += 40
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + 100], radius=14, fill=AMBER)
    fc = F("Bold", 40)
    d.text(((W - d.textlength(cta, font=fc)) / 2, y + 26), cta, font=fc, fill=(24, 20, 10))
    footer(im); return im

def f_cta(kick, headline, cta, dot=None, size=62):
    im = bg(); d = ImageDraw.Draw(im)
    fh = F("Bold", size)
    hl = wrap(d, headline, fh, CW)
    lh = int(size * 1.26)
    total = 74 + len(hl) * lh + 48 + 100
    y = kicker(im, kick, max(300, 920 - total // 2)) + 10
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += lh
    y += 48
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + 100], radius=14, fill=AMBER)
    fc = F("Bold", 40)
    d.text(((W - d.textlength(cta, font=fc)) / 2, y + 26), cta, font=fc, fill=(24, 20, 10))
    footer(im, dot); return im

def save(im, path):
    im.save(path, "JPEG", quality=88, optimize=True, progressive=True)
    return os.path.getsize(path)
