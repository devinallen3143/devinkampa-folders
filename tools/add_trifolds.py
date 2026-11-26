#!/usr/bin/env python3
"""Add the two homebuyer trifolds (Mortgage Basics left, At-Home Calculations right) to the right pocket of an
Azure-style folder, with the real fold/unfold motion. Usage: python3 tools/add_trifolds.py <slug> <img dir with basics-1/2.jpg calc-1/2.jpg>
Page 1 of each PDF = outside, page 2 = inside (standard imposition)."""
import sys, os, re, json, base64, io
from PIL import Image
slug, imgdir = sys.argv[1], sys.argv[2]
p = os.path.join(slug, 'index.html'); s = open(p, encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
def enc(path, w):
    im = Image.open(path).convert('RGB')
    if w != im.size[0]: im = im.resize((w, round(im.size[1] * w / im.size[0])), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=85 if w > 1000 else 80, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
m = re.search(r'const IMG=(\{.*?\});</script>', s, re.S); IMG = json.loads(m.group(1))
for k, f in (('basics1', 'basics-1.jpg'), ('basics2', 'basics-2.jpg'), ('calc1', 'calc-1.jpg'), ('calc2', 'calc-2.jpg')):
    full = os.path.join(imgdir, f); IMG[k] = enc(full, 1857); IMG[k + '_s'] = enc(full, 960)
s = s.replace(m.group(0), 'const IMG=' + json.dumps(IMG) + ';</script>')
# items in the right pocket: two trifold stacks in front of the papers, as in the grey template
rep("agentCard('cardR','R',300,2);", "tri('triA','R','basics1','basics2',160,113.5);\ntri('triB','R','calc1','calc2',440,113.5);\nagentCard('cardR','R',300,2);")
# hit zones: the Numbers sheet now peeks above the trifolds only
rep("num:{p:'R',z:47,up:110,r:[{x:0,y:RT.num-4,w:596,h:470}]},",
    "num:{p:'R',z:47,up:110,r:[{x:0,y:RT.num-4,w:596,h:250-(RT.num-4)}]},\n  triA:{p:'R',z:50,up:110,r:[{x:47,y:250,w:226,h:278}]},\n  triB:{p:'R',z:50,up:110,r:[{x:327,y:250,w:226,h:278}]},")
# tour scenes: the trifolds unfold (no closed:true), right after the left-hand flyers
rep(" {id:'num',focus:'num'",
    " {id:'triA',focus:'triA',flip:0,dur:9,t:'Mortgage basics, made simple',s:'How a mortgage works, what sets your rate, and five moves toward your best deal.'},\n"
    " {id:'triB',focus:'triB',flip:0,dur:9,t:'The 3-legged mortgage stool',s:'Credit, income and assets: the three essentials to qualify, and how to check each one from home.'},\n"
    " {id:'num',focus:'num'")
rep("The numbers and move-in costs on the right.", "The numbers, move-in costs and two homebuyer guides on the right.")
rep("const DOTIDS=['home','neigh','num','move'];", "const DOTIDS=['home','neigh','triA','triB','num','move'];")
rep("const TRI_CAP={}, ALT={};",
    "const TRI_CAP={triA:{t:'Mortgage basics, made simple',s:'How a mortgage works, what sets your rate, and five moves toward your best deal.'},triB:{t:'The 3-legged mortgage stool',s:'Credit, income and assets: the three essentials to qualify, and how to check each one from home.'}};\n"
    "const ALT={triA:{t:'A homebuyer\\u2019s guide',s:'The cover, plus what a mortgage is and how to choose a lender.'},triB:{t:'Why three legs?',s:'The cover, the three-legs overview, and a place to jot down your numbers.'}};")
rep("move:S('move'), num:S('num'),", "move:S('move'), num:S('num'), triA:TRI_CAP.triA, triB:TRI_CAP.triB,")
open(p, 'w', encoding='utf-8').write(s); print('ok', p, len(s) // 1024, 'KB')
