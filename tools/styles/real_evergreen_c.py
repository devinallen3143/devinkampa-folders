import os, io, base64
import common
from common import render, page, fontcss, icon, usd, S, NEIGH, MOVE, CARDS, DELTAS, HS, LO
import real_evergreen as R          # loads real data, photos P, mapdata()
import t5_evergreen as t5
from t5_evergreen import CSS, FONTS, FOR, FOR2, COP, COPL, CREAM, SAGE, INK, MUTE
t5.DISC=R.DISC
P=R.P
LAB={'ext':'Digitally Altered','kit':'Digitally Altered','liv':'Digitally Altered','bbq':'Digitally Altered','aer':'Digitally Altered','prim':'Virtually Staged','sun':None}
def pic(key,x,y,w,h,pos='50% 50%',extra=''):
    lab=LAB[key]
    tag=f'<span style="position:absolute;right:8px;bottom:6px;font:600 11px sans-serif;color:#fff;background:rgba(0,0,0,.55);padding:2px 7px;border-radius:3px">{lab}</span>' if lab else ''
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:url({P[key]}) {pos}/cover no-repeat;{extra}">{tag}</div>'
# ---- t5-driven pages (neighborhood, move-in) ----
MAP=(580,480); MURI=R.mapdata(580,480)
def mapsvg():
    ink=FOR; pins=''
    for ic,dx,dy in [('tree',-18,-47),('tree',-177,57),('cart',-267,-72),('cart',-270,-140)]:
        px,py=365+dx,265+dy
        pins+=f'<div style="position:absolute;left:{px-19}px;top:{py-19}px;width:38px;height:38px;border-radius:50%;background:{FOR};border:3px solid #fff;display:grid;place-items:center">{icon(ic,20,COPL,1.8)}</div>'
    home=f'<div style="position:absolute;left:{365-24}px;top:{265-24}px;width:48px;height:48px;border-radius:50%;background:{COP};border:4px solid #fff;display:grid;place-items:center">{icon("home",24,"#fff",1.8)}</div>'
    cap='<div style="position:absolute;right:6px;bottom:6px;font:600 10px sans-serif;color:#555;background:rgba(255,255,255,.85);padding:2px 5px">Map © OpenStreetMap contributors · pins approximate</div>'
    return f'<div style="position:relative;width:580px;height:480px;background:url({MURI}) center/cover">{pins}{home}{cap}</div>'
t5.mapsvg=mapsvg
SL={(790,0,434,290):('aer','50% 45%'),(820,0,404,280):('prim','45% 55%')}
def ph5(x,y,w,h,cls='ph',extra=''):
    k=SL.get((x,y,w,h))
    return pic(k[0],x,y,w,h,k[1],extra) if k else ''
t5.ph=ph5
def strip(y,keys,h=130):
    n=len(keys); gap=14; w=(1084-gap*(n-1))//n
    return ''.join(pic(k,70+i*(w+gap),y,w,h,pos,'border:5px solid #fff;box-sizing:border-box;box-shadow:0 0 0 1.5px '+COP) for i,(k,pos) in enumerate(keys))
def neigh():
    h=t5.neigh()
    return h.replace('<div class="foot">',strip(1215,[('bbq','50% 60%'),('sun','50% 50%'),('ext','50% 60%')],200)+'<div class="foot">',1)
def move():
    h=t5.move()
    h=h.replace('height:820px','height:930px').replace('top:1262px','top:1372px')
    h=h.replace('lo/4}%','lo/8}%').replace('(hi-lo)/4}%','(hi-lo)/8}%')
    tot=f'<div class="abs" style="left:650px;top:940px;width:504px;border-top:2px solid {COP};padding:14px 0;display:flex;justify-content:space-between;align-items:baseline"><span style="font:700 14px Karla;letter-spacing:.16em;text-transform:uppercase">Utilities total<span style="font-weight:400;letter-spacing:0;text-transform:none;color:{MUTE}"> · excl. HOA</span></span><span class="fr" style="font:700 30px Fraunces;color:{FOR}">$660–$1,340</span></div>'+pic('sun',650,1032,504,308,'50% 50%','border:6px solid #fff;box-sizing:border-box;box-shadow:0 0 0 1.5px '+COP)
    h=h.replace('<div class="foot">',pic('ext',70,940,440,400,'55% 55%','border:6px solid #fff;box-sizing:border-box;box-shadow:0 0 0 1.5px '+COPL)+tot+'<div class="foot">',1)
    return h
# ---- Home: hero fades into cream ----
def home():
    stats=[('bed',S['beds'],'Beds'),('bath',S['baths'],'Baths'),('sqft',S['sqft'],'Sq ft'),('garage',S['garage'],'Garage')]
    st=''.join(f'<div style="flex:1;text-align:center;{"border-left:1px solid "+COP if i else ""}">{icon(ic,36,COPL,1.4)}<div class="fr" style="font:600 40px Fraunces;color:#fff;margin:4px 0 2px">{v}</div><div style="font:700 12px Karla;letter-spacing:.24em;text-transform:uppercase;color:{COPL}">{lb}</div></div>' for i,(ic,v,lb) in enumerate(stats))
    bl=''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:9px;font:500 19px Karla"><span style="width:11px;height:11px;background:{COP};transform:rotate(45deg);flex:none"></span>{b}</div>' for b in S['bullets'])
    body=f'''{pic('ext',0,0,1224,720,'50% 42%')}
<div class="abs" style="left:0;top:0;width:1224px;height:720px;background:linear-gradient(180deg,rgba(247,242,232,0) 38%,rgba(247,242,232,.82) 74%,{CREAM} 100%)"></div>
<div class="abs" style="left:70px;top:0;width:176px;height:96px;background:{FOR};border-bottom:5px solid {COP};text-align:center;padding-top:20px;box-sizing:border-box"><div class="fr" style="font:600 25px/1.15 Fraunces;color:#fff;letter-spacing:.08em">OPEN<br>HOUSE</div></div>
<div class="abs" style="left:70px;top:556px"><div class="cap">{S['hood']} · {S['city']}, Texas</div><div class="fr" style="font:600 84px/1.04 Fraunces;color:{FOR};margin-top:8px;white-space:nowrap">{S['street']}</div><div style="display:flex;align-items:center;gap:18px;margin-top:6px"><div style="width:90px;height:4px;background:{COP}"></div><div class="fr" style="font:italic 400 25px Fraunces;color:{MUTE}">{S['city']}, {S['state']} {S['zip']}</div></div></div>
<div class="abs" style="left:70px;top:778px;width:1084px;height:122px;background:{FOR};display:flex;align-items:center;padding:0 20px;box-sizing:border-box;box-shadow:inset 0 0 0 1.5px {COP}">{st}</div>
<div class="abs" style="left:70px;top:932px;width:520px"><div class="cap">Offered at</div><div class="fr" style="font:700 80px/1.05 Fraunces;color:{FOR}">{usd(S['price'])}</div><div style="width:120px;height:4px;background:{COP};margin:12px 0 18px"></div><div style="font:italic 400 23px/1.5 Fraunces;color:{INK}">{S['about']}</div></div>
<div class="abs" style="left:630px;top:932px;width:524px;padding:26px 34px 12px;background:{SAGE};box-sizing:border-box"><div class="cap" style="margin-bottom:16px">Home highlights</div>{bl}</div>
{strip(1288,[('kit','45% 55%'),('liv','45% 45%'),('bbq','50% 60%')],130)}{t5.foot()}'''
    return page(fontcss(FONTS),CSS,body)
# ---- Numbers: one card + photo ----
def numbers():
    c=CARDS[0]
    def r(a,b,bold=False): return f'<div class="r"><span>{a}</span><b>{b}</b></div>'
    card=f'''<div class="abs" style="left:60px;top:360px;width:540px;height:700px;background:#fff;border:2px solid {FOR};outline:2px solid {COP};outline-offset:-10px;box-sizing:border-box">
<div style="background:{FOR};padding:18px 30px"><div class="cap" style="color:{COPL};font-size:12px">{c['tag']}</div><div class="fr" style="font:600 28px Fraunces;color:#fff;margin-top:4px">{c['title']} · {c['title2']}</div></div>
<div style="padding:16px 30px 0"><div class="cap" style="font-size:12px">Est. monthly payment</div><div class="fr" style="font:700 58px/1.1 Fraunces;color:{FOR}">{usd(c['mo'])}<span style="font:500 22px Karla;color:{MUTE}">/mo</span></div>
{r('Principal &amp; interest',usd(c['pi']))}{r('Property taxes',usd(c['tax']))}{r('Home insurance','$650')}{r('Mortgage insurance','$0')}
<div class="cap" style="font-size:12px;margin:16px 0 2px">Up-front costs</div>
{r('Down payment',usd(c['down']))}{r('Est. closing costs',usd(c['closing']))}{r('Seller title credit','–'+usd(c['credit']))}</div>
<div style="position:absolute;left:10px;right:10px;bottom:10px;height:122px;background:{FOR};padding:20px 26px;color:#fff;box-sizing:border-box"><div class="cap" style="color:{COPL};font-size:12px">Est. cash to close</div><div class="fr" style="font:700 54px Fraunces">{usd(c['cash'])}</div></div></div>'''
    dl=''.join(f'<div style="flex:1;display:flex;align-items:center;gap:18px"><span class="fr" style="font:700 44px Fraunces;color:{COP};white-space:nowrap">{a}</span><span style="font:500 18px/1.4 Karla">{b}</span></div>' for a,b in DELTAS)
    css=CSS+f".r{{display:flex;justify-content:space-between;font:500 18px Karla;padding:9px 0;border-top:1px solid #D9D3C2}} .r b{{font-weight:700;color:{FOR}}}"
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:320px;background:{FOR}"></div>{pic('sun',760,0,464,320,'50% 50%')}
<div class="abs" style="left:70px;top:54px"><div class="cap" style="color:{COPL}">Example figures · {S['full']}</div><div class="fr" style="font:600 100px/1.02 Fraunces;color:#fff;margin-top:12px">The Numbers</div><div style="font:500 21px Karla;color:{COPL};margin-top:12px">{usd(S['price'])} · {S['beds']} BD · {S['baths']} BA · {S['sqft']} SF</div></div>
{card}{pic('bbq',630,360,534,700,'60% 55%','border:6px solid #fff;box-sizing:border-box;box-shadow:0 0 0 2px '+COP)}
<div class="abs" style="left:60px;top:1090px;width:1104px;display:flex;gap:36px;padding:16px 0;border-top:2px solid {COP};border-bottom:2px solid {COP}">{dl}</div>
<div class="abs" style="left:60px;top:1196px;width:1104px;font:400 12.5px/1.5 Karla;color:{MUTE}">{R.DISC}</div>
<div class="abs" style="left:60px;top:1360px;width:1104px;display:flex;justify-content:space-between;align-items:center"><div style="border-left:5px solid {COP};padding-left:20px"><div class="fr" style="font:600 28px Fraunces;color:{FOR}">{S['agent']}</div><div style="font:400 15px/1.5 Karla;color:{MUTE}">{S['agent_t']} · {S['brokerage']}<br>{S['aphone']} · {S['aemail']}</div></div><div style="display:flex;align-items:center;gap:18px"><img src="{HS}" style="width:84px;height:84px;border-radius:50%;object-fit:cover;border:3px solid {COP}"><div><div class="fr" style="font:600 28px Fraunces;color:{FOR}">Devin Kampa</div><div style="font:400 15px/1.5 Karla;color:{MUTE}">Loan Officer · NMLS #2532480<br>320-241-5823 · dkampa@highlandsmortgage.com</div></div></div></div>
<div class="abs" style="left:0;right:0;bottom:0;height:74px;background:{FOR};border-top:5px solid {COP};color:#fff;display:flex;justify-content:center;align-items:center;font:500 20px Karla;white-space:nowrap">Need estimates on another home? Call or text Devin <b style="color:{COPL};margin:0 10px">{LO['phone']}</b> · {LO['web']}</div>'''
    return page(fontcss(FONTS),css,body)
def build():
    d={'home':home(),'neigh':neigh(),'num':numbers(),'move':move()}
    d['neigh']=d['neigh'].replace('Sample figures','Example figures')
    return d
if __name__=='__main__':
    os.makedirs('real_ec',exist_ok=True)
    render([(f'/home/claude/work/styles/real_ec/{k}.jpg',h) for k,h in build().items()]); print('ok')
