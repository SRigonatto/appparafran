import os
from PIL import Image, ImageDraw
out = 'assets'
os.makedirs(out, exist_ok=True)
BLUE = (29, 106, 208, 255)
WHITE = (255, 255, 255, 255)
N = 2048

def bubble(d, scale):
    cx, cy = N/2, N/2 - 40*scale
    w, h = 1000*scale, 720*scale
    x0, y0, x1, y1 = cx-w/2, cy-h/2, cx+w/2, cy+h/2
    d.rounded_rectangle([x0, y0, x1, y1], radius=210*scale, fill=WHITE)
    d.polygon([(x0+190*scale, y1-30*scale), (x0+170*scale, y1+250*scale), (x0+470*scale, y1-30*scale)], fill=WHITE)
    INK = (27, 42, 74, 255)
    r = 62*scale
    for k in (-1, 1):
        x = cx + k*200*scale
        d.ellipse([x-r, cy-60*scale-r, x+r, cy-60*scale+r], fill=INK)
    d.arc([cx-190*scale, cy+10*scale, cx+190*scale, cy+210*scale], start=20, end=160, fill=INK, width=int(46*scale))
    pr = 58*scale
    for k in (-1, 1):
        x = cx + k*340*scale
        d.ellipse([x-pr, cy+60*scale-pr, x+pr, cy+60*scale+pr], fill=(255, 158, 181, 255))

def save(img, name):
    img.resize((1024, 1024), Image.LANCZOS).save(f'{out}/{name}')

img = Image.new('RGBA', (N, N), BLUE); bubble(ImageDraw.Draw(img), 1.0); save(img, 'icon-only.png')
fg = Image.new('RGBA', (N, N), (0, 0, 0, 0)); bubble(ImageDraw.Draw(fg), 0.72); save(fg, 'icon-foreground.png')
bg = Image.new('RGBA', (N, N), BLUE); save(bg, 'icon-background.png')
