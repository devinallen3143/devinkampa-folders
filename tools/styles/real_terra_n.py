import os
import common, light
from common import render, page, fontcss, icon, usd, S, NEIGH, MOVE, CARDS, DELTAS, HS, LO
import real_terra as R
from real_terra_c import pic, P
FONTS=light.STY['terra']['fonts']
INK='#111111'; MUTE='#666666'; LINE='#D6D6D6'; TINT='#F3F3F3'
CSS=f"""body{{background:#fff;color:{INK};font-family:Nunito,sans-serif}} .abs{{position:absolute}} .q{{font-family:Quicksand,sans-serif;font-weight:700}}
.cap{{font:700 12px Nunito;letter-spacing:.22em;text-transform:uppercase;color:{MUTE}}}
.pill{{display:inline-flex;align-items:center;gap:8px;border:1.5px solid {INK};border-radius:99px;padding:7px 20px;background:#fff}}
.card{{border:1.5px solid {LINE};border-radius:28px;background:#fff;box-sizing:border-box}} .tile{{background:{TINT};border-radius:26px;box-sizing:border-box}}
.r{{display:flex;justify-content:space-between;font:600 17px Nunito;padding:9px 0;border-top:1px solid {LINE}}} .r b{{font-weight:800}}"""
RD='border-radius:28px;'
def foot():
    return f'<div class="abs" style="left:70px;right:70px;bottom:0;height:150px;border-top:2px solid {INK};display:flex;align-items:center;gap:22px"><div style="width:84px;height:84px;border-radius:50%;border:2px solid #BBB;flex:none"></div><div style="flex:1"><div class="q" style="font-size:30px">{S["agent"]}</div><div class="cap" style="font-size:11px;margin-top:4px">{S["agent_t"]} · {S["brokerage"]}</div></div><div style="text-align:right;font:600 19px/1.6 Nunito">{S["aphone"]}<br>{S["aemail"]}</div></div>'
def hdr(eyebrow,title,sub,y=54,sw=880):
    return f'<div class="abs" style="left:0;right:0;top:{y}px;text-align:center"><div class="cap">{eyebrow}</div><div class="q" style="font-size:68px;line-height:1.05;margin-top:10px">{title}</div><div style="font:italic 400 21px/1.5 Nunito;color:{MUTE};margin:10px auto 0;width:{sw}px">{sub}</div></div>'
def home():
    stats=[('bed',S['beds'],'Beds'),('bath',S['baths'],'Baths'),('sqft',S['sqft'],'Sq ft'),('garage',S['garage'],'Garage')]
    st=''.join(f'<div class="tile" style="flex:1;text-align:center;padding:14px 0 10px">{icon(ic,30,INK,1.4)}<div class="q" style="font-size:32px;line-height:1.1">{v}</div><div class="cap" style="font-size:11px">{lb}</div></div>' for ic,v,lb in stats)
    bl=''.join(f'<div style="display:flex;gap:12px;align-items:center;margin-bottom:5px;font:600 17px Nunito"><span style="width:8px;height:8px;border-radius:50%;background:{INK};flex:none"></span>{b}</div>' for b in S['bullets'])
    body=f'''{pic('ext',40,40,1144,560,'50% 50%',RD+'border-radius:44px')}
<div class="abs" style="left:40px;top:40px;width:1144px;height:560px;border-radius:44px;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(0,0,0,.28) 100%)"></div>
<div class="abs" style="left:112px;top:520px;width:1000px;height:206px;background:#fff;border-radius:40px;box-shadow:0 14px 40px rgba(0,0,0,.14);text-align:center;box-sizing:border-box;padding-top:26px"><div class="pill" style="font:800 12px Nunito;letter-spacing:.22em;text-transform:uppercase;padding:6px 18px">Open house · {S['hood']}</div><div class="q" style="font-size:72px;line-height:1.08;margin-top:10px;white-space:nowrap">{S['street']}</div><div style="font:italic 400 22px Nunito;color:{MUTE};margin-top:2px">{S['city']}, {S['state']} {S['zip']}</div></div>
<div class="abs" style="left:0;right:0;top:748px;text-align:center"><div class="pill" style="padding:8px 40px;gap:16px;border-width:2px"><span class="cap" style="color:{INK}">Offered at</span><span class="q" style="font-size:46px;line-height:1.1">{usd(S['price'])}</span></div></div>
<div class="abs" style="left:70px;top:836px;width:1084px;display:flex;gap:14px">{st}</div>
<div class="abs tile" style="left:70px;top:952px;width:520px;height:292px;padding:26px 30px"><div class="cap" style="margin-bottom:12px">About the home</div><div style="font:italic 400 22px/1.55 Nunito">{S['about']}</div></div>
<div class="abs card" style="left:612px;top:952px;width:542px;height:292px;padding:24px 30px"><div class="cap" style="margin-bottom:12px">What we love</div>{bl}</div>
{pic('kit',70,1262,344,158,'45% 55%',RD)}{pic('liv',440,1262,344,158,'45% 50%',RD)}{pic('bed',810,1262,344,158,'50% 60%',RD)}{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def neigh():
    def lst(items,mi=False):
        return ''.join(f'<div style="display:flex;justify-content:space-between;gap:10px;margin-bottom:12px"><div><div style="font:800 17px Nunito">{i[0]}</div><div style="font:500 13.5px Nunito;color:{MUTE}">{i[1]}</div></div>{"<div class=q style=font-size:16px>"+i[2]+"</div>" if mi else ""}</div>' for i in items)
    def col(x,ic,t,items,mi=False):
        return f'<div class="abs card" style="left:{x}px;top:734px;width:344px;height:258px;padding:20px 24px"><div class="pill" style="border-color:{LINE};background:{TINT};margin-bottom:14px;font:800 15px Quicksand">{icon(ic,20,INK,1.6)}{t}</div>{lst(items,mi)}</div>'
    chips=''.join(f'<span class="tile" style="padding:8px 18px;border-radius:99px;font:800 16px Nunito">{t} <span style="font-weight:600;color:{MUTE};font-size:13px">{n}</span></span>' for n,t in NEIGH['drive'])
    body=f'''{hdr(S['hood']+' · '+S['city']+', '+S['state'],'Neighborhood Highlights',NEIGH['intro'],54,860)}
<div class="abs" style="left:70px;top:300px;width:1084px;height:360px;{RD}overflow:hidden;border:1.5px solid {LINE}">{MAPHTML}</div>
<div class="abs" style="left:70px;top:678px;width:1084px;display:flex;gap:10px;justify-content:center">{chips}</div>
{col(70,'tree','Parks &amp; Trails',NEIGH['parks'])}{col(440,'cart','Errands',NEIGH['errands'],True)}{col(810,'dine','Eat &amp; Drink',NEIGH['eat'])}
{pic('bed',70,1012,530,404,'50% 60%',RD)}{pic('kit',624,1012,530,404,'45% 55%',RD)}{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def mapfn(w=1084,h=280):
    uri=R.mapdata(w,h,15); pins=''
    for ic,dx,dy in R.PINS:
        px,py=w/2+dx,h/2+dy
        pins+=f'<div style="position:absolute;left:{px-22}px;top:{py-22}px;width:44px;height:44px;border-radius:50%;background:#fff;border:3px solid {INK};display:grid;place-items:center">{icon(ic,22,INK,1.8)}</div>'
    home=f'<div style="position:absolute;left:{w/2-26}px;top:{h/2-26}px;width:52px;height:52px;border-radius:50%;background:{INK};border:4px solid #fff;display:grid;place-items:center">{icon("home",26,"#fff",1.8)}</div>'
    cap='<div style="position:absolute;right:12px;bottom:8px;font:600 11px sans-serif;color:#555;background:rgba(255,255,255,.85);padding:2px 6px">Map © OpenStreetMap contributors · pins approximate</div>'
    return f'<div style="position:relative;width:{w}px;height:{h}px;background:url({uri}) center/cover">{pins}{home}{cap}</div>'
MAPHTML=mapfn(1084,360)
def numbers():
    def col(c,x):
        return f'''<div class="abs" style="left:{x}px;top:0;width:542px;height:640px;text-align:center;padding:26px 36px 0;box-sizing:border-box"><span class="pill" style="font:800 11px Nunito;letter-spacing:.18em;text-transform:uppercase;padding:5px 16px">{c['tag']}</span><div class="q" style="font-size:25px;margin-top:10px">{c['title']} · {c['title2']}</div><div class="cap" style="font-size:11px;margin-top:12px">Est. monthly payment</div><div class="q" style="font-size:62px;line-height:1.15;margin-top:8px">{usd(c['mo'])}<span style="font:600 20px Nunito;color:{MUTE}">/mo</span></div>
<div style="text-align:left;margin-top:8px">{r('Principal &amp; interest',usd(c['pi']))}{r('Property taxes',usd(c['tax']))}{r('Home insurance','$250')}{r('Mortgage insurance',usd(c['mi']))}<div class="cap" style="font-size:11px;margin:14px 0 2px;text-align:center">Up-front costs</div>{r('Down payment',usd(c['down']))}{r('Est. closing costs',usd(c['closing']))}{r('Seller title credit','–'+usd(c['credit']))}</div>
<div class="tile" style="position:absolute;left:30px;right:30px;bottom:24px;height:96px;padding-top:14px"><div class="cap" style="font-size:11px">Est. cash to close</div><div class="q" style="font-size:46px;line-height:1.15">{usd(c['cash'])}</div></div></div>'''
    def r(a,b): return f'<div class="r"><span>{a}</span><b>{b}</b></div>'
    dl=''.join(f'<div style="flex:1;display:flex;align-items:center;gap:16px"><span class="q" style="font-size:42px;white-space:nowrap">{a}</span><span style="font:600 17px/1.4 Nunito">{b}</span></div>' for a,b in DELTAS)
    body=f'''{hdr('Example figures · '+S['full'],'The Numbers',f"{usd(S['price'])} · {S['beds']} BD · {S['baths']} BA · {S['sqft']} SF",50,880).replace('font:italic 400 21px/1.5 Nunito','font:italic 400 20px/1.3 Nunito')}
{pic('kit',70,222,530,220,'50% 55%',RD)}{pic('bath',624,222,530,220,'50% 40%',RD)}
<div class="abs card" style="left:70px;top:462px;width:1084px;height:640px;border:2px solid {INK};border-radius:36px">{col(CARDS[0],0)}<div class="abs" style="left:542px;top:30px;bottom:30px;border-left:1.5px solid {LINE}"></div>{col(CARDS[1],542)}</div>
<div class="abs" style="left:70px;top:1122px;width:1084px;display:flex;gap:30px;padding:14px 0;border-top:1.5px solid {LINE};border-bottom:1.5px solid {LINE}">{dl}</div>
<div class="abs" style="left:70px;top:1226px;width:1084px;font:500 12.5px/1.5 Nunito;color:{MUTE}">{R.DISC}</div>
<div class="abs" style="left:70px;top:1352px;width:1084px;display:flex;justify-content:space-between;align-items:center"><div style="border-left:4px solid {INK};padding-left:18px"><div class="q" style="font-size:26px">{S['agent']}</div><div style="font:500 14.5px/1.5 Nunito;color:{MUTE}">{S['agent_t']} · {S['brokerage']}<br>{S['aphone']} · {S['aemail']}</div></div><div style="display:flex;align-items:center;gap:16px"><img src="{HS}" style="width:80px;height:80px;border-radius:50%;object-fit:cover"><div><div class="q" style="font-size:26px">Devin Kampa</div><div style="font:500 14.5px/1.5 Nunito;color:{MUTE}">Loan Officer · NMLS #2532480<br>320-241-5823 · dkampa@highlandsmortgage.com</div></div></div></div>
<div class="abs" style="left:70px;right:70px;bottom:0;height:90px;border-top:2px solid {INK};display:flex;align-items:center;justify-content:center;font:600 19px Nunito">Need estimates on another home? Call or text Devin <b style="margin:0 8px">{LO['phone']}</b> · {LO['web']}</div>'''
    return page(fontcss(FONTS),CSS,body)
def move():
    su=''.join(f'<div class="card" style="position:absolute;left:{70+i*278}px;top:344px;width:256px;height:224px;padding:18px 18px;text-align:center"><div class="q" style="width:42px;height:42px;border-radius:50%;background:{INK};color:#fff;display:grid;place-items:center;margin:0 auto 8px;font-size:20px">{i+1}</div><div class="q" style="font-size:18px;line-height:1.2">{a}</div><div style="font:500 13px/1.35 Nunito;color:{MUTE};margin-top:6px">{b}<br>{c}</div><div class="pill" style="margin-top:10px;font:800 13px Nunito;padding:4px 14px">{d}</div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
    ics=['bolt','flame','drop','wifi','home']; tiles=''; lo_t=hi_t=0
    for i,(a,b,lo,hi) in enumerate(MOVE['monthly']):
        val=f'${lo}–${hi}' if lo else MOVE['hoa']
        if lo: lo_t+=lo; hi_t+=hi
        x=70+(i%3)*368; y=632+(i//3)*150
        tiles+=f'<div class="tile abs" style="left:{x}px;top:{y}px;width:348px;height:134px;padding:18px 24px"><div style="display:flex;align-items:center;gap:10px;font:800 16px Nunito">{icon(ics[i],22,INK,1.7)}{a}</div><div class="q" style="font-size:32px;margin-top:6px">{val}</div><div style="font:500 13px Nunito;color:{MUTE};margin-top:2px">{b}</div></div>'
    tiles+=f'<div class="abs card" style="left:{70+2*368}px;top:782px;width:348px;height:134px;padding:18px 24px;border:2px solid {INK}"><div class="cap" style="color:{INK}">Utilities total</div><div class="q" style="font-size:32px;margin-top:6px">${lo_t}–${hi_t}</div><div style="font:500 13px Nunito;color:{MUTE};margin-top:2px">Typical monthly total, excluding HOA.</div></div>'
    body=f'''{hdr('Your first week at '+S['street'],'Move-In Costs',MOVE['intro'],50,900)}
<div class="abs" style="left:0;right:0;top:304px;text-align:center"><span class="pill" style="font:800 12px Nunito;letter-spacing:.2em;text-transform:uppercase;padding:5px 18px;border-color:{LINE};background:{TINT}">Set up before you arrive</span></div>{su}
<div class="abs" style="left:0;right:0;top:590px;text-align:center"><span class="pill" style="font:800 12px Nunito;letter-spacing:.2em;text-transform:uppercase;padding:5px 18px;border-color:{LINE};background:{TINT}">Typical monthly costs</span></div>{tiles}
{pic('bed',70,946,520,470,'50% 55%',RD)}{pic('ext',614,946,540,226,'50% 55%',RD)}{pic('liv2',614,1190,540,226,'50% 50%',RD)}{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def build(): return {'home':home(),'neigh':neigh(),'num':numbers(),'move':move()}
if __name__=='__main__':
    os.makedirs('real_tn',exist_ok=True)
    d={k:light.postproc('terra',v,k) for k,v in build().items()}
    render([(f'/home/claude/work/styles/real_tn/{k}.jpg',h) for k,h in d.items()]); print('ok')
