from common import *
NAME='evergreen'; TITLE='Evergreen'
FONTS=[('Fraunces','fraunces',w,'normal') for w in (400,600,700)]+[('Fraunces','fraunces',400,'italic')]+[('Karla','karla',w,'normal') for w in (400,500,700)]
FOR='#1F3A2E'; FOR2='#2D5240'; COP='#B26A3C'; COPL='#D9A07A'; CREAM='#F7F2E8'; SAGE='#DDE4D3'; INK='#1F2A24'; MUTE='#5F6B62'
CSS=f"""
body{{background:{CREAM};color:{INK};font-family:Karla,sans-serif}}
.ph{{background:#CFD6C4}} .abs{{position:absolute}} .fr{{font-family:Fraunces,serif}}
.cap{{font:700 15px Karla;letter-spacing:.26em;text-transform:uppercase;color:{COP}}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:150px;background:{FOR};color:#fff;display:flex;align-items:center;padding:0 70px;gap:28px;border-top:6px solid {COP}}}
"""
def leaf(x,y,s=1,rot=0,c=COP,o=1):
    return ''
    return f'<svg class="abs" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({s});opacity:{o}" width="120" height="220" viewBox="0 0 120 220"><path d="M60 215V20" stroke="{c}" stroke-width="3" fill="none"/>'+''.join(f'<path d="M60 {40+i*34}C{20 if i%2 else 100} {20+i*34} {18 if i%2 else 102} {50+i*34} 60 {58+i*34}Z" fill="{c}"/>' for i in range(5))+'<path d="M60 20C45 5 75 5 60 20Z" fill="'+c+'"/></svg>'
def foot():
    return f'<div class="foot"><div style="width:92px;height:92px;border-radius:50%;background:{FOR2};border:3px solid {COPL};flex:none"></div><div style="flex:1"><div class="fr" style="font:600 34px Fraunces">{S["agent"]}</div><div class="cap" style="font-size:12px;color:{COPL};margin-top:4px">{S["agent_t"]} · {S["brokerage"]}</div></div><div style="text-align:right;font:500 20px/1.6 Karla">{S["aphone"]}<br>{S["aemail"]}</div></div>'
def home():
    st=''.join(f'<div style="flex:1;text-align:center;{"border-left:1px solid "+COPL if i else ""}">{icon(ic,34,COP,1.5)}<div class="fr" style="font:600 36px Fraunces;margin-top:4px">{v}</div><div style="font:700 12px Karla;letter-spacing:.2em;text-transform:uppercase;color:{MUTE}">{lb}</div></div>' for i,(ic,v,lb) in enumerate([('bed',S['beds'],'Beds'),('bath',S['baths'],'Baths'),('sqft',S['sqft'],'Sq ft'),('garage',S['garage'],'Garage')]))
    bl=''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:11px;font:500 21px Karla"><span style="width:12px;height:12px;background:{COP};transform:rotate(45deg);flex:none"></span>{b}</div>' for b in S['bullets'][:6])
    body=f'''{ph(0,0,1224,640,extra="")}
<div class="abs" style="left:70px;top:420px;width:760px;background:{FOR};padding:34px 46px;border-bottom:6px solid {COP}"><div class="cap" style="color:{COPL}">Open house · {S['hood']}</div><div class="fr" style="font:600 78px/1.02 Fraunces;color:#fff;margin-top:10px">123 Sample Street</div><div class="fr" style="font:italic 400 26px Fraunces;color:{COPL};margin-top:8px">{S['city']}, {S['state']}</div></div>
{leaf(980,420,1.1,8,COP,.9)}{leaf(1070,470,.8,-10,FOR,.9)}
<div class="abs" style="left:70px;top:770px;width:520px"><div class="cap">Offered at</div><div class="fr" style="font:700 84px/1.05 Fraunces;color:{FOR}">{usd(S['price'])}</div><div style="width:120px;height:4px;background:{COP};margin:14px 0 22px"></div><div style="font:400 21px/1.5 Karla;color:{INK}">{S['about']}</div></div>
<div class="abs" style="left:650px;top:770px;width:504px;padding:30px 40px 14px;background:{SAGE};"><div class="cap" style="margin-bottom:18px">Home highlights</div>{bl}</div>
<div class="abs" style="left:70px;top:1085px;width:1084px;display:flex;padding:14px 0;border-top:2px solid {COP};border-bottom:2px solid {COP}">{st}</div>
{ph(70,1215,340,76,extra="border:6px solid #fff")}{ph(440,1215,340,76,extra="border:6px solid #fff")}{ph(810,1215,344,76,extra="border:6px solid #fff")}{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def mapsvg():
    pts=[(110,100,'tree'),(310,70,'tree'),(480,200,'cart'),(110,340,'dine'),(420,370,'coffee')]
    p=''.join(f'<circle cx="{x}" cy="{y}" r="24" fill="{FOR}"/><path transform="translate({x-12},{y-12})" d="{IC[ic]}" fill="none" stroke="{COPL}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>' for x,y,ic in pts)
    return f'<svg width="580" height="480" viewBox="0 0 580 480"><rect width="580" height="480" fill="#EEEAD9"/><g fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round"><path d="M0 200C150 150 260 280 400 220S540 180 580 200"/><path d="M180 0C200 150 150 300 220 480"/></g><circle cx="110" cy="100" r="64" fill="#C9D4B6"/><circle cx="440" cy="400" r="70" fill="#C9D4B6"/>{p}<circle cx="260" cy="250" r="32" fill="{COP}" stroke="#fff" stroke-width="5"/><path transform="translate(245,235) scale(1.25)" d="{IC["home"]}" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def neigh():
    def col(x,ic,title,items,mi=False):
        rows=''.join(f'<div style="margin-bottom:13px;display:flex;justify-content:space-between;gap:8px"><div><div style="font:700 19px Karla">{i[0]}</div><div style="font:400 15px Karla;color:{MUTE}">{i[1]}</div></div>{"<div class=fr style=font-size:17px;color:"+COP+">"+i[2]+"</div>" if mi else ""}</div>' for i in items)
        return f'<div class="abs" style="left:{x}px;top:880px;width:340px"><div style="display:flex;align-items:center;gap:12px;border-bottom:3px solid {COP};padding-bottom:10px;margin-bottom:14px">{icon(ic,32,COP,1.5)}<div class="fr" style="font:600 27px Fraunces;color:{FOR}">{title}</div></div>{rows}</div>'
    tl=''.join(f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:16px"><span style="width:16px;height:16px;border-radius:50%;background:{COP};border:3px solid {FOR2};box-sizing:content-box;flex:none"></span><span style="flex:1;font:500 19px Karla;color:#fff">{n}</span><span class="fr" style="font:600 22px Fraunces;color:{COPL}">{t}</span></div>' for n,t in NEIGH['drive'])
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:290px;background:{FOR}"></div>{ph(790,0,434,290,extra="")}{leaf(740,40,.9,-6,COP,.95)}
<div class="abs" style="left:70px;top:54px"><div class="cap" style="color:{COPL}">{S['hood']} · {S['city']}, {S['state']}</div><div class="fr" style="font:600 76px/1.02 Fraunces;color:#fff;margin-top:12px">Neighborhood<br><i style="font-weight:400;color:{COPL}">Highlights</i></div></div>
<div class="abs" style="left:70px;top:330px;width:580px;height:480px;border:8px solid #fff;box-shadow:0 0 0 2px {COP};box-sizing:content-box;overflow:hidden;margin:0">{mapsvg()}</div>
<div class="abs" style="left:716px;top:330px;width:438px"><div class="fr" style="font:italic 400 25px/1.5 Fraunces;color:{FOR}">{NEIGH['intro']}</div><div style="margin-top:26px;background:{FOR2};padding:26px 30px 10px"><div class="cap" style="color:{COPL};margin-bottom:16px">Drive times</div>{tl}</div></div>
{col(70,'tree','Parks &amp; Trails',NEIGH['parks'][:4])}{col(442,'cart','Errands',NEIGH['errands'][:4],True)}{col(814,'dine','Eat &amp; Drink',NEIGH['eat'][:4])}{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def numbers():
    cards=''
    for i,c in enumerate(CARDS):
        x=60+i*(356+20)
        rows=f'<div class="r"><span>Down payment</span><b>{usd(c["down"])}</b></div><div class="r"><span>Est. closing costs</span><b>{usd(c["closing"])}</b></div><div class="r"><span>Seller credit{" ("+str(c["credit_pct"])+"%)" if c["credit"] else ""}</span><b>{"–"+usd(c["credit"]) if c["credit"] else "$0"}</b></div>'
        cards+=f'''<div class="abs" style="left:{x}px;top:370px;width:356px;height:630px;background:#fff;border:2px solid {FOR};outline:2px solid {COP};outline-offset:-10px"><div style="background:{FOR};padding:16px 28px"><div class="cap" style="color:{COPL};font-size:13px">{c['tag']}</div></div><div style="padding:22px 30px 0"><div class="fr" style="font:600 27px/1.15 Fraunces;color:{FOR}">{c['title']}<br>{c['title2']}</div><div style="font:700 12px Karla;letter-spacing:.2em;text-transform:uppercase;color:{MUTE};margin-top:18px">Est. monthly payment</div><div class="fr" style="font:700 60px/1.1 Fraunces">{usd(c['mo'])}<span style="font:400 22px Karla;color:{MUTE}">/mo</span></div><div style="margin-top:10px">{rows}</div></div>
<div style="position:absolute;left:10px;right:10px;bottom:10px;height:130px;background:{FOR};padding:22px 24px;color:#fff"><div class="cap" style="color:{COPL};font-size:12px">Est. cash to close</div><div class="fr" style="font:700 54px Fraunces">{usd(c['cash'])}</div></div></div>'''
    dl=''.join(f'<div style="flex:1;display:flex;align-items:center;gap:18px"><span class="fr" style="font:700 46px Fraunces;color:{COP};white-space:nowrap">{a}</span><span style="font:500 18px/1.4 Karla">{b}</span></div>' for a,b in DELTAS)
    css=CSS+f".r{{display:flex;justify-content:space-between;font:500 18px Karla;padding:9px 0;border-top:1px solid #D9D3C2}} .r b{{font-weight:700;color:{FOR}}}"
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:320px;background:{FOR}"></div>{ph(800,0,424,320,extra="")}{leaf(750,50,.9,-6,COP,.95)}
<div class="abs" style="left:70px;top:48px"><div class="cap" style="color:{COPL}">Sample figures · official estimate format</div><div class="fr" style="font:600 100px/1.02 Fraunces;color:#fff;margin-top:12px">The Numbers</div><div style="font:500 21px Karla;color:#C9D7CC;margin-top:10px">{S['full']} · {usd(S['price'])} · {S['beds']} BD · {S['baths']} BA · {S['sqft']} SF</div></div>
{cards}
<div class="abs" style="left:60px;top:1030px;width:1104px;display:flex;gap:36px;padding:18px 0;border-top:2px solid {COP};border-bottom:2px solid {COP}">{dl}</div>
<div class="abs" style="left:60px;top:1160px;width:1104px;font:400 13px/1.55 Karla;color:{MUTE}">{DISC}</div>
<div class="abs" style="left:60px;top:1296px;width:1104px;display:flex;justify-content:space-between"><div style="border-left:5px solid {COP};padding-left:20px"><div class="fr" style="font:600 28px Fraunces;color:{FOR}">{S['agent']}</div><div style="font:400 17px/1.55 Karla;color:{MUTE}">{S['agent_t']} · {S['brokerage']}<br><b style="color:{INK}">{S['aphone']}</b><br>{S['aemail']}</div></div><div style="display:flex;gap:22px;align-items:center;border-left:5px solid {COP};padding-left:20px"><img src="{HS}" style="width:118px;height:118px;border-radius:50%;object-fit:cover;border:3px solid {FOR}"><div><div class="fr" style="font:600 28px Fraunces;color:{FOR}">{LO['name']}</div><div style="font:400 17px/1.55 Karla;color:{MUTE}">{LO['t']}<br><b style="color:{INK}">{LO['phone']}</b><br>{LO['email']}</div></div></div></div>
<div class="abs" style="left:0;right:0;bottom:0;height:74px;background:{FOR};border-top:5px solid {COP};color:#fff;display:flex;justify-content:center;align-items:center;font:500 20px Karla;white-space:nowrap">Need estimates on another home? Call or text Devin <b style="color:{COPL};margin:0 8px">{LO['phone']}</b> · {LO['web']}</div>'''
    return page(fontcss(FONTS),css,body)
def move():
    su=''.join(f'<div style="display:flex;gap:20px;position:relative;padding-bottom:26px"><div style="width:44px;display:flex;flex-direction:column;align-items:center"><div class="fr" style="width:44px;height:44px;border-radius:50%;background:{COP};color:#fff;display:grid;place-items:center;font:700 22px Fraunces">{i+1}</div><div style="flex:1;width:2px;background:{COPL};margin-top:4px"></div></div><div style="flex:1"><div style="font:700 21px Karla;color:#fff">{a}</div><div style="font:400 15px/1.35 Karla;color:#C9D7CC">{c}</div><div class="fr" style="font:italic 400 18px Fraunces;color:{COPL};margin-top:4px">{d}</div></div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
    ics=['bolt','flame','drop','wifi','home']
    mo=''.join(f'<div style="display:flex;align-items:center;gap:18px;padding:16px 0;border-bottom:1px solid #D9D3C2"><div style="width:50px;height:50px;border-radius:50%;border:2px solid {COP};display:grid;place-items:center;flex:none">{icon(ics[i],26,COP,1.7)}</div><div style="flex:1"><div style="font:700 21px Karla">{a}</div><div style="font:400 14.5px Karla;color:{MUTE}">{b}</div></div><div class="fr" style="font:600 27px Fraunces;color:{FOR}">{"$"+str(lo)+"–$"+str(hi) if lo else MOVE["hoa"]}</div></div>' for i,(a,b,lo,hi) in enumerate(MOVE['monthly']))
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:280px;background:{FOR}"></div>{ph(820,0,404,280,extra="")}{leaf(770,36,.85,-6,COP,.95)}
<div class="abs" style="left:70px;top:50px"><div class="cap" style="color:{COPL}">Your first week at {S['street']}</div><div class="fr" style="font:600 92px/1.02 Fraunces;color:#fff;margin-top:12px">Move-In <i style="font-weight:400;color:{COPL}">Costs</i></div></div>
<div class="abs" style="left:70px;top:310px;width:1084px;font:italic 400 24px/1.5 Fraunces;color:{FOR}">{MOVE['intro']}</div>
<div class="abs" style="left:0;top:430px;width:560px;height:820px;background:{FOR2};padding:44px 40px 0 70px"><div class="cap" style="color:{COPL};margin-bottom:28px">Set up before you arrive</div>{su}</div>
<div class="abs" style="left:610px;top:430px;width:544px;padding-top:44px"><div class="cap" style="margin-bottom:12px">Typical monthly costs</div>{mo}</div>
<div class="abs" style="left:70px;top:1262px;width:1084px;font:400 12.5px/1.5 Karla;color:{MUTE}">{MOVE['fine']}</div>{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def all(): return {'home':home(),'neigh':neigh(),'num':numbers(),'move':move()}
