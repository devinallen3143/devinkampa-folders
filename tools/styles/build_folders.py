import re,sys,io,base64,os,importlib
from PIL import Image
from common import fontcss
SRC=open('/home/claude/devinkampa-folders/1460-latigo-ct/index.html').read()

def leaf(x,y,s,rot,c,o=1):
    return f'<svg style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({s});opacity:{o}" width="120" height="220" viewBox="0 0 120 220"><path d="M60 215V20" stroke="{c}" stroke-width="3" fill="none"/>'+''.join(f'<path d="M60 {40+i*34}C{20 if i%2 else 100} {20+i*34} {18 if i%2 else 102} {50+i*34} 60 {58+i*34}Z" fill="{c}"/>' for i in range(5))+f'<path d="M60 20C45 5 75 5 60 20Z" fill="{c}"/></svg>'

SHARP_DEFAULT='<path class="s1" d="M5 25 C80 14 215 13 295 21" stroke-width="11"/>'
T={}
# ---------------- HEIRLOOM ----------------
T['heirloom']=dict(
 title='Heirloom', mod='t1_heirloom',
 fonts=[('Playfair Display','playfair-display',w,'normal') for w in (400,500,600,700)]+[('Playfair Display','playfair-display',400,'italic'),('Jost','jost',400,'normal'),('Jost','jost',500,'normal'),('Jost','jost',600,'normal')],
 head="'Playfair Display',Georgia,serif", body="Jost,system-ui,sans-serif", script="'Playfair Display',Georgia,serif",
 sharp='<path class="s1" d="M8 22 C90 16 210 16 292 22" stroke-width="3.5"/><path class="s1" d="M8 31 C90 26 210 26 292 31" stroke-width="1.6"/>',
 css="""
:root{--bg1:#f8f3ea;--bg2:#f3ecdd;--bg3:#ebe1ca;--haze:rgba(248,243,234,.94);--ink:#141c2b;--ink2:#5d6574;--pill:rgba(255,252,245,.86);--pillb:rgba(184,145,90,.5);--accent:#141c2b;--accent-ink:#d9bc87;--sh:rgba(20,28,43,.38)}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#1d2638 0%,#141c2b 55%,#0e1420 100%)}
.cf{background:linear-gradient(155deg,#1f293d 0%,#141c2b 50%,#0c121d 100%);border-radius:4px 14px 14px 4px}
.pocket{background:linear-gradient(180deg,#222d44 0%,#18202f 45%,#101725 100%)}
.stitch{border:2px dashed #c9a56a;border-radius:6px 14px 14px 6px;filter:drop-shadow(0 0 2px rgba(217,188,135,.45));box-shadow:0 0 0 1px rgba(0,0,0,.5)}
.pocket i{border-color:#c9a56a}
.cf .spine{background:linear-gradient(90deg,rgba(0,0,0,.4),#b8915a 40%,#8c6a3a 55%,rgba(0,0,0,.35));width:16px}
.cf .addr{padding:0 46px}
.cf .addr b{font-family:'Playfair Display',serif;font-weight:600;font-size:54px;letter-spacing:.01em;color:#f3e6c8;line-height:1.08}
.cf .addr span{font-family:Jost,sans-serif;color:#d9bc87;letter-spacing:.38em;font-size:12px}
.cf .agname{font-family:Jost,sans-serif;color:rgba(217,188,135,.8);letter-spacing:.34em}
.cf .orn{position:absolute;inset:44px 44px 44px 50px;border:1.5px solid rgba(217,188,135,.75);pointer-events:none}
.cf .orn::after{content:"";position:absolute;inset:6px;border:1px solid rgba(217,188,135,.4)}
.cf .eyb{position:absolute;left:0;right:0;top:215px;text-align:center;font:500 12px Jost;letter-spacing:.5em;color:#d9bc87;padding-left:.5em}
.cf .gl{position:absolute;left:230px;width:140px;height:1.5px;background:linear-gradient(90deg,transparent,#d9bc87,transparent)}
#fullB,#tourB,.btn.primary{background:linear-gradient(135deg,#e3c88f 0%,#b8915a 100%)!important;color:#141c2b!important;border-color:transparent!important}
#cap h1{font-weight:500;letter-spacing:-.01em}#cap h1 .sharpie{color:#b8915a}
#cap h1 .script{font-style:italic;font-weight:400;font-size:1.3em}
.btn{border-radius:2px;letter-spacing:.06em;text-transform:uppercase;font-size:13px}
#toast{background:#141c2b;color:#d9bc87}#nudge{background:#fffaf0}
.bc.ag{background:linear-gradient(135deg,#1d2638,#0e1420);color:#f3e6c8;box-shadow:inset 0 0 0 1px rgba(217,188,135,.55)}
.bc.ag .bl2{color:#d9bc87}.bc.ag .bn{color:#fff;font-family:'Playfair Display',serif}.bc.ag .br,.bc.ag .bm{color:#cfc6b0}.bc.ag .bp{color:#fff}.bc.ag .bp b{color:#d9bc87}
.bc.ag .bph{background:#27324a;box-shadow:0 0 0 2px rgba(217,188,135,.6)}.bc.ag .bs{background:linear-gradient(180deg,#e3c88f,#8c6a3a)}
""",
 cover='<div class="orn"></div><div class="eyb">OPEN HOUSE</div><div class="gl" style="top:250px"></div><div class="gl" style="top:566px"></div>'
       '<div class="addr"><b>123 Sample<br>Street</b><span>Anytown, Texas</span></div><div class="agname">Your Name Here</div>')
# ---------------- METROPOLITAN ----------------
T['metropolitan']=dict(
 title='Metropolitan', mod='t2_metropolitan',
 fonts=[('Oswald','oswald',w,'normal') for w in (400,500,600,700)]+[('Allura','allura',400,'normal'),('Lato','lato',400,'normal'),('Lato','lato',700,'normal')],
 head="Oswald,sans-serif", body="Lato,system-ui,sans-serif", script="Allura,cursive",
 sharp='<path class="s1" d="M4 24 L296 14" stroke-width="7"/>',
 css="""
:root{--bg1:#f3eee4;--bg2:#ece5d6;--bg3:#e2dac6;--haze:rgba(243,238,228,.94);--ink:#12233a;--ink2:#5e6a7b;--pill:rgba(255,255,255,.88);--pillb:rgba(201,162,77,.55);--accent:#12233a;--accent-ink:#c9a24d;--sh:rgba(18,35,58,.4)}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#1b3250 0%,#12233a 60%,#0b172a 100%)}
.cf{background:#12233a;border-radius:0;overflow:hidden}
.cf::after{background:none}
.pocket{background:linear-gradient(180deg,#1b3250 0%,#12233a 100%);border-radius:0!important}
.stitch{border:5px double #c9a24d;border-radius:0!important;filter:none;box-shadow:none;inset:16px}
.pocket i{border:5px double #c9a24d;border-top:0;border-radius:0}
.cf .spine{background:#c9a24d;width:12px;border-radius:0}
.cf .cut{position:absolute;left:0;right:0;bottom:0;height:300px;background:#c9a24d;clip-path:polygon(0 62%,100% 0,100% 100%,0 100%)}
.cf .cut2{position:absolute;left:0;right:0;bottom:0;height:300px;background:#f3eee4;clip-path:polygon(0 86%,100% 40%,100% 100%,0 100%)}
.cf .addr{top:150px;bottom:auto;display:block;padding:0 50px;text-align:left}
.cf .addr b{font-family:Oswald,sans-serif;font-weight:700;font-size:64px;line-height:.98;text-transform:uppercase;color:#fff;letter-spacing:.01em}
.cf .addr span{font-family:Lato,sans-serif;font-weight:700;font-size:13px;letter-spacing:.34em;color:#c9a24d;margin-top:20px;padding-left:0}
.cf .sc{position:absolute;left:46px;top:58px;font:400 84px Allura;color:#c9a24d;transform:rotate(-4deg)}
.cf .agname{left:50px;right:auto;text-align:left;bottom:34px;color:#12233a;font:700 12px Lato;letter-spacing:.3em;padding-left:0;z-index:2}
#cap h1{font-weight:600;text-transform:uppercase;letter-spacing:.02em}
#cap h1 .script{text-transform:none;font-size:1.7em;color:#c9a24d;font-weight:400}
#cap h1 .sharpie{color:#c9a24d}
.btn{border-radius:0;clip-path:polygon(10px 0,100% 0,calc(100% - 10px) 100%,0 100%);padding:0 26px;text-transform:uppercase;letter-spacing:.12em;font-size:13px;font-weight:700;border:0}
.btn.primary,#tourB,#fullB{background:#c9a24d!important;color:#12233a!important}
#toast{background:#12233a;color:#c9a24d;border-radius:0}#nudge{background:#fff;border-radius:0;border-top:5px solid #c9a24d}
#nudge a.go{border-radius:0;background:#12233a;color:#c9a24d}
.bc.ag{background:#12233a;color:#fff;box-shadow:inset 0 0 0 1px #c9a24d}
.bc.ag .bl2{color:#c9a24d}.bc.ag .bn{color:#fff;font-family:Oswald;text-transform:uppercase}.bc.ag .br,.bc.ag .bm{color:#cdd5e0}.bc.ag .bp{color:#fff}.bc.ag .bp b{color:#c9a24d}
.bc.ag .bph{background:#2a4366;box-shadow:0 0 0 2px #c9a24d}.bc.ag .bs{background:#c9a24d}
""",
 cover='<div class="cut"></div><div class="cut2"></div><div class="addr"><b>123 Sample<br>Street</b><span>ANYTOWN · TEXAS</span></div><div class="sc">Open House</div><div class="agname">YOUR NAME HERE</div>')
# ---------------- AZURE ----------------
T['azure']=dict(
 title='Azure', mod='t3_azure',
 fonts=[('Poppins','poppins',w,'normal') for w in (400,500,600,700,800)]+[('Inter','inter',w,'normal') for w in (400,500,600)],
 head="Poppins,sans-serif", body="Inter,system-ui,sans-serif", script="Poppins,sans-serif",
 sharp='<path class="s1" d="M4 22 L296 22" stroke-width="12" stroke-linecap="butt"/>',
 css="""
:root{--bg1:#ffffff;--bg2:#eef3fc;--bg3:#dfe8f8;--haze:rgba(238,243,252,.94);--ink:#0f1218;--ink2:#5b6170;--pill:#fff;--pillb:rgba(15,18,24,.18);--accent:#0f1218;--accent-ink:#fff;--sh:rgba(26,63,140,.38)}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#2f62c1 0%,#2756ab 60%,#1a3f8c 100%)}
.cf{background:#2f62c1;border-radius:6px 22px 22px 6px;overflow:hidden}
.cf::after{background:none}
.pocket{background:#0f1218;border-radius:0 0 22px 6px}
.cb .pocket{border-radius:0 0 6px 22px}
.stitch{border:4px dotted #fff;border-radius:6px 20px 20px 6px;filter:none;box-shadow:none}
.pocket i{border:4px dotted #8fb0ec;border-top:0}
.cf .spine{background:#0f1218;width:18px;border-radius:0}
.cf .band{position:absolute;left:-40px;right:-40px;top:420px;height:150px;background:#fff;transform:rotate(-14deg);transform-origin:center}
.cf .band2{position:absolute;left:-40px;right:-40px;top:578px;height:36px;background:#0f1218;transform:rotate(-14deg)}
.cf .addr{top:80px;bottom:auto;display:block;padding:0 46px;text-align:left}
.cf .addr b{font-family:Poppins,sans-serif;font-weight:800;font-size:60px;line-height:1;text-transform:uppercase;color:#fff;letter-spacing:-.01em}
.cf .addr span{font:600 13px Inter;letter-spacing:.3em;color:#cfe0ff;margin-top:18px;padding-left:0}
.cf .tag{position:absolute;left:44px;bottom:150px;font:800 38px Poppins;color:#0f1218;transform:rotate(-14deg);transform-origin:left;white-space:nowrap}
.cf .agname{left:44px;right:auto;text-align:left;bottom:36px;color:#fff;font:700 12px Inter;letter-spacing:.24em;padding-left:0}
#cap h1{font-weight:800;text-transform:uppercase;letter-spacing:-.01em}
#cap h1 .script{font-family:Poppins;font-weight:800;font-size:1em;color:#2f62c1;margin-right:.3em}
#cap h1 .sharpie{color:#2f62c1;bottom:-.18em;height:.34em}
.btn{border-radius:14px;font-weight:700;letter-spacing:.02em;border:2px solid #0f1218;background:#fff}
.btn.primary,#tourB{background:#0f1218!important;color:#fff!important;border-color:#0f1218!important}
#fullB{background:#2f62c1!important;color:#fff!important;border-color:#2f62c1!important}
#toast{background:#0f1218;color:#fff}#nudge{background:#fff;border:2px solid #0f1218;border-radius:18px}
#nudge a.go{background:#2f62c1;border-radius:12px}
.bc.ag{background:#0f1218;color:#fff;box-shadow:inset 0 0 0 2px #2f62c1}
.bc.ag .bl2{color:#8fb0ec}.bc.ag .bn{color:#fff;font-family:Poppins;font-weight:700}.bc.ag .br,.bc.ag .bm{color:#cdd5e6}.bc.ag .bp{color:#fff}.bc.ag .bp b{color:#8fb0ec}
.bc.ag .bph{background:#2f62c1;box-shadow:0 0 0 2px #fff}.bc.ag .bs{background:#2f62c1}
""",
 cover='<div class="band"></div><div class="band2"></div><div class="addr"><b>Open<br>House</b><span>123 SAMPLE STREET · ANYTOWN, TX</span></div><div class="tag">ASK ME HOW</div><div class="agname">YOUR NAME HERE</div>')
# ---------------- TERRA ----------------
T['terra']=dict(
 title='Terra', mod='t4_terra',
 fonts=[('Nunito','nunito',w,'normal') for w in (400,600,700,800)]+[('Quicksand','quicksand',w,'normal') for w in (500,600,700)],
 head="Quicksand,sans-serif", body="Nunito,system-ui,sans-serif", script="Quicksand,sans-serif",
 sharp='<path class="s1" d="M6 24 C90 14 210 34 294 20" stroke-width="10"/>',
 css="""
:root{--bg1:#f6f1e7;--bg2:#efe7d8;--bg3:#e6dccb;--haze:rgba(246,241,231,.94);--ink:#3a3629;--ink2:#7a735f;--pill:rgba(255,255,255,.9);--pillb:rgba(107,116,73,.4);--accent:#6b7449;--accent-ink:#fff;--sh:rgba(78,86,52,.34)}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#c9bba3 0%,#b9a890 60%,#ab9a82 100%)}
.cf{background:linear-gradient(155deg,#c4b49a 0%,#b9a890 50%,#a99880 100%);border-radius:10px 44px 44px 10px;overflow:hidden}
.cf::after{background:linear-gradient(120deg,rgba(255,255,255,.16),rgba(255,255,255,0) 40%)}
#base .inner{border-radius:10px 44px 44px 10px}.cb .inner{border-radius:44px 10px 10px 44px}
.pocket{background:linear-gradient(180deg,#76804f 0%,#6b7449 50%,#5e673f 100%)}
#base .pocket{border-radius:0 0 44px 10px}.cb .pocket{border-radius:0 0 10px 44px}
.stitch{border:5px dotted #fff;border-radius:10px 36px 36px 10px;filter:none;box-shadow:none;inset:18px}
#base .stitch{border-radius:10px 36px 36px 10px}.cb .stitch{border-radius:36px 10px 10px 36px}
.pocket i{border:5px dotted #f2ecdc;border-top:0}
.cf .spine{background:linear-gradient(90deg,rgba(0,0,0,.18),rgba(255,255,255,.1));width:20px}
.cf .pill{position:absolute;left:0;right:0;top:232px;text-align:center}
.cf .pill i{display:inline-block;background:#6b7449;color:#fff;font:700 16px Quicksand;letter-spacing:.2em;padding:10px 26px;border-radius:99px;font-style:normal;padding-left:calc(26px + .2em)}
.cf .addr b{font-family:Quicksand,sans-serif;font-weight:700;font-size:58px;line-height:1.04;color:#4e5634;letter-spacing:-.01em}
.cf .addr span{font:700 14px Nunito;color:#fff;letter-spacing:.26em;margin-top:22px}
.cf .blob{position:absolute;border-radius:50%}
.cf .agname{font:700 13px Nunito;color:#4e5634;letter-spacing:.22em;bottom:50px}
#cap h1{font-weight:700;letter-spacing:-.015em}
#cap h1 .script{font-family:Quicksand;font-weight:700;font-size:1.05em;color:#4e5634}
#cap h1 .sharpie{color:#c97b4f}
.btn{border-radius:999px;font-weight:700;border:2px solid rgba(107,116,73,.45);background:#fff;color:#4e5634}
.btn.primary,#tourB{background:#6b7449!important;color:#fff!important;border-color:#6b7449!important}
#fullB{background:#c97b4f!important;color:#fff!important;border-color:#c97b4f!important}
#toast{background:#4e5634;color:#fff}#nudge{background:#fffaf0;border-radius:28px;border:2px solid #e6dccb}
#nudge a.go{background:#6b7449}
.bc.ag{background:#f6f1e7;color:#3a3629;box-shadow:inset 0 0 0 3px #6b7449;border-radius:28px}
.bc.ag .bl2{color:#6b7449}.bc.ag .bn{color:#4e5634;font-family:Quicksand;font-weight:700}.bc.ag .br,.bc.ag .bm{color:#7a735f}.bc.ag .bp{color:#3a3629}.bc.ag .bp b{color:#6b7449}
.bc.ag .bph{background:#e6dccb;box-shadow:0 0 0 3px #6b7449}.bc.ag .bs{background:#6b7449}
""",
 cover='<div class="blob" style="left:-60px;top:-60px;width:220px;height:220px;background:rgba(255,255,255,.14)"></div><div class="blob" style="right:-80px;bottom:-60px;width:300px;height:300px;background:rgba(107,116,73,.28)"></div>'
       '<div class="pill"><i>OPEN HOUSE</i></div><div class="addr"><b>123 Sample<br>Street</b><span>ANYTOWN, TEXAS</span></div><div class="agname">YOUR NAME HERE</div>')
# ---------------- EVERGREEN ----------------
T['evergreen']=dict(
 title='Evergreen', mod='t5_evergreen',
 fonts=[('Fraunces','fraunces',w,'normal') for w in (400,600,700)]+[('Fraunces','fraunces',400,'italic'),('Karla','karla',400,'normal'),('Karla','karla',500,'normal'),('Karla','karla',700,'normal')],
 head="Fraunces,Georgia,serif", body="Karla,system-ui,sans-serif", script="Fraunces,Georgia,serif",
 sharp='<path class="s1" d="M6 24 C70 12 120 30 190 18 S270 16 294 22" stroke-width="5"/>',
 css="""
:root{--bg1:#f7f2e8;--bg2:#f0e9da;--bg3:#e6ddc8;--haze:rgba(247,242,232,.94);--ink:#1f2a24;--ink2:#5f6b62;--pill:rgba(255,252,245,.88);--pillb:rgba(178,106,60,.5);--accent:#1f3a2e;--accent-ink:#e8c7a8;--sh:rgba(31,58,46,.4)}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#2d5240 0%,#1f3a2e 60%,#16291f 100%)}
.cf{background:linear-gradient(155deg,#2d5240 0%,#1f3a2e 52%,#15271e 100%);border-radius:4px 12px 12px 4px;overflow:hidden}
.pocket{background:linear-gradient(180deg,#2d5240 0%,#1f3a2e 50%,#17291f 100%)}
.stitch{border:2px dashed #d9a07a;border-radius:4px 12px 12px 4px;filter:drop-shadow(0 0 2px rgba(217,160,122,.4));box-shadow:0 0 0 1px rgba(0,0,0,.45)}
.pocket i{border-color:#d9a07a}
.cf .spine{background:linear-gradient(90deg,rgba(0,0,0,.4),#b26a3c 45%,#8a4f28 60%,rgba(0,0,0,.3));width:14px}
.cf .frame{position:absolute;inset:50px 46px 50px 52px;border:1.5px solid #d9a07a;pointer-events:none}
.cf .frame::before,.cf .frame::after{content:"";position:absolute;width:18px;height:18px;border:1.5px solid #d9a07a;background:#1f3a2e}
.cf .frame::before{left:-10px;top:-10px}.cf .frame::after{right:-10px;bottom:-10px}
.cf .addr{padding:0 60px}
.cf .addr b{font-family:Fraunces,serif;font-weight:600;font-size:56px;line-height:1.05;color:#f4e6d6}
.cf .addr span{font:700 12px Karla;color:#d9a07a;letter-spacing:.38em;margin-top:24px}
.cf .eyb{position:absolute;left:0;right:0;top:300px;text-align:center;font:italic 400 24px Fraunces;color:#d9a07a}
.cf .agname{font:700 11.5px Karla;color:rgba(217,160,122,.85);letter-spacing:.3em;bottom:78px}
#cap h1{font-weight:600;letter-spacing:-.01em}
#cap h1 .script{font-family:Fraunces,serif;font-style:italic;font-weight:400;font-size:1.25em}
#cap h1 .sharpie{color:#b26a3c}
.btn{border-radius:3px;font-weight:700;letter-spacing:.04em;border:1.5px solid #b26a3c;background:#fffaf0;color:#1f3a2e}
.btn.primary,#tourB{background:#1f3a2e!important;color:#f4e6d6!important;border-color:#1f3a2e!important}
#fullB{background:#b26a3c!important;color:#fff!important;border-color:#b26a3c!important}
#toast{background:#1f3a2e;color:#e8c7a8;border-radius:3px}#nudge{background:#fffaf0;border-radius:4px;border:1.5px solid #b26a3c}
#nudge a.go{background:#1f3a2e;border-radius:3px;color:#f4e6d6}
.bc.ag{background:#1f3a2e;color:#f4e6d6;box-shadow:inset 0 0 0 1.5px #d9a07a}
.bc.ag .bl2{color:#d9a07a}.bc.ag .bn{color:#fff;font-family:Fraunces;font-weight:600}.bc.ag .br,.bc.ag .bm{color:#cfd9cf}.bc.ag .bp{color:#fff}.bc.ag .bp b{color:#d9a07a}
.bc.ag .bph{background:#2d5240;box-shadow:0 0 0 2px #d9a07a}.bc.ag .bs{background:#b26a3c}
""",
 cover=None)
T['evergreen']['cover']='<div class="frame"></div>'+leaf(430,40,.8,14,'#b26a3c',.9)+leaf(30,600,.7,-160,'#b26a3c',.85)+'<div class="eyb">Open House</div><div class="addr"><b>123 Sample<br>Street</b><span>ANYTOWN · TEXAS</span></div><div class="agname">YOUR NAME HERE</div>'


import copy
from palettes import PAL
def mix(a,b,t):
    a=[int(a[i:i+2],16) for i in (1,3,5)]; b=[int(b[i:i+2],16) for i in (1,3,5)]
    return '#%02x%02x%02x'%tuple(round(a[i]+(b[i]-a[i])*t) for i in range(3))
def themed(p):
    t=copy.deepcopy(T['heirloom']); dk=p['NAVY']; g=p['GOLD']; cr=p['CREAM']
    M={'#141c2b':dk,'#1d2638':mix(dk,'#ffffff',.07),'#0e1420':mix(dk,'#000000',.3),'#222d44':mix(dk,'#ffffff',.12),'#18202f':mix(dk,'#ffffff',.03),'#101725':mix(dk,'#000000',.2),'#27324a':mix(dk,'#ffffff',.14),'#1f293d':mix(dk,'#ffffff',.06),'#0c121d':mix(dk,'#000000',.4),
       '#c9a56a':g,'#d9bc87':mix(g,'#ffffff',.3),'#b8915a':g,'#8c6a3a':mix(g,'#000000',.35),'#e3c88f':mix(g,'#ffffff',.38),'#f3e6c8':mix(cr,'#ffffff',.5),
       '#f8f3ea':cr,'#f3ecdd':mix(cr,'#000000',.03),'#ebe1ca':p['SAND'],'#5d6574':p['MUTE'],'#fffaf0':mix(cr,'#ffffff',.6),'#fffcf5':mix(cr,'#ffffff',.6),'#cfc6b0':mix(cr,dk,.25)}
    def conv(x):
        for k,v in M.items(): x=x.replace(k,v)
        x=x.replace('rgba(184,145,90,','rgba(%d,%d,%d,'%tuple(int(g[i:i+2],16) for i in (1,3,5))).replace('rgba(217,188,135,','rgba(%d,%d,%d,'%tuple(int(mix(g,'#ffffff',.3)[i:i+2],16) for i in (1,3,5))).replace('rgba(20,28,43,','rgba(%d,%d,%d,'%tuple(int(dk[i:i+2],16) for i in (1,3,5)))
        return x
    t['css']=conv(t['css']); t['cover']=conv(t['cover']); t['sharp']=t['sharp']; t['title']=p['NAME']
    return t
for k,p in PAL.items(): T[k]=themed(p)


# ---- restrained covers (Heirloom-level polish) ----
T['metropolitan']['css']+="""
.cf .cut,.cf .cut2,.cf .sc{display:none}
.cf .cor{position:absolute;right:0;bottom:0;width:0;height:0;border-style:solid;border-width:0 0 150px 150px;border-color:transparent transparent #c9a24d transparent}
.cf .rl{position:absolute;left:50px;width:70px;height:3px;background:#c9a24d}
.cf .addr{top:200px}
.cf .addr b{font-size:60px}
.cf .eyb2{position:absolute;left:50px;top:130px;font:700 13px Lato;letter-spacing:.4em;color:#c9a24d}
.stitch{border:2px solid #c9a24d!important;inset:18px}
.pocket i{border:2px solid #c9a24d!important;border-top:0!important}
"""
T['metropolitan']['cover']='<div class="cor"></div><div class="eyb2">OPEN HOUSE</div><div class="rl" style="top:166px"></div><div class="addr"><b>123 Sample<br>Street</b><span>ANYTOWN · TEXAS</span></div><div class="agname" style="color:#c9a24d">YOUR NAME HERE</div>'
T['azure']['css']+="""
.cf .band,.cf .band2,.cf .tag{display:none}
.cf .addr{top:auto;bottom:150px;display:block}
.cf .addr b{font-size:56px;text-transform:uppercase}
.cf .bar{position:absolute;left:0;right:0;bottom:0;height:96px;background:#0f1218}
.cf .eyb3{position:absolute;left:46px;top:70px;font:700 13px Inter;letter-spacing:.34em;color:#cfe0ff}
.cf .rl{position:absolute;left:46px;top:104px;width:70px;height:5px;background:#fff}
.cf .agname{bottom:36px;z-index:2}
"""
T['azure']['cover']='<div class="eyb3">OPEN HOUSE</div><div class="rl"></div><div class="addr"><b>123 Sample<br>Street</b><span>ANYTOWN, TEXAS</span></div><div class="bar"></div><div class="agname">YOUR NAME HERE</div>'
T['terra']['css']+=".cf .blob{display:none}.cf .pill{top:250px}.cf .addr b{font-size:56px}\n"
T['terra']['cover']='<div class="pill"><i>OPEN HOUSE</i></div><div class="addr"><b>123 Sample<br>Street</b><span>ANYTOWN, TEXAS</span></div><div class="agname">YOUR NAME HERE</div>'
T['evergreen']['css']+="""
.cf .frame{display:none}.cf .vr{position:absolute;left:52px;top:60px;bottom:60px;width:2px;background:#d9a07a}
.cf .addr{top:auto;bottom:130px;display:block;text-align:left;padding:0 50px 0 78px}.cf .addr b{font-size:52px}.cf .eyb{text-align:left;left:78px;top:92px;font-size:22px}.cf .agname{text-align:left;left:78px;right:auto;bottom:62px;padding-left:0}
"""
T['evergreen']['cover']='<div class="vr"></div><div class="eyb">Open House</div><div class="addr"><b>123 Sample<br>Street</b><span>ANYTOWN · TEXAS</span></div><div class="agname">YOUR NAME HERE</div>'

# ---- palette revision (Metropolitan: yellow/black stitch, Azure: greys, Evergreen: forest/bronze) ----
def rep(t,M):
    for k in ('css','cover'):
        for a,b in M.items(): t[k]=t[k].replace(a,b)
Y='#ffe81a'
rep(T['metropolitan'],{'#c9a24d':Y,'rgba(201,162,77,.55)':'rgba(255,232,26,.8)','color:'+Y+'"':'color:#12233a"'})
T['metropolitan']['css']+="""
.cf{background:linear-gradient(155deg,#efe8d8 0%,#e6dcc7 55%,#dbd0b6 100%)}
.cf .spine{background:#12233a}
.pocket{background:linear-gradient(180deg,#efe8d8 0%,#e3d9c3 100%)}
.stitch{border:3px double #090b0f!important}
.pocket i{border:3px double #090b0f!important;border-top:0!important}
.cf .rl{background:#12233a}
.cf .addr b{color:#12233a}.cf .addr span{color:#12233a}
.cf .eyb2{color:#12233a;background:#ffe81a;padding:6px 12px;left:38px}
.cf .agname{color:#12233a!important}
#cap h1 .script{color:#12233a}#cap h1 .sharpie{color:#ffe81a}
.btn{border:0}
.btn.primary,#tourB,#fullB{background:#ffe81a!important;color:#12233a!important}
#toast{background:#12233a;color:#ffe81a}
"""
rep(T['azure'],{'#2f62c1':'#5d636b','#2756ab':'#535960','#1a3f8c':'#43484f','#cfe0ff':'#e1e3e6','#8fb0ec':'#b9bdc3','#eef3fc':'#f1f2f3','#dfe8f8':'#e3e5e8','rgba(238,243,252,.94)':'rgba(241,242,243,.94)','rgba(26,63,140,.38)':'rgba(20,22,26,.38)','#cdd5e6':'#cfd2d7','#cdd5e6':'#cfd2d7'})
T['azure']['css']+="\n#cap h1 .script,#cap h1 .sharpie{color:#5d636b}\n"
T['azure']['css']+="""
:root{--bg1:#0a0a0b;--bg2:#000;--bg3:#000;--haze:rgba(8,9,11,.94);--ink:#f4f4f5;--ink2:#a9adb4;--pill:rgba(255,255,255,.09);--pillb:rgba(255,255,255,.28);--accent:#fff;--accent-ink:#0f1218;--sh:rgba(0,0,0,.75)}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#e9eaec 0%,#dcdee1 60%,#d0d2d6 100%)}
.cf{background:linear-gradient(155deg,#ffffff 0%,#f6f6f7 55%,#ececee 100%)}
.pocket{background:linear-gradient(180deg,#ffffff 0%,#f3f3f4 100%)}
.stitch{border:4px dotted #111!important}
.pocket i{border:4px dotted #111!important;border-top:0!important}
.cf .addr b{color:#0f1218}.cf .addr span{color:#6b7078}
.cf .eyb3{color:#6b7078}.cf .rl{background:#0f1218}
.btn{border:2px solid rgba(255,255,255,.4);background:rgba(255,255,255,.08);color:#f4f4f5}
.btn.primary,#tourB{background:#fff!important;color:#0f1218!important;border-color:#fff!important}
#fullB{background:#d5d7db!important;color:#0f1218!important;border-color:#d5d7db!important}
#cap h1 .script,#cap h1 .sharpie{color:#fff}
#toast{background:#fff;color:#0f1218}
#nudge{background:#17181c;border:2px solid rgba(255,255,255,.35);color:#f4f4f5}
#nudge a.go{background:#fff;color:#0f1218}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#c4c7cc 0%,#b4b8be 60%,#a6aab1 100%)}
.cf{box-shadow:0 0 0 2px rgba(255,255,255,.85),0 0 70px rgba(255,255,255,.16)}
.floor{box-shadow:0 0 0 2px rgba(255,255,255,.7),0 0 80px rgba(255,255,255,.16)}
.noise{opacity:.12}
.pocket{box-shadow:inset 0 1px 0 #fff,0 -1px 0 rgba(0,0,0,.25)}
"""
rep(T['evergreen'],{'#1f3a2e':'#183024','#2d5240':'#234434','#16291f':'#0f2018','#15271e':'#0e1d15','#17291f':'#0f2119','#b26a3c':'#a8793a','#d9a07a':'#cfa66b','#8a4f28':'#7a5624','#e8c7a8':'#e3c999','#f4e6d6':'#f1e7d3','rgba(217,160,122,':'rgba(207,166,107,','rgba(178,106,60,':'rgba(168,121,58,','rgba(31,58,46,':'rgba(15,32,24,','#1f2a24':'#14281e'})

# ---- soften pass (Apple-like): light type, mixed case, soft shadows, thin stitching, gentle buttons ----
SOFT_COMMON="""
#cap h1{text-transform:none!important;letter-spacing:-.018em}
#cap h1 .script{text-transform:none!important}
.btn{text-transform:none!important;letter-spacing:0!important;font-size:15px;font-weight:500;box-shadow:0 1px 2px rgba(0,0,0,.10),0 4px 14px rgba(0,0,0,.06)}
.btn.primary,#tourB,#fullB{font-weight:600}
#toast,#nudge{box-shadow:0 8px 30px rgba(0,0,0,.14)}
"""
T['metropolitan']['css']+=SOFT_COMMON+"""
#cap h1{font-weight:400!important}
.btn{clip-path:none!important;border-radius:9px!important;padding:0 22px!important;border:1px solid rgba(18,35,58,.16)!important}
.btn.primary,#tourB{background:linear-gradient(180deg,#fff25a,#ffe81a)!important;border-color:rgba(0,0,0,.08)!important}
#fullB{background:linear-gradient(180deg,#fff25a,#ffe81a)!important;border-color:rgba(0,0,0,.08)!important}
#nudge{border-radius:16px!important;border-top:0!important;border:1px solid rgba(18,35,58,.08)!important}
#nudge a.go{border-radius:9px!important}#toast{border-radius:12px!important}
.stitch{border:1.5px dashed #090b0f!important}
.pocket i{border:1.5px dashed #090b0f!important;border-top:0!important}
.cf{border-radius:4px 10px 10px 4px!important}
.cf .addr b{font-weight:500;text-transform:none;font-size:62px}
.cf .eyb2{font-weight:600;letter-spacing:.26em;border-radius:3px}
.bc.ag{box-shadow:inset 0 0 0 1px rgba(255,232,26,.55)}
"""
T['azure']['css']+=SOFT_COMMON+"""
#cap h1{font-weight:500!important;font-size:clamp(22px,3.1vw,34px)}
.btn{border-radius:12px!important;border:1px solid rgba(255,255,255,.28)!important}
.btn.primary,#tourB{background:linear-gradient(180deg,#ffffff,#e9eaec)!important}
#fullB{background:linear-gradient(180deg,#e6e8eb,#cfd2d6)!important}
#nudge{border-radius:18px!important;border:1px solid rgba(255,255,255,.18)!important}
#nudge a.go{border-radius:10px!important}#toast{border-radius:12px!important}
.stitch{border:2.5px dotted #111!important}
.pocket i{border:2.5px dotted #111!important;border-top:0!important}
.cf{box-shadow:0 0 0 1px rgba(255,255,255,.5),0 0 60px rgba(255,255,255,.10)!important}
.floor{box-shadow:0 0 0 1px rgba(255,255,255,.4),0 0 70px rgba(255,255,255,.10)!important}
.noise{opacity:.25}
.cf .addr b{font-weight:600;text-transform:none;font-size:58px;letter-spacing:-.02em}
"""
T['azure']['css']+="""
:root{--bg1:#ffffff;--bg2:#f5f5f6;--bg3:#ececee;--haze:rgba(255,255,255,.94);--ink:#0f1218;--ink2:#6b7078;--pill:#ffffff;--pillb:#d6d8dc;--accent:#3a3d43;--accent-ink:#ffffff;--sh:rgba(20,22,26,.35)}
.cf{background:linear-gradient(155deg,#4b4f56 0%,#3b3e44 55%,#2d3034 100%)!important;box-shadow:0 18px 40px rgba(20,22,26,.28),0 2px 6px rgba(20,22,26,.18)!important}
.floor{box-shadow:0 18px 40px rgba(20,22,26,.25),0 2px 6px rgba(20,22,26,.15)!important}
.cf .spine{background:#14161a}
.cf .addr b{color:#ffffff}.cf .addr span{color:#c9ccd1}.cf .eyb3{color:#c9ccd1}.cf .rl{background:#ffffff}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#464a51 0%,#3a3d43 60%,#2f3236 100%)}
.pocket{background:linear-gradient(180deg,#4a4e55 0%,#3c3f45 100%)!important}
.stitch{border:2.5px dotted #e9eaec!important}
.pocket i{border:2.5px dotted #e9eaec!important;border-top:0!important}
.noise{opacity:.3}
.btn{background:#ffffff!important;color:#0f1218!important;border:1px solid #d6d8dc!important}
.btn.primary,#tourB{background:linear-gradient(180deg,#4d5157,#34373c)!important;color:#fff!important;border-color:transparent!important}
#fullB{background:linear-gradient(180deg,#f1f2f3,#e1e3e6)!important;color:#0f1218!important;border-color:#d6d8dc!important}
#cap h1 .script,#cap h1 .sharpie{color:#3a3d43}
#toast{background:#2f3236;color:#fff}
#nudge{background:#ffffff;border:1px solid #e1e3e6!important;color:#0f1218}
#nudge a.go{background:#2f3236;color:#fff}
"""
T['terra']['css']+=SOFT_COMMON+"""
#cap h1{font-weight:500!important}
.btn{border:1px solid rgba(107,116,73,.35)!important;font-weight:600}
#nudge{border:1px solid rgba(107,116,73,.2)!important}
.stitch{border:3px dotted #fff!important}.pocket i{border:3px dotted #f2ecdc!important;border-top:0!important}
.cf .addr b{font-weight:600}
"""
T['evergreen']['css']+=SOFT_COMMON+"""
#cap h1{font-weight:400!important}
.btn{border-radius:9px!important;border:1px solid rgba(168,121,58,.55)!important}
.btn.primary,#tourB{background:linear-gradient(180deg,#24442f,#183024)!important}
#fullB{background:linear-gradient(180deg,#b88a47,#a8793a)!important}
#nudge{border-radius:16px!important;border:1px solid rgba(168,121,58,.3)!important}
#nudge a.go{border-radius:9px!important}#toast{border-radius:12px!important}
.stitch{border:1.5px dashed #cfa66b!important}
.cf{border-radius:4px 14px 14px 4px!important}
.cf .addr b{font-weight:500}
"""

# ---- palette round 3: Metropolitan = oxblood & ivory (rose-brass), Terra = cognac & espresso ----
rep(T['metropolitan'],{'#ffe81a':'#c9a08f','#fff25a':'#d8b3a3','rgba(255,232,26,':'rgba(201,160,143,','#12233a':'#3a1219','rgba(18,35,58,':'rgba(58,18,25,','#1b3250':'#4a1a24','#0b172a':'#24090e','#2a4366':'#5a2230','#cdd5e0':'#e6d5cf','#5e6a7b':'#7a5f62','#090b0f':'#d9b8a8'})
T['metropolitan']['css']+="""
.cf{background:linear-gradient(155deg,#732636 0%,#5e1c2a 55%,#4a1520 100%)!important}
.cf .spine{background:#2b0a11}
.cf .cor{border-color:transparent transparent #c9a08f transparent}
.cf .rl{background:#efe4d6}
.cf .addr b{color:#f6eee3}.cf .addr span{color:#e2cbbd}
.cf .eyb2{background:#c9a08f;color:#3a1219}
.cf .agname{color:#efe4d6!important}
.cf .eyb3{color:#e2cbbd}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#43151f 0%,#35101a 60%,#2a0c14 100%)}
.pocket{background:linear-gradient(180deg,#7a2a3a 0%,#611e2c 100%)!important}
.stitch{border:1.5px dashed #e0bfae!important}
.pocket i{border:1.5px dashed #e0bfae!important;border-top:0!important}
.btn{background:#fff!important;color:#3a1219!important;border:1px solid rgba(58,18,25,.18)!important}
.btn.primary,#tourB{background:linear-gradient(180deg,#7d2b3c,#5a1b28)!important;color:#f6eee3!important;border-color:transparent!important}
#fullB{background:linear-gradient(180deg,#dcb9aa,#c9a08f)!important;color:#3a1219!important;border-color:transparent!important}
#cap h1 .script{color:#3a1219}#cap h1 .sharpie{color:#c9a08f}
#toast{background:#3a1219;color:#efe4d6}
#nudge a.go{background:#5a1b28;color:#f6eee3}
.bc.ag{box-shadow:inset 0 0 0 1px rgba(201,160,143,.7)}
"""
rep(T['terra'],{'#6b7449':'#9a5b30','#4e5634':'#7a4524','#76804f':'#a8693a','#5e673f':'#6b3c1f','rgba(107,116,73,':'rgba(154,91,48,','rgba(78,86,52,':'rgba(122,69,36,','#c9bba3':'#a8693a','#ab9a82':'#8f5429','#c4b49a':'#a5663a','#a99880':'#8a5129','#b9a890':'#9d6034','#3a3629':'#2e1d14','#7a735f':'#7c6a5c','#c97b4f':'#d19a62'})
T['terra']['css']+="""
.cf{background:linear-gradient(155deg,#b2733f 0%,#9a5b30 55%,#82491f 100%)!important}
.cf .pill{background:#2e1d14!important;color:#f2e6d3!important}
.cf .addr b,.cf .addr span{color:#f8efe2!important}
.cf .agname{color:#f2e0c6!important}
.paperbg,.inner,.cb .inner{background:linear-gradient(165deg,#4a2f20 0%,#3b2418 60%,#2e1c12 100%)}
.pocket{background:linear-gradient(180deg,#5a3a28 0%,#46291b 100%)!important}
.stitch{border:3px dotted #e8cfae!important}
.pocket i{border:3px dotted #e8cfae!important;border-top:0!important}
.btn{background:#fff!important;color:#2e1d14!important;border:1px solid rgba(154,91,48,.35)!important}
.btn.primary,#tourB{background:linear-gradient(180deg,#ad6d3c,#8a4d26)!important;color:#fff7ea!important;border-color:transparent!important}
#fullB{background:linear-gradient(180deg,#f2dcc0,#e3c299)!important;color:#2e1d14!important;border-color:transparent!important}
#cap h1 .script{color:#8a4d26}#cap h1 .sharpie{color:#d19a62}
#toast{background:#2e1d14;color:#f2e6d3}
#nudge a.go{background:#8a4d26;color:#fff7ea}
"""

T['terra']['css']+="""
.cf{background:linear-gradient(155deg,#553726 0%,#46291b 55%,#34200f 100%)!important}
.cf .pill{background:#9a5b30!important}
.cf .pill i{background:#2a1a10!important;color:#f2e6d3!important}
.cf .spine{background:linear-gradient(90deg,rgba(0,0,0,.35),rgba(255,255,255,.06))}
"""

T['terra']['css']+="""
.cf .pill{background:#0d0d0d!important}
.cf .pill i{background:#ffffff!important;color:#0d0d0d!important}
.stitch{border:3px dotted #ffffff!important}
.pocket i{border:3px dotted #ffffff!important;border-top:0!important}
.btn.primary,#tourB{background:linear-gradient(180deg,#2a2a2a,#0d0d0d)!important;color:#fff!important}
.btn{border:1px solid rgba(0,0,0,.18)!important}
#fullB{background:#ffffff!important;color:#0d0d0d!important;border:1px solid rgba(0,0,0,.18)!important}
#cap h1 .script{color:#0d0d0d}#cap h1 .sharpie{color:#0d0d0d}
#toast{background:#0d0d0d;color:#fff}
#nudge a.go{background:#0d0d0d;color:#fff}
"""

def imgs(name):
    d={}
    for k in ('home','neigh','num','move'):
        im=Image.open(f'out/{name}/{k}.jpg').convert('RGB')
        b=io.BytesIO(); im.resize((1224,1584)).save(b,'JPEG',quality=82,optimize=True)
        d[k]='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
        b=io.BytesIO(); im.resize((612,792)).save(b,'JPEG',quality=78,optimize=True)
        d[k+'_s']='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
    return d

def sub(s,pat,rep,flags=0,count=1):
    n=re.subn(pat,lambda m:rep,s,count=count,flags=flags)
    if n[1]==0: raise SystemExit('NO MATCH: '+pat[:70])
    return n[0]

def build(name):
    t=T[name]; s=SRC
    s=s.replace('1460 Latigo Ct Folder',f'123 Sample Street Folder - {t["title"]}')
    s=re.sub(r"@font-face\{font-family:['\"](CormorantCover|ScriptWelcome)['\"][^}]*\}",'',s)
    s=s.replace('<style>\n','<style>\n'+fontcss(t['fonts'],True)+f"\nhtml,body,button,a,input{{font-family:{t['body']}}}\n",1)
    lux=f'<style id="lux">\n{t["css"]}\n#cap h1{{font-family:{t["head"]}}}\n#cap h1 .script{{font-family:{t["script"]}}}\n</style>'
    s=sub(s,r'<style id="lux">.*?</style>',lux,re.S)
    # cover
    s=sub(s,r'<div class="face cf" id="coverFront">.*?(?=<div class="face cb" id="faceL">)','<div class="face cf" id="coverFront">\n<div class="noise"></div><div class="spine"></div>\n<div class="stitch"></div>\n'+t['cover']+'\n</div>\n      ',re.S)
    # images
    s=sub(s,r'<script>const IMG=\{.*?\};</script>','<script>const IMG='+__import__('json').dumps(imgs(name))+';</script>',re.S)
    # download button hidden (previews have no pdf)
    s=s.replace('id="dlB" href="folder.pdf"','id="dlB" style="display:none" href="#"')
    s=re.sub(r'download="1460 Latigo Ct - Listing Folder.pdf"','',s)
    # placeholders
    s=s.replace('Text John for a quick estimate.','Text your agent for a quick estimate.').replace('Text John','Text your agent').replace('Hi%20John%2C','Hi%2C').replace('Call John','Call the Agent')
    s=s.replace('john.realtor@example.com','you@example.com')
    s=s.replace('<div class="bn">John Realtor</div>','<div class="bn">Your Name Here</div>')
    s=s.replace('1460 Latigo Ct, Prosper, TX 75078','123 Sample Street, Anytown, TX 75000').replace('1460 Latigo Ct.','123 Sample Street')
    # scene
    s=sub(s,r"const RT=\{move:12,pics:66\};","const RT={move:12,num:66};")
    s=sub(s,r"\[\['move',-1\.2,0\],\['pics',\.9,1\]\]\.forEach\(\(\[k,rz,i\]\)=>paper\(k,'R',k,\{x:284\+i\*8,y:RT\[k\]-59,z:2\+i,rz\},300,k==='pics'\?'pics2':null\)\);","[['move',-1.2,0],['num',.9,1]].forEach(([k,rz,i])=>paper(k,'R',k,{x:284+i*8,y:RT[k]-59,z:2+i,rz},300,null));")
    sc='''const SC=[
 {id:'closed',open:0,cam:{cx:300,cy:0,w:700,h:900,tilt:15,yaw:-7,dy:-14},t:'Welcome to 123 Sample Street',s:''},
 {id:'open',open:1,cam:OV,dur:4,t:"Here's what's inside",s:'Home and neighborhood highlights on the left. The numbers and move-in costs on the right.'},
 {id:'home',focus:'home',dur:7.5,t:'Home highlights',s:'Sample copy: bedrooms, baths, square footage and the features that make this home stand out.'},
 {id:'neigh',focus:'neigh',dur:8.5,t:'Neighborhood highlights',s:'Parks and trails, everyday errands, restaurants, and drive times to popular destinations.'},
 {id:'num',focus:'num',dur:9,t:'The numbers',s:'Different ways to structure a purchase, side by side: estimated monthly payment and cash to close. Sample figures only.'},
 {id:'move',focus:'move',dur:9,t:'Move-in costs',s:'What to set up before you arrive, and typical monthly costs.'},
 {id:'done',open:1,cam:OV,explore:true,t:"Here's your folder.",s:'Tap any flyer to take a closer look, or let us walk you through it.'}
];'''
    s=sub(s,r"const SC=\[.*?\n\];",sc,re.S)
    s=sub(s,r"const DOTIDS=\['home','neigh','move','pics','pics2'\];","const DOTIDS=['home','neigh','num','move'];")
    s=sub(s,r"ALT=\{pics:\{[^}]*\}\};","ALT={};")
    s=sub(s,r"move:S\('move'\), pics:S\('pics'\),","move:S('move'), num:S('num'),")
    s=sub(s,r"pics:\{p:'R',z:47,up:110,r:\[\{x:0,y:RT\.pics-4,w:596,h:470\}\]\},","num:{p:'R',z:47,up:110,r:[{x:0,y:RT.num-4,w:596,h:470}]},")
    # script/sharpie path
    s=sub(s,r'<path class="s1" d="M5 25 C80 14 215 13 295 21" stroke-width="11"/>',t['sharp'])
    os.makedirs(f'out/{name}',exist_ok=True)
    open(f'out/{name}/folder.html','w').write(s)
    print(name,len(s)//1024,'KB')

for n in (sys.argv[1:] or ['heirloom','metropolitan','azure','terra','evergreen']): build(n)
