import asyncio, json, subprocess
from playwright.async_api import async_playwright
s=json.loads(subprocess.check_output(['python3','-I','/home/claude/tools/maxsave.py','2.21.48']).decode())
s['tut']={'k':1,'t':1}; s['settings']['story']=False
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']); pg=await b.new_page(viewport={'width':412,'height':860})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.add_init_script("window.__au=[];const P=HTMLMediaElement.prototype.play;HTMLMediaElement.prototype.play=function(){if(!window.__au.includes(this))window.__au.push(this);return P.call(this)};")
        await pg.add_init_script("if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.setItem('mc_sweet_merge_cafe_save', %s)}" % json.dumps(json.dumps(s)))
        st=lambda: pg.evaluate("window.__au.map(a=>(a.src||'').split('/').pop().slice(0,5)+(a.paused?':P':':▶')+':'+a.currentTime.toFixed(1))")
        await pg.goto('http://localhost:8795/'); await pg.wait_for_timeout(3500)
        await pg.evaluate("document.querySelectorAll('.mc-modal').forEach(m=>m.remove())"); await pg.mouse.click(5,840)
        await pg.wait_for_timeout(2500); print('kitchen', await st())
        await pg.click('#mc-cafeb'); await pg.wait_for_timeout(3500); print('town', await st())
        await pg.evaluate("document.querySelectorAll('.mc-modal').forEach(m=>m.remove())")
        k=pg.locator('[data-tw="cafe"], .tw-kit, [data-tw="back"]').first
        print('kbtn', await k.count())
        if await k.count(): await k.click(); await pg.wait_for_timeout(3500); print('back', await st())
        # settings off
        await pg.click('.mc-lv'); await pg.wait_for_timeout(600)
        await pg.screenshot(path='/tmp/bset.png')
        await pg.click('[data-bgm="0"]'); await pg.wait_for_timeout(2500); print('off', await st())
        await pg.click('[data-bgm="1"]'); await pg.wait_for_timeout(2500); print('on', await st())
        print('errs',errs[:3]); await b.close()
asyncio.run(main())
