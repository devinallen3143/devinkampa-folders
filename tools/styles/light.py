from common import *
def mix(a,b,t):
    a=[int(a[i:i+2],16) for i in (1,3,5)]; b=[int(b[i:i+2],16) for i in (1,3,5)]
    return '#%02x%02x%02x'%tuple(round(a[i]+(b[i]-a[i])*t) for i in range(3))
STY={
 'metropolitan':dict(fonts=[('Oswald','oswald',w,'normal') for w in (400,500,600,700)]+[('Allura','allura',400,'normal'),('Lato','lato',400,'normal'),('Lato','lato',700,'normal')],
   head='Oswald,sans-serif',hw=600,upper=True,body='Lato,sans-serif',ink='#111111',acc='#111111',mark='#F2C9CF',tint='#F3F3F3',bg='#FFFFFF',mute='#666666',line='#D6D6D6',
   rad=0,chamf=True,hero='right',pshape='clip-path:polygon(70px 0,100% 0,100% 100%,0 100%)',script='Allura',tsize=90,cs=1.0,sec='under'),
 'azure':dict(fonts=[('Poppins','poppins',w,'normal') for w in (400,500,600,700,800)]+[('Inter','inter',w,'normal') for w in (400,500,600)],
   head='Poppins,sans-serif',hw=800,upper=True,body='Inter,sans-serif',ink='#111111',acc='#111111',mark='#CFD2D7',tint='#F3F3F3',bg='#FFFFFF',mute='#666666',line='#D6D6D6',
   rad=14,chamf=False,hero='right',pshape='border-radius:0 0 0 90px',script=None,tsize=78,cs=.98,sec='chip',qr=True),
 'terra':dict(fonts=[('Nunito','nunito',w,'normal') for w in (400,600,700,800)]+[('Quicksand','quicksand',w,'normal') for w in (500,600,700)],
   head='Quicksand,sans-serif',hw=700,upper=False,body='Nunito,sans-serif',ink='#111111',acc='#111111',mark='#E2BD93',tint='#F3F3F3',bg='#FFFFFF',mute='#666666',line='#D6D6D6',
   rad=28,chamf=False,hero='band',pshape='border-radius:40px',script=None,tsize=80,cs=1.0,sec='pill',center=True),
 'evergreen':dict(fonts=[('Fraunces','fraunces',w,'normal') for w in (400,600,700)]+[('Fraunces','fraunces',400,'italic'),('Karla','karla',400,'normal'),('Karla','karla',500,'normal'),('Karla','karla',700,'normal')],
   head='Fraunces,serif',hw=600,upper=False,body='Karla,sans-serif',ink='#111111',acc='#111111',mark='#E3C48C',tint='#F3F3F3',bg='#FFFFFF',mute='#666666',line='#D6D6D6',
   rad=0,chamf=False,hero='flip',pshape='',script=None,tsize=84,cs=1.0,sec='diamond',frame=True),
}
def build(name):
    st=STY[name]; I,A,T,M,L,B=st['ink'],st['acc'],st['tint'],st['mute'],st['line'],st['bg']
    HF=st['head']; HW=st['hw']; UP='uppercase' if st['upper'] else 'none'; R=st['rad']
    center=st.get('center',False)
    css=f"""body{{background:{B};color:{I};font-family:{st['body']}}} .ph{{background:{mix(T,'#ffffff',.5)};border:1.5px solid {L}}} .abs{{position:absolute}}
.hd{{font-family:{HF};font-weight:{HW};text-transform:{UP}}} .ey{{font:700 14px {st['body']};letter-spacing:.3em;text-transform:uppercase;color:{A}}}
.rw{{display:flex;justify-content:space-between;align-items:baseline;font:400 18px {st['body']};padding:10px 0;border-top:1px solid {L}}} .rw b{{font-weight:700}}
.card{{position:absolute;background:#fff;border:2px solid {I};border-radius:{R}px;{'clip-path:polygon(0 0,calc(100% - 34px) 0,100% 34px,100% 100%,0 100%);' if st['chamf'] else ''}}}"""
    if st.get('frame'): css+=f".frm{{position:absolute;inset:26px;border:2px solid {I};pointer-events:none}} .frm::after{{content:'';position:absolute;inset:6px;border:1px solid {A}}}"
    def frame(): return '<div class="frm"></div>' if st.get('frame') else ''
    P=lambda x,y,w,h,extra='':ph(x,y,w,h,extra=st['pshape']+';'+extra)
    def sec(x,y,w,ic,label):
        shape='50%' if st['sec'] in('under','diamond','pill') else '10px'
        if st['sec']=='pill': lab=f'<div style="display:inline-block;border:1.5px solid {A};border-radius:99px;padding:6px 18px;font:700 14px {st["body"]};letter-spacing:.16em;text-transform:uppercase;color:{A}">{label}</div>'
        else: lab=f'<div class="hd" style="font-size:25px;letter-spacing:.05em">{label}</div>'
        return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px"><div style="display:flex;align-items:center;gap:14px;padding-bottom:12px;border-bottom:1.5px solid {L};position:relative"><div style="width:44px;height:44px;border-radius:{shape};border:1.5px solid {A};display:grid;place-items:center;flex:none">{icon(ic,24,A,1.6)}</div>{lab}<div style="position:absolute;left:0;bottom:-2px;width:64px;height:3px;background:{A}"></div></div></div>'
    def foot():
        return f'<div class="abs" style="left:70px;right:70px;bottom:44px;height:92px;border-top:2px solid {A};display:flex;align-items:center;justify-content:space-between"><div style="display:flex;align-items:center;gap:18px"><div style="width:62px;height:62px;border-radius:50%;border:1.5px solid {A};background:{T};flex:none"></div><div><div class="hd" style="font-size:30px;text-transform:none">{S["agent"]}</div><div style="font:700 12px {st["body"]};letter-spacing:.2em;text-transform:uppercase;color:{M}">{S["agent_t"]} · {S["brokerage"]}</div></div></div><div style="text-align:right;font:500 19px/1.55 {st["body"]}"><b>{S["aphone"]}</b><br>{S["aemail"]}</div></div>'
    def titleblock(eyebrow,line1,line2='',x=70,y=70,w=540,align='left',size=None,script=False):
        size=size or st['tsize']
        sc=f'<div style="font:400 {size*.85:.0f}px {st["script"]};color:{A};line-height:1;margin:2px 0 4px">Open House</div>' if script and st['script'] else ''
        return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;text-align:{align}"><div class="ey">{eyebrow}</div>{sc}<div class="hd" style="font-size:{size}px;line-height:{st["cs"]};margin-top:12px">{line1}</div>{("<div class=hd style=font-size:%dpx;line-height:%s;color:%s>%s</div>"%(size,st["cs"],A,line2)) if line2 else ""}</div>'
    def hero_photo(h=420):
        if st['hero']=='right': return P(630,64,534,h)
        if st['hero']=='flip': return P(60,64,534,h)
        return ''
    def head(eyebrow,l1,l2,small=False):
        h=230 if small else 420
        if small and st['hero'] in('right','flip'):
            return P(840,56,314,200)+titleblock(eyebrow,l1+' '+l2,'',70,74,740,size=st['tsize']-24)
        if st['hero']=='right': return hero_photo(h)+titleblock(eyebrow,l1,l2,70,74,560,size=st['tsize'],script=True)
        if st['hero']=='flip': return hero_photo(h)+titleblock(eyebrow,l1,l2,650,74,520,size=st['tsize']-8,script=False)
        if small: return P(840,56,314,200)+titleblock(eyebrow,l1+' '+l2,'',70,74,740,size=st['tsize']-14)
        return P(70,64,1084,300)+titleblock(eyebrow,l1+' '+l2,'',70,404,1084,'center',size=st['tsize']-10)
    # ---------- HOME ----------
    def home():
        stats=''.join(f'<div style="flex:1;text-align:center;{"border-left:1.5px solid "+L if i else ""}">{icon(ic,30,A,1.5)}<div class="hd" style="font-size:34px;line-height:1.1;margin-top:2px;text-transform:none">{v}</div><div style="font:700 11px {st["body"]};letter-spacing:.2em;text-transform:uppercase;color:{M}">{lb}</div></div>' for i,(ic,v,lb) in enumerate([('bed',S['beds'],'Bedrooms'),('bath',S['baths'],'Bathrooms'),('sqft',S['sqft'],'Sq ft'),('garage',S['garage'],'Garage')]))
        bl=''.join(f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:9px;font:500 20px {st["body"]}"><span style="width:9px;height:9px;background:{A};transform:rotate(45deg);flex:none"></span>{b}</div>' for b in S['bullets'])
        body=ph(0,0,1224,640,extra="clip-path:polygon(0 0,100% 0,100% 86%,0 100%)")
        body+=f'<div class="abs" style="left:70px;top:640px;width:700px"><div class="ey">{S["hood"]} · {S["city"]}, {S["state"]}</div><div style="font:400 64px {st["script"]};color:{A};line-height:1;margin-top:2px">Open House</div><div class="hd" style="font-size:70px;line-height:1;margin-top:2px">123 Sample Street</div></div>'
        body+=f'<div class="abs" style="right:70px;top:668px;text-align:right"><div class="ey">Offered at</div><div class="hd" style="font-size:66px;line-height:1.05;text-transform:none">{usd(S["price"])}</div></div>'
        body+=f'<div class="abs" style="left:70px;top:870px;width:1084px;display:flex;padding:16px 0;border-top:1.5px solid {L};border-bottom:1.5px solid {L}">{stats}</div>'
        body+=f'<div class="abs" style="left:70px;top:1010px;width:480px"><div class="ey" style="margin-bottom:12px">About the home</div><div style="font:italic 400 22px/1.5 {st["body"]}">{S["about"]}</div></div><div class="abs" style="left:620px;top:1010px;width:534px"><div class="ey" style="margin-bottom:14px">Property highlights</div>{bl}</div>'
        body+=ph(70,1320,340,110,extra=st['pshape'])+ph(442,1320,340,110,extra=st['pshape'])+ph(814,1320,340,110,extra=st['pshape'])+foot()
        return page(fontcss(st['fonts']),css,body)
    def mapsvg():
        pts=[(110,100,'tree'),(310,80,'tree'),(480,200,'cart'),(110,340,'dine'),(420,370,'coffee')]
        p=''.join(f'<circle cx="{x}" cy="{y}" r="22" fill="#fff" stroke="{A}" stroke-width="3"/><path transform="translate({x-11},{y-11})" d="{IC[ic]}" fill="none" stroke="{A}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>' for x,y,ic in pts)
        return f'<svg width="580" height="480" viewBox="0 0 580 480" style="display:block"><rect width="580" height="480" fill="{T}"/><g fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round"><path d="M0 190C150 150 260 270 400 220S540 190 580 200"/><path d="M190 0C210 150 160 300 230 480"/></g><rect x="40" y="40" width="130" height="90" rx="{min(R,12)}" fill="{mix(A,"#ffffff",.78)}"/><rect x="410" y="330" width="130" height="100" rx="{min(R,12)}" fill="{mix(A,"#ffffff",.78)}"/>{p}<circle cx="260" cy="250" r="30" fill="{I}" stroke="#fff" stroke-width="4"/><path transform="translate(245,235) scale(1.25)" d="{IC["home"]}" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    # ---------- NEIGH ----------
    def neigh():
        def col(x,ic,title,items,mi=False):
            rows=''.join(f'<div style="display:flex;justify-content:space-between;gap:8px;margin-bottom:14px"><div><div style="font:700 19px {st["body"]}">{i[0]}</div><div style="font:400 15px {st["body"]};color:{M}">{i[1]}</div></div>{"<div class=hd style=font-size:18px;color:%s;text-transform:none>%s</div>"%(A,i[2]) if mi else ""}</div>' for i in items)
            return sec(x,880,340,ic,title)+f'<div class="abs" style="left:{x}px;top:962px;width:340px">{rows}</div>'
        drv=''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:11px 0;border-top:1px solid {L}"><span style="font:700 16px {st["body"]};letter-spacing:.14em;text-transform:uppercase;color:{M}">{n}</span><span class="hd" style="font-size:28px;color:{I};text-transform:none">{t}</span></div>' for n,t in NEIGH['drive'])
        body=frame()+head(f"{S['hood']} · {S['city']}, {S['state']}",'Neighborhood','Highlights',small=True)
        body+=f'<div class="abs" style="left:70px;top:290px;width:1084px;font:italic 400 25px/1.5 {st["body"]};color:{I};{"text-align:center" if center else ""}">{NEIGH["intro"]}</div>'
        body+=f'<div class="abs" style="left:70px;top:380px;width:580px;height:480px;border:2px solid {I};border-radius:{R}px;overflow:hidden">{mapsvg()}</div>'
        body+=f'<div class="abs" style="left:700px;top:380px;width:454px"><div class="ey" style="margin-bottom:8px">Drive times</div>{drv}</div>'
        body+=col(70,'tree','Parks &amp; Trails',NEIGH['parks'][:4])+col(442,'cart','Errands',NEIGH['errands'][:4],True)+col(814,'dine','Eat &amp; Drink',NEIGH['eat'][:4])+foot()
        return page(fontcss(st['fonts']),css,body)
    # ---------- NUMBERS ----------
    def numbers():
        cards=''
        for i,c in enumerate(CARDS):
            x=70+i*(352+14+ (0))
            pr=lambda a,v:f'<div class="rw" style="padding:6px 0;font-size:16.5px"><span>{a}</span><b>{v}</b></div>'
            mrows=pr('Principal &amp; interest',usd(c['pi']))+pr('Property taxes',usd(c['tax']))+pr('Home insurance','$300')+pr('Mortgage insurance',usd(c['mi']) if c['mi'] else '$0')
            rows=f'<div class="rw"><span>Down payment</span><b>{usd(c["down"])}</b></div><div class="rw"><span>Est. closing costs</span><b>{usd(c["closing"])}</b></div><div class="rw"><span>Seller credit{" ("+str(c["credit_pct"])+"%)" if c["credit"] else ""}</span><b>{"–"+usd(c["credit"]) if c["credit"] else "$0"}</b></div>'
            tag=f'<span style="display:inline-block;border:1.5px solid {A};{"border-radius:99px;" if R>=14 else ""}padding:5px 14px;font:700 12px {st["body"]};letter-spacing:.16em;text-transform:uppercase;color:{A}">{c["tag"]}</span>'
            cards+=f'''<div class="card" style="left:{x}px;top:330px;width:352px;height:700px"><div style="padding:24px 28px 0">{tag}<div class="hd" style="font-size:27px;line-height:1.18;margin-top:16px;text-transform:none">{c['title']}<br>{c['title2']}</div><div style="font:700 12px {st["body"]};letter-spacing:.2em;text-transform:uppercase;color:{M};margin-top:20px">Est. monthly payment</div><div class="hd" style="font-size:60px;line-height:1.1;text-transform:none">{usd(c['mo'])}<span style="font:500 22px {st["body"]};color:{M}">/mo</span></div><div style="margin-top:8px">{mrows}</div><div style="font:700 12px {st["body"]};letter-spacing:.2em;text-transform:uppercase;color:{M};margin:16px 0 0">Up-front costs</div><div style="margin-top:2px">{rows}</div></div><div style="position:absolute;left:0;right:0;bottom:0;height:128px;background:{T};border-top:3px solid {A};padding:22px 28px"><div style="font:700 12px {st["body"]};letter-spacing:.2em;text-transform:uppercase;color:{M}">Est. cash to close</div><div class="hd" style="font-size:52px;text-transform:none">{usd(c['cash'])}</div></div></div>'''
        dl=''.join(f'<div style="flex:1;display:flex;align-items:center;gap:18px"><span class="hd" style="font-size:44px;color:{A};white-space:nowrap;text-transform:none">{a}</span><span style="font:500 18px/1.4 {st["body"]}">{b}</span></div>' for a,b in DELTAS)
        body=frame()+head(f"Sample figures · {S['full']}",'The','Numbers',small=True) if st['hero']!='band' else frame()+P(840,56,314,200)+titleblock(f"Sample figures · {S['full']}",'The Numbers','',70,74,740,size=st['tsize']-8)
        body+=f'<div class="abs" style="left:70px;top:262px;width:700px;font:600 19px {st["body"]};color:{M}">{usd(S["price"])} · {S["beds"]} BD · {S["baths"]} BA · {S["sqft"]} SF</div>'
        body+=cards
        body+=f'<div class="abs" style="left:70px;top:1050px;width:1084px;display:flex;gap:36px;padding:16px 0;border-top:1.5px solid {L};border-bottom:1.5px solid {L}">{dl}</div>'
        body+=f'<div class="abs" style="left:70px;top:1160px;width:1084px;font:400 13px/1.55 {st["body"]};color:{M}">{DISC}</div>'
        body+=f'<div class="abs" style="left:70px;top:1300px;width:1084px;display:flex;justify-content:space-between"><div style="border-left:4px solid {A};padding-left:18px"><div class="hd" style="font-size:28px;text-transform:none">{S["agent"]}</div><div style="font:400 17px/1.55 {st["body"]};color:{M}">{S["agent_t"]} · {S["brokerage"]}<br><b style="color:{I}">{S["aphone"]}</b><br>{S["aemail"]}</div></div><div style="display:flex;gap:20px;align-items:center;border-left:4px solid {A};padding-left:18px"><img src="{HS}" style="width:112px;height:112px;border-radius:50%;object-fit:cover;border:2px solid {A}"><div><div class="hd" style="font-size:28px;text-transform:none">{LO["name"]}</div><div style="font:400 17px/1.55 {st["body"]};color:{M}">{LO["t"]}<br><b style="color:{I}">{LO["phone"]}</b><br>{LO["email"]}</div></div></div></div>'
        body+=f'<div class="abs" style="left:70px;right:70px;bottom:44px;border-top:2px solid {A};padding-top:18px;text-align:center;font:500 19px {st["body"]}">Need estimates on another home? Call or text Devin <b style="color:{A}">{LO["phone"]}</b> · {LO["web"]}</div>'
        return page(fontcss(st['fonts']),css,body)
    # ---------- MOVE ----------
    def move():
        ics=['bolt','flame','drop','wifi','home']
        su=''.join(f'<div style="display:flex;align-items:center;gap:20px;padding:14px 0;border-top:1px solid {L}"><div class="hd" style="width:48px;height:48px;border-radius:{"50%" if R!=0 or st["sec"]!="under" else "0"};border:1.5px solid {A};color:{A};display:grid;place-items:center;font-size:22px;flex:none;text-transform:none">{i+1}</div><div style="flex:1"><div style="font:700 21px {st["body"]}">{a}</div><div style="font:400 15px {st["body"]};color:{M}">{b} · {c}</div></div><div class="hd" style="font-size:20px;color:{A};text-transform:none;text-align:right">{d}</div></div>' for i,(a,b,c,d) in enumerate(MOVE['setup']))
        mo=''
        for i,(a,b,lo,hi) in enumerate(MOVE['monthly']):
            val=f'${lo}–${hi}' if lo else MOVE['hoa']
            bar=f'<div style="height:6px;background:{T};margin-top:8px;position:relative;border-radius:{min(R,6)}px"><div style="position:absolute;left:{lo/4}%;width:{(hi-lo)/4}%;top:0;bottom:0;background:{A};border-radius:{min(R,6)}px"></div></div>' if lo else ''
            mo+=f'<div style="display:flex;align-items:center;gap:18px;padding:12px 0;border-top:1px solid {L}"><div style="width:46px;height:46px;border-radius:{"50%" if R!=0 else "0"};border:1.5px solid {A};display:grid;place-items:center;flex:none">{icon(ics[i],24,A,1.6)}</div><div style="flex:1"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font:700 20px {st["body"]}">{a}</span><span class="hd" style="font-size:25px;text-transform:none">{val}</span></div><div style="font:400 14.5px {st["body"]};color:{M}">{b}</div>{bar}</div></div>'
        body=frame()+head(f"Your first week at {S['street']}",'Move-In','Costs',small=True) if st['hero']!='band' else frame()+P(840,56,314,200)+titleblock(f"Your first week at {S['street']}",'Move-In Costs','',70,74,740,size=st['tsize']-8)
        body+=f'<div class="abs" style="left:70px;top:290px;width:1084px;font:italic 400 23px/1.5 {st["body"]}">{MOVE["intro"]}</div>'
        body+=f'<div class="abs" style="left:70px;top:390px;width:1084px"><div class="ey" style="margin-bottom:10px">Set up before you arrive</div>{su}</div>'
        body+=f'<div class="abs" style="left:70px;top:820px;width:1084px"><div class="ey" style="margin-bottom:10px">Typical monthly costs</div>{mo}</div>'
        body+=f'<div class="abs" style="left:70px;top:1388px;width:1084px;font:400 12.5px/1.5 {st["body"]};color:{M}">{MOVE["fine"]}</div>'+foot().replace('bottom:44px','bottom:30px')
        return page(fontcss(st['fonts']),css,body)
    return {'home':home(),'neigh':neigh(),'num':numbers(),'move':move()}
if __name__=='__main__':
    import sys,os
    for n in sys.argv[1:]:
        os.makedirs(f'out/{n}',exist_ok=True)
        render([(f'/home/claude/work/styles/out/{n}/{k}.jpg',h) for k,h in build(n).items()]); print('ok',n)

import re as _re
def postproc(name,html,page='home'):
    K=STY[name]['mark']; TH=22 if page=='num' else 28
    hl=f'background:linear-gradient(transparent 50%,{K} 50%);box-shadow:-4px 0 0 {K},4px 0 0 {K};'
    ms=[]
    pat=_re.compile(r'(<(?:div|span|b)[^>]*?font(?:-size)?:[^">;]*?(\d+(?:\.\d+)?)px[^>]*>)(\$[\d,]+(?:[–-]\$[\d,]+)?(?:/mo)?)(<|$)')
    allm=[m for m in pat.finditer(html) if float(m.group(2))>=TH]
    if page=='move': allm=allm[-1:]
    keep={m.start() for m in allm}
    def f(m):
        if m.start() not in keep: return m.group(0)
        return m.group(1)+'<span style="'+hl+'">'+m.group(3)+'</span>'+m.group(4)
    return pat.sub(f,html)
