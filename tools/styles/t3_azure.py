from common import *
NAME='azure'; TITLE='Azure'
FONTS=[('Poppins','poppins',w,'normal') for w in (400,500,600,700,800)]+[('Inter','inter',w,'normal') for w in (400,500,600)]
BLUE='#2F62C1'; DEEP='#1A3F8C'; BLACK='#0F1218'; GREY='#A9ABAE'; LIGHT='#E9EFFA'; INK='#0F1218'; MUTE='#5B6170'
CSS=f"""
body{{background:#fff;color:{INK};font-family:Inter,sans-serif}}
.ph{{background:#DCE3F0}} .abs{{position:absolute}} .p8{{font-family:Poppins,sans-serif;font-weight:800;text-transform:uppercase}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:128px;background:{BLACK};color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 70px}}
.foot .n{{font:700 32px Poppins}} .foot .r{{font:500 15px Inter;letter-spacing:.14em;text-transform:uppercase;color:#8FB0EC;margin-top:4px}} .foot .c{{text-align:right;font:500 20px/1.6 Inter}}
.dot{{width:11px;height:11px;border-radius:50%;background:#fff;flex:none;margin-right:16px}}
"""
def foot():
    return f'<div class="foot"><div><div class="n">{S["agent"]}</div><div class="r">{S["agent_t"]} · {S["brokerage"]}</div></div><div class="c">{S["aphone"]}<br>{S["aemail"]}</div></div>'
def home():
    st=''.join(f'<div style="display:flex;align-items:center;gap:12px;width:160px">{icon(ic,36,BLUE,1.6)}<div><div style="font:700 28px Poppins;line-height:1">{v}</div><div style="font:500 13px Inter;letter-spacing:.12em;text-transform:uppercase;color:{MUTE}">{lb}</div></div></div>' for ic,v,lb in [('bed',S['beds'],'Beds'),('bath',S['baths'],'Baths'),('sqft',S['sqft'],'Sq ft'),('garage',S['garage'],'Garage')])
    bl=''.join(f'<div style="display:flex;align-items:center;font:500 21px Inter;color:#fff;margin-bottom:18px"><span class="dot"></span>{b}</div>' for b in S['bullets'][:8])
    qr=qr_svg('https://devinkampa.com/folder',BLACK,size=150)
    body=f'''{ph(380,0,844,870,extra="clip-path:polygon(270px 0,100% 0,100% 100%,0 100%)")}
<div class="abs" style="left:70px;top:64px;display:flex;align-items:center;gap:14px"><div style="width:52px;height:52px;background:{BLUE};border-radius:16px;position:relative"><div style="position:absolute;inset:12px;border:6px solid {BLACK};border-radius:50%"></div></div><div style="font:600 22px/1.1 Poppins">Your<br>Company</div></div>
<div class="abs p8" style="left:70px;top:170px;font-size:84px;line-height:1.02;letter-spacing:-.01em">Open House<br><span style="color:{BLUE}">123 Sample<br>Street</span></div>
<div class="abs" style="left:70px;top:520px"><div style="font:600 24px Poppins;margin-bottom:8px">About Our Property</div><div style="font:400 19px/1.6 Inter;color:{MUTE};width:400px">{S['about']}</div></div>
<div class="abs" style="left:70px;top:742px;width:340px;display:grid;grid-template-columns:1fr 1fr;gap:20px 14px"></div>
<div class="abs" style="left:70px;top:700px;display:flex;flex-wrap:wrap;gap:16px 8px;width:380px">{st}</div>
<div class="abs" style="left:0;top:818px;display:none"></div>
<div class="abs" style="left:70px;top:848px;display:flex;height:82px"><div style="width:190px;background:{BLUE};color:#fff;display:grid;place-items:center;font:700 32px Poppins">ONLY</div><div style="width:430px;background:{GREY};color:#fff;display:flex;align-items:center;padding-left:30px;font:700 52px Poppins">{usd(S['price'])}</div></div>
<div class="abs" style="left:0;top:960px;width:1224px;height:274px;background:{BLUE}"></div>
<div class="abs" style="left:70px;top:990px;width:760px"><div style="font:500 22px Poppins;color:#CFE0FF;margin-bottom:18px">Features &amp; Facility</div><div style="column-count:2;column-gap:26px">{bl}</div></div>
<div class="abs" style="left:860px;top:996px;width:320px;text-align:center;color:#fff"><div style="font:400 24px Poppins;letter-spacing:.06em">SPECIAL OFFER</div><div class="p8" style="font-size:96px;line-height:1">3%</div><div style="font:600 20px Poppins;letter-spacing:.04em">SELLER CREDIT</div><div style="display:inline-block;background:{BLACK};padding:6px 20px;font:700 19px Poppins;margin-top:12px;letter-spacing:.04em">ASK ME HOW</div></div>
{ph(0,1234,760,222,extra="clip-path:polygon(0 0,100% 0,78% 100%,0 100%)")}
<div class="abs" style="left:790px;top:1262px;width:380px"><div style="display:flex;gap:26px;align-items:center">{qr}<div style="font:500 14px/1.4 Inter;color:{MUTE};width:130px">Scan for the interactive folder</div></div>
<div style="font:700 28px Poppins;margin-top:20px">{S['aphone']}</div><div style="font:500 17px/1.6 Inter;color:{MUTE}">{S['agent']} · {S['brokerage']}<br>{S['aemail']}</div></div>'''
    return page(fontcss(FONTS),CSS,body)
def neigh():
    items=[('tree',NEIGH['parks'][0][0],NEIGH['parks'][0][1],'Parks'),('tree',NEIGH['parks'][1][0],NEIGH['parks'][1][1],'Trails'),
           ('cart',NEIGH['errands'][0][0],NEIGH['errands'][0][1],NEIGH['errands'][0][2]),('cross',NEIGH['errands'][1][0],NEIGH['errands'][1][1],NEIGH['errands'][1][2]),
           ('dine',NEIGH['eat'][0][0],NEIGH['eat'][0][1],'Dining'),('coffee',NEIGH['eat'][3][0],NEIGH['eat'][3][1],'Coffee'),
           ('school','Top-rated schools','Zoned schools nearby','8 min'),('home','Community Pool','Neighborhood amenity','On site')]
    tiles=''
    for i,(ic,t,d,chip) in enumerate(items):
        x=70+(i%2)*540; y=430+(i//2)*168
        tiles+=f'<div class="abs" style="left:{x}px;top:{y}px;width:510px;height:140px;display:flex;align-items:center;gap:24px"><div style="width:92px;height:92px;border-radius:50%;background:{BLUE};display:grid;place-items:center;flex:none">{icon(ic,46,"#fff",1.7)}</div><div style="flex:1"><div style="font:600 25px Poppins">{t}</div><div style="font:400 17px Inter;color:{MUTE}">{d}</div></div><div style="background:{LIGHT};color:{DEEP};font:700 15px Poppins;padding:7px 14px;border-radius:99px;white-space:nowrap">{chip}</div></div>'
    drv=''.join(f'<div style="flex:1;text-align:center;{"border-left:1px solid #34405A" if i else ""}"><div class="p8" style="font-size:38px;color:#8FB0EC">{t}</div><div style="font:500 13px Inter;letter-spacing:.1em;text-transform:uppercase;color:#fff;margin-top:2px">{n}</div></div>' for i,(n,t) in enumerate(NEIGH['drive']))
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:330px;background:{BLUE}"></div>{ph(660,0,564,330,extra="clip-path:polygon(120px 0,100% 0,100% 100%,0 100%)")}
<div class="abs" style="left:70px;top:58px;color:#fff"><div style="font:600 17px Inter;letter-spacing:.3em;text-transform:uppercase;color:#CFE0FF">{S['hood']} · {S['city']}, {S['state']}</div><div class="p8" style="font-size:68px;line-height:1.04;margin-top:14px">Neighborhood<br>Highlights</div></div>
<div class="abs" style="left:0;top:330px;width:1224px;height:62px;background:{BLACK};color:#fff;display:flex;align-items:center;padding:0 70px;font:500 20px Inter">{NEIGH['intro']}</div>
{tiles}
<div class="abs" style="left:0;top:1112px;width:1224px;height:210px;background:{BLACK}"></div><div class="abs" style="left:70px;top:1136px;font:600 20px Poppins;color:#fff;letter-spacing:.14em">DRIVE TIMES</div><div class="abs" style="left:70px;top:1190px;width:1084px;display:flex">{drv}</div>{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def numbers():
    cards=''
    for i,c in enumerate(CARDS):
        x=70+i*(352+24)
        rows=f'<div class="r"><span>Down payment</span><b>{usd(c["down"])}</b></div><div class="r"><span>Est. closing costs</span><b>{usd(c["closing"])}</b></div><div class="r"><span>Seller credit{" ("+str(c["credit_pct"])+"%)" if c["credit"] else ""}</span><b>{"–"+usd(c["credit"]) if c["credit"] else "$0"}</b></div>'
        cards+=f'''<div class="abs" style="left:{x}px;top:390px;width:352px;height:630px;border:2px solid {LIGHT};box-shadow:0 8px 24px rgba(15,18,24,.08)"><div style="height:12px;background:{BLUE}"></div><div style="padding:22px 26px"><div style="font:700 14px Poppins;letter-spacing:.14em;text-transform:uppercase;color:{BLUE}">{c['tag']}</div><div style="font:600 26px/1.2 Poppins;margin:10px 0 18px">{c['title']}<br>{c['title2']}</div><div style="font:500 13px Inter;letter-spacing:.14em;text-transform:uppercase;color:{MUTE}">Est. monthly payment</div><div class="p8" style="font-size:54px;line-height:1.15">{usd(c['mo'])}<span style="font:500 22px Inter;color:{MUTE};text-transform:none">/mo</span></div><div style="margin-top:10px">{rows}</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:140px;background:{BLUE};color:#fff;padding:22px 26px"><div style="font:600 13px Inter;letter-spacing:.16em;text-transform:uppercase;color:#CFE0FF">Est. cash to close</div><div class="p8" style="font-size:50px">{usd(c['cash'])}</div></div></div>'''
    dl=''.join(f'<div style="display:flex;height:72px;width:520px"><div style="width:210px;background:{BLUE};color:#fff;display:grid;place-items:center;font:800 32px Poppins">{a}</div><div style="flex:1;background:{GREY};color:#fff;display:flex;align-items:center;padding:0 22px;font:500 17px/1.35 Inter">{b}</div></div>' for a,b in DELTAS)
    css=CSS+f".r{{display:flex;justify-content:space-between;font:400 18px Inter;padding:10px 0;border-top:1px solid #E3E8F2}} .r b{{font-weight:700}}"
    body=f'''<div class="abs" style="left:0;top:0;width:1224px;height:290px;background:{BLUE}"></div>{ph(700,0,524,290,extra="clip-path:polygon(110px 0,100% 0,100% 100%,0 100%)")}
<div class="abs p8" style="left:70px;top:60px;font-size:96px;line-height:1.02;color:#fff">The<br>Numbers</div>
<div class="abs" style="left:0;top:290px;width:1224px;height:70px;background:{BLACK};color:#fff;display:flex;align-items:center;padding:0 70px;gap:30px;font:600 21px Poppins">{S['full']}<span style="font:400 18px Inter;color:#A8B6D0">{usd(S['price'])} · {S['beds']} BD · {S['baths']} BA · {S['sqft']} SF</span><span style="margin-left:auto;background:{BLUE};padding:5px 16px;font:600 14px Poppins;letter-spacing:.14em">SAMPLE FIGURES</span></div>
{cards}
<div class="abs" style="left:70px;top:1050px;width:1084px;display:flex;justify-content:space-between">{dl}</div>
<div class="abs" style="left:70px;top:1150px;width:1084px;font:400 13px/1.55 Inter;color:{MUTE}">{DISC}</div>
<div class="abs" style="left:70px;top:1296px;width:1084px;display:flex;justify-content:space-between;align-items:center"><div style="border-left:6px solid {BLUE};padding-left:20px"><div style="font:700 28px Poppins">{S['agent']}</div><div style="font:400 17px/1.55 Inter;color:{MUTE}">{S['agent_t']} · {S['brokerage']}<br><b style="color:{INK}">{S['aphone']}</b><br>{S['aemail']}</div></div>
<div style="display:flex;gap:22px;align-items:center;border-left:6px solid {BLUE};padding-left:20px"><img src="{HS}" style="width:122px;height:122px;border-radius:50%;object-fit:cover"><div><div style="font:700 28px Poppins">{LO['name']}</div><div style="font:400 17px/1.55 Inter;color:{MUTE}">{LO['t']}<br><b style="color:{INK}">{LO['phone']}</b><br>{LO['email']}</div></div></div></div>
<div class="abs" style="left:0;right:0;bottom:0;height:80px;background:{BLACK};color:#fff;display:flex;justify-content:center;align-items:center;font:500 21px Inter;white-space:nowrap;gap:10px">Need estimates on another home? Call or text Devin <b style="color:#8FB0EC;font-weight:700">{LO['phone']}</b> · {LO['web']}</div>'''
    return page(fontcss(FONTS),css,body)
def move():
    su=''.join(f'<div style="display:flex;align-items:center;gap:22px;padding:15px 0;border-bottom:1px solid #E3E8F2"><div class="p8" style="width:62px;height:62px;border-radius:50%;background:{BLUE};color:#fff;display:grid;place-items:center;font-size:28px;flex:none">{i+1}</div><div style="flex:1"><div style="font:600 23px Poppins">{a}</div><div style="font:400 16px Inter;color:{MUTE}">{c}</div></div><div style="background:{LIGHT};color:{DEEP};font:700 16px Poppins;padding:8px 16px;border-radius:99px;white-space:nowrap">{d}</div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
    icons=['bolt','flame','drop','wifi','home']
    mo=''.join(f'<div style="display:flex;align-items:center;gap:20px;padding:13px 0;border-bottom:1px solid #E3E8F2"><div style="width:54px;height:54px;border-radius:14px;background:{BLUE};display:grid;place-items:center;flex:none">{icon(icons[i],28,"#fff",1.8)}</div><div style="flex:1"><div style="font:600 22px Poppins">{a}</div><div style="font:400 15px Inter;color:{MUTE}">{b}</div></div><div class="p8" style="font-size:25px;color:{BLUE};text-transform:none;font-weight:700">{"$"+str(lo)+"–$"+str(hi) if lo else MOVE["hoa"]}</div></div>' for i,(a,b,lo,hi) in enumerate(MOVE['monthly']))
    body=f'''<div class="abs" style="left:0;top:0;width:400px;height:1456px;background:{BLUE}"></div>
<div class="abs" style="left:50px;top:60px;color:#fff;width:310px"><div style="font:600 15px Inter;letter-spacing:.26em;text-transform:uppercase;color:#CFE0FF">Your first week at<br>{S['street']}</div><div class="p8" style="font-size:78px;line-height:1.02;margin-top:22px">Move-<br>In<br>Costs</div></div>
{ph(50,520,300,300,extra="border-radius:24px;background:#5B84D3")}
<div class="abs" style="left:50px;top:860px;width:310px;color:#fff;font:400 20px/1.6 Inter">{MOVE['intro']}</div>
<div class="abs" style="left:450px;top:60px;width:704px"><div class="p8" style="font-size:26px;color:{BLUE};margin-bottom:6px">Set up before you arrive</div><div style="height:5px;background:{BLACK};width:70px;margin-bottom:6px"></div>{su}
<div class="p8" style="font-size:26px;color:{BLUE};margin:34px 0 6px">Typical monthly costs</div><div style="height:5px;background:{BLACK};width:70px;margin-bottom:6px"></div>{mo}
<div style="font:400 12.5px/1.5 Inter;color:{MUTE};margin-top:18px">{MOVE['fine']}</div></div>{foot()}'''
    return page(fontcss(FONTS),CSS,body)
def all(): return {'home':home(),'neigh':neigh(),'num':numbers(),'move':move()}
