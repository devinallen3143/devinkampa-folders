import os,re
import real_evergreen_c as C, light
from common import render
def plain(h):
    h=h.replace('background:#B26A3C;color:#fff','background:#fff;color:#111;border:2px solid #111')
    h=h.replace('rgba(247,242,232,','rgba(255,255,255,').replace('#F7F2E8','#FFFFFF')
    h=re.sub(r'(?<![-\w])color:#(1F3A2E|2D5240)','color:#111111',h)
    h=h.replace('border-bottom:6px solid #B26A3C','border-bottom:3px solid #B26A3C')
    for a,b in (('#1F3A2E','#F3F3F3'),('#2D5240','#F3F3F3'),('#DDE4D3','#F3F3F3'),('#B26A3C','#111111'),('#D9A07A','#666666'),('#1F2A24','#111111'),('#5F6B62','#666666'),('#CFD6C4','#EEEEEE'),('#D9D3C2','#D6D6D6'),('#EEEAD9','#EEEEEE')):
        h=h.replace(a,b)
    h=re.sub(r'color:rgba\(255,255,255,[.\d]+\)','color:#555555',h)
    h=re.sub(r'color:#(C9D7CC|BFD0C4|DDE4D3|F7F2E8)','color:#555555',h)
    h=h.replace('color:#fff','color:#111')
    h=h.replace('height:74px;background:#F3F3F3','height:74px;background:#fff')
    # header title blocks and footer get a rule instead of a color band
    h=re.sub(r'(left:0;top:0;width:1224px;height:\d+px;background:#F3F3F3)',r'\1;border-bottom:2px solid #111;box-sizing:border-box',h)
    h=re.sub(r'(left:0;top:0;width:1224px;height:\d+px;)background:#F3F3F3',r'\1background:#fff',h)
    h=h.replace('height:150px;background:#F3F3F3','height:150px;background:#fff')
    h=h.replace('border-top:6px solid #111111','border-top:2px solid #111111')
    return h
def build():
    d={k:plain(v) for k,v in C.build().items()}
    return {k:light.postproc('evergreen',v,k) for k,v in d.items()}
if __name__=='__main__':
    os.makedirs('real_ep',exist_ok=True)
    render([(f'/home/claude/work/styles/real_ep/{k}.jpg',h) for k,h in build().items()]); print('ok')
