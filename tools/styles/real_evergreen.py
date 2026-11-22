import io,base64,math,requests,os
from PIL import Image, ImageEnhance
import common, lay, light
from common import render
UP='/mnt/user-data/uploads/'
def pho(i,w=1700):
    im=Image.open(UP+i+'-image.png').convert('RGB'); im.thumbnail((w,w)); b=io.BytesIO(); im.save(b,'JPEG',quality=86)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
P=dict(ext=pho('c3895f01'),liv=pho('29090b71'),aer=pho('062af330'),kit=pho('6fd95218'),bbq=pho('f37979e9'),prim=pho('dc2d0b96'),sun=pho('c2f5fe62'))
S=common.S
S.update(street="7241 Cliffbrook Dr",city="Dallas",state="TX",zip="75254",full="7241 Cliffbrook Dr, Dallas, TX 75254",hood="Northwood Hills",price=1397400,beds=5,baths="6.5",sqft="5,197",garage=2,
 about="A sprawling one-story Northwood Hills home on a 0.42-acre corner lot, with beamed ceilings, a kitchen built around a long island and a backyard made for entertaining: a diving pool, outdoor kitchen and fire pit.",
 bullets=["Coffered beam ceilings and fireplace","Chef's kitchen with an oversized island","Primary suite with its own fireplace","Sunroom opens to the pool","Renovated 37-ft heated diving pool","Outdoor kitchen, grill and fire pit","Circular drive on a 0.42-acre corner lot","Richardson ISD, built in 1968"])
common.NEIGH.update(
 intro="A quiet, tree-lined pocket of Northwood Hills in Richardson ISD, with Fretz Park close by and groceries, coffee and dinner along Preston and Belt Line roads.",
 parks=[("Fretz Park","Rec center, aquatic center with lazy river, tennis and fields"),("Bert Fields Park","Rec center and fields on Spring Valley Rd"),("Celestial Park","Neighborhood park nearby")],
 errands=[("Trader Joe's","14856 Preston Rd","1.4 mi"),("Tom Thumb","14999 Preston Rd","1.5 mi"),("Whole Foods Market","5100 Belt Line Rd","~3 mi")],
 eat=[("Chamberlain's Steak & Chop House","5330 Belt Line Rd"),("Mendocino Farms","5294 Belt Line Rd"),("Shake Shack","5290 Belt Line Rd")],
 drive=[("Preston Road","5 min"),("US 75","7 min"),("Galleria Dallas","12 min"),("Love Field","18 min"),("Downtown","22 min"),("DFW Airport","28 min")])
common.MOVE.update(
 intro="Water, sewer and trash come from the City of Dallas, gas from Atmos Energy, and you choose your electricity and internet providers. Start these a week or two ahead so everything is on the day you get the keys.",
 setup=[("Water, sewer & trash","City of Dallas Water Utilities","Open an account online or call 214-651-1441","Online or call"),
        ("Electricity","Oncor delivers; you choose the provider","Compare plans at powertochoose.org","Pick a provider"),
        ("Natural gas","Atmos Energy","Call 888-286-6700 to set a start date","Call to start"),
        ("Internet","Choose a provider for this address","Compare fiber and cable plans before move-in","Up to $90")],
 monthly=[("Electricity","Roughly 5,197 sq ft plus a pool; summer runs highest",350,700),("Natural gas","Heat and water heating; winter runs highest",70,200),("Water, sewer & trash","City of Dallas bill; pool and irrigation raise summer use",180,350),("Internet","Fiber or cable",60,90),("HOA","$33/mo per the loan worksheet",None,None)],
 hoa="$33/mo")
common.CARDS[:]=[dict(tag="Estimate at 20% down",title="20% down",title2="80% LTV",down=279480,closing=29305,credit=6839,credit_pct=.5,mo=10672,cash=301946,pi=7809,tax=2213,mi=0)]
common.DELTAS[:]=[("$301,946","est. cash to close"),("$10,672/mo","est. payment, plus $33/mo HOA")]
DISC=("Example figures, prepared 11/21/2026; estimates only, not a loan approval or commitment to lend. $1,397,400 price, 20% down, 30-year fixed conventional at 7.490% (APR 7.546%). "
 "Payment = principal, interest, est. taxes ($2,213/mo) and insurance ($650/mo); no mortgage insurance with 20% down; HOA ($33/mo) not included. "
 "Cash to close includes the down payment, est. closing costs, prepaid items and escrow reserves, less a $6,839 seller title credit, which must be agreed in the contract and is subject to loan program limits. "
 "Actual rate, payment and costs could be higher; get an official Loan Estimate before choosing a loan. Devin Kampa is a loan officer, not a licensed real estate agent or Realtor, and this listing is exclusive to the listing Realtor or builder. "
 "Highlands Residential Mortgage, Ltd., NMLS #134871 (www.nmlsconsumeraccess.org). Equal Housing Lender.")
for m in (common,lay): m.DISC=DISC
import lay_evergreen2
lay_evergreen2.DISC=DISC
# ---- photo slots ----
SL={(70,70,560,700):('ext','40% 55%','Digitally Altered'),(70,1140,345,260):('kit','45% 50%','Digitally Altered'),(442,1140,345,260):('liv','40% 50%','Digitally Altered'),(814,1140,340,260):('bbq','50% 55%','Digitally Altered'),(690,1260,464,120):('aer','50% 40%','Digitally Altered')}
cnt={'n':0}
def ph(x,y,w,h,cls='ph',extra=''):
    k=(x,y,w,h)
    if k==(930,70,224,190):
        cnt['n']+=1; v=('sun','50% 50%',None) if cnt['n']==1 else ('prim','45% 55%','Virtually Staged')
    else: v=SL.get(k)
    if not v: return f'<div class="{cls}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}"></div>'
    key,pos,lab=v
    tag=f'<span style="position:absolute;right:8px;bottom:6px;font:600 11px sans-serif;color:#fff;background:rgba(0,0,0,.55);padding:2px 7px;border-radius:3px">{lab}</span>' if lab else ''
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:url({P[key]}) {pos}/cover no-repeat;{extra}">{tag}</div>'
lay.ph=ph
# ---- map: z14 centred up-left of home so Preston Rd stores are in frame ----
def mapdata(w=464,h=470,z=14):
    lat,lon=32.9456,-96.7805; n=2**z
    hx=(lon+180)/360*n*256; hy=(1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*n*256
    cx,cy=hx-75,hy-25; x0,y0=cx-w/2,cy-h/2
    big=Image.new('RGB',(w+512,h+512),'white')
    for tx in range(int(x0//256),int((x0+w)//256)+1):
        for ty in range(int(y0//256),int((y0+h)//256)+1):
            r=requests.get(f'https://tile.openstreetmap.org/{z}/{tx}/{ty}.png',headers={'User-Agent':'devinkampa-folders/1.0'},timeout=20)
            big.paste(Image.open(io.BytesIO(r.content)).convert('RGB'),(int(tx*256-x0),int(ty*256-y0)))
    im=big.crop((0,0,w,h)).convert('L'); im=ImageEnhance.Contrast(im).enhance(.85).convert('RGB')
    b=io.BytesIO(); im.save(b,'JPEG',quality=88)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
MAPURI=mapdata()
PINS=[('tree',289,213),('tree',130,317),('cart',40,188),('cart',37,120)]
_ctx=lay.ctx
def ctx2(name):
    X=_ctx(name); A=X['A']; I=X['I']; icon=common.icon
    def mp(w,h):
        pins=''
        for ic,px,py in PINS:
            pins+=f'<div style="position:absolute;left:{px-17}px;top:{py-17}px;width:34px;height:34px;border-radius:50%;background:#fff;border:3px solid {A};display:grid;place-items:center">{icon(ic,18,A,1.8)}</div>'
        home=f'<div style="position:absolute;left:{307-22}px;top:{260-22}px;width:44px;height:44px;border-radius:50%;background:{I};border:4px solid #fff;display:grid;place-items:center">{icon("home",22,"#fff",1.8)}</div>'
        cap='<div style="position:absolute;right:6px;bottom:6px;font:600 10px sans-serif;color:#555;background:rgba(255,255,255,.8);padding:2px 5px">Map © OpenStreetMap contributors · pins approximate</div>'
        return f'<div style="position:relative;width:{w}px;height:{h}px;background:url({MAPURI}) center/cover">{pins}{home}{cap}</div>'
    X['map']=mp; return X
lay.ctx=ctx2; lay_evergreen2.ctx=ctx2
def build():
    d=lay_evergreen2.build()
    d['home']=d['home'].replace('123 Sample','7241').replace('>Street<','>Cliffbrook Dr<')
    d['num']=d['num'].replace('Sample figures','Example figures').replace('Seller credit','Seller title credit').replace(' (0.5%)','')
    return d
if __name__=='__main__':
    os.makedirs('real_e',exist_ok=True)
    d={k:light.postproc('evergreen',v,k) for k,v in build().items()}
    render([(f'/home/claude/work/styles/real_e/{k}.jpg',h) for k,h in d.items()]); print('ok')
