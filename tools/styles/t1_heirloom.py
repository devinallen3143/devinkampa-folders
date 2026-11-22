from common import *
NAME='heirloom'; TITLE='Heirloom'
FONTS=[('Playfair','playfair-display',w,'normal') for w in (400,500,600,700)]+[('Playfair','playfair-display',400,'italic')]+[('Jost','jost',w,'normal') for w in (300,400,500,600)]
NAVY='#141C2B'; NAVY2='#1d2a43'; GOLD='#B8915A'; GOLDL='#D9BC87'; CREAM='#F8F3EA'; INK='#1B2233'; MUTE='#6C7080'; TINT='#EFE6D3'
CSS=f"""
body{{background:{CREAM};color:{INK};font-family:Jost,sans-serif}}
.ph{{background:#E8E0CF}} .frame{{position:absolute;inset:24px;border:1.5px solid {GOLD};pointer-events:none;z-index:9}}
.cap{{font:500 15px Jost;letter-spacing:.34em;text-transform:uppercase;color:{GOLD}}}
.pf{{font-family:Playfair,serif}} .gold{{color:{GOLD}}}
.dia{{display:inline-block;width:9px;height:9px;background:{GOLD};transform:rotate(45deg);margin-right:14px;flex:none}}
.foot{{position:absolute;left:24px;right:24px;bottom:24px;height:132px;background:{NAVY};color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 56px;z-index:8}}
.foot .n{{font:500 36px Playfair;letter-spacing:.01em}} .foot .r{{font:400 15px Jost;letter-spacing:.3em;text-transform:uppercase;color:{GOLDL};margin-top:8px}}
.foot .c{{text-align:right;font:400 20px Jost;line-height:1.6;letter-spacing:.03em}} .foot .c b{{color:{GOLDL};font-weight:500;margin-right:10px}}
.rule{{height:1.5px;background:{GOLD}}}
"""
def foot():
    return f'<div class="foot"><div><div class="n">{S["agent"]}</div><div class="r">{S["agent_t"]} · {S["brokerage"]}</div></div><div class="c"><div><b>T</b>{S["aphone"]}</div><div><b>E</b>{S["aemail"]}</div></div></div>'
def orn(w=360):
    return f'<div style="display:flex;align-items:center;justify-content:center;gap:16px;width:{w}px;margin:0 auto"><div class="rule" style="flex:1"></div><span class="dia" style="margin:0"></span><div class="rule" style="flex:1"></div></div>'
def home():
    stats=[('bed',S['beds'],'Bedrooms'),('bath',S['baths'],'Bathrooms'),('sqft',S['sqft'],'Sq Ft'),('garage',S['garage'],'Car Garage')]
    st=''.join(f'<div style="flex:1;text-align:center;{"border-left:1px solid "+GOLD if i else ""}">{icon(ic,40,GOLDL,1.3)}<div class="pf" style="font-size:46px;color:{GOLDL};margin:6px 0 4px;font-weight:400">{v}</div><div style="font:400 14px Jost;letter-spacing:.3em;text-transform:uppercase;color:#fff">{lb}</div></div>' for i,(ic,v,lb) in enumerate(stats))
    bl=''.join(f'<div style="display:flex;align-items:center;font:400 24px Jost;margin:0 0 13px"><span class="dia"></span>{b}</div>' for b in S['bullets'])
    body=f'''<div class="frame"></div>
{ph(520,24,680,720)}<div style="position:absolute;left:520px;top:24px;width:340px;height:720px;background:linear-gradient(90deg,{CREAM},rgba(248,243,234,0))"></div>
<div style="position:absolute;left:1004px;top:24px;width:196px;height:230px;background:{NAVY};clip-path:polygon(0 0,100% 0,100% 100%,50% 88%,0 100%);color:#fff;text-align:center;padding-top:50px;z-index:5"><div class="pf" style="font-size:36px;line-height:1.15;letter-spacing:.06em">OPEN<br>HOUSE</div><div style="width:64px;height:1.5px;background:{GOLD};margin:16px auto 0"></div></div>
<div style="position:absolute;left:84px;top:96px"><div class="cap" style="font-size:14px">{S['hood']} · {S['city']}, Texas</div></div>
<div class="pf" style="position:absolute;left:80px;top:170px;font-size:104px;line-height:.98;font-weight:500;color:{NAVY};letter-spacing:.005em">123<br>SAMPLE</div>
<div class="pf" style="position:absolute;left:80px;top:384px;font-size:104px;line-height:.98;font-weight:500;color:{GOLD};letter-spacing:.005em">STREET</div>
<div class="rule" style="position:absolute;left:84px;top:540px;width:120px"></div>
<div style="position:absolute;left:84px;top:572px;font:400 22px/1.7 Jost;letter-spacing:.2em;text-transform:uppercase;color:{INK}">A home to come<br>home to.</div>
<div style="position:absolute;left:84px;top:690px;display:flex;align-items:center;gap:16px;font:400 18px Jost;letter-spacing:.16em;text-transform:uppercase">{icon('pin',30,GOLD,1.5)}<div>{S['street']}<br>{S['city']}, {S['state']} {S['zip']}</div></div>
<div style="position:absolute;left:24px;top:790px;width:1090px;height:176px;background:{NAVY};display:flex;align-items:center;padding:0 20px;box-shadow:inset 0 0 0 1.5px {GOLD};outline:1.5px solid {GOLD};outline-offset:-9px">{st}</div>
<div style="position:absolute;left:84px;top:1024px;width:480px"><div class="cap" style="margin-bottom:16px">About the home</div><div class="pf" style="font:italic 400 28px/1.55 Playfair;color:{INK}">{S['about']}</div><div style="margin-top:34px" class="cap">Offered at</div><div class="pf" style="font-size:60px;color:{NAVY};font-weight:500;margin-top:4px">{usd(S['price'])}</div></div>
<div style="position:absolute;left:660px;top:1016px;width:480px">{bl}</div>{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def neigh():
    def lst(items,mi=False):
        return ''.join(f'<div style="display:flex;justify-content:space-between;gap:16px;margin-bottom:11px"><div><div style="font:500 20px Jost;color:{NAVY}">{i[0]}</div><div style="font:400 15.5px Jost;color:{MUTE};margin-top:1px">{i[1]}</div></div>{"<div class=pf style=color:"+GOLD+";font-size:20px>"+i[2]+"</div>" if mi else ""}</div>' for i in items)
    def card(x,y,ic,title,inner):
        return f'<div style="position:absolute;left:{x}px;top:{y}px;width:520px"><div style="display:flex;align-items:center;gap:18px;margin-bottom:16px"><div style="width:64px;height:64px;border:1.5px solid {GOLD};border-radius:50%;display:grid;place-items:center;color:{GOLD}">{icon(ic,30,GOLD,1.4)}</div><div class="cap" style="color:{NAVY};font-size:17px">{title}</div></div><div class="rule" style="margin-bottom:18px"></div>{inner}</div>'
    drv=''.join(f'<div style="display:flex;align-items:baseline;gap:14px;margin-bottom:6px"><span class="pf" style="font-size:28px;color:{GOLD};width:96px">{t}</span><span style="font:500 15px Jost;letter-spacing:.2em;text-transform:uppercase;color:{NAVY}">{n}</span></div>' for n,t in NEIGH['drive'])
    body=f'''<div class="frame"></div>{ph(24,24,1176,236)}
<div style="position:absolute;left:0;right:0;top:290px;text-align:center"><div class="cap">{S['hood']} · {S['city']}, Texas</div><div class="pf" style="font-size:80px;font-weight:500;color:{NAVY};margin:14px 0 18px">Neighborhood Highlights</div>{orn(420)}<div style="font:italic 400 27px/1.5 Playfair;color:{INK};max-width:900px;margin:22px auto 0">{NEIGH['intro']}</div></div>
{card(84,664,'tree','Parks &amp; Trails',lst(NEIGH['parks']))}{card(620,664,'cart','Everyday Errands',lst(NEIGH['errands'][:4],True))}
{card(84,1012,'dine','Eat &amp; Drink',lst([(a,b) for a,b in NEIGH['eat'][:3]]))}{card(620,1012,'clock','Drive Times',drv)}{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def numbers():
    cols=''
    for i,c in enumerate(CARDS):
        x=72+i*(352+24)
        rows=f'<div class="row"><span>Down payment</span><b>{usd(c["down"])}</b></div><div class="row"><span>Est. closing costs</span><b>{usd(c["closing"])}</b></div>'+(f'<div class="row"><span>Seller credit ({c["credit_pct"]}%)</span><b>–{usd(c["credit"])}</b></div>' if c['credit'] else f'<div class="row"><span>Seller credit</span><b>$0</b></div>')
        cols+=f'''<div class="card" style="left:{x}px"><div class="cap" style="font-size:13px;letter-spacing:.26em;color:{GOLD}">{c['tag']}</div><div style="font:500 25px/1.25 Jost;color:{NAVY};margin:12px 0 22px">{c['title']}<br>{c['title2']}</div><div class="cap" style="font-size:12px;color:{MUTE};letter-spacing:.24em">Est. monthly payment</div><div class="pf" style="font-size:60px;font-weight:700;color:{NAVY};line-height:1.15;margin:4px 0 14px">{usd(c['mo'])}<span style="font:400 22px Jost;color:{MUTE}">/mo</span></div>{rows}<div class="cash"><div class="cap" style="font-size:12px;letter-spacing:.24em;color:{MUTE}">Est. cash to close</div><div class="pf" style="font-size:46px;font-weight:700;color:{NAVY}">{usd(c['cash'])}</div></div></div>'''
    css=CSS+f""".card{{position:absolute;top:410px;width:352px;height:610px;background:#fff;border:1.5px solid {GOLD};padding:28px 26px 0;outline:1px solid {GOLD};outline-offset:-9px}}
.row{{display:flex;justify-content:space-between;font:400 18px Jost;padding:11px 0;border-top:1px solid #e6dcc6}} .row b{{font-weight:600;color:{NAVY}}}
.cash{{position:absolute;left:0;right:0;bottom:0;height:132px;background:{TINT};padding:22px 26px;border-top:1.5px solid {GOLD}}}"""
    dl=''.join(f'<div style="display:flex;align-items:center;gap:22px;width:540px"><span class="pf" style="font-size:44px;color:{GOLD};font-weight:500;white-space:nowrap">{a}</span><span style="font:400 19px/1.4 Jost;color:{INK}">{b}</span></div>' for a,b in DELTAS)
    body=f'''<div class="frame"></div>{ph(24,24,392,330)}{ph(424,24,392,330)}{ph(824,24,376,330)}
<div style="position:absolute;left:72px;top:238px;width:700px;height:150px;background:{NAVY};outline:1.5px solid {GOLD};outline-offset:-10px;display:grid;place-items:center"><div class="pf" style="font-size:88px;font-weight:500;color:#fff;letter-spacing:.01em">The Numbers</div></div>
<div style="position:absolute;left:800px;top:402px;width:352px;text-align:right"></div>
<div style="position:absolute;left:72px;top:388px;width:1080px;display:none"></div>
{cols.replace('top:410px','')}
<div style="position:absolute;left:72px;top:1052px;width:1080px;display:flex;justify-content:space-between;border-top:1.5px solid {GOLD};padding-top:26px">{dl}</div>
<div style="position:absolute;left:72px;top:1156px;width:1080px;font:400 13px/1.55 Jost;color:{MUTE}">{DISC}</div>
<div style="position:absolute;left:72px;top:1308px;width:1080px;display:flex;justify-content:space-between;align-items:center">
 <div><div class="pf" style="font-size:36px;color:{NAVY}">{S['agent']}</div><div style="font:400 17px/1.55 Jost;color:{MUTE}">{S['agent_t']} · {S['brokerage']}<br><b style="color:{INK};font-weight:600">{S['aphone']}</b><br>{S['aemail']}</div></div>
 <div style="display:flex;align-items:center;gap:26px"><img src="{HS}" style="width:130px;height:130px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 2px {GOLD}"><div><div class="pf" style="font-size:36px;color:{NAVY}">{LO['name']}</div><div style="font:400 17px/1.55 Jost;color:{MUTE}">{LO['t']}<br><b style="color:{INK};font-weight:600">{LO['phone']}</b><br>{LO['email']}</div></div></div></div>
<div style="position:absolute;left:24px;right:24px;bottom:24px;height:74px;background:{NAVY};color:#fff;display:flex;justify-content:center;align-items:center;gap:10px;font:400 20px Jost;letter-spacing:.02em;white-space:nowrap">Need estimates on another home? Call or text Devin <b style="color:{GOLDL};margin:0 8px;font-weight:600">{LO['phone']}</b> · {LO['web']}</div>'''
    # cards need top: restore
    body=body.replace('class="card" style="left:','class="card" style="top:410px;left:')
    return page(fontcss(FONTS),css,body)
def move():
    su=''.join(f'<div style="display:flex;align-items:center;gap:26px;padding:17px 0;border-top:1px solid #e3d8c0"><div class="pf" style="width:54px;height:54px;border:1.5px solid {GOLD};border-radius:50%;display:grid;place-items:center;font-size:22px;color:{GOLD};flex:none">{["I","II","III","IV"][i]}</div><div style="width:300px"><div style="font:500 22px Jost;color:{NAVY}">{a}</div><div style="font:400 15px Jost;color:{MUTE}">{b}</div></div><div style="flex:1;font:400 18px/1.4 Jost">{c}</div><div class="pf" style="font-size:26px;color:{NAVY};text-align:right;width:210px">{d}</div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
    mo=''
    for a,b,lo,hi in MOVE['monthly']:
        amt=f'${lo} to ${hi}' if lo else MOVE['hoa']
        mo+=f'<div style="display:flex;align-items:center;gap:26px;padding:14px 0;border-top:1px solid #e3d8c0"><div style="width:354px"><div style="font:500 22px Jost;color:{NAVY}">{a}</div></div><div style="flex:1;font:400 17px/1.4 Jost;color:{MUTE}">{b}</div><div class="pf" style="font-size:26px;color:{NAVY};text-align:right;width:210px">{amt}</div></div>'
    body=f'''<div class="frame"></div>{ph(24,24,1176,190)}
<div style="position:absolute;left:72px;top:238px;width:1080px"><div class="cap">Your first week at {S['street']}</div><div class="pf" style="font-size:80px;font-weight:500;color:{NAVY};margin:10px 0 16px">Move-In Costs</div><div class="rule" style="width:140px"></div><div style="font:italic 400 24px/1.55 Playfair;margin:20px 0 26px">{MOVE['intro']}</div>
<div class="cap" style="color:{NAVY};font-size:17px;margin-bottom:12px">Set up before you arrive</div><div class="rule"></div>{su}
<div class="cap" style="color:{NAVY};font-size:17px;margin:34px 0 12px">Typical monthly costs</div><div class="rule"></div>{mo}
<div style="font:400 12.5px/1.5 Jost;color:{MUTE};margin-top:18px;border-top:1px solid #e3d8c0;padding-top:14px">{MOVE['fine']}</div></div>{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def all(): return {'home':home(),'neigh':neigh(),'num':numbers(),'move':move()}
