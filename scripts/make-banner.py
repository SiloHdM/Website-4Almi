"""Erzeugt das Banner oben auf der Website (src/assets/banner-4almi.png).

Collage aus Ladenfotos, links das Graffiti "Chill mal Ludwigsburg",
in der Mitte das 4Almi-Logo, rechts Almi mit Sprechblase "Was geht ab?!".
Aufruf aus dem Projektordner: python3 scripts/make-banner.py
"""
import math
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

M = 'src/assets/media/'
W, H = 2400, 560
FONT_BLACK = '/usr/share/fonts/opentype/inter/InterDisplay-Black.otf'


def cover(img, w, h, focus_y=0.5):
    """Bild auf w x h zuschneiden, wie object-fit: cover."""
    img = ImageOps.exif_transpose(img).convert('RGB')
    s = max(w / img.width, h / img.height)
    img = img.resize((math.ceil(img.width * s), math.ceil(img.height * s)), Image.LANCZOS)
    x = (img.width - w) // 2
    y = int((img.height - h) * focus_y)
    return img.crop((x, y, x + w, y + h))


# 1. Hintergrund: fünf Ladenfotos nebeneinander
shots = ['laden-theke.jpeg', 'laden-snackregal.jpeg', 'laden-kasse.jpeg',
         'laden-kuehlregale-gang.jpeg', 'laden-lotto.jpeg']
bg = Image.new('RGB', (W, H))
slice_w = W // len(shots)
for i, name in enumerate(shots):
    bg.paste(cover(Image.open(M + name), slice_w, H, 0.45), (i * slice_w, 0))
bg = bg.filter(ImageFilter.GaussianBlur(1.2))
bg = ImageEnhance.Brightness(bg).enhance(0.55)
bg = ImageEnhance.Color(bg).enhance(1.15)
canvas = bg.convert('RGBA')

# Abdunkeln links (Graffiti) und rechts (Sprechblase), Mitte bleibt heller
shade = Image.new('L', (W, H))
d = ImageDraw.Draw(shade)
for x in range(W):
    t = abs(x - W / 2) / (W / 2)
    d.line([(x, 0), (x, H)], fill=int(170 * t ** 1.4))
canvas = Image.composite(Image.new('RGBA', (W, H), (0, 0, 0, 255)), canvas, shade)

# 2. Links: Graffiti freigestellt. Die Wand ist dunkel, die Farben hell: Maske aus dem hellsten Kanal
graf = Image.open(M + 'graffiti-chill-mal-ludwigsburg.jpeg').convert('RGB').crop((250, 20, 1330, 470))
graf = ImageEnhance.Color(graf).enhance(1.25)
r, g, b = graf.split()
brightest = ImageChops.lighter(ImageChops.lighter(r, g), b)
mask = brightest.point(lambda v: max(0, min(255, (v - 150) * 6)))
mask = mask.filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(0.6))
graf = graf.convert('RGBA')
graf.putalpha(mask)
gw = 780
graf = graf.resize((gw, int(graf.height * gw / graf.width)), Image.LANCZOS)
gx, gy = 30, (H - graf.height) // 2 - 25
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
glow.paste((0, 0, 0, 230), (gx + 6, gy + 10), graf.getchannel('A'))
canvas.alpha_composite(glow.filter(ImageFilter.GaussianBlur(10)))
canvas.alpha_composite(graf, (gx, gy))

# 3. Mitte: 4Almi-Logo mit Schatten
logo = Image.open('src/assets/logo-4almi.png').convert('RGBA')
lw = 900
logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
lx, ly = (W - lw) // 2, (H - logo.height) // 2
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
shadow.paste((0, 0, 0, 200), (lx + 10, ly + 16), logo.getchannel('A'))
canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))
canvas.alpha_composite(logo, (lx, ly))

# 4. Rechts: Sprechblase "WAS GEHT AB?!" als Comic-Zacke
bx, by, br = 1840, 250, 175
pts = []
for k in range(28):
    a = k / 28 * 2 * math.pi
    r = br * (1.0 if k % 2 == 0 else 0.78)
    pts.append((bx + r * math.cos(a) * 1.15, by + r * math.sin(a)))
burst = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bd = ImageDraw.Draw(burst)
bd.polygon(pts, fill=(0, 120, 180, 255), outline=(255, 255, 255, 255), width=10)
font = ImageFont.truetype(FONT_BLACK, 74)
for i, line in enumerate(['WAS', 'GEHT', 'AB?!']):
    tw = bd.textlength(line, font=font)
    bd.text((bx - tw / 2, by - 118 + i * 74), line, font=font, fill=(216, 36, 36, 255),
            stroke_width=7, stroke_fill=(255, 255, 255, 255))
burst = burst.rotate(-8, center=(bx, by), resample=Image.BICUBIC)
canvas.alpha_composite(burst)

# Almi als Karikatur ganz rechts
kari = Image.open('src/assets/almi-karikatur.png').convert('RGBA').resize((330, 330), Image.LANCZOS)
canvas.alpha_composite(kari, (W - 330 - 40, H - 330 - 50))

canvas.convert('RGB').save('src/assets/banner-4almi.png')
print('banner', canvas.size)
