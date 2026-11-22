from lay import *
def build():
    X=ctx('terra'); st,I,A,T,M,L,B,R,BF=[X[k] for k in ('st','I','A','T','M','L','B','R','BF')]
    P,H,ey,sec,foot,page=X['P'],X['H'],X['ey'],X['sec'],X['foot'],X['page']
    C='text-align:center'
    soft=f'background:{T};border-radius:28px'
    def home():
        tiles=''.join(f'<div style="flex:1;{soft};padding:22px 0;text-align:center">{icon(ic,34,A,1.5)}{H(36,v,extra="margin-top:6px;text-transform:none")}<div style="font:700 12px {BF};letter-spacing:.18em;text-transform:uppercase;color:{M}">{lb}</div></div>' for ic,v,lb in X['stats'])
        bl=''.join(f'<div style="display:flex;gap:12px;align-items:center;margin-bottom:12px;font:600 20px {BF}"><span style="{X["bul"]()}"></span>{b}</div>' for b in S['bullets'])
        body=P(70,64,1084,560)
        body+=f'<div class="abs" style="left:70px;top:650px;width:1084px;{C}">{ey(S["hood"]+" · "+S["city"]+", "+S["state"])}{H(70,"123 Sample Street",extra="margin-top:6px;text-transform:none")}</div>'
        body+=f'<div class="abs" style="left:262px;top:790px;width:700px;border:2px solid {A};border-radius:99px;padding:10px 0;{C};display:flex;justify-content:center;align-items:baseline;gap:20px"><span class="ey">Offered at</span>{H(50,usd(S["price"]),extra="text-transform:none")}</div>'
        tiles=tiles.replace("padding:22px 0","padding:14px 0").replace("size","size")
        body+=f'<div class="abs" style="left:70px;top:890px;width:1084px;display:flex;gap:18px">{tiles}</div>'
        body+=f'<div class="abs" style="left:70px;top:1050px;width:520px;{soft};padding:24px 30px;height:360px;box-sizing:border-box">{ey("About the home","margin-bottom:12px")}<div style="font:400 20px/1.55 {BF}">{S["about"]}</div></div>'
        body+=f'<div class="abs" style="left:620px;top:1050px;width:534px;border:2px solid {L};border-radius:28px;padding:24px 30px;height:360px;box-sizing:border-box">{ey("What we love","margin-bottom:12px")}{bl.replace("margin-bottom:12px","margin-bottom:6px").replace("font:600 20px","font:600 18px")}</div>'
        return page(body+foot())
    def neigh():
        def card(x,ic,title,items,mi=False):
            return f'<div class="abs" style="left:{x}px;top:780px;width:344px;height:600px;border:2px solid {L};border-radius:28px;padding:26px 28px;box-sizing:border-box"><div style="display:flex;align-items:center;gap:12px;margin-bottom:18px"><div style="width:44px;height:44px;border-radius:50%;background:{T};display:grid;place-items:center">{icon(ic,24,A,1.7)}</div>{H(24,title,extra="text-transform:none")}</div>{X["lis"](items,mi,16)}</div>'
        pills=''.join(f'<span style="display:inline-flex;align-items:baseline;gap:8px;background:{T};border-radius:99px;padding:8px 13px;margin:0 3px 8px;white-space:nowrap">{H(20,t,A,"text-transform:none")}<span style="font:700 12px {BF};color:{M}">{n}</span></span>' for n,t in NEIGH['drive'])
        body=f'<div class="abs" style="left:70px;top:70px;width:1084px;{C}">{ey(S["hood"]+" · "+S["city"]+", "+S["state"])}{H(64,"Neighborhood Highlights",extra="margin-top:10px;text-transform:none")}<div style="font:italic 400 22px/1.5 {BF};color:{M};margin-top:12px;padding:0 90px">{NEIGH["intro"]}</div></div>'
        body+=f'<div class="abs" style="left:70px;top:330px;width:1084px;height:330px;border-radius:36px;overflow:hidden;border:2px solid {L}">{X["map"](1084,330)}</div>'
        body+=f'<div class="abs" style="left:70px;top:690px;width:1084px;{C}"><div class="ey" style="margin-bottom:10px">Drive times</div>{pills}</div>'
        body+=card(70,'tree','Parks &amp; Trails',NEIGH['parks'])+card(440,'cart','Errands',NEIGH['errands'],True)+card(810,'dine','Eat &amp; Drink',NEIGH['eat'])
        return page(body+foot())
    def numbers():
        cols=''
        for i,c in enumerate(CARDS):
            cols+=f'''<div style="flex:1;padding:30px 28px;{"border-left:2.5px dotted "+L if i else ""};text-align:center"><span style="display:inline-block;border:1.5px solid {A};border-radius:99px;padding:5px 14px;font:700 12px {BF};letter-spacing:.14em;text-transform:uppercase;color:{A}">{c['tag']}</span>{H(26,c['title']+'<br>'+c['title2'],extra="margin-top:16px;text-transform:none")}<div style="font:700 12px {BF};letter-spacing:.2em;text-transform:uppercase;color:{M};margin-top:22px">Est. monthly payment</div>{H(62,usd(c['mo'])+'<span style="font:600 22px '+BF+';color:'+M+'">/mo</span>',extra="text-transform:none;margin-top:2px")}<div style="margin-top:8px;text-align:left">{X['mrows'](c,5,16)}</div><div style="font:700 12px {BF};letter-spacing:.2em;text-transform:uppercase;color:{M};margin-top:16px">Up-front costs</div><div style="text-align:left">{X['urows'](c,5,16)}</div><div style="margin-top:18px;background:{T};border-radius:99px;padding:14px 0"><div style="font:700 11px {BF};letter-spacing:.2em;text-transform:uppercase;color:{M}">Est. cash to close</div>{H(40,usd(c['cash']),extra="text-transform:none")}</div></div>'''
        body=f'<div class="abs" style="left:70px;top:64px;width:1084px;{C}">{ey("Sample figures · "+S["full"])}{H(72,"The Numbers",extra="margin-top:10px;text-transform:none")}<div style="font:600 19px {BF};color:{M};margin-top:8px">{usd(S["price"])} · {S["beds"]} BD · {S["baths"]} BA · {S["sqft"]} SF</div></div>'
        body+=f'<div class="abs" style="left:70px;top:290px;width:1084px;border:2px solid {I};border-radius:36px;display:flex;overflow:hidden">{cols}</div>'
        body+=f'<div class="abs" style="left:70px;top:1090px;width:1084px;display:flex;gap:36px;padding:14px 0;border-top:1.5px solid {L};border-bottom:1.5px solid {L}">{X["dl"]()}</div>'+X['disc'](1175)+X['contacts'](1318)+X['bottom']()
        return page(body)
    def move():
        su=''.join(f'<div style="flex:1;border:2px solid {L};border-radius:28px;padding:24px 22px;text-align:center"><div class="hd nu" style="width:52px;height:52px;border-radius:50%;background:{T};color:{A};display:grid;place-items:center;font-size:24px;margin:0 auto 14px">{i+1}</div><div style="font:700 20px/1.25 {BF}">{a}</div><div style="font:400 14.5px/1.4 {BF};color:{M};margin-top:6px">{b}<br>{c}</div><div style="display:inline-block;margin-top:12px;border:1.5px solid {A};color:{A};border-radius:99px;font:700 13px {BF};padding:4px 12px">{d}</div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
        tiles=''
        lo_t,hi_t=X['tot']
        for i,(a,b,lo,hi) in enumerate(MOVE['monthly']):
            val=f'${lo}–${hi}' if lo else MOVE['hoa']
            tiles+=f'<div style="width:344px;box-sizing:border-box;{soft};padding:24px 26px"><div style="display:flex;align-items:center;gap:12px"><div style="width:46px;height:46px;border-radius:50%;background:#fff;display:grid;place-items:center">{icon(X["ics"][i],24,A,1.7)}</div><div style="font:700 20px {BF}">{a}</div></div>{H(34,val,A,"margin-top:14px;text-transform:none")}<div style="font:400 14.5px/1.4 {BF};color:{M};margin-top:6px">{b}</div></div>'
        tiles+=f'<div style="width:344px;box-sizing:border-box;border:2px solid {A};border-radius:28px;padding:24px 26px"><div class="ey">Utilities total</div>{H(36,"$"+str(lo_t)+"–$"+str(hi_t),extra="margin-top:14px;text-transform:none")}<div style="font:400 14.5px/1.4 {BF};color:{M};margin-top:6px">Typical monthly total, excluding HOA.</div></div>'
        body=f'<div class="abs" style="left:70px;top:64px;width:1084px;{C}">{ey("Your first week at "+S["street"])}{H(72,"Move-In Costs",extra="margin-top:10px;text-transform:none")}<div style="font:italic 400 22px/1.5 {BF};color:{M};margin-top:12px;padding:0 90px">{MOVE["intro"]}</div></div>'
        body+=f'<div class="abs" style="left:70px;top:350px;width:1084px"><div class="ey" style="text-align:center;margin-bottom:14px">Set up before you arrive</div><div style="display:flex;gap:16px">{su}</div></div>'
        body+=f'<div class="abs" style="left:70px;top:770px;width:1084px"><div class="ey" style="text-align:center;margin-bottom:14px">Typical monthly costs</div><div style="display:flex;flex-wrap:wrap;gap:20px 24px">{tiles}</div></div>'
        body+=f'<div class="abs" style="left:70px;top:1400px;width:1084px;font:400 12.5px/1.5 {BF};color:{M};{C}">{MOVE["fine"]}</div>'
        return page(body+foot(30))
    return dict(home=home(),neigh=neigh(),num=numbers(),move=move())
