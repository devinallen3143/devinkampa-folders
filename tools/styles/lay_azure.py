from lay import *
def build():
    X=ctx('azure'); st,I,A,T,M,L,B,R,BF=[X[k] for k in ('st','I','A','T','M','L','B','R','BF')]
    P,H,ey,sec,foot,page=X['P'],X['H'],X['ey'],X['sec'],X['foot'],X['page']
    def home():
        sb=''.join(f'<div style="display:flex;align-items:center;gap:16px;padding:16px 0;border-top:1.5px solid {L}">{icon(ic,34,A,1.5)}<div class="hd nu" style="font-size:34px;width:92px">{v}</div><div style="font:700 13px {BF};letter-spacing:.16em;text-transform:uppercase;color:{M}">{lb}</div></div>' for ic,v,lb in X['stats'])
        bl=''.join(f'<div style="display:flex;gap:12px;align-items:center;font:500 20px {BF}"><span style="{X["bul"]()}"></span>{b}</div>' for b in S['bullets'])
        body=f'<div class="abs" style="left:70px;top:64px;display:flex;align-items:center;gap:12px"><div style="width:44px;height:44px;border-radius:14px;border:2px solid {A};display:grid;place-items:center"><div style="width:16px;height:16px;border:4px solid {I};border-radius:50%"></div></div><div class="hd nu" style="font-size:20px;line-height:1.1">Your<br>Company</div></div>'
        body+=f'<div class="abs" style="left:70px;top:190px;width:310px">{ey("Offered at")}{H(54,usd(S["price"]),extra="margin-top:6px;letter-spacing:-.01em")}<div style="width:70px;height:5px;background:{A};margin:16px 0 28px"></div>{sb}<div style="border-top:1.5px solid {L};padding-top:26px;display:flex;align-items:center;gap:16px">{qr_svg("https://devinkampa.com/folder",I,size=120)}<div style="font:600 14px/1.4 {BF};color:{M}">Scan for the interactive folder</div></div></div>'
        body+=f'<div class="abs" style="left:420px;top:70px;height:1360px;border-left:1.5px solid {L}"></div>'
        body+=P(460,64,694,600)
        body+=f'<div class="abs" style="left:460px;top:690px;width:694px">{ey(S["hood"]+" · "+S["city"]+", "+S["state"])}{H(60,"Open House",extra="margin-top:8px")}{H(60,"123 Sample Street",A)}</div>'
        body+=f'<div class="abs" style="left:460px;top:880px;width:694px;font:400 20px/1.5 {BF};color:{I}">{S["about"]}</div>'
        body+=f'<div class="abs" style="left:460px;top:1005px;width:694px">{ey("Features &amp; facility","margin-bottom:12px")}<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px 20px">{bl}</div></div>'
        body+=P(460,1195,340,225)+P(814,1195,340,225)+foot()
        return page(body)
    def neigh():
        items=[('tree',)+NEIGH['parks'][0][:2]+('Park',),('tree',)+NEIGH['parks'][1][:2]+('Trail',),('cart',)+NEIGH['errands'][0][:2]+(NEIGH['errands'][0][2],),('cross',)+NEIGH['errands'][1][:2]+(NEIGH['errands'][1][2],),('dine',)+NEIGH['eat'][0][:2]+('Dining',),('coffee',)+NEIGH['eat'][3][:2]+('Coffee',),('school','Top-rated schools','Zoned schools nearby','8 min'),('home','Community Pool','Neighborhood amenity','On site')]
        tl=''
        for i,(ic,t,d,chip) in enumerate(items):
            x=70+(i%2)*550; y=500+(i//2)*128
            tl+=f'<div class="abs" style="left:{x}px;top:{y}px;width:534px;height:110px;border-top:1.5px solid {L};display:flex;align-items:center;gap:20px"><div style="width:64px;height:64px;border-radius:14px;border:1.5px solid {A};display:grid;place-items:center;flex:none">{icon(ic,32,A,1.6)}</div><div style="flex:1"><div class="hd nu" style="font-size:23px">{t}</div><div style="font:400 16px {BF};color:{M}">{d}</div></div><div style="border:1.5px solid {A};color:{A};border-radius:99px;font:700 14px {BF};padding:5px 14px;white-space:nowrap">{chip}</div></div>'
        dr=''.join(f'<div style="flex:1;text-align:center;{"border-left:1.5px solid "+L if i else ""}">{H(36,t,A,"text-transform:none")}<div style="font:700 12px {BF};letter-spacing:.12em;text-transform:uppercase;color:{M};margin-top:4px">{n}</div></div>' for i,(n,t) in enumerate(NEIGH["drive"]))
        body=f'<div class="abs" style="left:70px;top:64px;width:740px">{ey(S["hood"]+" · "+S["city"]+", "+S["state"])}{H(56,"Neighborhood",extra="margin-top:10px")}{H(56,"Highlights",A)}</div>'+P(880,56,274,230)
        body+=f'<div class="abs" style="left:70px;top:292px;width:760px;font:400 21px/1.5 {BF}">{NEIGH["intro"]}</div>'
        body+=f'<div class="abs" style="left:70px;top:352px;width:1084px;display:none"></div>'
        body+=f'<div class="abs" style="left:70px;top:372px;width:1084px;display:flex;padding:20px 0;border-top:2px solid {I};border-bottom:1.5px solid {L}">{dr}</div>'
        body+=tl+f'<div class="abs" style="left:70px;top:1130px;width:1084px;height:290px;border-radius:{R}px;overflow:hidden;border:2px solid {I}">{X["map"](1084,330)}</div>'+foot()
        return page(body)
    def numbers():
        rows=''
        for i,c in enumerate(CARDS):
            y=300+i*272
            rows+=f'''<div class="abs" style="left:70px;top:{y}px;width:1084px;height:252px;border:2px solid {I};border-radius:{R}px;display:flex"><div style="width:250px;padding:24px 24px;border-right:1.5px solid {L}"><div style="display:inline-block;background:{A};color:#fff;border-radius:99px;font:700 12px {BF};letter-spacing:.12em;text-transform:uppercase;padding:5px 12px">{c['tag']}</div>{H(25,c['title']+'<br>'+c['title2'],extra="margin-top:16px;text-transform:none")}</div>
<div style="width:300px;padding:20px 24px;border-right:1.5px solid {L}"><div style="font:700 12px {BF};letter-spacing:.16em;text-transform:uppercase;color:{M}">Est. monthly payment</div>{H(54,usd(c['mo'])+'<span style="font:500 20px '+BF+';color:'+M+'">/mo</span>',extra="margin:4px 0 8px;text-transform:none")}{X['mrows'](c,4,15)}</div>
<div style="width:290px;padding:20px 24px;border-right:1.5px solid {L}"><div style="font:700 12px {BF};letter-spacing:.16em;text-transform:uppercase;color:{M};margin-bottom:8px">Up-front costs</div>{X['urows'](c,9,16.5)}</div>
<div style="flex:1;padding:20px 24px;background:{T};display:flex;flex-direction:column;justify-content:center"><div style="font:700 12px {BF};letter-spacing:.16em;text-transform:uppercase;color:{M}">Est. cash to close</div>{H(44,usd(c['cash']),extra="margin-top:6px;text-transform:none")}<div style="width:50px;height:4px;background:{A};margin-top:14px"></div></div></div>'''
        body=f'<div class="abs" style="left:70px;top:64px">{ey("Sample figures · "+S["full"])}{H(66,"The Numbers",extra="margin-top:10px")}<div style="font:600 19px {BF};color:{M};margin-top:12px">{usd(S["price"])} · {S["beds"]} BD · {S["baths"]} BA · {S["sqft"]} SF</div></div>'+P(880,56,274,200)
        body+=rows+f'<div class="abs" style="left:70px;top:1135px;width:1084px;display:flex;gap:36px;padding:14px 0;border-top:1.5px solid {L};border-bottom:1.5px solid {L}">{X["dl"]()}</div>'+X['disc'](1225)+X['contacts'](1335)+X['bottom']()
        return page(body)
    def move():
        su=''.join(f'<div style="display:flex;gap:18px;padding:30px 0;border-top:1.5px solid {L}"><div class="hd nu" style="width:50px;height:50px;border-radius:14px;border:1.5px solid {A};color:{A};display:grid;place-items:center;font-size:24px;flex:none">{i+1}</div><div style="flex:1"><div style="font:700 21px {BF}">{a}</div><div style="font:400 15px/1.45 {BF};color:{M}">{b}<br>{c}</div><div style="display:inline-block;margin-top:8px;border:1.5px solid {A};color:{A};border-radius:99px;font:700 13px {BF};padding:4px 12px">{d}</div></div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
        mo=''
        for i,(a,b,lo,hi) in enumerate(MOVE['monthly']):
            val=f'${lo}–${hi}' if lo else MOVE['hoa']
            bar=f'<div style="height:6px;background:{T};margin-top:10px;border-radius:6px;position:relative"><div style="position:absolute;left:{lo/4}%;width:{(hi-lo)/4}%;top:0;bottom:0;background:{A};border-radius:6px"></div></div>' if lo else ''
            mo+=f'<div style="display:flex;gap:16px;padding:27px 0;border-top:1.5px solid {L}"><div style="width:48px;height:48px;border-radius:14px;border:1.5px solid {A};display:grid;place-items:center;flex:none">{icon(X["ics"][i],26,A,1.6)}</div><div style="flex:1"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font:700 20px {BF}">{a}</span>{H(24,val,extra="text-transform:none")}</div><div style="font:400 14.5px {BF};color:{M}">{b}</div>{bar}</div></div>'
        lo,hi=X['tot']
        body=f'<div class="abs" style="left:70px;top:64px;width:740px">{ey("Your first week at "+S["street"])}{H(56,"Move-In",extra="margin-top:10px")}{H(56,"Costs",A)}</div>'+P(880,56,274,230)
        body+=f'<div class="abs" style="left:70px;top:292px;width:1084px;font:400 21px/1.5 {BF}">{MOVE["intro"]}</div>'
        body+=f'<div class="abs" style="left:70px;top:400px;width:500px">{ey("Set up before you arrive","margin-bottom:14px")}{su}</div><div class="abs" style="left:620px;top:400px;width:534px">{ey("Typical monthly costs","margin-bottom:14px")}{mo}</div>'
        body+=f'<div class="abs" style="left:620px;top:1230px;width:534px;border:2px solid {I};border-radius:{R}px;padding:18px 24px;display:flex;justify-content:space-between;align-items:center"><div style="font:700 13px {BF};letter-spacing:.14em;text-transform:uppercase;color:{M}">Typical utilities total<br><span style="font-weight:400;letter-spacing:0;text-transform:none">Excludes HOA</span></div>{H(34,"$"+str(lo)+"–$"+str(hi),A,"text-transform:none")}</div>'
        body+=f'<div class="abs" style="left:70px;top:1400px;width:1084px;font:400 12.5px/1.5 {BF};color:{M}">{MOVE["fine"]}</div>'+foot(30)
        return page(body)
    return dict(home=home(),neigh=neigh(),num=numbers(),move=move())
