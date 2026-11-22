from common import *
from light import STY, mix
def ctx(name):
    st=STY[name]; I,A,T,M,L,B=st['ink'],st['acc'],st['tint'],st['mute'],st['line'],st['bg']; R=st['rad']; BF=st['body']
    UP='uppercase' if st['upper'] else 'none'
    css=f"""body{{background:{B};color:{I};font-family:{BF}}} .ph{{background:{mix(T,'#ffffff',.5)};border:1.5px solid {L}}} .abs{{position:absolute}}
.hd{{font-family:{st['head']};font-weight:{st['hw']};text-transform:{UP}}} .nu{{text-transform:none}} .ey{{font:700 14px {BF};letter-spacing:.3em;text-transform:uppercase;color:{A}}}
.rw{{display:flex;justify-content:space-between;align-items:baseline;font:400 17px {BF};padding:7px 0;border-top:1px solid {L}}} .rw b{{font-weight:700}}"""
    if st.get('frame'): css+=f".frm{{position:absolute;inset:26px;border:2px solid {I};pointer-events:none}} .frm::after{{content:'';position:absolute;inset:6px;border:1px solid {A}}}"
    X=dict(st=st,I=I,A=A,T=T,M=M,L=L,B=B,R=R,BF=BF,css=css)
    X['frame']=lambda:'<div class="frm"></div>' if st.get('frame') else ''
    X['P']=lambda x,y,w,h,extra='':ph(x,y,w,h,extra=st['pshape']+';'+extra)
    X['P0']=lambda x,y,w,h,extra='':ph(x,y,w,h,extra=extra)
    def H(size,txt,color=None,extra='',up=None):
        return f'<div class="hd{"" if up is None or up else " nu"}" style="font-size:{size}px;line-height:1.08;{"color:"+color+";" if color else ""}{extra}">{txt}</div>'
    X['H']=H
    X['ey']=lambda t,extra='':f'<div class="ey" style="{extra}">{t}</div>'
    def sec(x,y,w,ic,label,center=False):
        shape='50%' if st['sec'] in('under','diamond','pill') else '10px'
        lab=(f'<div style="border:1.5px solid {A};border-radius:99px;padding:6px 18px;font:700 14px {BF};letter-spacing:.16em;text-transform:uppercase;color:{A}">{label}</div>' if st['sec']=='pill' else f'<div class="hd" style="font-size:25px;letter-spacing:.04em">{label}</div>')
        return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px"><div style="display:flex;align-items:center;gap:14px;padding-bottom:12px;border-bottom:1.5px solid {L};position:relative{";justify-content:center" if center else ""}"><div style="width:44px;height:44px;border-radius:{shape};border:1.5px solid {A};display:grid;place-items:center;flex:none">{icon(ic,24,A,1.6)}</div>{lab}<div style="position:absolute;{"left:50%;margin-left:-32px" if center else "left:0"};bottom:-2px;width:64px;height:3px;background:{A}"></div></div></div>'
    X['sec']=sec
    X['foot']=lambda bottom=44:f'<div class="abs" style="left:70px;right:70px;bottom:{bottom}px;height:92px;border-top:2px solid {A};display:flex;align-items:center;justify-content:space-between"><div style="display:flex;align-items:center;gap:18px"><div style="width:62px;height:62px;border-radius:50%;border:1.5px solid {A};background:{T};flex:none"></div><div><div class="hd nu" style="font-size:30px">{S["agent"]}</div><div style="font:700 12px {BF};letter-spacing:.2em;text-transform:uppercase;color:{M}">{S["agent_t"]} · {S["brokerage"]}</div></div></div><div style="text-align:right;font:500 19px/1.55 {BF}"><b>{S["aphone"]}</b><br>{S["aemail"]}</div></div>'
    def mapsvg(w=580,h=480):
        pts=[(110,100,'tree'),(310,80,'tree'),(480,200,'cart'),(110,340,'dine'),(420,370,'coffee')]
        p=''.join(f'<circle cx="{x}" cy="{y}" r="22" fill="#fff" stroke="{A}" stroke-width="3"/><path transform="translate({x-11},{y-11})" d="{IC[ic]}" fill="none" stroke="{A}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>' for x,y,ic in pts)
        g=mix(A,"#ffffff",.78)
        return f'<svg width="{w}" height="{h}" viewBox="0 0 580 480" preserveAspectRatio="xMidYMid slice" style="display:block"><rect width="580" height="480" fill="{T}"/><g fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round"><path d="M0 190C150 150 260 270 400 220S540 190 580 200"/><path d="M190 0C210 150 160 300 230 480"/></g><rect x="40" y="40" width="130" height="90" rx="{min(R,12)}" fill="{g}"/><rect x="410" y="330" width="130" height="100" rx="{min(R,12)}" fill="{g}"/>{p}<circle cx="260" cy="250" r="30" fill="{I}" stroke="#fff" stroke-width="4"/><path transform="translate(245,235) scale(1.25)" d="{IC["home"]}" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    X['map']=mapsvg
    X['page']=lambda body,extra='':page(fontcss(st['fonts']),css+extra,body)
    X['bul']=lambda:f'width:9px;height:9px;background:{A};{"border-radius:50%" if R>=14 else "transform:rotate(45deg)"};flex:none'
    X['lis']=lambda items,mi=False,gap=14:''.join(f'<div style="display:flex;justify-content:space-between;gap:8px;margin-bottom:{gap}px"><div><div style="font:700 19px {BF}">{i[0]}</div><div style="font:400 15px {BF};color:{M}">{i[1]}</div></div>{("<div class=hd style=font-size:18px;color:%s>%s</div>"%(A,i[2])) if mi and len(i)>2 else ""}</div>' for i in items)
    X['stat']=lambda ic,v,lb:(ic,v,lb)
    X['stats']=[('bed',S['beds'],'Bedrooms'),('bath',S['baths'],'Bathrooms'),('sqft',S['sqft'],'Sq ft'),('garage',S['garage'],'Garage')]
    X['mrows']=lambda c,pad=6,fs=16.5:''.join(f'<div class="rw" style="padding:{pad}px 0;font-size:{fs}px"><span>{a}</span><b>{v}</b></div>' for a,v in [('Principal &amp; interest',usd(c['pi'])),('Property taxes',usd(c['tax'])),('Home insurance','$300'),('Mortgage insurance',usd(c['mi']) if c['mi'] else '$0')])
    X['urows']=lambda c,pad=6,fs=16.5:''.join(f'<div class="rw" style="padding:{pad}px 0;font-size:{fs}px"><span>{a}</span><b>{v}</b></div>' for a,v in [('Down payment',usd(c['down'])),('Est. closing costs',usd(c['closing'])),('Seller credit'+(f" ({c['credit_pct']}%)" if c['credit'] else ''),('–'+usd(c['credit'])) if c['credit'] else '$0')])
    X['dl']=lambda:''.join(f'<div style="flex:1;display:flex;align-items:center;gap:18px"><span class="hd nu" style="font-size:42px;color:{A};white-space:nowrap">{a}</span><span style="font:500 18px/1.4 {BF}">{b}</span></div>' for a,b in DELTAS)
    X['contacts']=lambda y:f'<div class="abs" style="left:70px;top:{y}px;width:1084px;display:flex;justify-content:space-between"><div style="border-left:4px solid {A};padding-left:18px"><div class="hd nu" style="font-size:28px">{S["agent"]}</div><div style="font:400 17px/1.55 {BF};color:{M}">{S["agent_t"]} · {S["brokerage"]}<br><b style="color:{I}">{S["aphone"]}</b><br>{S["aemail"]}</div></div><div style="display:flex;gap:20px;align-items:center;border-left:4px solid {A};padding-left:18px"><img src="{HS}" style="width:112px;height:112px;border-radius:50%;object-fit:cover;border:2px solid {A}"><div><div class="hd nu" style="font-size:28px">{LO["name"]}</div><div style="font:400 17px/1.55 {BF};color:{M}">{LO["t"]}<br><b style="color:{I}">{LO["phone"]}</b><br>{LO["email"]}</div></div></div></div>'
    X['bottom']=lambda:f'<div class="abs" style="left:70px;right:70px;bottom:44px;border-top:2px solid {A};padding-top:18px;text-align:center;font:500 19px {BF}">Need estimates on another home? Call or text Devin <b style="color:{A}">{LO["phone"]}</b> · {LO["web"]}</div>'
    X['disc']=lambda y:f'<div class="abs" style="left:70px;top:{y}px;width:1084px;font:400 13px/1.55 {BF};color:{M}">{DISC}</div>'
    ics=['bolt','flame','drop','wifi','home']; X['ics']=ics
    lo_t=sum(m[2] for m in MOVE['monthly'] if m[2]); hi_t=sum(m[3] for m in MOVE['monthly'] if m[3]); X['tot']=(lo_t,hi_t)
    return X
