from lay import *
def build():
    X=ctx('evergreen'); st,I,A,T,M,L,B,R,BF=[X[k] for k in ('st','I','A','T','M','L','B','R','BF')]
    P,H,ey,sec,foot,page,fr=X['P'],X['H'],X['ey'],X['sec'],X['foot'],X['page'],X['frame']
    def home():
        sb=''.join(f'<div style="display:flex;align-items:center;gap:18px;padding:18px 0;border-top:1px solid {L}">{icon(ic,36,A,1.4)}<div><div class="hd nu" style="font-size:36px;line-height:1">{v}</div><div style="font:700 12px {BF};letter-spacing:.2em;text-transform:uppercase;color:{M};margin-top:4px">{lb}</div></div></div>' for ic,v,lb in X['stats'])
        bl=''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:13px;font:500 21px {BF}"><span style="{X["bul"]()}"></span>{b}</div>' for b in S['bullets'])
        st2=''.join(f'<div style="display:flex;align-items:center;gap:14px;padding:16px 0;border-top:1px solid {L}">{icon(ic,34,A,1.4)}<div><div class="hd nu" style="font-size:32px;line-height:1">{v}</div><div style="font:700 11px {BF};letter-spacing:.18em;text-transform:uppercase;color:{M};margin-top:3px">{lb}</div></div></div>' for ic,v,lb in X['stats'])
        bl=bl.replace("margin-bottom:13px","margin-bottom:8px").replace("font:500 21px","font:500 19px")
        body=fr()+X['P0'](70,70,560,700)
        body+=f'<div class="abs" style="left:670px;top:76px;width:484px">{ey("Open house · "+S["hood"])}{H(60,"123 Sample",extra="margin-top:12px;text-transform:none;line-height:1.02")}{H(60,"Street",A,"text-transform:none;line-height:1.02")}<div style="width:90px;height:3px;background:{A};margin:16px 0 12px"></div><div style="font:italic 400 22px {BF};color:{M}">{S["city"]}, {S["state"]} {S["zip"]}</div><div style="margin-top:18px">{ey("Offered at")}{H(58,usd(S["price"]),extra="margin-top:2px;text-transform:none")}</div></div>'
        body+=f'<div class="abs" style="left:670px;top:470px;width:484px;display:grid;grid-template-columns:1fr 1fr;column-gap:24px">{st2}</div>'
        body+=f'<div class="abs" style="left:70px;top:810px;width:520px">{ey("About the home","margin-bottom:10px")}<div style="font:italic 400 22px/1.5 {BF}">{S["about"]}</div></div><div class="abs" style="left:640px;top:810px;width:514px">{ey("Home highlights","margin-bottom:12px")}{bl}</div>'
        body+=X['P0'](70,1140,345,260)+X['P0'](442,1140,345,260)+X['P0'](814,1140,340,260)
        return page(body+foot(52))
    def neigh():
        def blk(y,ic,title,items,mi=False):
            return sec(70,y,560,ic,title)+f'<div class="abs" style="left:70px;top:{y+72}px;width:560px;display:grid;grid-template-columns:1fr;gap:0">{X["lis"](items[:4],mi,14)}</div>'
        tl=''.join(f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:0;padding:11px 0;border-top:1px solid {L}"><span style="width:12px;height:12px;border-radius:50%;border:2px solid {A};flex:none"></span><span style="flex:1;font:700 16px {BF};letter-spacing:.1em;text-transform:uppercase;color:{M}">{n}</span>{H(24,t,I,"text-transform:none")}</div>' for n,t in NEIGH['drive'])
        body=fr()+f'<div class="abs" style="left:80px;top:76px;width:1064px">{ey(S["hood"]+" · "+S["city"]+", "+S["state"])}{H(66,"Neighborhood <i style=font-weight:400;color:"+A+">Highlights</i>",extra="margin-top:10px;text-transform:none")}<div style="font:italic 400 24px/1.5 {BF};color:{M};margin-top:14px;width:880px">{NEIGH["intro"]}</div></div>'
        body+=blk(340,'tree','Parks &amp; Trails',NEIGH['parks'])+blk(700,'cart','Everyday Errands',NEIGH['errands'],True)+blk(1060,'dine','Eat &amp; Drink',NEIGH['eat'])
        body+=f'<div class="abs" style="left:690px;top:340px;width:464px;height:470px;border:2px solid {I};overflow:hidden">{X["map"](464,470)}</div>'
        body+=f'<div class="abs" style="left:690px;top:850px;width:464px">{ey("Drive times","margin-bottom:8px")}{tl}</div>'
        body+=X['P0'](690,1260,464,120)
        return page(body+foot(52))
    def numbers():
        hd=''.join(f'<div style="flex:1;padding:18px 20px;border-left:1px solid {L};text-align:left"><div style="font:700 12px {BF};letter-spacing:.14em;text-transform:uppercase;color:{A}">{c["tag"]}</div>{H(22,c["title"]+"<br>"+c["title2"],extra="margin-top:10px;text-transform:none")}</div>' for c in CARDS)
        def row(label,vals,big=False,bg=None,bold=False,h=52):
            cells=''.join(f'<div style="flex:1;padding:0 20px;border-left:1px solid {L};display:flex;align-items:center;font:{"700" if bold else "500"} {"30px "+st["head"] if big else "18px "+BF}">{v}</div>' for v in vals)
            return f'<div style="display:flex;height:{h}px;border-top:1px solid {L};{"background:"+bg+";" if bg else ""}"><div style="width:310px;padding:0 20px;display:flex;align-items:center;font:{"700" if bold else "500"} {"20px "+BF if big else "17px "+BF};{"color:"+M if not bold else ""}">{label}</div>{cells}</div>'
        def sub(t): return f'<div style="height:40px;border-top:1.5px solid {A};display:flex;align-items:center;padding:0 20px">{ey(t)}</div>'
        tb=f'<div style="display:flex"><div style="width:310px;padding:18px 20px">{ey("Scenario")}</div>{hd}</div>'
        tb+=row('Est. monthly payment',[usd(c['mo'])+'/mo' for c in CARDS],True,None,True,92)
        tb+=row('Principal &amp; interest',[usd(c['pi']) for c in CARDS])+row('Property taxes',[usd(c['tax']) for c in CARDS])+row('Home insurance',['$650']*len(CARDS))+row('Mortgage insurance',[usd(c['mi']) if c['mi'] else '$0' for c in CARDS])
        tb+=sub('Up-front costs')
        tb+=row('Down payment',[usd(c['down']) for c in CARDS])+row('Est. closing costs',[usd(c['closing']) for c in CARDS])+row('Seller credit',[('–'+usd(c['credit'])+f" ({c['credit_pct']}%)") if c['credit'] else '$0' for c in CARDS])
        tb+=row('Est. cash to close',[usd(c['cash']) for c in CARDS],True,T,True,100)
        body=fr()+f'<div class="abs" style="left:80px;top:76px">{ey("Sample figures · "+S["full"])}{H(72,"The Numbers",extra="margin-top:12px;text-transform:none")}<div style="font:italic 400 22px {BF};color:{M};margin-top:10px">{usd(S["price"])} · {S["beds"]} BD · {S["baths"]} BA · {S["sqft"]} SF</div></div>'+X['P0'](930,70,224,190)
        body+=f'<div class="abs" style="left:70px;top:300px;width:1084px;border:2px solid {I}">{tb}</div>'
        body+=f'<div class="abs" style="left:70px;top:1090px;width:1084px;display:flex;gap:36px;padding:14px 0;border-top:1.5px solid {L};border-bottom:1.5px solid {L}">{X["dl"]()}</div>'+X['disc'](1165)+X['contacts'](1310)
        body+=f'<div class="abs" style="left:70px;right:70px;bottom:56px;border-top:2px solid {A};padding-top:14px;text-align:center;font:500 19px {BF}">Need estimates on another home? Call or text Devin <b style="color:{A}">{LO["phone"]}</b> · {LO["web"]}</div>'
        return page(body)
    def move():
        n=len(MOVE['setup'])
        su=''.join(f'<div style="display:flex;gap:20px"><div style="width:48px;display:flex;flex-direction:column;align-items:center"><div class="hd nu" style="width:48px;height:48px;border-radius:50%;border:2px solid {A};color:{A};display:grid;place-items:center;font-size:22px;background:{B}">{i+1}</div>{"<div style=flex:1;width:2px;background:"+L+";min-height:60px></div>" if i<n-1 else ""}</div><div style="flex:1;padding-bottom:34px"><div style="font:700 22px {BF}">{a}</div><div style="font:400 15.5px/1.45 {BF};color:{M}">{b}<br>{c}</div>{H(19,d,A,"font-style:italic;font-weight:400;margin-top:6px;text-transform:none")}</div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
        mo=''
        for i,(a,b,lo,hi) in enumerate(MOVE['monthly']):
            val=f'${lo}–${hi}' if lo else MOVE['hoa']
            bar=f'<div style="height:5px;background:{T};margin-top:8px;position:relative"><div style="position:absolute;left:{lo/8}%;width:{(hi-lo)/8}%;top:0;bottom:0;background:{A}"></div></div>' if lo else ''
            mo+=f'<div style="padding:16px 0;border-top:1px solid {L}"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="display:flex;align-items:center;gap:12px;font:700 21px {BF}">{icon(X["ics"][i],24,A,1.6)}{a}</span>{H(26,val,extra="text-transform:none")}</div><div style="font:400 14.5px {BF};color:{M};margin:4px 0 0 36px">{b}</div>{bar}</div>'
        lo,hi=X['tot']
        body=fr()+f'<div class="abs" style="left:80px;top:76px;width:830px">{ey("Your first week at "+S["street"])}{H(72,"Move-In <i style=font-weight:400;color:"+A+">Costs</i>",extra="margin-top:12px;text-transform:none")}<div style="font:italic 400 23px/1.5 {BF};color:{M};margin-top:12px">{MOVE["intro"]}</div></div>'+X['P0'](930,70,224,190)
        body+=f'<div class="abs" style="left:80px;top:370px;width:480px">{ey("Set up before you arrive","margin-bottom:22px")}{su}</div>'
        body+=f'<div class="abs" style="left:610px;top:370px;height:880px;border-left:1px solid {L}"></div>'
        body+=f'<div class="abs" style="left:650px;top:370px;width:504px">{ey("Typical monthly costs","margin-bottom:10px")}{mo}<div style="border-top:2px solid {A};padding:16px 0;display:flex;justify-content:space-between;align-items:baseline"><span style="font:700 14px {BF};letter-spacing:.16em;text-transform:uppercase">Utilities total<span style="font-weight:400;letter-spacing:0;text-transform:none;color:{M}"> · excl. HOA</span></span>{H(30,"$"+str(lo)+"–$"+str(hi),A,"text-transform:none")}</div></div>'
        body+=f'<div class="abs" style="left:80px;top:1360px;width:1064px;font:400 12.5px/1.5 {BF};color:{M}">{MOVE["fine"]}</div>'
        return page(body+foot(52))
    return dict(home=home(),neigh=neigh(),num=numbers(),move=move())
