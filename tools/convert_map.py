#!/usr/bin/env python3
"""Converte una mappa del gioco nel formato UNICO usato dal sito.

Procedura unica e consistente per TUTTE le immagini (manuale o via routine):
- appiattisce l'eventuale trasparenza (canale alpha) su sfondo BIANCO
  (senza questo passaggio le zone trasparenti diventano nere);
- ridimensiona a 840x1050 (LANCZOS), stesso formato delle immagini esistenti;
- salva in WebP quality 78 (~50 KB), come le altre.

Uso:
    python3 tools/convert_map.py <input: png/jpg/webp> <output.webp>
"""
import sys
from PIL import Image

W, H, QUALITY = 840, 1050, 78


def convert(src_path, dst_path):
    im = Image.open(src_path)
    # Appiattisci su bianco se c'è un canale alpha / palette con trasparenza.
    if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        rgba = im.convert("RGBA")
        bg = Image.new("RGB", rgba.size, (255, 255, 255))
        bg.paste(rgba, mask=rgba.split()[-1])  # usa l'alpha come maschera
        im = bg
    else:
        im = im.convert("RGB")
    im = im.resize((W, H), Image.LANCZOS)
    im.save(dst_path, "WEBP", quality=QUALITY, method=6)
    # Guardia: l'angolo in alto a sinistra deve essere bianco.
    corner = Image.open(dst_path).convert("RGB").getpixel((2, 2))
    print(f"OK {dst_path}  size={im.size}  corner_rgb={corner}")
    if corner != (255, 255, 255):
        print("ATTENZIONE: angolo non bianco, controllare lo sfondo.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
