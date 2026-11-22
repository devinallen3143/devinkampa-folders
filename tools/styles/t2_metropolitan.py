from common import *
import os,json
_P=json.loads(os.environ.get('PAL','{}'))
NAME=_P.get('NAME','metropolitan'); TITLE=NAME
FONTS=[('Oswald','oswald',w,'normal') for w in (400,500,600,700)]+[('Allura','allura',400,'normal')]+[('Lato','lato',w,'normal') for w in (400,700)]
NAVY=_P.get('NAVY','#12233A'); NAVY2=_P.get('NAVY2','#1B3250'); GOLD=_P.get('GOLD','#C9A24D'); CREAM=_P.get('CREAM','#F3EEE4'); SAND=_P.get('SAND','#E7E0D0'); INK=_P.get('INK',NAVY); MUTE=_P.get('MUTE','#5E6A7B')
SOFT=_P.get('SOFT','#C9D2DE'); AVT=_P.get('AVT','#2a4366'); MAPBG=_P.get('MAPBG','#EAE4D6'); MAPGRN=_P.get('MAPGRN','#CBD3B8'); PHC=_P.get('PHC','#D9D2C1'); RULE=_P.get('RULE','#E1DACB')
CSS=f"""
body{{background:{CREAM};color:{INK};font-family:Lato,sans-serif}}
.ph{{background:{PHC}}} .os{{font-family:Oswald,sans-serif;text-transform:uppercase}} .sc{{font-family:Allura,cursive;color:{GOLD}}}
.cap{{font:700 15px Lato;letter-spacing:.3em;text-transform:uppercase;color:{GOLD}}}
.abs{{position:absolute}}
.foot{{position:absolute;left:0;right:0;bottom:54px;height:176px;display:flex}}
.foot .l{{width:640px;background:{CREAM};display:flex;align-items:center;gap:26px;padding:0 60px}}
.foot .r{{flex:1;background:{NAVY};clip-path:polygon(110px 0,100% 0,100% 100%,0 100%);margin-left:-110px;padding:0 30px 0 170px;display:flex;align-items:center;gap:24px;color:#fff}}
.strip{{position:absolute;left:0;right:0;bottom:0;height:54px;background:{GOLD};display:flex;justify-content:center;align-items:center;font:700 15px Lato;letter-spacing:.42em;text-transform:uppercase;color:{NAVY};white-space:nowrap}}
"""
def foot(tag='Schedule a<br>private tour'):
    return f'''<div class="foot"><div class="l"><div style="width:86px;height:86px;border-radius:50%;background:{NAVY};display:grid;place-items:center;flex:none">{icon('cal',40,GOLD,1.5)}</div><div class="os" style="font:600 46px/1.02 Oswald;color:{NAVY}">{tag}</div><div style="font-size:40px;color:{GOLD}">→</div></div>
<div class="r"><div style="width:100px;height:100px;border-radius:50%;background:{AVT};border:3px solid {GOLD};flex:none"></div><div><div class="os" style="font:600 34px Oswald;letter-spacing:.03em;white-space:nowrap">{S['agent']}</div><div class="cap" style="font-size:11px;letter-spacing:.2em;margin:2px 0 6px;white-space:nowrap">{S['agent_t']} · {S['brokerage']}</div><div style="font:400 18px/1.5 Lato;white-space:nowrap">{S['aphone']}<br>{S['aemail']}</div></div></div></div>
<div class="strip">Modern home. Prime location. Better life.</div>'''
def home():
    stats=[('bed',S['beds'],'Beds'),('bath',S['baths'],'Baths'),('sqft',S['sqft'],'Sq Ft'),('garage',S['garage'],'Garage')]
    st=''.join(f'<div style="flex:1;text-align:center;{"border-left:1.5px solid "+GOLD if i else ""}">{icon(ic,38,GOLD,1.4)}<div class="os" style="font:500 40px Oswald;margin-top:4px;color:{NAVY}">{v}</div><div style="font:700 13px Lato;letter-spacing:.22em;text-transform:uppercase;color:{MUTE}">{lb}</div></div>' for i,(ic,v,lb) in enumerate(stats))
    hl=''.join(f'<div style="display:flex;align-items:center;gap:20px;margin-bottom:26px">{icon(ic,34,GOLD,1.4)}<span style="font:400 24px Lato;color:#fff">{t}</span></div>' for ic,t in zip(['home','tree','check','garage'],S['bullets'][:4]))
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:540px;background:{NAVY}"></div>
{ph(430,0,794,540,extra="clip-path:polygon(150px 0,100% 0,100% 100%,0 100%)")}
<div class="abs" style="left:70px;top:62px"><div class="cap" style="font-size:14px">{S['hood']} · {S['city']}, {S['state']}</div></div>
<div class="abs sc" style="left:66px;top:98px;font-size:84px;line-height:1">Open House</div>
<div class="abs os" style="left:70px;top:210px;font:700 90px/.98 Oswald;color:#fff">123 SAMPLE<br>STREET</div>
<div class="abs" style="left:74px;top:430px;font:400 17px Lato;letter-spacing:.22em;text-transform:uppercase;color:{SOFT};width:380px;line-height:1.6">Modern living.<br>Timeless comfort.</div>
<div class="abs" style="left:0;top:540px;width:850px;height:320px;background:{CREAM}"></div>
<div class="abs" style="left:700px;top:540px;width:524px;height:320px;background:{GOLD};clip-path:polygon(130px 0,100% 0,100% 100%,0 100%)"></div>
<div class="abs" style="left:884px;top:588px;color:{NAVY}"><div style="font:700 16px Lato;letter-spacing:.34em;text-transform:uppercase">Offered at</div><div class="os" style="font:700 74px/1.05 Oswald;margin-top:6px">{usd(S['price'])}</div><div style="width:260px;height:2px;background:{NAVY};margin-top:14px"></div></div>
<div class="abs sc" style="left:70px;top:568px;font-size:62px">Modern Residence</div>
<div class="abs os" style="left:72px;top:644px;font:500 38px Oswald;letter-spacing:.06em;display:flex;align-items:center;gap:14px">{icon('pin',32,GOLD,1.6)}{S['street']} · {S['city']}, {S['state']}</div>
<div class="abs" style="left:60px;top:726px;width:700px;display:flex">{st}</div>
{ph(0,860,300,440,extra="clip-path:polygon(0 0,100% 0,calc(100% - 60px) 100%,0 100%)")}{ph(240,860,300,440,extra="clip-path:polygon(60px 0,100% 0,calc(100% - 60px) 100%,0 100%);outline:6px solid {CREAM}")}{ph(480,860,300,440,extra="clip-path:polygon(60px 0,100% 0,calc(100% - 60px) 100%,0 100%)")}
<div class="abs" style="left:690px;top:860px;width:534px;height:440px;background:{NAVY};clip-path:polygon(150px 0,100% 0,100% 100%,0 100%)"></div>
<div class="abs" style="left:830px;top:900px;width:360px"><div class="cap" style="margin-bottom:22px;font-size:17px">Property highlights</div>{hl}</div>
{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def mapsvg():
    pins=[(120,120,'tree','Sample Park'),(300,90,'tree','Creekside Trail'),(470,200,'cart','Grocery'),(130,330,'dine','Local Italian'),(400,380,'coffee','Coffee Shop'),(250,230,None,'')]
    roads='<g stroke="#fff" stroke-width="16" fill="none" stroke-linecap="round"><path d="M0 170H580M0 300H580M200 0V480M400 0V480"/><path d="M0 460L580 40" stroke-width="22"/></g>'
    park=f'<rect x="40" y="50" width="130" height="90" rx="10" fill="{MAPGRN}"/><rect x="420" y="320" width="120" height="110" rx="10" fill="{MAPGRN}"/>'
    p=''
    for x,y,ic,lb in pins:
        if ic is None:
            p+=f'<circle cx="{x}" cy="{y}" r="26" fill="{NAVY}" stroke="{GOLD}" stroke-width="4"/><path transform="translate({x-13},{y-13}) scale(1.08)" d="{IC["home"]}" fill="none" stroke="{GOLD}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><text x="{x}" y="{y+52}" text-anchor="middle" font-family="Oswald" font-weight="600" font-size="19" fill="{NAVY}" letter-spacing="1.5">HOME</text>'
        else:
            p+=f'<circle cx="{x}" cy="{y}" r="22" fill="{GOLD}"/><path transform="translate({x-11},{y-11}) scale(.92)" d="{IC[ic]}" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><text x="{x}" y="{y+44}" text-anchor="middle" font-family="Lato" font-weight="700" font-size="15" fill="{NAVY}">{lb}</text>'
    return f'<svg width="580" height="480" viewBox="0 0 580 480" style="display:block"><rect width="580" height="480" fill="{MAPBG}"/>{park}{roads}{p}</svg>'
def neigh():
    def col(x,ic,title,items,mi=False):
        rows=''.join(f'<div style="margin-bottom:14px;display:flex;justify-content:space-between;gap:10px"><div><div style="font:700 19px Lato;color:{NAVY}">{i[0]}</div><div style="font:400 14.5px Lato;color:{MUTE}">{i[1]}</div></div>{"<div class=os style=font-size:19px;color:"+GOLD+">"+i[2]+"</div>" if mi else ""}</div>' for i in items)
        return f'<div class="abs" style="left:{x}px;top:860px;width:340px;background:#fff;padding:26px 26px 14px;clip-path:polygon(0 0,calc(100% - 34px) 0,100% 34px,100% 100%,0 100%);border-top:6px solid {GOLD};min-height:330px"><div style="display:flex;align-items:center;gap:14px;margin-bottom:16px">{icon(ic,34,GOLD,1.5)}<div class="os" style="font:600 25px Oswald;letter-spacing:.06em;color:{NAVY}">{title}</div></div>{rows}</div>'
    drv=''.join(f'<div style="flex:1;text-align:center;{"border-left:1.5px solid "+GOLD if i else ""}"><div class="os" style="font:600 40px Oswald;color:{GOLD}">{t}</div><div style="font:700 12px Lato;letter-spacing:.14em;text-transform:uppercase;color:#fff;margin-top:2px">{n}</div></div>' for i,(n,t) in enumerate(NEIGH['drive']))
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:270px;background:{NAVY}"></div>{ph(700,0,524,270,extra="clip-path:polygon(110px 0,100% 0,100% 100%,0 100%)")}
<div class="abs os" style="left:70px;top:46px;font:700 100px/1 Oswald;color:#fff">Neighborhood</div><div class="abs sc" style="left:78px;top:140px;font-size:96px;line-height:1">Highlights</div>
<div class="abs" style="left:60px;top:310px;width:600px;height:500px;box-shadow:0 0 0 6px #fff,0 8px 24px rgba(0,0,0,.12);overflow:hidden;transform-origin:0 0"><div style="transform:scale(1.034);transform-origin:0 0;width:580px;height:480px">{mapsvg()}</div></div>
<div class="abs" style="left:700px;top:310px;width:470px"><div class="cap" style="margin-bottom:12px">{S['hood']} · {S['city']}, {S['state']}</div><div style="font:400 23px/1.45 Lato;color:{INK}">{NEIGH['intro']}</div>
<div style="margin-top:22px;background:{NAVY};padding:18px 30px 12px;clip-path:polygon(0 0,100% 0,100% calc(100% - 30px),calc(100% - 30px) 100%,0 100%)"><div class="cap" style="margin-bottom:12px">Drive times</div>{''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid rgba(255,255,255,.14);padding:4px 0"><span style="font:400 16px Lato;color:#fff;text-transform:uppercase;letter-spacing:.12em">{n}</span><span class=os style="font:600 24px Oswald;color:{GOLD}">{t}</span></div>' for n,t in NEIGH['drive'])}</div></div>
{col(60,'tree','Parks &amp; Trails',NEIGH['parks'][:4])}{col(442,'cart','Everyday Errands',NEIGH['errands'][:4],True)}{col(824,'dine','Eat &amp; Drink',NEIGH['eat'][:4])}{foot('Love where<br>you live')}'''
    return page(fontcss(FONTS),CSS,body)
def numbers():
    cards=''
    for i,c in enumerate(CARDS):
        x=60+i*(356+20)
        rows=f'<div class="r"><span>Down payment</span><b>{usd(c["down"])}</b></div><div class="r"><span>Est. closing costs</span><b>{usd(c["closing"])}</b></div><div class="r"><span>Seller credit{" ("+str(c["credit_pct"])+"%)" if c["credit"] else ""}</span><b>{"–"+usd(c["credit"]) if c["credit"] else "$0"}</b></div>'
        cards+=f'''<div class="abs" style="left:{x}px;top:420px;width:356px;height:620px;background:{NAVY};clip-path:polygon(0 0,calc(100% - 40px) 0,100% 40px,100% 100%,0 100%)"><div style="position:absolute;inset:3px;background:#fff;clip-path:polygon(0 0,calc(100% - 38px) 0,100% 38px,100% 100%,0 100%)">
<div style="background:{GOLD};padding:14px 24px"><div style="font:700 13px Lato;letter-spacing:.24em;text-transform:uppercase;color:{NAVY}">{c['tag']}</div></div>
<div style="padding:22px 24px 0"><div class="os" style="font:500 30px/1.12 Oswald;color:{NAVY}">{c['title']}<br>{c['title2']}</div><div style="font:700 12px Lato;letter-spacing:.2em;text-transform:uppercase;color:{MUTE};margin-top:18px">Est. monthly payment</div><div class="os" style="font:700 66px/1.1 Oswald;color:{NAVY}">{usd(c['mo'])}<span style="font:400 22px Lato;color:{MUTE}">/mo</span></div><div style="margin-top:12px">{rows}</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:140px;background:{NAVY};padding:24px"><div style="font:700 12px Lato;letter-spacing:.2em;text-transform:uppercase;color:{GOLD}">Est. cash to close</div><div class="os" style="font:700 56px Oswald;color:#fff">{usd(c['cash'])}</div></div></div></div>'''
    dl=''.join(f'<div style="flex:1;display:flex;align-items:center;gap:20px"><span class="os" style="font:700 50px Oswald;color:{GOLD};white-space:nowrap">{a}</span><span style="font:400 19px/1.4 Lato">{b}</span></div>' for a,b in DELTAS)
    css=CSS+f".r{{display:flex;justify-content:space-between;font:400 18px Lato;padding:10px 0;border-top:1px solid {RULE}}} .r b{{font-weight:700;color:{NAVY}}}"
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:370px;background:{NAVY}"></div>{ph(640,0,584,370,extra="clip-path:polygon(120px 0,100% 0,100% 100%,0 100%)")}
<div class="abs os" style="left:64px;top:44px;font:700 112px/1 Oswald;color:#fff">The Numbers</div>
<div class="abs sc" style="left:70px;top:166px;font-size:70px;line-height:1">sample figures</div>
<div class="abs" style="left:70px;top:276px;font:700 18px Lato;letter-spacing:.2em;text-transform:uppercase;color:#fff;line-height:1.7">{S['full']}<br><span style="color:{SOFT};font-weight:400">{usd(S['price'])} · {S['beds']} BD · {S['baths']} BA · {S['sqft']} SF</span></div>
{cards}
<div class="abs" style="left:60px;top:1070px;width:1104px;display:flex;gap:40px;padding:0 0 20px;border-bottom:2px solid {GOLD}">{dl}</div>
<div class="abs" style="left:60px;top:1170px;width:1104px;font:400 13px/1.55 Lato;color:{MUTE}">{DISC}</div>
<div class="abs" style="left:0;right:0;top:1330px;height:180px;display:flex"><div style="width:640px;background:{CREAM};padding:20px 60px"><div class="os" style="font:600 36px Oswald;color:{NAVY}">{S['agent']}</div><div style="font:400 17px/1.55 Lato;color:{MUTE}">{S['agent_t']} · {S['brokerage']}<br><b style="color:{INK}">{S['aphone']}</b><br>{S['aemail']}</div></div>
<div style="flex:1;background:{NAVY};clip-path:polygon(100px 0,100% 0,100% 100%,0 100%);margin-left:-100px;padding:20px 40px 0 180px;display:flex;gap:24px;color:#fff"><img src="{HS}" style="width:124px;height:124px;border-radius:50%;object-fit:cover;border:3px solid {GOLD}"><div><div class="os" style="font:600 36px Oswald">{LO['name']}</div><div style="font:400 17px/1.55 Lato;color:{SOFT}">{LO['t']}<br><b style="color:#fff">{LO['phone']}</b><br>{LO['email']}</div></div></div></div>
<div class="strip" style="height:74px;bottom:0;font-size:19px;letter-spacing:.06em;text-transform:none;font-weight:400">Need estimates on another home? Call or text Devin&nbsp;<b>{LO['phone']}</b>&nbsp;· {LO['web']}</div>'''
    return page(fontcss(FONTS),css,body)
def move():
    su=''.join(f'<div style="display:flex;gap:22px;align-items:flex-start;margin-bottom:34px"><div class="os" style="width:54px;height:54px;border-radius:50%;background:{GOLD};color:{NAVY};display:grid;place-items:center;font:700 26px Oswald;flex:none">{i+1}</div><div style="flex:1"><div style="font:700 22px Lato;color:#fff">{a}</div><div style="font:400 16px/1.4 Lato;color:{SOFT}">{c}</div></div><div class="os" style="font:500 22px Oswald;color:{GOLD};text-align:right;width:130px;line-height:1.2">{d}</div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
    mo=''
    for a,b,lo,hi in MOVE['monthly']:
        if lo:
            mo+=f'<div style="margin-bottom:26px"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font:700 21px Lato;color:{NAVY}">{a}</span><span class="os" style="font:600 26px Oswald;color:{NAVY}">${lo}–${hi}</span></div><div style="height:12px;background:{RULE};margin:8px 0 6px;position:relative"><div style="position:absolute;left:{lo/4}%;width:{(hi-lo)/4}%;top:0;bottom:0;background:{GOLD}"></div></div><div style="font:400 14.5px Lato;color:{MUTE}">{b}</div></div>'
        else:
            mo+=f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font:700 21px Lato;color:{NAVY}">{a}</span><span class="os" style="font:600 24px Oswald;color:{NAVY}">{MOVE["hoa"]}</span></div><div style="font:400 14.5px Lato;color:{MUTE}">{b}</div>'
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:300px;background:{NAVY}"></div>{ph(700,0,524,300,extra="clip-path:polygon(110px 0,100% 0,100% 100%,0 100%)")}
<div class="abs" style="left:70px;top:44px"><div class="cap" style="font-size:14px">Your first week at {S['street']}</div></div>
<div class="abs os" style="left:68px;top:78px;font:700 110px/1 Oswald;color:#fff">Move-In</div><div class="abs sc" style="left:440px;top:150px;font-size:96px;line-height:1">Costs</div>
<div class="abs" style="left:70px;top:340px;width:1084px;font:400 22px/1.55 Lato;color:{INK}">{MOVE['intro']}</div>
<div class="abs" style="left:0;top:468px;width:640px;height:760px;background:{NAVY};padding:46px 40px 0 70px;clip-path:polygon(0 0,100% 0,calc(100% - 60px) 100%,0 100%)"><div class="cap" style="margin-bottom:30px;font-size:17px">Set up before you arrive</div>{su}</div>
<div class="abs" style="left:680px;top:468px;width:484px;height:760px;padding-top:46px"><div class="cap" style="margin-bottom:30px;font-size:17px;color:{NAVY}">Typical monthly costs</div>{mo}</div>
<div class="abs" style="left:70px;top:1250px;width:1084px;font:400 13px/1.5 Lato;color:{MUTE}">{MOVE['fine']}</div>{foot('Your move,<br>made easy')}'''
    return page(fontcss(FONTS),CSS,body)
def all(): return {'home':home(),'neigh':neigh(),'num':numbers(),'move':move()}
