# -*- coding: utf-8 -*-
"""
Gera os ícones das ODS 7 e 12 com o cabeçalho em português (padrão visual do ícone oficial
da ODS 9 já presente no template), a partir dos ícones oficiais em inglês da ONU
(https://sdgs.un.org/goals): o pictograma original é mantido; apenas o número e o nome são
redesenhados em português. Substitua por arquivos oficiais em PT (assets/ods_7.png / ods_12.png)
quando disponíveis — o gerador usa o que estiver nesses nomes.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialnb.ttf",     # Arial Narrow Bold
    r"C:\Windows\Fonts\bahnschrift.ttf",
    r"C:\Windows\Fonts\arialbd.ttf",
]


def load_font(size):
    for f in FONT_CANDIDATES:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


# n: (arquivo-fonte, linhas do nome em PT, y inicial do pictograma em fração da altura)
ICONS = {
    7: ("ods_7_un_en.jpg", ["ENERGIA LIMPA", "E ACESSÍVEL"], 0.33),
    12: ("ods_12_un_en.jpg", ["CONSUMO E", "PRODUÇÃO", "RESPONSÁVEIS"], 0.44),
}


def build(n):
    src, lines, cut = ICONS[n]
    im = Image.open(os.path.join(ASSETS, src)).convert("RGB")
    W, H = im.size
    S = 4  # supersampling
    bg = im.getpixel((6, 6))
    tile = Image.new("RGB", (W, H), bg)
    y0 = int(H * cut)
    tile.paste(im.crop((0, y0, W, H)), (0, y0))
    big = tile.resize((W * S, H * S), Image.LANCZOS)
    d = ImageDraw.Draw(big)
    num_font = load_font(int(0.20 * H * S))
    txt_font = load_font(int(0.092 * H * S))
    d.text((0.05 * W * S, 0.035 * H * S), str(n), font=num_font, fill="white")
    x = 0.30 * W * S
    y = 0.06 * H * S
    for ln in lines:
        d.text((x, y), ln, font=txt_font, fill="white")
        y += 0.105 * H * S
    out = big.resize((W, H), Image.LANCZOS)
    out.save(os.path.join(ASSETS, f"ods_{n}.png"))
    print("ok", n, out.size)


if __name__ == "__main__":
    for n in ICONS:
        build(n)
