import asyncio, json, subprocess, time
from playwright.async_api import async_playwright
s=json.loads(subprocess.check_output(['python3','-I','/home/claude/tools/maxsave.py','2.21.46']).decode())
s['tut']={'k':1,'t':1}; s['settings']['story']=False; s['spin']={'d':''}
now=int(time.time()*1000)
s['mail']={'list':[
 {'id':'r-a','k':'r','a':1,'from':'다람이','ti':'아침 편지','t':'안녕!','rw':{'e':10,'c':0,'s':0,'x':[]},'at':now,'got':True},
 {'id':'r-b','k':'r','a':2,'from':'병아리','ti':'저녁 편지','t':'선물이야','rw':{'e':0,'c':50,'s':0,'x':[]},'at':now,'got':False},
 {'id':'d-1','k':'d','a':-1,'from':'개발자','ti':'','t':'고마워요','rw':{'e':0,'c':0,'s':0,'x':[]},'at':now,'got':False}],
 'got':{'d-1':1},'am':time.strftime('%Y-%m-%d'),'pm':time.strftime('%Y-%m-%d')}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']); pg=await b.new_page(viewport={'width':412,'height':860},device_scale_factor=1.5)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.add_init_script("window.__osc=0;const _C=(window.AudioContext);const P=_C.prototype.createOscillator;_C.prototype.createOscillator=function(){window.__osc++;return P.call(this)};")
        await pg.add_init_script("if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.setItem('mc_sweet_merge_cafe_save', %s)}" % json.dumps(json.dumps(s)))
        await pg.goto('http://localhost:8765/'); await pg.wait_for_timeout(3000)
        await pg.evaluate("document.querySelectorAll('.mc-modal').forEach(m=>m.remove())")
        await pg.click('#mc-cafeb'); await pg.wait_for_timeout(2500)
        await pg.evaluate("document.querySelectorAll('.mc-modal').forEach(m=>m.remove())")
        await pg.click('[data-tw="mail"]'); await pg.wait_for_timeout(600)
        await pg.screenshot(path='/tmp/m1.png')
        print('rows before',await pg.locator('.ml-row').count())
        await pg.click('[data-del]'); await pg.wait_for_timeout(600)
        print('rows after',await pg.locator('.ml-row').count(), await pg.locator('.ml-row b').all_text_contents())
        await pg.screenshot(path='/tmp/m2.png')
        await pg.evaluate("document.querySelectorAll('.mc-modal').forEach(m=>m.remove())")
        await pg.click('[data-tw="spin"]'); await pg.wait_for_timeout(600)
        o0=await pg.evaluate('window.__osc')
        await pg.click('.sp-go'); await pg.wait_for_timeout(5000)
        print('oscillators during spin', await pg.evaluate('window.__osc')-o0)
        print('errs',errs[:3]); await b.close()
asyncio.run(main())
