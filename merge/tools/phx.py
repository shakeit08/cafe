import asyncio, json
from playwright.async_api import async_playwright
ALL='cafe,flower,ice,park,post,book,plaza,station,photo,store,bath,teahouse,tackle,dock'.split(',')
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(); ctx=await b.new_context(viewport={'width':390,'height':780},device_scale_factor=2)
        pg=await ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: errs.append('C:'+m.text) if 'ext' in m.text or 'rror' in m.text else None)
        bad=[]; pg.on('requestfailed',lambda r: bad.append(r.url[:80]))
        await pg.goto('http://localhost:8765/../ph2.html') if False else await pg.goto('http://localhost:8766/ph2.html'); await pg.wait_for_function('window.__btns.length>0',timeout=20000)
        await pg.evaluate('window.__btns[0]()'); await pg.wait_for_timeout(1500)
        try: await pg.get_by_text('건너뛰기').first.click(timeout=1500)
        except Exception: pass
        await pg.wait_for_timeout(6000)
        await pg.wait_for_timeout(4000); store=json.loads(await pg.evaluate("JSON.stringify(window.__store)")); print(list(store), errs[:4])
        k=[x for x in store if 'save' in x][0]; S=json.loads(store[k]) if isinstance(store[k],str) else store[k]
        S['savedAt']=9999999999999; S['level']=27;S['stars']=40;S['story']={'intro':True,'seen':{}};S['seenVer']='9.9.9'
        S['areaDone']={x:True for x in ALL[:9]}
        store[k]=json.dumps(S)
        await pg.goto('http://localhost:8766/blank.html'); await pg.wait_for_timeout(300)
        await pg.evaluate("s=>localStorage.setItem('mock_store',s)",json.dumps(store))
        await pg.goto('http://localhost:8766/ph2.html'); await pg.wait_for_function('window.__btns.length>0',timeout=20000)
        await pg.evaluate('window.__btns[0]()'); await pg.wait_for_timeout(4000)
        await pg.evaluate("document.querySelector('.mc-modal')?.remove();document.querySelector('.mc-story')?.remove()")
        await pg.click('[data-act="cafe"]'); await pg.wait_for_timeout(5000)
        await pg.evaluate("document.querySelector('.mc-modal')?.remove()")
        await pg.evaluate("document.querySelector('[data-tw=\"ch2\"]')?.click()"); await pg.wait_for_timeout(3000)
        await pg.screenshot(path='/tmp/gm/phx_ch2.png')
        print(await pg.evaluate("[...document.querySelectorAll('img')].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.getAttribute('src').slice(0,30)).slice(0,8)"))
        print(errs[:6],bad[:5]); await b.close()
asyncio.run(m())
