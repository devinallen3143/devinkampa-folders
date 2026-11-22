import base64, os, io, math, json
FD='/home/claude/work/styles/fonts'
W,H=1224,1584

def fontcss(spec, embed=False):
    """spec: list of (family, dir, weight, style)"""
    out=[]
    for fam,d,wt,st in spec:
        p=f'{FD}/{d}/files/{d}-latin-{wt}-{st}.woff2'
        if embed: url='data:font/woff2;base64,'+base64.b64encode(open(p,'rb').read()).decode()
        else: url='file://'+p
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{wt};font-style:{st};font-display:block;src:url({url}) format('woff2')}}")
    return '\n'.join(out)

def page(fonts, css, body):
    return f"<!doctype html><html><head><meta charset=utf-8><style>{fonts}\n*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:{W}px;height:{H}px;overflow:hidden}}body{{position:relative;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}}\n{css}</style></head><body>{body}</body></html>"

# ---------- sample listing (example only) ----------
S=dict(street="123 Sample Street", city="Anytown", state="TX", zip="75000", full="123 Sample Street, Anytown, TX 75000",
  hood="Sample Heights", price=450000, beds=4, baths=3, sqft="2,450", lot="0.25", year=2018, garage=2,
  agent="Your Name Here", agent_t="Real Estate Agent", brokerage="Your Brokerage", aphone="(555) 555-5555", aemail="you@example.com",
  about="A bright, open floor plan with a chef's kitchen, a private primary suite and a backyard made for entertaining, set on a quiet street close to everything.",
  bullets=["Primary suite on the main level","Chef's kitchen with island","Open living and dining","Covered patio and fenced yard","Dedicated home office","Walk-in closets throughout","Two-car garage, built in 2018","Highly rated schools nearby"],
  caption="Add a one-line, sales-style caption about the home here.")
LO=dict(name="Devin Kampa", t="Loan Officer · NMLS #2532480", phone="320-241-5823", email="dkampa@highlandsmortgage.com", web="devinkampa.com")
NEIGH=dict(
 intro="A friendly, established neighborhood with sidewalks, mature trees and a community pool, minutes from shopping, dining and top-rated schools.",
 parks=[("Sample Park","Trails, playground and picnic pavilion"),("Creekside Trail","Paved walking and biking path"),("Community Pool","Neighborhood amenity and clubhouse"),("Neighborhood Dog Park","Fenced, off-leash")],
 errands=[("Grocery Store","Groceries and pharmacy","0.5 mi"),("Pharmacy","Prescriptions and essentials","0.8 mi"),("Home Improvement","Hardware and garden","1.9 mi"),("Fitness Center","Gym and classes","1.4 mi"),("Big-Box Retailer","Everyday needs","2.0 mi")],
 eat=[("Local Italian Kitchen","Handmade pasta, wood-fired pizza"),("Neighborhood Grill","Family favorite"),("Sushi & Ramen","Casual dinner"),("Corner Coffee Shop","Morning stop")],
 drive=[("Downtown","15 min"),("Shopping center","10 min"),("Major highway","5 min"),("Top-rated schools","8 min"),("Hospital","12 min"),("Airport","35 min")])
MOVE=dict(
 intro="Water and trash are usually set up with the city. Electricity, gas and internet are your choice of provider. Start these a week or two ahead so everything is on the day you get the keys.",
 setup=[("Water, wastewater & trash","City utilities","Start online or at City Hall","Online or in person"),
        ("Electricity","Choose a provider","Confirm the providers for this address","Pick a provider"),
        ("Natural gas","Local gas utility","Set a start date for the house","Call to start"),
        ("Internet","Fiber or cable","Speeds from 300 Mbps to 1 Gig","Up to $90")],
 monthly=[("Electricity","Roughly 2,450 sq ft; summer runs highest",180,320),("Natural gas","Heat and water heating; winter runs highest",40,120),
          ("Water, sewer & trash","City utilities",90,160),("Internet","Fiber or cable",60,90),("HOA","Annual dues, per public record",None,None)],
 hoa="Per listing", fine="Estimates only, not quotes. Figures are examples scaled to home size and typical ranges; actual costs depend on usage, provider and plan. Verify with each provider before you move in.")

# ---------- example numbers ----------
def pmt(P,rate,n=360):
    i=rate/1200; return P*i/(1-(1+i)**-n)
RATE=7.00
def scen(down_pct,credit_pct,closing,mi_pct):
    price=S['price']; down=price*down_pct/100; loan=price-down
    pi=pmt(loan,RATE); tax=price*0.021/12; ins=300; mi=loan*mi_pct/1200
    mo=pi+tax+ins+mi; credit=price*credit_pct/100
    cash=down+closing-credit
    return dict(down_pct=down_pct,credit_pct=credit_pct,down=round(down),closing=closing,credit=round(credit),mo=round(mo),cash=round(cash),pi=round(pi),tax=round(tax),mi=round(mi))
CARDS=[ dict(tag="Lowest cash to close", title="5% down +", title2="3% seller credit", **scen(5,3,14400,.55)),
        dict(tag="Balanced", title="10% down +", title2="no seller credit", **scen(10,0,12600,.35)),
        dict(tag="Lowest monthly payment", title="20% down +", title2="no seller credit", **scen(20,0,11700,0)) ]
def usd(n): return f"${n:,.0f}"
DELTAS=[(usd(CARDS[1]['cash']-CARDS[0]['cash']),"more cash to close with 10% down than with 5% down."),
        (usd(CARDS[0]['mo']-CARDS[2]['mo'])+"/mo","lower payment with 20% down vs. 5% down.")]
DISC=("Sample figures for illustration only; not based on a real listing or a real loan scenario. Estimates only, prepared "+"11/18/2026; not a loan approval or commitment to lend. $450,000 price, 30-year fixed conventional at 7.000% interest. "
 "Payment = principal, interest, est. taxes ($788/mo), insurance ($300/mo) and mortgage insurance where it applies. Seller credits must be agreed in the contract and are subject to loan program limits. "
 "Actual rate, payment and costs could be higher; get an official Loan Estimate before choosing a loan. Devin Kampa is a loan officer, not a licensed real estate agent or Realtor, and this listing is exclusive to the listing Realtor or builder. "
 "Highlands Residential Mortgage, Ltd., NMLS #134871 (www.nmlsconsumeraccess.org). Equal Housing Lender.")

# ---------- icons (24px line icons) ----------
IC={
 'bed':'M3 18V7M3 14h18v4M21 14v-3a3 3 0 0 0-3-3h-7v6M6.5 11.5h.01',
 'bath':'M4 12h16v3a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4zM6 12V6a2 2 0 0 1 4 0M7 19l-1 2M17 19l1 2',
 'sqft':'M4 4h16v16H4zM4 12h8v8M12 4v8',
 'garage':'M3 11l2-5h14l2 5v6h-3v-2H6v2H3zM3 11h18M7 14h.01M17 14h.01',
 'tree':'M12 21v-5M12 16c-4 0-6-2.5-6-5.5 0-2 1.2-3.2 2.4-3.8C8.4 4.5 10 3 12 3s3.6 1.5 3.6 3.7C16.8 7.3 18 8.5 18 10.5 18 13.5 16 16 12 16z',
 'cart':'M3 4h3l2.5 11h9.5l2-8H7M10 20h.01M17 20h.01',
 'dine':'M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10M17 3c-2 1.5-3 4-3 7h3v11',
 'clock':'M12 7v5l3 2M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z',
 'school':'M2 9l10-5 10 5-10 5zM6 11v5c3 2.5 9 2.5 12 0v-5',
 'coffee':'M4 8h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM17 9h2a2 2 0 0 1 0 4h-2M7 3v2M11 3v2',
 'drop':'M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z',
 'bolt':'M13 3L5 13h6l-1 8 8-10h-6z',
 'flame':'M12 3c1 4 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 2 2 2 0-3-1-5 1-8z',
 'wifi':'M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M12 19.5h.01',
 'trash':'M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13',
 'home':'M3 11l9-7 9 7M5 10v10h14V10M10 20v-6h4v6',
 'check':'M5 12l5 5 9-10',
 'pin':'M12 21s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12zM12 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z',
 'phone':'M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z',
 'mail':'M3 6h18v12H3zM3 7l9 7 9-7',
 'cal':'M4 6h16v14H4zM4 10h16M8 3v4M16 3v4',
 'cross':'M10 4h4v6h6v4h-6v6h-4v-6H4v-4h6z',
 'plane':'M21 3L3 11l7 2 2 7z',
 'road':'M8 3L5 21M16 3l3 18M12 4v3M12 11v3M12 18v3',
 'leaf':'M5 19C5 10 11 5 20 4c0 9-5 15-14 15zM5 19c3-4 6-7 10-9',
}
def icon(name,size=24,color='currentColor',sw=1.6,fill='none'):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"><path d="{IC[name]}"/></svg>'
NEIGH_ICONS={'park':'tree','err':'cart','eat':'dine','drive':'clock'}

def qr_svg(url,color='#000',bg='none',size=170):
    import segno
    q=segno.make(url,error='m',micro=False); b=io.BytesIO(); q.save(b,kind='svg',scale=1,border=0,dark=color,light=None,xmldecl=False,svgns=True,nl=False)
    s=b.getvalue().decode()
    import re
    m=re.search(r'<svg[^>]*>',s).group(0)
    w=int(re.search(r'width="(\d+)',m).group(1)); h=int(re.search(r'height="(\d+)',m).group(1))
    m2=re.sub(r'\s(width|height)="[^"]*"','',m).replace('<svg',f'<svg width="{size}" height="{size}" viewBox="0 0 {w} {h}" shape-rendering="crispEdges"',1)
    return s.replace(m,m2,1)

# ---------- rendering ----------
async def _render(items):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':W,'height':H})
        for path,html in items:
            hp=path.rsplit('.',1)[0]+'.html'; open(hp,'w').write(html)
            await pg.goto('file://'+hp); await pg.wait_for_timeout(350)
            await pg.evaluate('document.fonts.ready')
            await pg.screenshot(path=path,type='jpeg',quality=90)
        await b.close()
def render(items):
    import asyncio; asyncio.run(_render(items))

def ph(x,y,w,h,cls='ph',extra=''):
    return f'<div class="{cls}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}"></div>'
def headshot_uri():
    from PIL import Image
    im=Image.open('/home/claude/work/styles/cardphoto.jpg').convert('RGB'); im.thumbnail((360,360)); b=io.BytesIO(); im.save(b,'JPEG',quality=88)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
HS=headshot_uri()
