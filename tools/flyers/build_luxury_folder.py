#!/usr/bin/env python3
"""Build a LUXURY listing folder: the 1-of-1 black leather folder (4824-cedar-creek-dr-v2) with the grey template's
layout and tour, ivory stage, brass-gold stitching. No sign-in sheet. Unbranded (placeholder agent).

Usage: python3 tools/flyers/build_luxury_folder.py <slug> <flyer dir with home/neigh/move/pics/pics2 .jpg> \
        --street "1460 Latigo Ct" --city "Prosper, Texas" --full "1460 Latigo Ct, Prosper, TX 75078" \
        --home-line "Six bedrooms, ..." [--base 4824-cedar-creek-dr-v2]
Then: python3 tools/optimize_folder.py <slug>  (adds light copies)"""
import argparse, base64, io, json, os, re
from PIL import Image
import img2pdf

ap = argparse.ArgumentParser()
ap.add_argument('slug'); ap.add_argument('flyers')
ap.add_argument('--street', required=True); ap.add_argument('--city', required=True); ap.add_argument('--full', required=True)
ap.add_argument('--home-line', required=True)
ap.add_argument('--base', default='4824-cedar-creek-dr-v2')
a = ap.parse_args()

s = open(os.path.join(a.base, 'index.html'), encoding='utf-8').read()

def rep(old, new, count=1):
    global s
    assert old in s, 'missing: ' + old[:80]
    s = s.replace(old, new) if count == 0 else s.replace(old, new, count)

# ---- remove sign-in sheet (sharpie underline starts on its own when #so is absent)
i, j = s.index('<!--SIGNIN-START-->'), s.index('<!--SIGNIN-END-->') + len('<!--SIGNIN-END-->')
s = s[:i] + s[j:]

# ---- images
def jpg(path, w=1224, q=86):
    im = Image.open(path).convert('RGB'); im = im.resize((w, round(im.size[1] * w / im.size[0])), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True); return b.getvalue()
IMG = {k: 'data:image/jpeg;base64,' + base64.b64encode(jpg(os.path.join(a.flyers, k + '.jpg'))).decode() for k in ('neigh', 'home', 'move', 'pics', 'pics2')}
i0 = s.index('const IMG=') + len('const IMG=')
_, n = json.JSONDecoder().raw_decode(s[i0:])
s = s[:i0] + json.dumps(IMG) + s[i0 + n:]

# ---- text
rep('4824 Cedar Creek Dr - Listing Folder', a.street + ' - Listing Folder')
rep('4824 Cedar Creek Dr, McKinney, TX 75070', a.full)
rep('<b>4824 Cedar Creek Dr.</b><span>McKinney, Texas</span>', f'<b>{a.street}.</b><span>{a.city}</span>')
s = s.replace('4824 Cedar Creek Dr', a.street)
rep('Four bedrooms, three baths, 3,178 square feet and a backyard pool with a waterfall.', a.home_line)
rep('Home and neighborhood highlights on the left. The cost of owning, a move-in guide, photos, and the inspection summary on the right.',
    'Home and neighborhood highlights on the left. Move-in costs and a double-sided photo flyer on the right.')
rep("t:'Move-in guide',s:'Utility providers, trash and recycling, internet speeds and cost, and nearby services.'",
    "t:'Move-in costs',s:'What to set up before you arrive, and typical monthly costs, with providers and phone numbers.'")

# ---- scenes: home, neigh, move, pics (front), pics (flipped)
i = s.index(" {id:'cost'"); j = s.index(" {id:'done'")
s = s[:i] + (" {id:'move',focus:'move',dur:9,t:'Move-in costs',s:'What to set up before you arrive, and typical monthly costs, with providers and phone numbers.'},\n"
             " {id:'pics',focus:'pics',dur:7,t:'The home',s:'Front, foyer, dining room, great room, living room and kitchen.'},\n"
             " {id:'pics2',focus:'pics',flip:1,dur:7,t:'Outdoors and retreats',s:'The pool, primary suite and bath, theater, closet and backyard.'},\n") + s[j:]
rep("const DOTIDS=['home','neigh','cost','move','pics','disc'];", "const DOTIDS=['home','neigh','move','pics','pics2'];")
rep("const TRI_CAP={}, ALT={};", "const TRI_CAP={}, ALT={pics:{t:'Outdoors and retreats',s:'The pool, primary suite and bath, theater, closet and backyard.'}};")
rep("  cost:S('cost'), move:S('move'), disc:S('disc'), pics:S('pics'), home:S('home'), neigh:S('neigh'),", "  move:S('move'), pics:S('pics'), home:S('home'), neigh:S('neigh'),")

# ---- right pocket: Move-in costs (back) + double-sided photo flyer (front)
rep("const RT={cost:8,move:46,pics:84,disc:112};", "const RT={move:12,pics:66};")
rep("[['cost',-1.2,0],['move',.9,1],['pics',-.8,2],['disc',1.1,3]].forEach(([k,rz,i])=>paper(k,'R',k,{x:284+i*8,y:RT[k]-59,z:2+i,rz},300));",
    "[['move',-1.2,0],['pics',.9,1]].forEach(([k,rz,i])=>paper(k,'R',k,{x:284+i*8,y:RT[k]-59,z:2+i,rz},300,k==='pics'?'pics2':null));")
# paper(): optional back face
rep("function paper(id,parent,key,rest,focusX){\n  return mk(id,{parent,w:530,h:682,fw:530,fh:682,type:'paper',key,rest,",
    "function paper(id,parent,key,rest,focusX,back){\n  return mk(id,{parent,w:530,h:682,fw:530,fh:682,type:'paper',key,back,rest,")
rep("build:(s2)=>{s2.classList.add('sheet');s2.style.backgroundImage=`url(${sceneSrc(key)})`}});",
    "build:(s2)=>{s2.classList.add('sheet');\n"
    "      if(!back){s2.style.backgroundImage=`url(${sceneSrc(key)})`;return}\n"
    "      const F='position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;background-size:100% 100%;background-repeat:no-repeat;';\n"
    "      div('',s2,F+`background-image:url(${sceneSrc(key)})`); div('',s2,F+`transform:rotateY(180deg);background-image:url(${sceneSrc(back)})`);}});")
# zones
rep("  cost:{p:'R',z:44,up:110,r:[{x:0,y:RT.cost-4,w:596,h:38}]},\n  move:{p:'R',z:45,up:110,r:[{x:0,y:RT.move-4,w:596,h:38}]},\n  disc:{p:'R',z:47,up:110,r:[{x:0,y:RT.disc-4,w:596,h:496}]},\n  pics:{p:'R',z:46,up:110,r:[{x:0,y:RT.pics-4,w:596,h:32}]},",
    "  move:{p:'R',z:45,up:110,r:[{x:0,y:RT.move-4,w:596,h:58}]},\n  pics:{p:'R',z:47,up:110,r:[{x:0,y:RT.pics-4,w:596,h:470}]},")
# reader + flip button for double-sided paper
rep("(it.type==='tri'?[it.out,it.inn]:[it.key])", "(it.type==='tri'?[it.out,it.inn]:(it.back?[it.key,it.back]:[it.key]))")
rep("show('#flipB',exFocus&&sc.focus&&items[sc.focus].type==='tri');", "show('#flipB',exFocus&&sc.focus&&(items[sc.focus].type==='tri'||!!items[sc.focus].back));")
rep("a=items[cur.focus].type==='tri'?(f?ALT[cur.focus]:FOCUS_CAP[cur.focus]):null;", "a=(items[cur.focus].type==='tri'||items[cur.focus].back)?(f?ALT[cur.focus]:FOCUS_CAP[cur.focus]):null;")

# ---- luxury look: black leather, brass-gold stitching, ivory stage
LUX = """<style id="lux">
:root{--bg1:#f6f1e7;--bg2:#f1ebdd;--bg3:#e9e1cf;--haze:rgba(246,241,231,.94);--ink:#14120e;--ink2:#6a6254;
 --pill:rgba(255,252,245,.82);--pillb:rgba(20,18,14,.14);--accent:#14120e;--accent-ink:#e8cd8c;--sh:rgba(20,16,8,.34)}
#fullB{background:linear-gradient(135deg,#e2c16f 0%,#a8864a 100%)!important;color:#14120e!important;box-shadow:0 4px 12px rgba(168,134,74,.35),inset 0 1px 0 rgba(255,255,255,.35)!important}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#1b1a18 0%,#121110 55%,#0a0a09 100%)}
.cf{background:linear-gradient(155deg,#201f1c 0%,#131211 48%,#080807 100%)}
.pocket{background:linear-gradient(180deg,#232220 0%,#171615 40%,#0e0d0c 100%)}
.stitch{border-color:#c6a04f;filter:drop-shadow(0 0 1.5px rgba(198,160,79,.4));box-shadow:0 0 0 1px rgba(0,0,0,.5)}
.pocket i{border-color:#c6a04f}
.cf .addr b{color:#f6efdc}.cf .addr span{color:#c6a04f}.cf .agname{color:rgba(198,160,79,.8)}
#cap h1 .sharpie{color:#a8864a}
.bc.ag{background:linear-gradient(135deg,#17150f,#0c0b09);color:#f3ecd9;box-shadow:inset 0 0 0 1px rgba(198,160,79,.5)}
.bc.ag .bl2{color:#c6a04f}.bc.ag .bn{color:#fff}.bc.ag .br,.bc.ag .bm{color:#cfc6b0}.bc.ag .bp{color:#fff}.bc.ag .bp b{color:#c6a04f}
.bc.ag .bph{background:#1f1d18;box-shadow:0 0 0 2px rgba(198,160,79,.55)}.bc.ag .bs{background:linear-gradient(180deg,#d9b866,#8f6f36)}
#toast{background:#14120e;color:#e8cd8c}
#nudge{background:#fffcf5}
#reader img{background:#f6f1e7}
</style>
"""
rep('<div id="stage"', LUX + '<div id="stage"')

out = a.slug; os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(s)

# PDF (no lender metadata)
tmp = []
for k in ('home', 'neigh', 'move', 'pics', 'pics2'):
    f = f'/tmp/_{a.slug}_{k}.jpg'; open(f, 'wb').write(base64.b64decode(IMG[k].split(',', 1)[1])); tmp.append(f)
lay = lambda w, h, d: (612.0, 792.0, 612.0, 792.0)
open(os.path.join(out, 'folder.pdf'), 'wb').write(img2pdf.convert(tmp, layout_fun=lay, title=a.street + ' - Listing Folder'))
print('wrote', out)
