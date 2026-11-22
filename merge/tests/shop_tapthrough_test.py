import asyncio, json, subprocess, time
from playwright.async_api import async_playwright
s=json.loads(subprocess.check_output(['python3','-I','/home/claude/tools/maxsave.py','2.21.48']).decode())
s['tut']={'k':1,'t':1}; s['settings']['story']=False; s['energy']=0; s['eTs']=int(time.time()*1000)
b=[None]*len(s['board']); b[6]={'g':'bakery','gl':5}; s['board']=b
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(); pg=await br.new_page(viewport={'width':412,'height':860})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.add_init_script("if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.setItem('mc_sweet_merge_cafe_save', %s)}" % json.dumps(json.dumps(s)))
        await pg.goto('http://localhost:8795/'); await pg.wait_for_timeout(3000)
        await pg.evaluate("document.querySelectorAll('.mc-modal').forEach(m=>m.remove())")
        en=lambda: pg.evaluate("document.querySelector('#mc-en .v').textContent")
        await pg.locator('.mc-board .c[data-i="6"]').click(); await pg.wait_for_timeout(80)
        bb=await pg.locator('[data-buy]').bounding_box(); x,y=bb['x']+bb['width']/2,bb['y']+bb['height']/2
        for k in range(12): await pg.mouse.click(x,y); await pg.wait_for_timeout(110)
        print('after spam energy',await en(),'shop open',await pg.locator('[data-buy]').count())
        await pg.wait_for_timeout(700); await pg.mouse.click(x,y); await pg.wait_for_timeout(300)
        print('after deliberate tap energy',await en(),'toast',await pg.evaluate("[...document.querySelectorAll('.mc-toast')].map(t=>t.textContent).join('|')"))
        print('errs',errs[:3]); await br.close()
asyncio.run(main())
