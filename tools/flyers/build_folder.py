#!/usr/bin/env python3
"""Make <slug>/index.html from template/index.html + a listing JSON + the rendered flyers.

Usage: python3 tools/flyers/build_folder.py <slug> tools/flyers/listings/<slug>.json <flyer dir with home/neigh/nums .jpg and w53/w5/w20 .jpg> [--agentphoto file.jpg]
Then:  python3 tools/optimize_folder.py <slug> && python3 tools/make_pdf.py <slug> "<Address> - Listing Folder"
JSON extras used here: "folder": {"home_caption": "...", "w53_label": "...", "labels": {"w53": "...", "w5": "...", "w20": "..."}} and "agent" (blank placeholders when absent).
"""
import argparse, base64, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ap = argparse.ArgumentParser(); ap.add_argument('slug'); ap.add_argument('config'); ap.add_argument('flyers'); ap.add_argument('--agentphoto')
a = ap.parse_args(); cfg = json.load(open(a.config)); fo = cfg.get('folder', {})
s = open(os.path.join(ROOT, 'template/index.html')).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) >= 1, 'missing in template: ' + old[:60]
    s = s.replace(old, new)
street, city, st_zip = [x.strip() for x in cfg['address'].split(',')]
state = st_zip.split()[0]; STATE = {'TX': 'Texas'}.get(state, state)
ag = cfg.get('agent') or {}
name = ag.get('name', 'Your Name Here'); brok = ag.get('brokerage', 'Your Brokerage'); title = ag.get('title', 'Real Estate Agent')
lic = ag.get('license', 'License #12345' if not ag else '')
phone = ag.get('phone', '(555) 555-5555'); email = ag.get('email', 'jonathan.realtor@example.com'); web = ag.get('web', 'www.example.com' if not ag else '')
digits = '+1' + re.sub(r'\D', '', phone) if ag else '+15555555555'
rep('<title>1108 Salado Dr Folder</title>', f'<title>{street} Folder</title>')
rep('<b>1108 Salado Dr.</b><span>Allen, Texas</span>', f'<b>{street}.</b><span>{city}, {STATE}</span>')
agline = f'{title} <i>·</i> {brok}' + (f' <i>·</i> {lic}' if lic else '')
rep('<strong>Jonathan Realtor</strong><div class="ag">Real Estate Agent <i>·</i> Your Brokerage <i>·</i> License #12345</div>', f'<strong>{name}</strong><div class="ag">{agline}</div>')
rep('download="1108 Salado Dr - Listing Folder.pdf"', f'download="{street} - Listing Folder.pdf"')
phs = '<div class="bph"></div>' if not ag.get('photo') else '<div class="bph" style="background-image:url(${IMG.agentphoto});background-size:cover;background-position:center 20%;color:transparent"></div>'
mail = f'{email}' + (f'<br>{web}' if web else '')
if ag.get('card'):  # use the agent's REAL uploaded card (straightened/enhanced by prep_card.py), not a recreated one
    i1 = s.index('<div class="bl2">Your Brokerage</div>'); j1 = s.index('<div class="bs"></div>', i1)
    s = s[:i1] + '<img class="agimg" src="${IMG.agentcard}" alt="">' + s[j1 + len('<div class="bs"></div>'):]
    rep("div('bc ag',s2)", "div('bc ag real',s2)")
    rep('.bc.ag{background:#fff;color:#14181D}', '.bc.ag{background:#fff;color:#14181D}.bc.ag.real{clip-path:none;border-radius:7px;box-shadow:0 0 0 1px rgba(20,24,29,.12)}.bc.ag.real .agimg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}')
else:
    rep('<div class="bl2">Your Brokerage</div><div class="bn">Jonathan Realtor</div><div class="br">Real Estate Agent<br>License #12345</div><div class="bp"><b>C:</b>(555) 555-5555</div><div class="bm">jonathan.realtor@example.com<br>www.example.com</div><div class="bph">JR</div>',
        f'<div class="bl2">{brok}</div><div class="bn">{name}</div><div class="br">{title}' + (f'<br>{lic}' if lic else '') + f'</div><div class="bp"><b>C:</b>{phone}</div><div class="bm">{mail}</div>{phs}')
rep('tel:+15555555555', 'tel:' + digits); rep('sms:+15555555555', 'sms:' + digits); rep('mailto:jonathan.realtor@example.com', 'mailto:' + email)
rep("t:'1108 Salado Dr, Allen, TX 75013'", "t:'" + cfg['address'] + "'")
rep("s:'Five bedrooms, four baths, 3,147 square feet and a backyard pool with a waterfall and spa.'", "s:'" + fo['home_caption'].replace("'", "\\'") + "'")
L = {'w53': fo.get('w53_label', '5% down with a 3% seller credit'), 'w5': '5% down', 'w20': '20% down'}; L.update(fo.get('labels', {}))
rep("const WSL={w53:'5% down with a 3% seller credit',w5:'5% down',w20:'20% down'};", "const WSL={w53:'" + L['w53'] + "',w5:'" + L['w5'] + "',w20:'" + L['w20'] + "'};")
rep("title='1108 Salado Dr, Allen, TX 75013', text='Take a look inside the listing folder for 1108 Salado Dr.'", f"title='{cfg['address']}', text='Take a look inside the listing folder for {street}.'")
# images
i0 = s.index('const IMG=') + len('const IMG='); IMG, n = json.JSONDecoder().raw_decode(s[i0:])
def b(p): return 'data:image/jpeg;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
F = a.flyers
IMG['neigh'] = b(f'{F}/neigh.jpg'); IMG['home'] = b(f'{F}/home.jpg'); IMG['num'] = b(f'{F}/nums.jpg')
for k in ('w53', 'w5', 'w20'):
    IMG.pop(k + '_s', None)
    if os.path.exists(f'{F}/{k}.jpg'): IMG[k] = b(f'{F}/{k}.jpg')
    else: IMG.pop(k, None)
if ag.get('card'): IMG['agentcard'] = b(os.path.join(os.path.dirname(os.path.abspath(a.config)), ag['card']))
else: IMG.pop('agentcard', None)
if ag.get('photo') and not ag.get('card'): IMG['agentphoto'] = b(a.agentphoto or os.path.join(os.path.dirname(os.path.abspath(a.config)), ag['photo']))
else: IMG.pop('agentphoto', None)
s = s[:i0] + json.dumps(IMG) + s[i0 + n:]
os.makedirs(os.path.join(ROOT, a.slug), exist_ok=True)
open(os.path.join(ROOT, a.slug, 'index.html'), 'w').write(s)
print('wrote', a.slug + '/index.html', [k for k in IMG if k in ('neigh', 'home', 'num', 'w53', 'w5', 'w20', 'agentphoto')])
