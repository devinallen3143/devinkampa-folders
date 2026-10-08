#!/usr/bin/env python3
"""Add lightweight copies of the flyer/worksheet/trifold images to a folder's index.html.

Usage: python3 tools/optimize_folder.py <folder-slug>
The 3D scene uses the small copies (key + '_s'); "View full size" and folder.pdf keep the full-size images.
This keeps phones from running out of memory and reloading. Safe to re-run.
"""
import sys, re, json, base64, io, os
from PIL import Image
p = os.path.join(sys.argv[1], 'index.html')
h = open(p, encoding='utf-8').read()
m = re.search(r'const IMG=(\{.*?\});</script>', h, re.S)
IMG = json.loads(m.group(1))
for k in [k for k in IMG if k.endswith('_s')]: IMG.pop(k)
for k in ('neigh', 'home', 'num', 'w53', 'w5', 'w20', 'proc1', 'proc2', 'high1', 'high2'):
    if k not in IMG: continue
    im = Image.open(io.BytesIO(base64.b64decode(IMG[k].split(',', 1)[1]))).convert('RGB')
    W = 800 if k in ('neigh', 'home', 'num') else (640 if k in ('w53', 'w5', 'w20') else 960)
    im = im.resize((W, round(im.size[1] * W / im.size[0])), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=82, optimize=True)
    IMG[k + '_s'] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
open(p, 'w', encoding='utf-8').write(h.replace(m.group(0), 'const IMG=' + json.dumps(IMG) + ';</script>'))
print(p, 'small copies:', sorted(k for k in IMG if k.endswith('_s')))
