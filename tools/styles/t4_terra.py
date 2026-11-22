from common import *
NAME='terra'; TITLE='Terra'
FONTS=[('Nunito','nunito',w,'normal') for w in (400,600,700,800)]+[('Quicksand','quicksand',w,'normal') for w in (500,600,700)]
TAUPE='#B9A890'; TAUPEL='#E6DCCB'; OLIVE='#6B7449'; OLIVED='#4E5634'; CREAM='#F6F1E7'; INK='#3A3629'; MUTE='#7A735F'; CLAY='#C97B4F'
CSS=f"""
body{{background:{CREAM};color:{INK};font-family:Nunito,sans-serif}}
.ph{{background:#D8CDB8}} .abs{{position:absolute}} .q{{font-family:Quicksand,sans-serif;font-weight:700}}
.pill{{display:inline-block;background:{OLIVE};color:#fff;border-radius:99px;padding:8px 22px;font:700 17px Quicksand;letter-spacing:.06em}}
.card{{background:#fff;border-radius:30px;box-shadow:0 6px 0 {TAUPEL}}}
.foot{{position:absolute;left:50px;right:50px;bottom:40px;height:130px;background:{OLIVE};border-radius:65px;display:flex;align-items:center;padding:0 40px 0 22px;gap:24px;color:#fff}}
"""
def foot(msg='Let’s tour it together'):
    return f'<div class="foot"><div style="width:90px;height:90px;border-radius:50%;background:{TAUPEL};border:4px solid #fff;flex:none"></div><div style="flex:1"><div class="q" style="font-size:32px">{S["agent"]}</div><div style="font:600 16px Nunito;opacity:.85">{S["agent_t"]} · {S["brokerage"]}</div></div><div style="text-align:right;font:700 19px/1.5 Nunito">{S["aphone"]}<br>{S["aemail"]}</div></div>'
def home():
    stats=''.join(f'<div class="card" style="width:232px;height:130px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px">{icon(ic,34,OLIVE,1.6)}<div class="q" style="font-size:28px;line-height:1">{v}</div><div style="font:700 13px Nunito;letter-spacing:.14em;text-transform:uppercase;color:{MUTE}">{lb}</div></div>' for ic,v,lb in [('bed',S['beds'],'Beds'),('bath',S['baths'],'Baths'),('sqft',S['sqft'],'Sq ft'),('garage',S['garage'],'Garage')])
    bl=''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:16px;font:600 22px Nunito"><span style="width:28px;height:28px;border-radius:50%;background:{OLIVE};display:grid;place-items:center;flex:none">{icon("check",16,"#fff",2.4)}</span>{b}</span></div>' for b in S['bullets'][:6])
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:620px;background:{TAUPEL};border-radius:0 0 90px 90px"></div>
{ph(50,50,640,530,extra="border-radius:48px")}{ph(710,50,464,255,extra="border-radius:48px")}{ph(710,325,464,255,extra="border-radius:48px")}
<div class="abs" style="left:50px;top:640px"><div class="pill">OPEN HOUSE</div><div class="q" style="font-size:78px;line-height:1.02;margin-top:18px;color:{OLIVED}">123 Sample Street</div><div style="font:600 24px Nunito;color:{MUTE};margin-top:8px">{S['hood']} · {S['city']}, {S['state']}</div></div>
<div class="abs" style="left:830px;top:650px;width:344px;height:170px;background:{OLIVE};border-radius:36px;color:#fff;text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-2deg)"><div style="font:700 16px Quicksand;letter-spacing:.24em">OFFERED AT</div><div class="q" style="font-size:58px;line-height:1.1">{usd(S['price'])}</div></div>
<div class="abs" style="left:50px;top:836px;display:flex;gap:18px">{stats}</div>
<div class="abs" style="left:50px;top:996px;width:560px"><div class="q" style="font-size:30px;color:{OLIVED};margin-bottom:14px">What we love</div>{bl}</div>
<div class="abs card" style="left:650px;top:996px;width:524px;height:210px;padding:26px 34px"><div class="q" style="font-size:26px;color:{OLIVE};margin-bottom:8px">About the home</div><div style="font:400 20px/1.55 Nunito;color:{INK}">{S['about']}</div></div>
<div class="abs" style="left:650px;top:1226px;width:524px;display:flex;gap:16px">{ph(0,0,254,140,extra="position:relative;border-radius:30px")}{ph(0,0,254,140,extra="position:relative;border-radius:30px")}</div>{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def mapsvg():
    pts=[(110,110,'tree'),(300,90,'tree'),(470,190,'cart'),(120,330,'dine'),(410,360,'coffee')]
    p=''.join(f'<circle cx="{x}" cy="{y}" r="26" fill="{OLIVE}"/><path transform="translate({x-13},{y-13}) scale(1.08)" d="{IC[ic]}" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/>' for x,y,ic in pts)
    return f'<svg width="580" height="480" viewBox="0 0 580 480"><rect width="580" height="480" fill="{TAUPEL}"/><path d="M-10 150C120 120 220 210 330 170S520 120 600 150V230C500 210 340 270 230 250S60 210-10 240Z" fill="#fff" opacity=".8"/><path d="M0 400C150 360 250 440 380 400S520 380 590 410V490H0Z" fill="#CBD0AE"/><ellipse cx="110" cy="110" rx="90" ry="60" fill="#CBD0AE"/>{p}<circle cx="260" cy="260" r="34" fill="{CLAY}" stroke="#fff" stroke-width="5"/><path transform="translate(244,244) scale(1.35)" d="{IC["home"]}" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def neigh():
    def card(x,y,w,ic,title,items,mi=False):
        rows=''.join(f'<div style="display:flex;justify-content:space-between;margin-bottom:12px"><div><div style="font:700 19px Nunito">{i[0]}</div><div style="font:400 15px Nunito;color:{MUTE}">{i[1]}</div></div>{"<div class=q style=font-size:17px;color:"+OLIVE+">"+i[2]+"</div>" if mi else ""}</div>' for i in items)
        return f'<div class="abs card" style="left:{x}px;top:{y}px;width:{w}px;padding:24px 28px 12px"><div style="display:flex;align-items:center;gap:14px;margin-bottom:16px"><div style="width:52px;height:52px;border-radius:50%;background:{OLIVE};display:grid;place-items:center">{icon(ic,28,"#fff",1.7)}</div><div class="q" style="font-size:26px;color:{OLIVED}">{title}</div></div>{rows}</div>'
    dr=''.join(f'<span style="display:inline-flex;align-items:baseline;gap:8px;background:{TAUPEL};border-radius:99px;padding:8px 20px;margin:0 8px 10px 0"><b class="q" style="font-size:22px;color:{OLIVED}">{t}</b><span style="font:700 14px Nunito;color:{MUTE}">{n}</span></span>' for n,t in NEIGH['drive'])
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:300px;background:{TAUPEL};border-radius:0 0 90px 90px"></div>{ph(790,40,384,220,extra="border-radius:48px")}
<div class="abs" style="left:50px;top:52px"><div class="pill">{S['hood']} · {S['city']}, {S['state']}</div><div class="q" style="font-size:78px;line-height:1.02;margin-top:16px;color:{OLIVED}">Neighborhood<br>Highlights</div></div>
<div class="abs" style="left:50px;top:330px;width:590px;height:470px;border-radius:44px;overflow:hidden;box-shadow:0 6px 0 {TAUPEL}"><div style="transform:scale(1.02);transform-origin:0 0">{mapsvg()}</div></div>
<div class="abs" style="left:670px;top:330px;width:504px"><div style="font:600 25px/1.5 Nunito;color:{INK}">{NEIGH['intro']}</div><div class="q" style="font-size:18px;letter-spacing:.14em;color:{MUTE};margin:22px 0 12px">DRIVE TIMES</div>{dr}</div>
{card(50,830,358,'tree','Parks &amp; Trails',NEIGH['parks'][:4])}{card(433,830,358,'cart','Errands',NEIGH['errands'][:4],True)}{card(816,830,358,'dine','Eat &amp; Drink',NEIGH['eat'][:4])}{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def numbers():
    cards=''
    for i,c in enumerate(CARDS):
        x=50+i*(358+25)
        rows=f'<div class="r"><span>Down payment</span><b>{usd(c["down"])}</b></div><div class="r"><span>Est. closing costs</span><b>{usd(c["closing"])}</b></div><div class="r"><span>Seller credit{" ("+str(c["credit_pct"])+"%)" if c["credit"] else ""}</span><b>{"–"+usd(c["credit"]) if c["credit"] else "$0"}</b></div>'
        cards+=f'''<div class="abs" style="left:{x}px;top:360px;width:358px;height:640px;background:{OLIVED};border-radius:40px;overflow:hidden"><div style="position:absolute;left:5px;right:5px;top:5px;bottom:5px;background:#fff;border-radius:36px;overflow:hidden">
<div style="background:{TAUPEL};padding:18px 26px"><span class="pill" style="font-size:14px;padding:6px 16px">{c['tag']}</span></div>
<div style="padding:20px 28px 0"><div class="q" style="font-size:28px;line-height:1.15;color:{OLIVED}">{c['title']}<br>{c['title2']}</div><div style="font:700 12px Nunito;letter-spacing:.18em;text-transform:uppercase;color:{MUTE};margin-top:18px">Est. monthly payment</div><div class="q" style="font-size:62px;line-height:1.1">{usd(c['mo'])}<span style="font:600 22px Nunito;color:{MUTE}">/mo</span></div><div style="margin-top:12px">{rows}</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:140px;background:{OLIVE};color:#fff;padding:24px 28px"><div style="font:700 12px Nunito;letter-spacing:.18em;text-transform:uppercase;opacity:.9">Est. cash to close</div><div class="q" style="font-size:54px">{usd(c['cash'])}</div></div></div></div>'''
    dl=''.join(f'<div style="flex:1;background:{TAUPEL};border-radius:30px;padding:16px 24px;display:flex;align-items:center;gap:18px"><span class="q" style="font-size:44px;color:{OLIVE};white-space:nowrap">{a}</span><span style="font:600 18px/1.35 Nunito">{b}</span></div>' for a,b in DELTAS)
    css=CSS+f".r{{display:flex;justify-content:space-between;font:600 18px Nunito;padding:10px 0;border-top:2px dotted {TAUPE}}} .r b{{font-weight:800}}"
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:310px;background:{TAUPEL};border-radius:0 0 90px 90px"></div>{ph(790,30,384,250,extra="border-radius:48px")}
<div class="abs" style="left:50px;top:48px"><div class="pill">SAMPLE FIGURES</div><div class="q" style="font-size:96px;line-height:1;margin-top:14px;color:{OLIVED}">The Numbers</div><div style="font:700 20px Nunito;color:{MUTE};margin-top:8px">{S['full']} · {usd(S['price'])} · {S['beds']} BD · {S['baths']} BA · {S['sqft']} SF</div></div>
{cards}
<div class="abs" style="left:50px;top:1022px;width:1124px;display:flex;gap:24px">{dl}</div>
<div class="abs" style="left:50px;top:1130px;width:1124px;font:400 13px/1.55 Nunito;color:{MUTE}">{DISC}</div>
<div class="abs" style="left:50px;top:1280px;width:1124px;display:flex;gap:24px"><div class="card" style="flex:1;padding:20px 28px"><div class="q" style="font-size:28px;color:{OLIVED}">{S['agent']}</div><div style="font:600 17px/1.55 Nunito;color:{MUTE}">{S['agent_t']} · {S['brokerage']}<br><b style="color:{INK}">{S['aphone']}</b> · {S['aemail']}</div></div>
<div class="card" style="flex:1;padding:20px 28px;display:flex;gap:20px;align-items:center"><img src="{HS}" style="width:100px;height:100px;border-radius:50%;object-fit:cover;border:4px solid {OLIVE}"><div><div class="q" style="font-size:28px;color:{OLIVED}">{LO['name']}</div><div style="font:600 17px/1.55 Nunito;color:{MUTE}">{LO['t']}<br><b style="color:{INK}">{LO['phone']}</b><br>{LO['email']}</div></div></div></div>
<div class="abs" style="left:50px;right:50px;bottom:30px;height:68px;background:{OLIVE};border-radius:34px;color:#fff;display:flex;justify-content:center;align-items:center;font:700 20px Nunito;white-space:nowrap">Need estimates on another home? Call or text Devin {LO['phone']} · {LO['web']}</div>'''
    return page(fontcss(FONTS),css,body)
def move():
    su=''.join(f'<div style="display:flex;align-items:center;gap:20px;margin-bottom:18px"><div class="q" style="width:56px;height:56px;border-radius:50%;background:{OLIVE};color:#fff;display:grid;place-items:center;font-size:26px;flex:none">{i+1}</div><div style="flex:1"><div style="font:800 21px Nunito">{a}</div><div style="font:400 15px Nunito;color:{MUTE}">{c}</div></div><span style="background:{TAUPEL};border-radius:99px;padding:6px 14px;font:700 14px Nunito;white-space:nowrap">{d}</span></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
    ics=['bolt','flame','drop','wifi','home']
    mo=''.join(f'<div class="abs card" style="left:{50+(i%3)*375 if i<3 else 237+(i-3)*375}px;top:{900+(0 if i<3 else 0)}px;width:350px;height:200px;padding:20px 24px;display:none"></div>' for i in range(0))
    tiles=''
    for i,(a,b,lo,hi) in enumerate(MOVE['monthly']):
        x=50+(i%3)*375 if i<3 else 237+(i-3)*375; y=850 if i<3 else 1090
        tiles+=f'<div class="abs card" style="left:{x}px;top:{y}px;width:350px;height:216px;padding:22px 26px"><div style="width:52px;height:52px;border-radius:50%;background:{OLIVE};display:grid;place-items:center">{icon(ics[i],28,"#fff",1.8)}</div><div style="font:800 22px Nunito;margin-top:12px">{a}</div><div class="q" style="font-size:34px;color:{OLIVED}">{"$"+str(lo)+"–$"+str(hi) if lo else MOVE["hoa"]}</div><div style="font:400 14px/1.35 Nunito;color:{MUTE}">{b}</div></div>'
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:290px;background:{TAUPEL};border-radius:0 0 90px 90px"></div>{ph(790,30,384,230,extra="border-radius:48px")}
<div class="abs" style="left:50px;top:50px"><div class="pill">Your first week at {S['street']}</div><div class="q" style="font-size:92px;line-height:1;margin-top:14px;color:{OLIVED}">Move-In Costs</div></div>
<div class="abs" style="left:50px;top:318px;width:1124px;font:600 22px/1.5 Nunito">{MOVE['intro']}</div>
<div class="abs card" style="left:50px;top:420px;width:1124px;padding:28px 40px 14px"><div class="q" style="font-size:26px;color:{OLIVE};margin-bottom:18px">Set up before you arrive</div><div style="display:grid;grid-template-columns:1fr 1fr;column-gap:50px">{su}</div></div>
<div class="abs q" style="left:50px;top:798px;font-size:26px;color:{OLIVE}">Typical monthly costs</div>{tiles}
<div class="abs" style="left:50px;top:1316px;width:1124px;font:400 12.5px/1.5 Nunito;color:{MUTE}">{MOVE['fine']}</div>{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def all(): return {'home':home(),'neigh':neigh(),'num':numbers(),'move':move()}
