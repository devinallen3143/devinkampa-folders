import io,base64,math,requests,glob
from PIL import Image, ImageEnhance
from lay import *
UP='/mnt/user-data/uploads/'
def _pho(i,w=1500):
    im=Image.open(glob.glob(UP+i+'-image.png')[0]).convert('RGB'); im.thumbnail((w,w)); b=io.BytesIO(); im.save(b,'JPEG',quality=86)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
PH=dict(ext=_pho('8412159e'),liv=_pho('38dea323'),kit=_pho('b089af83'),pool=_pho('305ffb31'),aer=_pho('52e3fda3'),bath=_pho('9c2dc49d'))
# ---- map (OSM tiles, z15, muted) ----
def mapimg(w=1084,h=370):
    z=15; hx,hy=(15149*256+430)/2,(26403*256+718)/2
    pins={'home':(hx,hy),'1':((15149*256+265)/2,(26403*256+600)/2),'2':((15149*256+297)/2,(26403*256+300)/2),'3':((15149*256+368)/2,(26403*256+288)/2),'4':((15149*256+330)/2,(26403*256+860)/2)}
    cx,cy=hx+25,hy-75
    x0,y0=cx-w/2,cy-h/2
    big=Image.new('RGB',(int(w)+512,int(h)+512),'white')
    for tx in range(int(x0//256),int((x0+w)//256)+1):
        for ty in range(int(y0//256),int((y0+h)//256)+1):
            r=requests.get(f'https://tile.openstreetmap.org/{z}/{tx}/{ty}.png',headers={'User-Agent':'devinkampa-folders/1.0'},timeout=20)
            big.paste(Image.open(io.BytesIO(r.content)).convert('RGB'),(int(tx*256-x0),int(ty*256-y0)))
    im=big.crop((0,0,int(w),int(h))).convert('L'); im=ImageEnhance.Contrast(im).enhance(.85).convert('RGB')
    b=io.BytesIO(); im.save(b,'JPEG',quality=88)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode(),{k:(px-x0,py-y0) for k,(px,py) in pins.items()}
MAP,PINS=mapimg()
ADDR="7707 La Avenida Dr."; FULL="7707 La Avenida Dr, Dallas, TX 75248"; HOOD="Richardson Heights Estates West · Dallas, TX"; MLS="MLS# 21438948"
PRICE=649000
def pic(x,y,w,h,k,pos='center',extra=''):
    return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:url({PH[k]}) {pos}/cover no-repeat;{extra}"></div>'
C97=dict(tag="Lowest cash to close",t1="3% down",t2="97% LTV",rate="7.490%",apr="7.732%",pi=4397.46,tax=1027.58,ins=400.00,mi=104.92,tot=5929.96,down=19470.00,cc=8252.10,pre=9205.36,cr=3497.00,cash=33430.46)
C80=dict(tag="Lowest monthly payment",t1="20% down",t2="80% LTV",rate="7.490%",apr="7.570%",pi=3626.77,tax=1027.58,ins=400.00,mi=None,tot=5054.35,down=129800.00,cc=8252.10,pre=8933.67,cr=3497.00,cash=143488.77)
def m2(n): return f"${n:,.2f}"
def m0(n): return f"${round(n):,}"
DELT=[(m0(C80['cash']-C97['cash']),"more cash to close with 20% down than with 3% down."),(m0(C97['tot']-C80['tot'])+"/mo","lower payment with 20% down vs. 3% down.")]
DISCR=("Example figures for illustration, prepared 11/21/2026; estimates only, not a loan approval or commitment to lend. $649,000 purchase price, 30-year fixed conventional at 7.490% (APR 7.732% at 3% down, 7.570% at 20% down). "
 "Payment = principal, interest, est. taxes ($1,027.58/mo), insurance ($400/mo) and mortgage insurance where it applies. Up-front costs = down payment, est. closing costs, prepaid items and escrow reserves, less a $3,497 seller title credit, which must be agreed in the contract and is subject to loan program limits. "
 "Actual rate, payment and costs could be higher; get an official Loan Estimate before choosing a loan. Devin Kampa is a loan officer, not a licensed real estate agent or Realtor, and this listing is exclusive to the listing Realtor or builder. "
 "Highlands Residential Mortgage, Ltd., NMLS #134871 (www.nmlsconsumeraccess.org). Equal Housing Lender.")
BULLETS=["3 bed, 2 bath and a dedicated office","Open-concept living and dining","Pool, built in 2021","Hardwood and tile flooring","Walk-in closets and a pantry","New roof, plumbing and foundation work (2026)","Two-car garage with rear entry","0.22-acre lot, built in 1966"]
ABOUT="A classic 1966 ranch, refreshed and move-in ready: a bright open living and dining space, a dedicated office and a backyard pool made for entertaining, on a landscaped lot in the Bowie Elementary zone."
DRIVE=[("Galleria Dallas","10 min"),("Love Field","24 min"),("Legacy West","20 min"),("Downtown Dallas","25 min"),("Downtown Fort Worth","40 min")]
TILES=[('tree','Preston Ridge Trail','6.3-mile trail linking Dallas and Plano','Trail'),('tree','Salado Park','4.2-acre park with benches and trails','Park'),
 ('cart','Walmart Supercenter','15757 Coit Rd · groceries and everyday needs','Coit Rd'),('cart','Target','16731 Coit Rd · home and everyday needs','Coit Rd'),
 ('dine','Jeng Chi','Taiwanese and Sichuan · 400 N. Greenville Ave.','Dining'),('dine','Kasra Persian Restaurant','Kabobs and stews · 525 W. Arapaho Rd.','Dining'),
 ('dine','Deli News','New York-style deli · 17062 Preston Rd.','Dining'),('school','Richardson ISD schools','Bowie Elem. · Westwood Jr. High · Pearce High','Zoned')]
NINTRO="Estates West is a tree-lined pocket of Far North Dallas with Richardson ISD schools, direct access to the Preston Ridge Trail and everyday shopping along Coit Road."
SETUP=[("Water, sewer &amp; trash","City of Dallas Water Utilities","Open an account on DallasGo or call 214-651-1441","Online or call"),
 ("Electricity","Oncor delivers; you choose the provider","Compare plans at powertochoose.org","Pick a provider"),
 ("Natural gas","Atmos Energy","Call 888-286-6700 to set a start date","Call to start"),
 ("Internet","Choose a provider for this address","Compare fiber and cable plans before move-in","Up to $90")]
MONTHLY=[("Electricity","Roughly 2,049 sq ft plus a pool; summer runs highest",180,320),("Natural gas","Heat and water heating; winter runs highest",40,120),("Water, sewer &amp; trash","City of Dallas utility bill",110,190),("Internet","Fiber or cable",60,90),("HOA","None listed",None,None)]
FINE="Estimates only, not quotes. Figures are examples scaled to home size and typical ranges; actual costs depend on usage, provider and plan. Verify with each provider before you move in."
def build():
    X=ctx('azure'); st,I,A,T,M,L,B,R,BF=[X[k] for k in ('st','I','A','T','M','L','B','R','BF')]
    H,ey,sec,foot,page=X['H'],X['ey'],X['sec'],X['foot'],X['page']; PS=st['pshape']
    def home():
        stats=[('bed',3,'Bedrooms'),('bath',2,'Bathrooms'),('sqft','2,049','Sq ft'),('garage',2,'Garage')]
        sb=''.join(f'<div style="display:flex;align-items:center;gap:16px;padding:16px 0;border-top:1.5px solid {L}">{icon(ic,34,A,1.5)}<div class="hd nu" style="font-size:34px;width:92px">{v}</div><div style="font:700 13px {BF};letter-spacing:.16em;text-transform:uppercase;color:{M}">{lb}</div></div>' for ic,v,lb in stats)
        bl=''.join(f'<div style="display:flex;gap:12px;align-items:flex-start;font:500 19px/1.25 {BF}"><span style="{X["bul"]()};margin-top:7px"></span>{b}</div>' for b in BULLETS)
        body=f'<div class="abs" style="left:70px;top:64px;display:flex;align-items:center;gap:12px"><div style="width:44px;height:44px;border-radius:14px;border:2px solid {A};display:grid;place-items:center"><div style="width:16px;height:16px;border:4px solid {I};border-radius:50%"></div></div><div class="hd nu" style="font-size:20px;line-height:1.1">Your<br>Company</div></div>'
        body+=f'<div class="abs" style="left:70px;top:190px;width:310px">{ey("Offered at")}{H(54,usd(PRICE),extra="margin-top:6px;letter-spacing:-.01em")}<div style="width:70px;height:5px;background:{A};margin:16px 0 14px"></div><div style="font:600 13px {BF};letter-spacing:.14em;color:{M};margin-bottom:14px">{MLS}</div>{sb}<div style="border-top:1.5px solid {L};padding-top:26px;display:flex;align-items:center;gap:16px">{qr_svg("https://devinkampa.com/folder/Azure/",I,size=120)}<div style="font:600 14px/1.4 {BF};color:{M}">Scan for the interactive folder</div></div></div>'
        body+=f'<div class="abs" style="left:420px;top:70px;height:1360px;border-left:1.5px solid {L}"></div>'
        body+=pic(460,64,694,600,'ext','center 60%',PS)+f'<div class="abs" style="left:460px;top:64px;width:694px;height:600px;{PS};background:linear-gradient(180deg,rgba(255,255,255,0) 70%,rgba(255,255,255,.94) 100%)"></div>'+pic(70,850,310,570,'pool','60% center','border-radius:155px 155px 14px 14px')
        body+=f'<div class="abs" style="left:460px;top:690px;width:694px">{ey(HOOD)}{H(60,"Open House",extra="margin-top:8px")}{H(60,ADDR,A)}</div>'
        body+=f'<div class="abs" style="left:460px;top:880px;width:694px;font:400 20px/1.5 {BF}">{ABOUT}</div>'
        body+=f'<div class="abs" style="left:460px;top:1000px;width:694px">{ey("Features &amp; facility","margin-bottom:12px")}<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px 22px">{bl}</div></div>'
        body+=pic(460,1215,694,205,'liv','center 55%','border-radius:14px')+foot()
        return page(body)
    def neigh():
        tl=''
        for i,(ic,t,d,chip) in enumerate(TILES):
            x=70+(i%2)*550; y=478+(i//2)*118
            tl+=f'<div class="abs" style="left:{x}px;top:{y}px;width:534px;height:102px;border-top:1.5px solid {L};display:flex;align-items:center;gap:18px"><div style="width:60px;height:60px;border-radius:14px;border:1.5px solid {A};display:grid;place-items:center;flex:none">{icon(ic,30,A,1.6)}</div><div style="flex:1"><div class="hd nu" style="font-size:22px">{t}</div><div style="font:400 14.5px/1.3 {BF};color:{M}">{d}</div></div><div style="border:1.5px solid {A};color:{A};border-radius:99px;font:700 13px {BF};padding:5px 13px;white-space:nowrap">{chip}</div></div>'
        dr=''.join(f'<div style="flex:1;text-align:center;{"border-left:1.5px solid "+L if i else ""}">{H(32,t,A,"text-transform:none")}<div style="font:700 11.5px {BF};letter-spacing:.1em;text-transform:uppercase;color:{M};margin-top:4px">{n}</div></div>' for i,(n,t) in enumerate(DRIVE))
        pins=''
        for k,(px,py) in PINS.items():
            if k=='home': pins+=f'<div class="abs" style="left:{px-24}px;top:{py-24}px;width:48px;height:48px;border-radius:50%;background:{I};border:4px solid #fff;display:grid;place-items:center">{icon("home",24,"#fff",1.8)}</div>'
            else: pins+=f'<div class="abs" style="left:{px-18}px;top:{py-18}px;width:36px;height:36px;border-radius:50%;background:#fff;border:2.5px solid {I};display:grid;place-items:center;font:700 18px {BF}">{k}</div>'
        leg=f'<div class="abs" style="left:70px;top:1382px;width:1084px;font:600 13px {BF};color:{M}"><b style="color:{I}">1</b> Preston Ridge Trail &nbsp; <b style="color:{I}">2</b> Salado Park &nbsp; <b style="color:{I}">3</b> Bowie Elementary &nbsp; <b style="color:{I}">4</b> Westwood Junior High &nbsp;·&nbsp; Locations and drive times approximate; confirm zoned schools with RISD.</div>'
        body=f'<div class="abs" style="left:70px;top:64px;width:740px">{ey(HOOD)}{H(56,"Neighborhood",extra="margin-top:10px")}{H(56,"Highlights",A)}</div>'+pic(880,56,274,230,'aer','center','border-radius:999px')
        body+=f'<div class="abs" style="left:70px;top:292px;width:1084px;font:400 21px/1.5 {BF}">{NINTRO}</div>'
        body+=f'<div class="abs" style="left:70px;top:384px;width:1084px;display:flex;padding:16px 0;border-top:2px solid {I};border-bottom:1.5px solid {L}">{dr}</div>'
        body+=tl+f'<div class="abs" style="left:70px;top:1000px;width:1084px;height:370px;border-radius:{R}px;overflow:hidden;border:2px solid {I}"><div style="position:absolute;left:0;top:0;width:1084px;height:370px;background:url({MAP}) center/cover"></div>{pins}</div>'+leg
        body+=f'<div class="abs" style="left:70px;top:1445px;width:1084px;height:0"></div>'+foot(24)
        return page(body)
    def numbers():
        def card(i,c):
            y=300+i*330
            mi=f'<div class="rw" style="padding:4px 0;font-size:15px"><span>Mortgage insurance</span><b>{m2(c["mi"])}</b></div>' if c['mi'] else ''
            mr=''.join(f'<div class="rw" style="padding:4px 0;font-size:15px"><span>{a}</span><b>{m2(v)}</b></div>' for a,v in [('Principal &amp; interest',c['pi']),('Property taxes',c['tax']),('Home insurance',c['ins'])])+mi
            ur=''.join(f'<div class="rw" style="padding:8px 0;font-size:15.5px"><span>{a}</span><b>{v}</b></div>' for a,v in [('Down payment',m2(c['down'])),('Est. closing costs',m2(c['cc'])),('Prepaids &amp; escrow',m2(c['pre'])),('Seller title credit','–'+m2(c['cr']))])
            return f'''<div class="abs" style="left:70px;top:{y}px;width:1084px;height:300px;border:2px solid {I};border-radius:{R}px;display:flex"><div style="width:250px;padding:24px;border-right:1.5px solid {L}"><div style="display:inline-block;background:{A};color:#fff;border-radius:99px;font:700 12px {BF};letter-spacing:.12em;text-transform:uppercase;padding:5px 12px">{c['tag']}</div>{H(28,c['t1']+'<br>'+c['t2'],extra="margin-top:18px;text-transform:none")}<div style="font:500 14.5px/1.5 {BF};color:{M};margin-top:16px">Rate {c['rate']}<br>APR {c['apr']}<br>30-year fixed</div></div>
<div style="width:310px;padding:22px 24px;border-right:1.5px solid {L}"><div style="font:700 12px {BF};letter-spacing:.16em;text-transform:uppercase;color:{M}">Est. monthly payment</div>{H(54,m0(c['tot'])+'<span style="font:500 20px '+BF+';color:'+M+'">/mo</span>',extra="margin:4px 0 10px;text-transform:none")}{mr}</div>
<div style="width:290px;padding:22px 24px;border-right:1.5px solid {L}"><div style="font:700 12px {BF};letter-spacing:.16em;text-transform:uppercase;color:{M};margin-bottom:8px">Up-front costs</div>{ur}</div>
<div style="flex:1;padding:22px 24px;background:{T};display:flex;flex-direction:column;justify-content:center"><div style="font:700 12px {BF};letter-spacing:.16em;text-transform:uppercase;color:{M}">Est. cash to close</div>{H(44,m0(c['cash']),extra="margin-top:6px;text-transform:none")}<div style="width:50px;height:4px;background:{A};margin-top:14px"></div></div></div>'''
        dl=''.join(f'<div style="flex:1;display:flex;align-items:center;gap:18px"><span class="hd nu" style="font-size:42px;color:{A};white-space:nowrap">{a}</span><span style="font:500 18px/1.4 {BF}">{b}</span></div>' for a,b in DELT)
        ct=f'<div class="abs" style="left:70px;top:1335px;width:1084px;display:flex;justify-content:space-between"><div style="border-left:4px solid {A};padding-left:18px"><div class="hd nu" style="font-size:28px">{S["agent"]}</div><div style="font:400 17px/1.55 {BF};color:{M}">{S["agent_t"]} · {S["brokerage"]}<br><b style="color:{I}">{S["aphone"]}</b><br>{S["aemail"]}</div></div><div style="display:flex;gap:20px;align-items:center;border-left:4px solid {A};padding-left:18px"><img src="{HS}" style="width:112px;height:112px;border-radius:50%;object-fit:cover;border:2px solid {A}"><div><div class="hd nu" style="font-size:28px">{LO["name"]}</div><div style="font:400 17px/1.55 {BF};color:{M}">{LO["t"]}<br><b style="color:{I}">{LO["phone"]}</b><br>{LO["email"]}</div></div></div></div>'
        body=f'<div class="abs" style="left:70px;top:64px">{ey("Example figures · "+FULL)}{H(66,"The Numbers",extra="margin-top:10px")}<div style="font:600 19px {BF};color:{M};margin-top:12px">{usd(PRICE)} · 3 BD · 2 BA · 2,049 SF · {MLS}</div></div>'+pic(880,56,274,200,'pool','center','border-radius:70px 0 0 0')
        body+=card(0,C97)+card(1,C80)+f'<div class="abs" style="left:70px;top:975px;width:1084px;display:flex;gap:36px;padding:14px 0;border-top:1.5px solid {L};border-bottom:1.5px solid {L}">{dl}</div>'
        body+=f'<div class="abs" style="left:70px;top:1075px;width:1084px;font:400 13px/1.55 {BF};color:{M}">{DISCR}</div>'+pic(70,1208,348,112,'ext','center 60%','border-radius:14px 0 0 14px')+pic(438,1208,348,112,'liv','center 55%','')+pic(806,1208,348,112,'kit','center 50%','border-radius:0 14px 14px 0')+ct+f'<div class="abs" style="left:70px;right:70px;bottom:44px;border-top:2px solid {A};padding-top:18px;text-align:center;font:500 19px {BF}">Need estimates on another home? Call or text Devin <b style="color:{A}">{LO["phone"]}</b> · {LO["web"]}</div>'
        return page(body)
    def move():
        su=''.join(f'<div style="display:flex;gap:18px;padding:30px 0;border-top:1.5px solid {L}"><div class="hd nu" style="width:50px;height:50px;border-radius:14px;border:1.5px solid {A};color:{A};display:grid;place-items:center;font-size:24px;flex:none">{i+1}</div><div style="flex:1"><div style="font:700 21px {BF}">{a}</div><div style="font:400 15px/1.45 {BF};color:{M}">{b}<br>{c}</div><div style="display:inline-block;margin-top:8px;border:1.5px solid {A};color:{A};border-radius:99px;font:700 13px {BF};padding:4px 12px">{d}</div></div></div>' for i,(a,b,c,d) in enumerate(SETUP))
        mo=''
        for i,(a,b,lo,hi) in enumerate(MONTHLY):
            val=f'${lo}–${hi}' if lo else 'None listed'
            bar=f'<div style="height:6px;background:{T};margin-top:10px;border-radius:6px;position:relative"><div style="position:absolute;left:{lo/4}%;width:{(hi-lo)/4}%;top:0;bottom:0;background:{A};border-radius:6px"></div></div>' if lo else ''
            mo+=f'<div style="display:flex;gap:16px;padding:27px 0;border-top:1.5px solid {L}"><div style="width:48px;height:48px;border-radius:14px;border:1.5px solid {A};display:grid;place-items:center;flex:none">{icon(X["ics"][i],26,A,1.6)}</div><div style="flex:1"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font:700 20px {BF}">{a}</span>{H(24,val,extra="text-transform:none")}</div><div style="font:400 14.5px {BF};color:{M}">{b}</div>{bar}</div></div>'
        lo=sum(m[2] for m in MONTHLY if m[2]); hi=sum(m[3] for m in MONTHLY if m[3])
        body=f'<div class="abs" style="left:70px;top:64px;width:740px">{ey("Your first week at "+ADDR)}{H(56,"Move-In",extra="margin-top:10px")}{H(56,"Costs",A)}</div>'+pic(880,56,274,230,'bath','center','border-radius:0 0 70px 0')
        body+=f'<div class="abs" style="left:70px;top:292px;width:1084px;font:400 21px/1.5 {BF}">Water, sewer and trash come from the City of Dallas, gas from Atmos Energy, and you choose your electricity and internet providers. Start these a week or two ahead so everything is on the day you get the keys.</div>'
        body+=f'<div class="abs" style="left:70px;top:400px;width:500px">{ey("Set up before you arrive","margin-bottom:14px")}{su}</div><div class="abs" style="left:620px;top:400px;width:534px">{ey("Typical monthly costs","margin-bottom:14px")}{mo}</div>'
        body+=f'<div class="abs" style="left:620px;top:1000px;width:534px;border:2px solid {I};border-radius:{R}px;padding:18px 24px;display:flex;justify-content:space-between;align-items:center"><div style="font:700 13px {BF};letter-spacing:.14em;text-transform:uppercase;color:{M}">Typical utilities total<br><span style="font-weight:400;letter-spacing:0;text-transform:none">No HOA listed</span></div>{H(34,"$"+str(lo)+"–$"+str(hi),A,"text-transform:none")}</div>'
        body+=pic(70,1100,500,285,'pool','center 60%','border-radius:14px')+pic(620,1100,534,285,'liv','center 50%','border-radius:0 80px 0 0')+f'<div class="abs" style="left:70px;top:1400px;width:1084px;font:400 12.5px/1.5 {BF};color:{M}">{FINE}</div>'+foot(30)
        return page(body)
    return dict(home=home(),neigh=neigh(),num=numbers(),move=move())
if __name__=='__main__':
    import os,light
    from common import render
    os.makedirs('real',exist_ok=True)
    d={k:light.postproc('azure',v,k) for k,v in build().items()}
    render([(f'/home/claude/work/styles/real/{k}.jpg',h) for k,h in d.items()]); print('ok')
