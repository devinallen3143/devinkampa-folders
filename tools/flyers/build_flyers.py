#!/usr/bin/env python3
"""Build the three listing flyers (Home, Neighborhood, The Numbers) from a listing JSON.

Usage:
  python3 tools/flyers/build_flyers.py tools/flyers/listings/<slug>.json --assets <dir with listing photos> --out <output dir>

Writes <out>/home.jpg, neigh.jpg, nums.jpg (1224x1584 JPEG, the sizes the folder expects) and, if the listing
has worksheets listed under "worksheets" (PDF paths), <out>/w53.jpg / w5.jpg / w20.jpg (clean, NO sticker).
Needs: playwright (+ chromium), pillow, node/npm (fonts are fetched once into ~/.cache/listing-flyers), pdftoppm.
The map uses OpenStreetMap tiles (tile.openstreetmap.org); Nominatim/Overpass/Google are not reachable from the sandbox.
See tools/flyers/README.md for the JSON fields and rules (blank agent, sticker only on The Numbers).
"""
import argparse, base64, json, math, os, subprocess, sys, urllib.request
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.expanduser('~/.cache/listing-flyers')

# ---------- fonts ----------
def ensure_fonts():
    base = os.path.join(CACHE, 'node_modules/@fontsource')
    if not os.path.isdir(base):
        os.makedirs(CACHE, exist_ok=True)
        subprocess.run(['npm', 'init', '-y'], cwd=CACHE, capture_output=True)
        subprocess.run(['npm', 'i', '@fontsource/cormorant-garamond', '@fontsource/montserrat'], cwd=CACHE, check=True, capture_output=True)
    return base

def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()

def fonts_css():
    F = ensure_fonts()
    def f(fam, wt, path):
        return f"@font-face{{font-family:'{fam}';font-weight:{wt};font-style:normal;src:url(data:font/woff2;base64,{b64(os.path.join(F, path))}) format('woff2')}}"
    cg = 'cormorant-garamond/files/cormorant-garamond-latin-%d-normal.woff2'
    mo = 'montserrat/files/montserrat-latin-%d-normal.woff2'
    return '\n'.join([f('Cormorant', w, cg % w) for w in (500, 600, 700)] + [f('Montserrat', w, mo % w) for w in (400, 500, 600, 700, 800)])

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1224px;height:1584px;background:#fff;color:#14181D;font-family:Montserrat,sans-serif;overflow:hidden}
.pg{position:relative;width:1224px;height:1584px;overflow:hidden;background:#fff}
.ph{position:absolute;background-size:cover;background-repeat:no-repeat}
.tbox{position:absolute;left:72px;background:#E6EBF0;display:flex;align-items:center}
.tbox h1{font-family:Cormorant,serif;font-weight:600;font-size:92px;line-height:1;white-space:nowrap}
.addr{position:absolute;left:72px;width:660px;text-align:center;font-weight:500;font-size:21px;letter-spacing:1.6px}
.sub{position:absolute;left:72px;width:660px;text-align:center;font-size:18px;color:#5a6370;letter-spacing:.3px}
.lab{font-family:Cormorant,serif;font-weight:700;font-size:23px;letter-spacing:5.5px;text-transform:uppercase}
.foot{position:absolute;left:72px;right:72px;height:170px}
.fb{position:absolute;top:0;height:140px}
.av{position:absolute;left:0;top:0;width:132px;height:132px;border-radius:50%;background-size:cover;background-position:center;background-color:#E6EBF0}
.ft{position:absolute;left:153px;top:-2px;white-space:nowrap}
.nm{font-family:Cormorant,serif;font-weight:600;font-size:35px;line-height:40px}
.fl{font-size:19px;line-height:25px;color:#5a6370}.fl.b{color:#14181D;font-weight:600}.fl.d{color:#14181D}
.div{position:absolute;left:540px;top:0;width:1px;height:166px;background:#cfd6de}
"""

class Ctx:
    def __init__(self, cfg, assets):
        self.cfg, self.assets = cfg, assets
    def img(self, name, base=None):
        p = name if os.path.isabs(name) else os.path.join(base or self.assets, name)
        ext = p.rsplit('.', 1)[1].lower()
        return f"data:image/{'jpeg' if ext in ('jpg','jpeg') else ext};base64," + b64(p)
    def lib(self, name): return self.img(os.path.join(HERE, 'assets', name), HERE)

AGENT_BLANK = dict(name='Your Name Here', title='Real Estate Agent', brokerage='Your Brokerage',
                   phone='(555) 555-5555', email='your.name@example.com', license='License #12345', photo=None)

def footer(cx, top):
    a = dict(AGENT_BLANK); a.update(cx.cfg.get('agent') or {})  # RULE: no business card uploaded => blank agent
    line1 = a.get('line1') or f"{a['title']} · {a['brokerage']}"
    photo = f"background-image:url({cx.img(a['photo'])})" if a.get('photo') else ''
    # agent.logo (brokerage logo cropped from the uploaded card): shown under the contact lines like Devin's logo; with no agent photo the circle is dropped and the text starts at the left edge
    logo = f'<img src="{cx.img(a["logo"])}" style="height:44px;margin-top:8px;display:block">' if a.get('logo') else ''
    av = f'<div class="av" style="{photo}"></div>' if (a.get('photo') or not a.get('logo')) else ''
    ftl = '' if av else ' style="left:0"'
    agent = f'<div class="fb" style="left:0">{av}<div class="ft"{ftl}><div class="nm">{a["name"]}</div><div class="fl">{line1}</div><div class="fl b">{a["phone"]}</div><div class="fl">{a["email"]}</div>{logo}</div></div>'
    dev = f'<div class="fb" style="left:578px"><div class="av" style="background-image:url({cx.lib("cardphoto.jpg")});background-color:#eef1f4"></div><div class="ft"><div class="nm">Devin Kampa</div><div class="fl">Loan Officer · NMLS #2532480</div><div class="fl b">320-241-5823</div><div class="fl d">dkampa@highlandsmortgage.com</div><img src="{cx.lib("logo.png")}" style="width:152px;margin-top:8px;display:block"></div></div>'
    return f'<div class="foot" style="top:{top}px">{agent}<div class="div"></div>{dev}</div>'

def page(body): return f'<!doctype html><html><head><meta charset="utf-8"><style>{fonts_css()}{BASE_CSS}</style></head><body><div class="pg">{body}</div></body></html>'

def photo(cx, key, l, t, w, h, pos='50% 50%'):
    return f'<div class="ph" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;background-image:url({cx.img(cx.cfg["photos"][key])});background-position:{pos}"></div>'

# ---------- sticker (bright red oval starburst; The Numbers ONLY) ----------
def stamp(w=270, rot=-8, lines=('SELLER PAYS', 'CLOSING COSTS')):
    n = 24; cx_, cy_ = 150, 80; rxo, ryo, rxi, ryi = 146, 76, 128, 60; pts = []
    for k in range(n * 2):
        a = math.pi * k / n - math.pi / 2
        rx, ry = (rxo, ryo) if k % 2 == 0 else (rxi, ryi)
        pts.append(f"{cx_ + rx * math.cos(a):.1f},{cy_ + ry * math.sin(a):.1f}")
    h = int(w * 160 / 300)
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 300 160" style="transform:rotate({rot}deg);overflow:visible;filter:drop-shadow(0 3px 4px rgba(0,0,0,.25))"><polygon points="{' '.join(pts)}" fill="#F0140B" stroke="#fff" stroke-width="5" stroke-linejoin="round"/><g fill="#fff" font-family="Montserrat" font-weight="800" text-anchor="middle"><text x="150" y="72" font-size="22" letter-spacing="1">{lines[0]}</text><text x="150" y="102" font-size="23">{lines[1]}</text></g></svg>'''

# ---------- Home ----------
def home_html(cx):
    c = cx.cfg; h = c['home']
    li = ''.join(f'<div style="font-size:21px;line-height:33px">• {b}</div>' for b in h['bullets'])
    body = (photo(cx, 'hero', 0, 0, 1224, 465, h.get('hero_pos', '50% 52%')) +
      '<div class="tbox" style="top:390px;width:660px;height:150px"><h1 style="padding-left:18px">Home Highlights</h1></div>' +
      f'<div class="addr" style="top:562px">{c["address"]}</div>'
      f'<div style="position:absolute;left:72px;top:625px;width:380px"><div class="lab" style="font-size:21px;letter-spacing:5px;margin-bottom:14px">The Home</div>{li}'
      f'<div class="lab" style="font-size:21px;letter-spacing:5px;margin:30px 0 12px">About the Property</div><div style="font-size:19.5px;line-height:30px;color:#5a6370">{h["about"]}</div></div>' +
      photo(cx, 'big', 474, 621, 678, 375, h.get('big_pos', '50% 55%')) + photo(cx, 'small', 474, 1014, 330, 225, h.get('small_pos', '40% 50%')) +
      f'<div style="position:absolute;left:822px;top:1014px;width:330px;height:225px;background:#E6EBF0"><div style="position:absolute;left:30px;top:68px;font-size:19px;letter-spacing:4px;font-weight:500;color:#3a4350">OFFERED AT</div><div style="position:absolute;left:30px;top:96px;font-size:50px;font-weight:700;letter-spacing:-.5px">{c["price"]}</div></div>' +
      footer(cx, 1404))
    return page(body)

# ---------- Numbers ----------
def card(x, w, k):
    rows = ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;height:46px;border-top:1px solid #dfe4ea"><span style="font-size:17px">{a}</span><span style="font-size:17px;font-weight:700">{b}</span></div>' for a, b in k['rows'])
    return f'''<div style="position:absolute;left:{x}px;top:553px;width:{w}px;height:474px;border:1px solid #c9d1da;background:#fff"><div style="padding:22px 24px 0"><div style="font-family:Cormorant,serif;font-weight:700;font-size:16.5px;letter-spacing:2.6px;color:#3E5C8A;text-transform:uppercase">{k['eyebrow']}</div><div style="font-weight:600;font-size:21px;line-height:29px;margin-top:10px;height:58px">{k['l1']}<br>{k['l2']}</div><div style="font-family:Cormorant,serif;font-weight:700;font-size:16px;letter-spacing:3px;color:#5a6370;margin-top:16px">EST. MONTHLY PAYMENT</div><div style="font-weight:700;font-size:48px;line-height:56px;margin:4px 0 14px">{k['pay']}<span style="font-size:21px;font-weight:500">/mo</span></div><div style="border-bottom:1px solid #dfe4ea">{rows}</div></div><div style="position:absolute;left:0;right:0;bottom:0;height:106px;background:#E6EBF0;padding:20px 24px"><div style="font-family:Cormorant,serif;font-weight:700;font-size:16px;letter-spacing:2px;color:#5a6370">EST. CASH TO CLOSE</div><div style="font-weight:700;font-size:44px;line-height:54px;color:#3E5C8A;margin-top:2px">{k['cash']}</div></div></div>'''

def nums_html(cx):
    c = cx.cfg; n = c['numbers']; ks = n['cards']
    cnt = len(ks); gap = 21; W = (1080 - gap * (cnt - 1)) / cnt
    cards = ''.join(card(72 + i * (W + gap), W, k) for i, k in enumerate(ks))
    st = ''
    for i, k in enumerate(ks):
        if k.get('stamp'):  # sticker/stamp ONLY here, never on worksheets
            s = k['stamp']; st += f'<div style="position:absolute;left:{s.get("left", 72 + i*(W+gap) + 150)}px;top:{s.get("top", 990)}px;z-index:5">{stamp(s.get("w", 270), s.get("rot", -8), tuple(s.get("lines", ("SELLER PAYS", "CLOSING COSTS"))))}</div>'
    d = n['deltas']
    dl = ''.join(f'<div style="position:absolute;left:{72 if j == 0 else 632}px;top:1124px;width:520px;border-top:1px solid #cfd6de;padding-top:14px;display:flex;gap:16px;align-items:center"><div style="font-family:Cormorant,serif;font-weight:600;font-size:40px;color:#3E5C8A;white-space:nowrap">{x["big"]}</div><div style="font-size:17.5px;line-height:25px;color:#3a4350">{x["text"]}</div></div>' for j, x in enumerate(d))
    body = (photo(cx, 'n1', 0, 0, 405, 375, n.get('pos1', '50% 55%')) + photo(cx, 'n2', 410, 0, 405, 375, n.get('pos2', '50% 50%')) + photo(cx, 'n3', 820, 0, 404, 375, n.get('pos3', '62% 50%')) +
      '<div class="tbox" style="top:300px;width:660px;height:150px"><h1 style="padding-left:62px">The Numbers</h1></div>'
      f'<div class="addr" style="top:472px">{c["address"]}</div><div class="sub" style="top:502px">{c["price"]} · {c["facts"]}</div>' + cards + st + dl +
      f'<div style="position:absolute;left:72px;top:1212px;width:1080px;font-size:14px;line-height:19px;color:#5a6370">{n["disclaimer"]}</div>' + footer(cx, 1352) +
      '<div style="position:absolute;left:0;top:1524px;width:1224px;height:60px;background:#E6EBF0;display:flex;align-items:center;justify-content:center;font-size:21px">Need estimates on another home? Call or text Devin&nbsp;&nbsp;<b>320-241-5823 · devinkampa.com</b></div>')
    return page(body)

# ---------- Neighborhood (OSM map) ----------
def tilexy(lat, lon, z):
    n = 2 ** z; return (lon + 180) / 360 * n, (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n

def make_map(lat, lon, out, z=14, R=3):
    cache = os.path.join(CACHE, 'tiles'); os.makedirs(cache, exist_ok=True)
    fx, fy = tilexy(lat, lon, z); cx, cy = int(fx), int(fy); W = 2 * R + 1
    im = Image.new('RGB', (W * 256, W * 256))
    for dx in range(-R, R + 1):
        for dy in range(-R, R + 1):
            p = os.path.join(cache, f'{z}_{cx+dx}_{cy+dy}.png')
            if not os.path.exists(p):
                rq = urllib.request.Request(f'https://tile.openstreetmap.org/{z}/{cx+dx}/{cy+dy}.png', headers={'User-Agent': 'devinkampa-folder-flyer/1.0 (dkampa@highlandsmortgage.com)'})
                open(p, 'wb').write(urllib.request.urlopen(rq, timeout=20).read())
            im.paste(Image.open(p).convert('RGB'), ((dx + R) * 256, (dy + R) * 256))
    hx, hy = ((fx - cx) + R) * 256, ((fy - cy) + R) * 256
    mpp = 156543.03 * math.cos(math.radians(lat)) / 2 ** z; Rpx = int(3 * 1609.344 / mpp)
    im.crop((int(hx - Rpx), int(hy - Rpx), int(hx + Rpx), int(hy + Rpx))).resize((1100, 1100), Image.LANCZOS).save(out, quality=92)

ICON = {
 'park': '<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M12 3 7 10h3l-4 6h5v4h2v-4h5l-4-6h3z" fill="#fff"/></svg>',
 'shop': '<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M8 10 11 5M16 10 13 5" stroke="#fff" stroke-width="1.8" fill="none" stroke-linecap="round"/><path d="M4 10h16l-1.6 8.5a1.5 1.5 0 0 1-1.5 1.2H7.1a1.5 1.5 0 0 1-1.5-1.2z" fill="#fff"/><path d="M9 13v4M12 13v4M15 13v4" stroke="#3E5C8A" stroke-width="1.3"/></svg>',
 'eat': '<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M3 11h11a5.5 5.5 0 0 0-11 0z" fill="#fff"/><rect x="3" y="12.2" width="11" height="1.8" rx=".9" fill="#fff"/><path d="M3 15h11v1.2a2.5 2.5 0 0 1-2.5 2.5h-6A2.5 2.5 0 0 1 3 16.2z" fill="#fff"/><path d="M16 9h5l-.8 9.5a1 1 0 0 1-1 .9h-1.4a1 1 0 0 1-1-.9z" fill="#fff"/></svg>'}
COL = {'park': '#3F8A52', 'shop': '#3E5C8A', 'eat': '#E08A2E'}

def pin(kind, n, x=None, y=None, size=36, flow=False):
    st = 'position:absolute;left:0;top:0;' if flow else f'position:absolute;left:{x-size/2}px;top:{y-size/2}px;'
    badge = f'<div style="position:absolute;right:-8px;top:-9px;width:20px;height:20px;border-radius:50%;background:#fff;border:1.5px solid {COL[kind]};color:{COL[kind]};font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center">{n}</div>' if n != '' else ''
    return f'<div style="{st}width:{size}px;height:{size}px;border-radius:50%;background:{COL[kind]};border:2px solid #fff;box-shadow:0 2px 4px rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center">{ICON[kind].format(s=int(size*.6))}{badge}</div>'

def neigh_html(cx, tmp):
    c = cx.cfg; nb = c['neighborhood']; lat, lon = nb['center']
    mp = os.path.join(tmp, 'map_crop.jpg'); make_map(lat, lon, mp)
    per_px = 275 / (3 * 1609.344)
    def xy(p):
        if p.get('pin_px'): return p['pin_px']
        mlat = 111320.0; mlon = 111320.0 * math.cos(math.radians(lat))
        return [275 + (p['lon'] - lon) * mlon * per_px, 275 - (p['lat'] - lat) * mlat * per_px]
    def miles(p):
        if p.get('dist'): return p['dist']
        mlat = 111320.0; mlon = 111320.0 * math.cos(math.radians(lat))
        d = math.hypot((p['lon'] - lon) * mlon, (p['lat'] - lat) * mlat) / 1609.344
        return 'On site' if d < .15 else f'{d:.1f} mi'
    def row(p, top):
        return (f'<div style="position:absolute;left:72px;top:{top}px;width:495px;height:63px">{pin(p["kind"], p["id"], flow=True, size=38)}'
                f'<div style="position:absolute;left:65px;top:-1px;font-size:21px;font-weight:600;line-height:26px">{p["name"]}</div><div style="position:absolute;right:0;top:0;font-size:19px;color:#5a6370;line-height:26px">{miles(p)}</div>'
                f'<div style="position:absolute;left:65px;top:26px;font-size:19px;color:#5a6370;line-height:26px;white-space:nowrap">{p["desc"]}</div></div>')
    def sec(label, top): return f'<div class="lab" style="position:absolute;left:72px;top:{top}px;width:495px;border-bottom:1px solid #d3d9e0;padding-bottom:6px;height:38px">{label}</div>'
    groups = [('park', 'Parks &amp; Trails', 405), ('shop', 'Everyday Errands', 660), ('eat', 'Eat &amp; Drink', 852)]
    rows = ''
    for kind, label, top in groups:
        rows += sec(label, top)
        for i, p in enumerate([q for q in nb['pois'] if q['kind'] == kind]): rows += row(p, top + 45 + i * 63)
    community = sec('In the Community', 1103) + f'<div style="position:absolute;left:72px;top:1155px;width:495px;font-size:19.5px;line-height:28px;color:#5a6370">{nb["community"]}</div>'
    ry = -1 if nb.get('ring_dir') in ('ne', 'nw') else 1; rx = -1 if nb.get('ring_dir') == 'nw' else 1  # ring labels on the SE diagonal by default; 'ne' when pins crowd the SE
    rings = ''.join(f'<circle cx="275" cy="275" r="{91.7*r}" fill="none" stroke="#3E5C8A" stroke-width="1.6" stroke-dasharray="5 5" opacity=".75"/><text x="{275+rx*91.7*r*0.707+6*rx}" y="{275+ry*91.7*r*0.707-4}" text-anchor="middle" font-size="15" font-weight="600" fill="#3a4350" stroke="#fff" stroke-width="4" paint-order="stroke" font-family="Montserrat">{r} mi</text>' for r in (1, 2, 3))
    pins = ''.join(pin(p['kind'], p['id'], *xy(p)) for p in nb['pois'] if not p.get('nopin'))
    mapdiv = (f'<div style="position:absolute;left:603px;top:403px;width:550px;height:550px;border-radius:12px;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.18);border:1px solid #cfd6de"><img src="{cx.img(mp)}" style="position:absolute;left:0;top:0;width:550px;height:550px"><svg style="position:absolute;left:0;top:0" width="550" height="550">{rings}</svg>{pins}'
      '<div style="position:absolute;left:255px;top:255px;width:40px;height:40px;border-radius:50%;background:#14181D;border:3px solid #fff;box-shadow:0 2px 5px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="24" height="24"><path d="M12 4 3 12h3v8h4.5v-5.5h3V20H18v-8h3z" fill="#fff"/></svg></div>'
      '<div style="position:absolute;left:0;width:550px;top:298px;text-align:center;font-weight:700;font-size:16px;text-shadow:0 0 4px #fff,0 0 4px #fff,0 0 4px #fff">Home</div>'
      '<div style="position:absolute;right:16px;top:14px;text-align:center;font-weight:700;font-size:13px"><svg width="22" height="26" viewBox="0 0 22 26"><path d="M11 0 19 22 11 17 3 22z" fill="#14181D"/></svg><div style="margin-top:-2px">N</div></div></div>')
    legend = ''.join(f'<div style="display:flex;align-items:center;gap:9px;font-size:18px;color:#3a4350"><div style="position:relative;width:30px;height:30px">{pin(k, "", size=30, flow=True)}</div>{t}</div>' for k, t in (('park', 'Parks &amp; trails'), ('shop', 'Everyday errands'), ('eat', 'Eat &amp; drink')))
    right = (mapdiv + f'<div style="position:absolute;left:603px;top:969px;width:550px;display:flex;justify-content:space-between">{legend}</div>'
      '<div style="position:absolute;left:603px;top:1016px;width:550px;font-size:16.5px;line-height:24px;color:#5a6370">Dashed rings mark 1, 2 and 3 miles from the home (straight-line distances; pins approximate). Map © OpenStreetMap contributors.</div>'
      '<div class="lab" style="position:absolute;left:603px;top:1092px;font-size:21px;letter-spacing:5px;width:550px;border-bottom:1px solid #d3d9e0;padding-bottom:6px">Drive Times From Home</div>')
    cells = ''.join(f'<div style="position:absolute;left:{603+(i%2)*289}px;top:{1146+(i//2)*44}px;width:262px;height:44px;border-bottom:1px solid #e1e6ec;display:flex;justify-content:space-between;align-items:center;font-size:17px"><span>{a}</span><b>{b}</b></div>' for i, (a, b) in enumerate(nb['drive_times']))
    body = (photo(cx, 'na', 0, 0, 610, 265, nb.get('pos_a', '50% 60%')) + photo(cx, 'nb', 615, 0, 609, 265, nb.get('pos_b', '50% 40%')) +
      '<div class="tbox" style="top:190px;width:810px;height:150px"><h1 style="padding-left:40px;font-size:74px">Neighborhood Highlights</h1></div>'
      f'<div class="addr" style="top:353px;width:810px">{c["address"]}</div>' + rows + community + right + cells + footer(cx, 1404))
    return page(body)

# ---------- worksheets (clean copies, NO sticker) ----------
def worksheets(cfg, out):
    for k, pdf in (cfg.get('worksheets') or {}).items():
        base = os.path.join(out, k)
        subprocess.run(['pdftoppm', '-r', '144', '-png', '-singlefile', pdf, base], check=True)
        Image.open(base + '.png').convert('RGB').resize((1224, 1584), Image.LANCZOS).save(base + '.jpg', quality=88); os.remove(base + '.png')

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('config'); ap.add_argument('--assets', required=True); ap.add_argument('--out', required=True)
    a = ap.parse_args(); cfg = json.load(open(a.config)); os.makedirs(a.out, exist_ok=True)
    cx = Ctx(cfg, a.assets)
    from playwright.sync_api import sync_playwright
    pages = [('home', home_html(cx)), ('nums', nums_html(cx)), ('neigh', neigh_html(cx, a.out))]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1224, 'height': 1584})
        for name, html in pages:
            f = os.path.join(a.out, name + '.html'); open(f, 'w').write(html)
            pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(700)
            pg.screenshot(path=os.path.join(a.out, name + '.jpg'), type='jpeg', quality=90); print('wrote', name + '.jpg')
        b.close()
    worksheets(cfg, a.out)

if __name__ == '__main__': main()
