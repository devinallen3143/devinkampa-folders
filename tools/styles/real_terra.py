import io,base64,math,requests,json,os
from PIL import Image, ImageEnhance
import common, lay, lay_terra, light
from common import render
UP='/mnt/user-data/uploads/'
def pho(i,w=1700):
    im=Image.open(UP+i+'-image.png').convert('RGB'); im.thumbnail((w,w)); b=io.BytesIO(); im.save(b,'JPEG',quality=86)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
EXT=pho('c3b6cb98')
# ---- listing data ----
S=common.S
S.update(street="4148 Hollow Oak Dr",city="Dallas",state="TX",zip="75287",full="4148 Hollow Oak Dr, Dallas, TX 75287",hood="Bent Tree Gables",price=360000,beds=2,baths=2,sqft="1,157",garage=1,
 about="A refreshed patio home in Bent Tree Gables with vaulted ceilings, a bright open living and dining space and a versatile upstairs flex space, minutes from the Dallas North Tollway and Frankford Road.",
 bullets=["Patio home with vaulted ceilings","Upstairs loft for flex space","Corner fireplace in the living room","Updated kitchen, blue tile backsplash","Breakfast nook with bay windows","Floating double vanity in the bath","French door out to the patio","Plano ISD, built 1984 on 0.18 acre"])
common.NEIGH.update(
 intro="A tree-lined pocket of Far North Dallas in Plano ISD, with Mitchell Elementary about 0.3 mile away and the Dallas North Tollway, Frankford Road shopping and big parks close by.",
 parks=[("Katie Jackson Park","45-acre park with trails, playground and pavilion"),("NorthBark Dog Park","22-acre off-leash park with trails"),("Keller Springs Park","Nearby neighborhood park")],
 errands=[("Tom Thumb","4625 Frankford Rd","0.7 mi"),("Kroger","3939 Frankford Rd","1.0 mi")],
 eat=[("The Blue Fish","Sushi at Dallas Pkwy and Frankford"),("Mizu Asian Fusion","Sushi and grill on Preston Rd"),("Cris and John","Viet-Mex kitchen on Campbell Rd")],
 drive=[("Tollway","3 min"),("Bush Tpke","5 min"),("Mitchell Elem.","2 min"),("Legacy West","15 min"),("Downtown","25 min"),("DFW","25 min")])
common.MOVE.update(
 intro="Water, sewer and trash come from the City of Dallas, gas from Atmos Energy, and you choose your electricity and internet providers. Start these a week or two ahead so everything is on the day you get the keys.",
 setup=[("Water, sewer & trash","City of Dallas Water Utilities","Open an account online or call 214-651-1441","Online or call"),
        ("Electricity","Oncor delivers; you choose the provider","Compare plans at powertochoose.org","Pick a provider"),
        ("Natural gas","Atmos Energy","Call 888-286-6700 to set a start date","Call to start"),
        ("Internet","Choose a provider for this address","Compare fiber and cable plans before move-in","Up to $90")],
 monthly=[("Electricity","Roughly 1,157 sq ft; summer runs highest",90,170),("Natural gas","Heat and water heating; winter runs highest",25,70),("Water, sewer & trash","City of Dallas utility bill",70,130),("Internet","Fiber or cable",60,90),("HOA","$92/mo per the loan worksheet",None,None)],
 hoa="$92/mo")
cards=[dict(tag="Lowest cash to close",title="3% down",title2="97% LTV",down=10800,closing=12041,credit=2064,credit_pct=.6,mo=3317,cash=20777,pi=2439,tax=570,mi=58),
       dict(tag="Lowest monthly payment",title="5% down",title2="95% LTV",down=18000,closing=12023,credit=2064,credit_pct=.6,mo=3266,cash=27959,pi=2389,tax=570,mi=57)]
common.CARDS[:]=cards
common.DELTAS[:]=[("$7,182","more cash to close with 5% down than with 3% down."),("$51.50/mo","lower payment with 5% down vs. 3% down.")]
DISC=("Example figures, prepared 11/21/2026; estimates only, not a loan approval or commitment to lend. $360,000 price, 30-year fixed conventional at 7.490% (APR 7.769% with 3% down; 7.765% with 5% down). "
 "Payment = principal, interest, est. taxes ($570/mo), insurance ($250/mo) and mortgage insurance ($58.20/mo with 3% down; $57.00/mo with 5% down); HOA ($92/mo) not included. "
 "Cash to close includes the down payment, est. closing costs, prepaid items and escrow reserves, less a $2,064 seller title credit, which must be agreed in the contract and is subject to loan program limits. "
 "Actual rate, payment and costs could be higher; get an official Loan Estimate before choosing a loan. Devin Kampa is a loan officer, not a licensed real estate agent or Realtor, and this listing is exclusive to the listing Realtor or builder. "
 "Highlands Residential Mortgage, Ltd., NMLS #134871 (www.nmlsconsumeraccess.org). Equal Housing Lender.")
for m in (common,lay,lay_terra): m.DISC=DISC
# ---- photo slot ----
_ph=lay.ph
def ph(x,y,w,h,cls='ph',extra=''):
    if (x,y,w,h)==(70,64,1084,560):
        return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:url({EXT}) 50% 60%/cover no-repeat;{extra}"></div>'
    return _ph(x,y,w,h,cls,extra)
lay.ph=ph
# ---- map ----
def mapdata(w=1084,h=330,z=15):
    lat,lon=32.9966,-96.8395; n=2**z
    cx=(lon+180)/360*n*256; cy=(1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*n*256
    hx,hy=cx+12,cy-6   # home sits just east of the Voss Rd / Hollow Oak Dr corner
    x0,y0=hx-w/2,hy-h/2
    big=Image.new('RGB',(w+512,h+512),'white')
    for tx in range(int(x0//256),int((x0+w)//256)+1):
        for ty in range(int(y0//256),int((y0+h)//256)+1):
            r=requests.get(f'https://tile.openstreetmap.org/{z}/{tx}/{ty}.png',headers={'User-Agent':'devinkampa-folders/1.0'},timeout=20)
            big.paste(Image.open(io.BytesIO(r.content)).convert('RGB'),(int(tx*256-x0),int(ty*256-y0)))
    im=big.crop((0,0,w,h)).convert('L'); im=ImageEnhance.Contrast(im).enhance(.85).convert('RGB')
    b=io.BytesIO(); im.save(b,'JPEG',quality=88)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
MAPURI=mapdata()
PINS=[('cart',-225,-18),('cart',235,-30),('dine',185,-110)]  # offsets (px at z15) from home: Kroger, Tom Thumb, Chick-fil-A, Blue Fish
_ctx=lay.ctx
def ctx2(name):
    X=_ctx(name); A=X['A']; I=X['I']; icon=common.icon
    def mp(w,h):
        pins=''
        for ic,dx,dy in PINS:
            px,py=w/2+dx,h/2+dy
            pins+=f'<div style="position:absolute;left:{px-22}px;top:{py-22}px;width:44px;height:44px;border-radius:50%;background:#fff;border:3px solid {A};display:grid;place-items:center">{icon(ic,22,A,1.8)}</div>'
        home=f'<div style="position:absolute;left:{w/2-26}px;top:{h/2-26}px;width:52px;height:52px;border-radius:50%;background:{I};border:4px solid #fff;display:grid;place-items:center">{icon("home",26,"#fff",1.8)}</div>'
        cap='<div style="position:absolute;right:12px;bottom:8px;font:600 11px sans-serif;color:#555;background:rgba(255,255,255,.8);padding:2px 6px">Map © OpenStreetMap contributors · pins approximate</div>'
        return f'<div style="position:relative;width:{w}px;height:{h}px;background:url({MAPURI}) center/cover">{pins}{home}{cap}</div>'
    X['map']=mp; return X
lay.ctx=ctx2; lay_terra.ctx=ctx2
def build():
    d=lay_terra.build()
    d['home']=d['home'].replace('123 Sample Street','4148 Hollow Oak Dr')
    d['num']=d['num'].replace('Sample figures','Example figures').replace('$300','$250').replace('Seller credit (0.6%)','Seller title credit')
    return d
if __name__=='__main__':
    os.makedirs('real_t',exist_ok=True)
    d={k:light.postproc('terra',v,k) for k,v in build().items()}
    render([(f'/home/claude/work/styles/real_t/{k}.jpg',h) for k,h in d.items()]); print('ok')
