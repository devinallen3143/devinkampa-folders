import base64, json, sys
L=[ # slug, address, city, beds, style, order
("1460-latigo-ct","1460 Latigo Ct","Prosper",6,"Luxury"),
("8610-brittania-way","8610 Brittania Way","Dallas",4,"Standard"),
("8630-rolling-rock-ln","8630 Rolling Rock Ln","Dallas",4,"Standard"),
("113-candlelite-trl","113 Candlelite Trl","Heath",4,"Standard"),
("1429-macrae-ct","1429 Macrae Ct","Allen",3,"Standard"),
("1008-10th-st","1008 10th St","Argyle",3,"Standard"),
("4824-cedar-creek-dr","4824 Cedar Creek Dr","McKinney",4,"Standard"),
("1001-lake-cypress-ln","1001 Lake Cypress Ln","Little Elm",4,"Standard"),
("2388-greymoore-dr","2388 Greymoore Dr","Frisco",4,"Standard"),
("1108-salado-dr","1108 Salado Dr","Allen",5,"Standard"),
]
mode=sys.argv[1]  # repo | preview
def img(p):
    if mode=='repo': return '/folder/'+p
    ext=p.split('.')[-1]; mime='image/webp' if ext=='webp' else 'image/png'
    return f"data:{mime};base64,"+base64.b64encode(open('site/'+p,'rb').read()).decode()
def link(s): return f"https://devinkampa.com/folder/{s}/"
CR={"1108-salado-dr","2388-greymoore-dr","4824-cedar-creek-dr"}
data=[dict(slug=s,addr=a,city=c,beds=b,credit=(s in CR),img=img(f'thumbs/{s}.webp'),href=link(s)) for s,a,c,b,st in L]
html=open('template.html').read().replace('__DATA__',json.dumps(data)).replace('__LOGO__',img('highlands-logo.png'))
open(f'site/index.html' if mode=='repo' else 'preview.html','w').write(html)
