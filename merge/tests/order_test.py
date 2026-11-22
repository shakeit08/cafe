import asyncio, json, subprocess
from playwright.async_api import async_playwright
s=json.loads(subprocess.check_output(['python3','-I','/home/claude/tools/maxsave.py','2.21.43']).decode())
s['tut']={'k':1,'t':1}; s['settings']['story']=False
s['orders']=[{'id':900,'a':1,'req':[{'c':'bakery','l':9},{'c':'coffee','l':10},{'c':'tea','l':4}],'coins':1,'xp':1,'en':0},
             {'id':901,'a':2,'req':[{'c':'bakery','l':9},{'c':'tea','l':4}],'coins':1,'xp':1,'en':0},
             {'id':902,'a':3,'req':[{'c':'berry','l':3}],'coins':1,'xp':1,'en':0}]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':412,'height':860})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.add_init_script("if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.setItem('mc_sweet_merge_cafe_save', %s)}" % json.dumps(json.dumps(s)))
        await pg.goto('http://localhost:8765/'); await pg.wait_for_timeout(3000)
        await pg.evaluate("document.querySelectorAll('.mc-modal [data-x], .mc-modal .mc-btn').forEach(b=>b.click())")
        await pg.mouse.click(5,5); await pg.wait_for_timeout(9500)
        sv=json.loads(await pg.evaluate("localStorage.getItem('mc_sweet_merge_cafe_save')"))
        print([(o['id'],[r['l'] for r in o['req']]) for o in sv['orders']]); print('errs',errs[:3])
        await b.close()
asyncio.run(main())
