#!/usr/bin/env python3
"""Luxury flyer set: photo flyer (2 sides, 2x3), Home, Neighborhood, Move-In Costs.
Usage: python3 build_luxury.py listings/<slug>.luxury.json --assets <photo dir> --out <dir>
Ivory paper, black ink, brass-gold rules. No Numbers sheet (added later)."""
import argparse, base64, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_flyers import fonts_css, b64

GOLD = '#A8864A'; INK = '#121212'; IVORY = '#F6F1E7'; MUTE = '#6B665C'
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1224px;height:1584px;overflow:hidden;background:%(IVORY)s;color:%(INK)s;font-family:Montserrat,sans-serif}
.pg{position:relative;width:1224px;height:1584px;overflow:hidden;background:%(IVORY)s}
.ph{position:absolute;background-size:cover;background-position:center;background-repeat:no-repeat}
.eb{position:absolute;font-size:17px;font-weight:600;letter-spacing:7px;text-transform:uppercase;color:%(GOLD)s}
.ti{position:absolute;font-family:Cormorant,serif;font-weight:600;line-height:1;white-space:nowrap}
.rule{position:absolute;height:2px;background:%(GOLD)s}
.lab{font-family:Cormorant,serif;font-weight:700;font-size:25px;letter-spacing:6px;text-transform:uppercase;color:%(INK)s;border-bottom:2px solid %(GOLD)s;padding-bottom:9px}
.dia{display:inline-block;width:9px;height:9px;background:%(GOLD)s;transform:rotate(45deg);margin-right:16px;flex:none;position:relative;top:-2px}
.li{display:flex;align-items:flex-start;font-size:21px;line-height:30px;margin-bottom:11px}
.mut{color:%(MUTE)s}
.foot{position:absolute;left:0;right:0;bottom:0;height:150px;background:%(INK)s;color:#fff}
.foot .nm{position:absolute;left:72px;top:34px;font-family:Cormorant,serif;font-size:38px;font-weight:600;color:#fff}
.foot .t1{position:absolute;left:72px;top:84px;font-size:15px;letter-spacing:4px;text-transform:uppercase;color:%(GOLD)s;font-weight:600}
.foot .r{position:absolute;right:72px;top:40px;text-align:right;font-size:20px;line-height:34px;color:#e9e3d6}
.foot .r b{color:%(GOLD)s;font-weight:600}
""" % dict(IVORY=IVORY, INK=INK, GOLD=GOLD, MUTE=MUTE)

def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{fonts_css()}{CSS}</style></head><body><div class="pg">{body}</div></body></html>'

class Cx:
    def __init__(s, cfg, assets): s.cfg, s.assets = cfg, assets
    def img(s, name):
        p = os.path.join(s.assets, name); ext = p.rsplit('.', 1)[-1].lower().replace('jpg', 'jpeg')
        return f'data:image/{ext};base64,{b64(p)}'

def ph(cx, key, l, t, w, h, pos='50% 50%'):
    return f'<div class="ph" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;background-image:url({cx.img(cx.cfg["photos"].get(key, key))});background-position:{pos}"></div>'

def footer(cx):
    a = cx.cfg.get('agent') or {}
    nm = a.get('name', 'Your Name Here'); tt = (a.get('title', 'Real Estate Agent') + ' · ' + a.get('brokerage', 'Your Brokerage')).upper()
    ph_ = a.get('phone', '(555) 555-5555'); em = a.get('email', 'you@example.com')
    return f'<div class="foot"><div class="nm">{nm}</div><div class="t1">{tt}</div><div class="r"><b>T</b>&nbsp; {ph_}<br><b>E</b>&nbsp; {em}</div></div>'

def short_addr(cx): return cx.cfg['address'].split(',')[0]

# ---------- photo flyer: 2 wide x 3 tall, thin black lines, address tag bottom-right ----------
def pics_html(cx, side):
    keys = cx.cfg['photo_sides'][side]; names = cx.cfg['photo_side_names']
    cells = ''
    for i, k in enumerate(keys):
        c, r = i % 2, i // 2
        cells += ph(cx, k['f'], c * 612, r * 528, 612, 528, k.get('pos', '50% 50%'))
    lines = '<div style="position:absolute;left:610px;top:0;width:4px;height:1584px;background:#000"></div>' + ''.join(f'<div style="position:absolute;left:0;top:{y-2}px;width:1224px;height:4px;background:#000"></div>' for y in (528, 1056))
    city = cx.cfg['address'].split(',', 1)[1].strip().rsplit(' ', 1)[0].upper()
    tag = (f'<div style="position:absolute;right:0;bottom:0;background:#000;padding:22px 34px 20px 38px;text-align:right;border-top:2px solid {GOLD};border-left:2px solid {GOLD}">'
           f'<div style="font-family:Cormorant,serif;font-weight:600;font-size:40px;color:#fff;line-height:1">{short_addr(cx)}</div>'
           f'<div style="font-size:13px;letter-spacing:5px;color:{GOLD};font-weight:600;margin-top:9px">{city} &nbsp;·&nbsp; {names[side].upper()}</div></div>')
    return page(cells + lines + tag)

# ---------- home highlights ----------
def home_html(cx):
    c = cx.cfg; h = c['home']
    facts = ''.join(f'<div style="flex:1;text-align:center;{"border-left:2px solid "+GOLD if i else ""}"><div style="font-family:Cormorant,serif;font-size:54px;font-weight:600;line-height:1">{a}</div><div style="font-size:13px;letter-spacing:5px;color:{MUTE};font-weight:600;margin-top:8px">{b}</div></div>' for i, (a, b) in enumerate(h['facts']))
    bl = ''.join(f'<div class="li"><span class="dia"></span><span>{b}</span></div>' for b in h['bullets'])
    body = (ph(cx, 'hero', 0, 0, 1224, 640, h.get('hero_pos', '50% 50%'))
            + f'<div class="eb" style="left:72px;top:690px">{h["eyebrow"]}</div>'
            + f'<div class="ti" style="left:72px;top:728px;font-size:112px">{short_addr(cx)}.</div>'
            + f'<div class="rule" style="left:72px;top:866px;width:1080px"></div>'
            + f'<div style="position:absolute;left:72px;top:892px;width:1080px;display:flex;padding:10px 0">{facts}</div>'
            + f'<div class="rule" style="left:72px;top:1030px;width:1080px"></div>'
            + f'<div style="position:absolute;left:72px;top:1066px;width:470px;font-family:Cormorant,serif;font-size:27px;line-height:36px;font-weight:500;font-style:italic">{h["about"]}</div>'
            + f'<div style="position:absolute;left:600px;top:1060px;width:552px">{bl}</div>'
            + footer(cx))
    return page(body)

# ---------- neighborhood highlights ----------
def neigh_html(cx):
    n = cx.cfg['neighborhood']
    def sec(title, rows, top, left, w):
        r = ''.join(f'<div style="display:flex;justify-content:space-between;gap:16px;margin-bottom:13px"><div><div style="font-size:20px;font-weight:600;line-height:26px">{a}</div><div class="mut" style="font-size:16px;line-height:21px">{b}</div></div><div style="font-size:16px;font-weight:600;color:{GOLD};white-space:nowrap;padding-top:3px">{d}</div></div>' for a, b, d in rows)
        return f'<div style="position:absolute;left:{left}px;top:{top}px;width:{w}px"><div class="lab" style="margin-bottom:20px">{title}</div>{r}</div>'
    body = (ph(cx, 'n1', 0, 0, 612, 330) + ph(cx, 'n2', 612, 0, 612, 330)
            + '<div style="position:absolute;left:610px;top:0;width:4px;height:330px;background:#000"></div>'
            + f'<div class="eb" style="left:72px;top:380px">{n["eyebrow"]}</div>'
            + f'<div class="ti" style="left:72px;top:416px;font-size:92px">Neighborhood Highlights</div>'
            + f'<div class="rule" style="left:72px;top:530px;width:1080px"></div>'
            + f'<div style="position:absolute;left:72px;top:556px;width:1080px;font-family:Cormorant,serif;font-size:27px;line-height:36px;font-style:italic;font-weight:500">{n["community"]}</div>'
            + sec('Parks &amp; trails', n['parks'], 700, 72, 520)
            + sec('Everyday errands', n['errands'], 700, 632, 520)
            + sec('Eat &amp; drink', n['eat'], 1060, 72, 520)
            + f'<div class="lab" style="position:absolute;left:632px;top:1060px;width:520px">Drive times</div>'
            + f'<div style="position:absolute;left:632px;top:1118px;width:520px;display:grid;grid-template-columns:1fr 1fr;row-gap:26px">'
            + ''.join(f'<div style="{"border-left:2px solid "+GOLD+";padding-left:20px" if i%2 else ""}"><div style="font-family:Cormorant,serif;font-size:44px;font-weight:600;line-height:1">{m}</div><div style="font-size:12px;letter-spacing:3px;color:{MUTE};font-weight:600;margin-top:6px;text-transform:uppercase">{p}</div></div>' for i, (p, m) in enumerate(n['drive_times']))
            + '</div>'
            + f'<div style="position:absolute;left:72px;right:72px;top:1432px;font-size:12px;line-height:17px;color:{MUTE}">{n["note"]}</div>'
            + footer(cx))
    return page(body)

# ---------- move-in costs ----------
def movein_html(cx):
    m = cx.cfg['movein']
    def row(a, b, c, d):
        return (f'<div style="display:flex;align-items:flex-start;padding:15px 0;border-bottom:1px solid #d9d1c0">'
                f'<div style="width:300px"><div style="font-size:21px;font-weight:600;line-height:26px">{a}</div><div class="mut" style="font-size:15px;line-height:20px">{b}</div></div>'
                f'<div style="flex:1;font-size:17px;line-height:24px;padding-right:20px">{c}</div>'
                f'<div style="width:190px;text-align:right;font-family:Cormorant,serif;font-size:30px;font-weight:600;line-height:30px;color:{INK}">{d}</div></div>')
    def block(title, rows, top):
        return f'<div style="position:absolute;left:72px;top:{top}px;width:1080px"><div class="lab">{title}</div>' + ''.join(row(*r) for r in rows) + '</div>'
    body = (ph(cx, 'm1', 0, 0, 1224, 260, m.get('pos', '50% 40%'))
            + f'<div class="eb" style="left:72px;top:300px">{m["eyebrow"]}</div>'
            + f'<div class="ti" style="left:72px;top:334px;font-size:92px">Move-In Costs</div>'
            + f'<div class="rule" style="left:72px;top:444px;width:1080px"></div>'
            + f'<div style="position:absolute;left:72px;top:464px;width:1080px;font-family:Cormorant,serif;font-size:25px;line-height:33px;font-style:italic;font-weight:500">{m["intro"]}</div>'
            + block('Set up before you arrive', m['setup'], 545)
            + block('Typical monthly costs', m['monthly'], 930)
            + f'<div style="position:absolute;left:72px;right:72px;top:1382px;font-size:12px;line-height:17px;color:{MUTE}">{m["note"]}</div>'
            + footer(cx))
    return page(body)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('config'); ap.add_argument('--assets', required=True); ap.add_argument('--out', required=True)
    a = ap.parse_args(); cfg = json.load(open(a.config)); os.makedirs(a.out, exist_ok=True); cx = Cx(cfg, a.assets)
    pages = [('pics', pics_html(cx, 'a')), ('pics2', pics_html(cx, 'b')), ('home', home_html(cx)), ('neigh', neigh_html(cx)), ('move', movein_html(cx))]
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1224, 'height': 1584}, device_scale_factor=1.5)
        for name, html in pages:
            f = os.path.join(a.out, name + '.html'); open(f, 'w').write(html)
            pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(700)
            pg.screenshot(path=os.path.join(a.out, name + '.jpg'), type='jpeg', quality=88); print('wrote', name + '.jpg')
        b.close()

if __name__ == '__main__': main()
