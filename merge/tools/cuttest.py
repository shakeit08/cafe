import asyncio, json, sys
from playwright.async_api import async_playwright
ALL=open('/tmp/gm/areas.txt').read().strip().split(',')
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(); ctx=await b.new_context(viewport={'width':390,'height':780})
        pg=await ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: errs.append('C:'+m.text) if 'ext' in m.text or 'rror' in m.text else None)
        U='http://localhost:8767/'
        await pg.goto(U+'blank.html'); await pg.evaluate("localStorage.clear()")
        await pg.goto(U+'ph3.html'); await pg.wait_for_function('window.__btns.length>0',timeout=20000)
        await pg.evaluate('window.__btns[0]()'); await pg.wait_for_timeout(1500)
        try: await pg.get_by_text('건너뛰기').first.click(timeout=1500)
        except Exception: pass
        await pg.wait_for_timeout(8000); print(errs[:5]); store=json.loads(await pg.evaluate("JSON.stringify(window.__store)"))
        k=[x for x in store if 'save' in x][0]; S=json.loads(store[k]) if isinstance(store[k],str) else store[k]
        S['savedAt']=9999999999999; S['level']=30;S['stars']=40;S['story']={'intro':True,'seen':{}};S['seenVer']='9.9.9'
        S['areaDone']={x:True for x in ALL}
        store[k]=json.dumps(S)
        await pg.goto(U+'blank.html'); await pg.evaluate("s=>localStorage.setItem('mock_store',s)",json.dumps(store))
        await pg.goto(U+'ph3.html'); await pg.wait_for_function('window.__btns.length>0',timeout=20000)
        await pg.evaluate('window.__btns[0]()'); await pg.wait_for_timeout(3000)
        await pg.evaluate("document.querySelector('.mc-modal')?.remove();document.querySelector('.mc-story')?.remove()")
        await pg.click('[data-act="cafe"]'); await pg.wait_for_timeout(15000)
        await pg.evaluate("document.querySelector('.mc-modal')?.remove()")
        for c in ['ch1','ch2','ch3','ch4']:
            await pg.evaluate(f"document.querySelector('[data-tw=\"{c}\"]')?.click()"); await pg.wait_for_timeout(1500)
            bad=await pg.evaluate("[...document.querySelectorAll('img')].filter(i=>i.complete&&i.naturalWidth===0).length")
            tot=await pg.evaluate("document.querySelectorAll('img').length")
            print(c,'imgs',tot,'broken',bad)
            await pg.screenshot(path=f'/tmp/gm/cut_{sys.argv[1]}_{c}.png')
        log=await pg.evaluate("window.__log"); print(len(log),'requests', [l for l in log if 'Range' in l][:3])
        print(errs[:6]); await b.close()
asyncio.run(m())
