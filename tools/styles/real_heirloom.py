import io,base64,glob,json,os
from PIL import Image
import t1_heirloom as t1
from common import render
A='/home/claude/lilac/assets/'
def pho(k,w=1500):
    im=Image.open(A+k+'.png').convert('RGB'); im.thumbnail((w,w)); b=io.BytesIO(); im.save(b,'JPEG',quality=86)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
P={k:pho(k) for k in ('front','patio','kitchen','living','bath','pool')}
MAP={(520,24,680,720):('front','50% 55%'),(24,24,1176,236):('pool','50% 60%'),(24,24,392,330):('pool','50% 55%'),(424,24,392,330):('living','50% 50%'),(824,24,376,330):('kitchen','50% 50%'),(24,24,1176,190):('bath','50% 45%')}
def ph(x,y,w,h,cls='ph',extra=''):
    k=MAP.get((x,y,w,h))
    if not k: return f'<div class="{cls}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}"></div>'
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:url({P[k[0]]}) {k[1]}/cover no-repeat;{extra}"></div>'
t1.ph=ph
_icon=t1.icon
t1.icon=lambda n,*a,**k:_icon('home' if n=='garage' else n,*a,**k)
cfg=json.load(open('/home/claude/lilac/lilac.json'))
t1.S.update(street="1902 Lilac Ct",city="Richardson",hood="J.J. Pearce Addition",price=799000,beds=4,baths="3.5",sqft="2,939",garage="1983",
 about="A two-story Richardson home on a quiet cul-de-sac, with a first-floor primary suite, a kitchen built for cooking and a backyard made for entertaining.",
 bullets=["Primary suite on the first floor","Vaulted great room, brick fireplace","Double ovens, gas range, pot filler","Cedar-carved bar and butcher block","New plank flooring, windows and doors","Pool with covered patio and fireplace","Built-in grill and beverage fridge","Quiet cul-de-sac on a 0.24-acre lot"])
t1.S['zip']='75080'
t1.NEIGH.update(
 intro="A quiet, tree-lined pocket of Richardson with Richardson ISD schools, neighborhood parks close by, and groceries, coffee and dinner a short drive away at Coit and Campbell.",
 parks=[("Mimosa Park","Neighborhood park close to home"),("Heights Park","Aquatic center, sports fields and rec center"),("Cottonwood Park","25-acre park on W Belt Line Rd"),("Campbell Ridge Park","Neighborhood park on W Campbell Rd")],
 errands=[("Tom Thumb","Full grocery at Coit and Campbell","0.6 mi"),("Sprouts Farmers Market","Fresh grocery at Coit and Campbell","0.6 mi"),("Natural Grocers","Organic grocery on W Campbell Rd","1.3 mi"),("Kroger","Grocery at 160 N Coit Rd","~2 mi")],
 eat=[("Hawaiian Bros Island Grill","Island plates on N Coit Rd"),("Asian Mint","Thai on W Campbell Rd"),("Bambu","Thai on N Coit Rd")],
 drive=[("US 75","6 min"),("Mohawk Elementary","3 min"),("UT Dallas","6 min"),("Legacy West","20 min"),("Downtown Dallas","25 min"),("DFW Airport","30 min")])
t1.MOVE.update(
 intro="Water, sewer and trash come from the City of Richardson, gas from Atmos Energy, and you choose your electricity and internet providers. Start these a week or two ahead so everything is on the day you get the keys.",
 setup=[("Water, sewer & trash","City of Richardson","Apply online or call 972-744-4120","Online or call"),
        ("Electricity","Oncor delivers; you choose the provider","Compare plans at powertochoose.org","Pick a provider"),
        ("Natural gas","Atmos Energy","Call 888-286-6700 to set a start date","Call to start"),
        ("Internet","Choose a provider for this address","Compare fiber and cable plans before move-in","Up to $90")],
 monthly=[("Electricity","Roughly 2,939 sq ft plus a pool; summer runs highest",250,450),("Natural gas","Heat and water heating; winter runs highest",50,140),("Water, sewer & trash","City of Richardson; pool adds to summer use",120,230),("Internet","Fiber or cable",60,90),("HOA","Voluntary, per listing",None,None)],
 hoa="Voluntary")
t1.CARDS=[dict(tag="Lowest cash to close",title="5% down",title2="95% LTV",credit_pct=.5,down=39950,closing=19836,credit=4233,mo=7144,cash=55553),
          dict(tag="Lowest monthly payment",title="20% down",title2="80% LTV",credit_pct=.5,down=159800,closing=19516,credit=4233,mo=6130,cash=175083)]
t1.DELTAS=[("$119,531","more cash to close with 20% down than with 5% down."),("$1,014/mo","lower payment with 20% down vs. 5% down.")]
t1.DISC=cfg['numbers']['disclaimer']
def build():
    d=t1.all()
    d['home']=d['home'].replace('Car Garage','Year Built').replace('123<br>SAMPLE','1902<br>LILAC').replace('>STREET<','>COURT<')
    n=d['num'].replace('Seller credit (0.5%)','Seller title credit').replace('class="card" style="top:410px;left:','class="card" style="top:410px;margin-left:188px;left:')
    d['num']=n
    return d
if __name__=='__main__':
    os.makedirs('real_h',exist_ok=True)
    render([(f'/home/claude/work/styles/real_h/{k}.jpg',h) for k,h in build().items()]); print('ok')
