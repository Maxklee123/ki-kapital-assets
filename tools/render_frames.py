#!/usr/bin/env python3
# Renderer @ki_innovation_biz - Markenlayout rekonstruiert aus den Frames vom 25.10.2026
import os, json, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
REPO = "/mnt/files/brand"
FD = REPO + "/fonts"
OUT = "/home/claude/out"

GREEN = (199, 241, 79)
WHITE = (255, 255, 255)
BODY = (240, 238, 248)
GREY = (138, 132, 160)
BG_TOP = (66, 56, 117)
BG_BOT = (7, 8, 12)

MARGIN = 93
CW = W - 2 * MARGIN  # 894

def F(name, size):
    return ImageFont.truetype(f"{FD}/Poppins-{name}.ttf", size)

# Mono-Ersatz fuer Kicker/Footer: Poppins-SemiBold mit Sperrung
def tw(d, txt, font, track=0):
    if track == 0:
        return d.textlength(txt, font=font)
    return sum(d.textlength(c, font=font) for c in txt) + track * max(0, len(txt) - 1)

def draw_tracked(d, xy, txt, font, fill, track):
    x, y = xy
    for c in txt:
        d.text((x, y), c, font=font, fill=fill)
        x += d.textlength(c, font=font) + track

def wrap(d, txt, font, maxw, track=0):
    words, lines, cur = txt.split(" "), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(d, t, font, track) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

def gradient_bg():
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / (H - 1)
        t2 = t ** 1.15
        c = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t2) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return im

def photo_bg(path, zoom=1.0):
    src = Image.open(path).convert("RGB")
    sw, sh = src.size
    scale = max(W / sw, H / sh) * zoom
    nw, nh = int(sw * scale) + 1, int(sh * scale) + 1
    src = src.resize((nw, nh), Image.LANCZOS)
    src = src.crop(((nw - W) // 2, (nh - H) // 2, (nw - W) // 2 + W, (nh - H) // 2 + H))
    ov = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(ov)
    for y in range(H):
        t = y / (H - 1)
        a = 0.52 + 0.40 * (t ** 1.4)          # unten dunkler
        if t < 0.12: a = 0.62 - 0.9 * t        # oben etwas dunkler fuer den Kicker
        d.line([(0, y), (W, y)], fill=(int(255 * a),) * 3)
    dark = Image.new("RGB", (W, H), (10, 9, 20))
    return Image.composite(dark, src, ov.convert("L"))

def kicker(im, txt):
    d = ImageDraw.Draw(im)
    f = F("SemiBold", 29)
    d.rounded_rectangle([MARGIN - 3, 86, MARGIN + 4, 120], radius=3, fill=GREEN)
    draw_tracked(d, (MARGIN + 21, 88), txt.upper(), f, GREEN, 6.5)

def footer(im, source_lines, shadow=False):
    d = ImageDraw.Draw(im)
    fs = F("SemiBold", 25)
    fr = F("Regular", 24)
    col = (150, 144, 172) if not shadow else (178, 173, 196)
    draw_tracked(d, (MARGIN, 1586), "DER 15-MINUTEN-VORSPRUNG", fs, col, 5.0)
    y = 1626
    for ln in source_lines:
        d.text((MARGIN, y), ln, font=fr, fill=col)
        y += 31
    # Handle-Pille
    fh = F("SemiBold", 26)
    label = "@ki_innovation_biz"
    twd = tw(d, label, fh, 1.2)
    x1, y1 = W - MARGIN, 1818
    x0, y0 = x1 - (twd + 62), 1762
    d.rounded_rectangle([x0, y0, x1, y1], radius=28, fill=(32, 29, 52), outline=(96, 90, 124), width=2)
    draw_tracked(d, (x0 + 31, y0 + 13), label, fh, (232, 230, 242), 1.2)

def text_shadow(im, draw_fn):
    """zeichnet Text mit weichem Schatten (nur Frame 1)"""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dl = ImageDraw.Draw(layer)
    draw_fn(dl, (0, 0, 0, 190))
    layer = layer.filter(ImageFilter.GaussianBlur(14))
    im_rgba = im.convert("RGBA")
    im_rgba.alpha_composite(layer)
    d2 = ImageDraw.Draw(im_rgba)
    draw_fn(d2, None)
    return im_rgba.convert("RGB")

# ---------------- Frame-Typen ----------------

def frame_hook(photo, headline, subline, kick, src, zoom):
    im = photo_bg(photo, zoom)
    kicker(im, kick)
    fh = F("ExtraBold", 84)
    fs = F("SemiBold", 42)
    d0 = ImageDraw.Draw(im)
    lines = wrap(d0, headline.upper(), fh, CW)
    sub = wrap(d0, subline, fs, CW)
    block_h = len(lines) * 96 + 14 + len(sub) * 52
    y0 = 1000 - block_h
    def paint(d, shadow_col):
        y = y0
        for ln in lines:
            d.text((MARGIN, y), ln, font=fh, fill=shadow_col or WHITE)
            y += 96
        y += 14
        for ln in sub:
            d.text((MARGIN, y), ln, font=fs, fill=shadow_col or (226, 223, 238))
            y += 52
    im = text_shadow(im, paint)
    footer(im, src, shadow=True)
    return im

def frame_text(kick, headline, body, src, hl_size=62):
    im = gradient_bg()
    kicker(im, kick)
    d = ImageDraw.Draw(im)
    fh = F("Bold", hl_size)
    fb = F("Regular", 42)
    hl = wrap(d, headline, fh, CW)
    bd = wrap(d, body, fb, CW) if body else []
    lh, lb = int(hl_size * 1.22), 56
    total = len(hl) * lh + (24 + len(bd) * lb if bd else 0)
    y = (H - 360 - total) // 2 + 60
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += lh
    y += 24
    for ln in bd:
        d.text((MARGIN, y), ln, font=fb, fill=BODY); y += lb
    footer(im, src)
    return im

def frame_number(kick, big, caption, body, src):
    im = gradient_bg()
    kicker(im, kick)
    d = ImageDraw.Draw(im)
    fn = F("ExtraBold", 210)
    fc = F("SemiBold", 27)
    fb = F("Bold", 46)
    bd = wrap(d, body, fb, CW)
    block = 250 + 46 + len(bd) * 62
    y = (H - 360 - block) // 2 + 40
    d.text((MARGIN - 6, y), big, font=fn, fill=GREEN)
    y += 232
    draw_tracked(d, (MARGIN, y), caption.upper(), fc, GREY, 5.5)
    y += 58
    for ln in bd:
        d.text((MARGIN, y), ln, font=fb, fill=WHITE); y += 62
    footer(im, src)
    return im

def frame_steps(kick, title, steps, src):
    im = gradient_bg()
    kicker(im, kick)
    d = ImageDraw.Draw(im)
    ft = F("ExtraBold", 72)
    fn = F("SemiBold", 27)
    fs = F("SemiBold", 37)
    cards = []
    for s in steps:
        cards.append(wrap(d, s, fs, CW - 125))
    hs = [max(2, len(c)) * 50 + 44 for c in cards]
    total = 100 + sum(hs) + 24 * (len(cards) - 1)
    y = (H - 360 - total) // 2 + 30
    d.text((MARGIN, y), title, font=ft, fill=WHITE)
    y += 118
    for i, (c, hgt) in enumerate(zip(cards, hs)):
        d.rounded_rectangle([MARGIN, y, W - MARGIN, y + hgt], radius=22,
                            fill=(59, 52, 94), outline=(84, 76, 124), width=2)
        draw_tracked(d, (MARGIN + 27, y + 20), f"0{i+1}", fn, GREEN, 1.5)
        ty = y + 16 + (hgt - 44 - len(c) * 50) // 2
        for ln in c:
            d.text((MARGIN + 97, ty), ln, font=fs, fill=WHITE); ty += 50
        y += hgt + 24
    footer(im, src)
    return im

def frame_cta(kick, statement, cta, src):
    im = gradient_bg()
    kicker(im, kick)
    d = ImageDraw.Draw(im)
    fh = F("Bold", 62)
    fc = F("Bold", 44)
    hl = wrap(d, statement, fh, CW)
    ct = wrap(d, cta, fc, CW - 100)
    box_h = len(ct) * 56 + 68
    total = len(hl) * 76 + 46 + box_h
    y = (H - 360 - total) // 2 + 40
    for ln in hl:
        d.text((MARGIN, y), ln, font=fh, fill=WHITE); y += 76
    y += 46
    d.rounded_rectangle([MARGIN, y, W - MARGIN, y + box_h], radius=18,
                        fill=(37, 52, 22), outline=GREEN, width=3)
    ty = y + 34
    for ln in ct:
        d.text((MARGIN + 48, ty), ln, font=fc, fill=GREEN); ty += 56
    footer(im, src)
    return im

# ---------------- Build ----------------

def build(slot, spec):
    dst = f"{OUT}/slot-{slot}"
    os.makedirs(dst, exist_ok=True)
    src = spec["source"]
    frames = []
    frames.append(frame_hook(spec["photo"], spec["f1"][0], spec["f1"][1], spec["f1"][2], src, spec.get("zoom", 1.0)))
    frames.append(frame_text(spec["f2"][0], spec["f2"][1], spec["f2"][2], src))
    frames.append(frame_number(spec["f3"][0], spec["f3"][1], spec["f3"][2], spec["f3"][3], src))
    frames.append(frame_text(spec["f4"][0], spec["f4"][1], spec["f4"][2], src))
    frames.append(frame_steps(spec["f5"][0], spec["f5"][1], spec["f5"][2], src) if spec["f5"][0] == "VIER SCHRITTE"
                  else frame_number(spec["f5"][0], spec["f5"][1], spec["f5"][2], spec["f5"][3], src))
    frames.append(frame_cta(spec["f6"][0], spec["f6"][1], spec["f6"][2], src))
    for i, fr in enumerate(frames, 1):
        p = f"{dst}/frame-{i}.jpg"
        fr.save(p, "JPEG", quality=88, optimize=True, progressive=True)
        print("  ", p, os.path.getsize(p))
    open(f"{dst}/caption.txt", "w").write(spec["caption"])
    print("  ", f"{dst}/caption.txt", os.path.getsize(f"{dst}/caption.txt"))

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    os.makedirs(OUT, exist_ok=True)
    for slot in ("1", "2"):
        print("slot", slot)
        build(slot, spec[slot])
