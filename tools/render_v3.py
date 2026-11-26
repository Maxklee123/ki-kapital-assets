# -*- coding: utf-8 -*-
# Renderer @ki_innovation_biz - Markenlayout v3, rekonstruiert aus den Frames vom 25.11.2026
# Dunkler Indigo-zu-Schwarz-Verlauf, feines Raster, Limettengruen-Akzent, Poppins + Mono.
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
BASE = os.environ.get("BRAND", os.path.dirname(os.path.abspath(__file__)))
FD = os.path.join(BASE, "fonts")

GREEN = (199, 241, 79)
WHITE = (255, 255, 255)
BODY  = (226, 227, 236)
GREY  = (138, 140, 158)
DIM   = (105, 107, 125)
CARD  = (26, 28, 38)
CARDL = (54, 57, 72)

MARGIN = 93
CW = W - 2 * MARGIN

MONO_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
]

def F(name, size):
    return ImageFont.truetype(os.path.join(FD, "Poppins-%s.ttf" % name), size)

def MONO(size):
    for p in MONO_CANDIDATES:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return F("Regular", size)

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
        cur = ""
        for w_ in para.split(" "):
            t = (cur + " " + w_).strip()
            if d.textlength(t, font=font) <= maxw or not cur:
                cur = t
            else:
                out.append(cur); cur = w_
        out.append(cur)
    return out

# ---- Rich-Text: **fett** innerhalb eines Absatzes -------------------------
def _tokens(txt):
    parts, bold = [], False
    for chunk in txt.split("**"):
        if chunk:
            parts.append((chunk, bold))
        bold = not bold
    return parts

def wrap_rich(d, txt, freg, fbold, maxw):
    """gibt Liste von Zeilen zurueck, Zeile = Liste (wort, bold)"""
    words = []
    for chunk, b in _tokens(txt):
        for i, w_ in enumerate(chunk.split(" ")):
            if w_ == "":
                continue
            words.append((w_, b))
    lines, cur, curw = [], [], 0.0
    space_r = d.textlength(" ", font=freg)
    for w_, b in words:
        wd = d.textlength(w_, font=fbold if b else freg)
        add = wd if not cur else wd + space_r
        if curw + add <= maxw or not cur:
            cur.append((w_, b)); curw += add
        else:
            lines.append(cur); cur = [(w_, b)]; curw = wd
    if cur:
        lines.append(cur)
    return lines

def draw_rich(d, xy, line, freg, fbold, fill, fill_bold=None):
    x, y = xy
    space_r = d.textlength(" ", font=freg)
    for i, (w_, b) in enumerate(line):
        if i:
            x += space_r
        f = fbold if b else freg
        d.text((x, y), w_, font=f, fill=(fill_bold or WHITE) if b else fill)
        x += d.textlength(w_, font=f)

# ---- Hintergrund ----------------------------------------------------------
def bg():
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = (y / (H - 1)) ** 0.75
        c = (int(20 + (5 - 20) * t), int(19 + (5 - 19) * t), int(42 + (9 - 42) * t))
        d.line([(0, y), (W, y)], fill=c)

    # feines Raster
    grid = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(grid)
    step = 68
    for x in range(0, W + 1, step):
        gd.line([(x, 0), (x, H)], fill=255, width=1)
    for y in range(0, H + 1, step):
        gd.line([(0, y), (W, y)], fill=255, width=1)
    fade = Image.new("L", (W, H))
    fd_ = ImageDraw.Draw(fade)
    for y in range(H):
        t = y / (H - 1)
        fd_.line([(0, y), (W, y)], fill=int(max(0, 26 * (1 - t * 1.25))))
    grid = Image.composite(fade, Image.new("L", (W, H), 0), grid)
    lines = Image.new("RGB", (W, H), (150, 150, 185))
    im = Image.composite(lines, im, grid)

    # Glows
    def glow(box, col, strength, blur):
        m = Image.new("L", (W, H), 0)
        md = ImageDraw.Draw(m)
        md.ellipse(box, fill=strength)
        m = m.filter(ImageFilter.GaussianBlur(blur))
        return Image.composite(Image.new("RGB", (W, H), col), im, m)

    im = glow([-430, -540, 640, 520], (74, 60, 150), 120, 190)   # Indigo oben links
    im = glow([560, -360, 1420, 420], (26, 54, 102), 86, 180)    # Blau oben rechts
    im = glow([430, 1430, 1340, 2120], (62, 76, 24), 70, 210)    # Gruen unten rechts
    return im

def kicker(im, txt):
    d = ImageDraw.Draw(im)
    tracked(d, (MARGIN, 88), txt.upper(), F("SemiBold", 29), GREEN, 6.5)

def footer(im, src=None, handle_left=False, arrow=False, save_hint=False):
    d = ImageDraw.Draw(im)
    fh = MONO(26)
    label = "@ki_innovation_biz"
    wd = tw(d, label, fh, 1.0)
    hx = MARGIN if handle_left else W - MARGIN - wd
    tracked(d, (hx, 1826), label, fh, (118, 120, 140), 1.0)
    if arrow:
        ax, ay = MARGIN, 1840
        d.line([(ax, ay), (ax + 34, ay)], fill=GREEN, width=5)
        d.polygon([(ax + 28, ay - 10), (ax + 44, ay), (ax + 28, ay + 10)], fill=GREEN)
    if src:
        fs = MONO(23)
        lines = wrap(d, src, fs, CW - 320)
        y = 1826 - (len(lines) - 1) * 30
        for ln in lines:
            d.text((MARGIN, y), ln, font=fs, fill=DIM)
            y += 30
    if save_hint:
        fsh = MONO(27)
        lbl = "LESEZEICHEN ANTIPPEN"
        wd2 = tw(d, lbl, fsh, 3.0)
        cx = W - MARGIN - wd2
        tracked(d, (cx, 1690), lbl, fsh, GREEN, 3.0)
        ax = cx + wd2 / 2
        d.line([(ax, 1742), (ax, 1788)], fill=GREEN, width=6)
        d.polygon([(ax - 15, 1782), (ax + 15, 1782), (ax, 1806)], fill=GREEN)

# ---- Frame-Typen ----------------------------------------------------------
def f_hook(kick, white_text, green_text, arrow=True):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    fh = F("ExtraBold", 86)
    lw = wrap(d, white_text.upper(), fh, CW)
    lg = wrap(d, green_text.upper(), fh, CW)
    lh = 98
    total = (len(lw) + len(lg)) * lh
    y = 958 - total // 2
    for ln in lw:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += lh
    for ln in lg:
        d.text((MARGIN, y), ln, font=fh, fill=GREEN); y += lh
    footer(im, arrow=arrow)
    return im

def f_text(kick, headline, body, src=None, size=66):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    fh = F("Bold", size); fb = F("Regular", 43); fbb = F("Bold", 43)
    hl = wrap(d, headline, fh, CW)
    bd = wrap_rich(d, body, fb, fbb, CW) if body else []
    lh, lb = int(size * 1.22), 58
    total = len(hl) * lh + (30 + len(bd) * lb if bd else 0)
    y = 950 - total // 2
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += lh
    if bd:
        y += 30
        for ln in bd:
            draw_rich(d, (MARGIN, y), ln, fb, fbb, BODY); y += lb
    footer(im, src)
    return im

def f_number(kick, big, caption, body, src=None):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    fn = F("ExtraBold", 190); fc = MONO(27)
    fb = F("Regular", 44); fbb = F("Bold", 44)
    bd = wrap_rich(d, body, fb, fbb, CW)
    nh = 215
    total = nh + 56 + 54 + len(bd) * 62
    y = 952 - total // 2
    d.text((MARGIN - 8, y - 42), big, font=fn, fill=GREEN)
    y += nh
    tracked(d, (MARGIN, y), caption.upper(), fc, GREY, 5.0)
    y += 56 + 24
    for ln in bd:
        draw_rich(d, (MARGIN, y), ln, fb, fbb, BODY); y += 62
    footer(im, src)
    return im

def f_steps(kick, title, steps, src=None):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    ft = F("Bold", 64); fn = MONO(28)
    fs = F("Regular", 37); fsb = F("Bold", 37)
    tl = wrap(d, title, ft, CW)
    cards = [wrap_rich(d, s, fs, fsb, CW - 190) for s in steps]
    hs = [len(c) * 50 + 56 for c in cards]
    total = len(tl) * 78 + 36 + sum(hs) + 22 * (len(cards) - 1)
    y = 958 - total // 2
    for ln in tl:
        d.text((MARGIN, y), ln, font=ft, fill=WHITE); y += 78
    y += 36
    for i, (c, hgt) in enumerate(zip(cards, hs)):
        d.rounded_rectangle([MARGIN, y, W - MARGIN, y + hgt], radius=20,
                            fill=CARD, outline=(42, 45, 58), width=2)
        tracked(d, (MARGIN + 33, y + 26), "0%d" % (i + 1), fn, GREEN, 1.5)
        ty = y + (hgt - len(c) * 50) // 2
        for ln in c:
            draw_rich(d, (MARGIN + 112, ty), ln, fs, fsb, BODY); ty += 50
        y += hgt + 22
    footer(im, src)
    return im

def f_save(kick, headline, save_title, save_sub):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    BOXBG = (20, 26, 16)
    fh = F("ExtraBold", 72)
    hl = wrap(d, headline.upper(), fh, CW)
    y = 168
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 84
    y += 46
    fst = F("Bold", 56); fss = F("Regular", 38)
    st = wrap(d, save_title, fst, CW - 170)
    ss = wrap(d, save_sub, fss, CW - 150)
    ICON_TOP, ICON_H, GAP = 58, 134, 54
    box_h = ICON_TOP + ICON_H + GAP + len(st) * 68 + 20 + len(ss) * 50 + 56
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + box_h], radius=26,
                        fill=BOXBG, outline=GREEN, width=3)
    # Lesezeichen-Icon: dicker gruener Rahmen mit V-Kerbe unten
    cx = W // 2
    x0, y0 = cx - 48, y + ICON_TOP
    x1, y1 = cx + 48, y0 + ICON_H
    sw = 13
    pts = [(x0, y0), (x1, y0), (x1, y1), (cx, y1 - 46), (x0, y1), (x0, y0)]
    d.line(pts, fill=GREEN, width=sw, joint="curve")
    ty = y1 + GAP
    for ln in st:
        d.text(((W - d.textlength(ln, font=fst)) / 2, ty), ln, font=fst, fill=WHITE); ty += 68
    ty += 20
    for ln in ss:
        d.text(((W - d.textlength(ln, font=fss)) / 2, ty), ln, font=fss, fill=BODY); ty += 50
    footer(im, handle_left=True, save_hint=True)
    return im

def f_cta(kick, statement, cta):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    fh = F("Bold", 66); fc = F("Bold", 44)
    hl = wrap(d, statement, fh, CW)
    ct = wrap(d, cta, fc, CW - 110)
    box_h = len(ct) * 58 + 72
    total = len(hl) * 80 + 52 + box_h
    y = 950 - total // 2
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 80
    y += 52
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + box_h], radius=20,
                        fill=(30, 42, 16), outline=GREEN, width=3)
    ty = y + 36
    for ln in ct:
        d.text(((W - d.textlength(ln, font=fc)) / 2, ty), ln, font=fc, fill=GREEN); ty += 58
    footer(im)
    return im

def f_teaser(kick, headline, body, src=None):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    fh = F("ExtraBold", 80); fb = F("Regular", 43); fbb = F("Bold", 43)
    hl = wrap(d, headline.upper(), fh, CW)
    bd = wrap_rich(d, body, fb, fbb, CW)
    total = len(hl) * 92 + 40 + len(bd) * 60
    y = 950 - total // 2
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 92
    y += 40
    for ln in bd:
        draw_rich(d, (MARGIN, y), ln, fb, fbb, BODY); y += 60
    footer(im, src)
    return im

def f_question(kick, headline, sub, options, badge):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    fh = F("ExtraBold", 80); fs = F("Regular", 42)
    fo = F("Regular", 42); fon = F("Bold", 42)
    hl = wrap(d, headline.upper(), fh, CW)
    sb = wrap(d, sub, fs, CW)
    opt = [wrap(d, o, fo, CW - 190) for o in options]
    box_h = sum(len(o) * 52 for o in opt) + 16 * (len(opt) - 1) + 64
    total = len(hl) * 92 + 26 + len(sb) * 56 + 46 + box_h + 36 + 70
    y = 950 - total // 2
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 92
    y += 26
    for ln in sb:
        d.text((MARGIN, y), ln, font=fs, fill=BODY); y += 56
    y += 46
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + box_h], radius=22,
                        fill=(20, 26, 16), outline=GREEN, width=3)
    ty = y + 32
    for i, o in enumerate(opt, 1):
        d.text((MARGIN + 42, ty), str(i), font=fon, fill=WHITE)
        for j, ln in enumerate(o):
            d.text((MARGIN + 90, ty), ln, font=fo, fill=BODY); ty += 52
        ty += 16
    y += box_h + 36
    fbg = MONO(25)
    bw = tw(d, badge.upper(), fbg, 3.0)
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + 70], radius=35, fill=(24, 26, 36), outline=(48, 51, 66), width=2)
    tracked(d, (MARGIN + 34, y + 21), badge.upper(), fbg, GREY, 3.0)
    footer(im)
    return im

def f_dm(kick, headline, keyword, body, cta):
    im = bg(); kicker(im, kick); d = ImageDraw.Draw(im)
    fh = F("ExtraBold", 80); fb = F("Regular", 43); fc = F("Bold", 42)
    hl = wrap(d, headline.upper(), fh, CW)
    bd = wrap(d, body, fb, CW)
    ct = wrap(d, cta, fc, CW - 110)
    kbox, cbox = 164, len(ct) * 56 + 68
    total = len(hl) * 92 + 44 + kbox + 40 + len(bd) * 60 + 44 + cbox
    y = 950 - total // 2
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 92
    y += 44
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + kbox], radius=22,
                        fill=(20, 26, 16), outline=GREEN, width=3)
    fk = F("ExtraBold", 78)
    tracked(d, ((W - tw(d, keyword, fk, 8.0)) / 2, y + 34), keyword, fk, GREEN, 8.0)
    y += kbox + 40
    for ln in bd:
        d.text((MARGIN, y), ln, font=fb, fill=BODY); y += 60
    y += 44
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + cbox], radius=20, fill=GREEN)
    ty = y + 34
    for ln in ct:
        d.text(((W - d.textlength(ln, font=fc)) / 2, ty), ln, font=fc, fill=(16, 20, 10)); ty += 56
    footer(im)
    return im

def save(im, path):
    im.save(path, "JPEG", quality=88, optimize=True, progressive=True)
    return os.path.getsize(path)
