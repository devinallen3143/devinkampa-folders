#!/usr/bin/env python3
"""Build folder.pdf (the Save button's download) from a listing folder's index.html.

Usage: python3 tools/make_pdf.py 1108-salado-dr "1108 Salado Dr - Listing Folder"
Needs: pip install img2pdf
Reads the flyer images embedded in <folder>/index.html (const IMG=...) and writes <folder>/folder.pdf,
one Letter page per flyer, in the same order as the folder.
"""
import sys, re, json, base64, tempfile, os
import img2pdf

folder = sys.argv[1]
title = sys.argv[2] if len(sys.argv) > 2 else folder
html = open(os.path.join(folder, 'index.html'), encoding='utf-8').read()
IMG = json.loads(re.search(r'const IMG=(\{.*?\});</script>', html, re.S).group(1))
ORDER = ['neigh', 'home', 'num', 'w53', 'w5', 'w20', 'proc1', 'proc2', 'high1', 'high2']

def layout(w, h, ndpi):
    pw, ph = (792.0, 612.0) if w > h else (612.0, 792.0)
    s = min(pw / w, ph / h)
    return pw, ph, w * s, h * s

tmp = tempfile.mkdtemp()
files = []
for k in [k for k in ORDER if k in IMG]:
    head, b64 = IMG[k].split(',', 1)
    f = os.path.join(tmp, k + ('.jpg' if 'jpeg' in head else '.png'))
    open(f, 'wb').write(base64.b64decode(b64))
    files.append(f)
data = img2pdf.convert(files, layout_fun=layout, title=title,
                       author='Devin Kampa, Highlands Residential Mortgage')
out = os.path.join(folder, 'folder.pdf')
open(out, 'wb').write(data)
print('wrote', out, round(len(data) / 1e6, 1), 'MB')
