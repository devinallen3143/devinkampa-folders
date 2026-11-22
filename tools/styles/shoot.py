import asyncio,sys
from playwright.async_api import async_playwright
async def main(names,mobile=False):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for n in names:
            ctx=await b.new_context(viewport={'width':390,'height':780} if mobile else {'width':1280,'height':800},device_scale_factor=1)
            pg=await ctx.new_page(); errs=[]
            pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
            await pg.goto(f'file:///home/claude/work/styles/out/{n}/folder.html'); await pg.wait_for_timeout(1800)
            tag='m' if mobile else 'd'
            await pg.screenshot(path=f'out/{n}/s_{tag}_closed.png')
            await pg.click('#openB'); await pg.wait_for_timeout(4500)
            await pg.screenshot(path=f'out/{n}/s_{tag}_open.png')
            await pg.click('#tourB'); await pg.wait_for_timeout(7000)
            await pg.screenshot(path=f'out/{n}/s_{tag}_t1.png')
            await pg.click('#nextB'); await pg.wait_for_timeout(2500)
            await pg.click('#nextB'); await pg.wait_for_timeout(3000)
            await pg.screenshot(path=f'out/{n}/s_{tag}_num.png')
            await pg.click('#skipB') if await pg.is_visible('#skipB') else None
            await pg.wait_for_timeout(3500)
            await pg.screenshot(path=f'out/{n}/s_{tag}_end.png')
            print(n,errs[:5]); await ctx.close()
        await b.close()
asyncio.run(main(sys.argv[2:],sys.argv[1]=='m'))
