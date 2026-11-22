import asyncio, json, subprocess, os, sys, re, secrets
from playwright.async_api import async_playwright
PLUG=open('/home/claude/work/merge/sweet_merge_cafe.js',encoding='utf-8').read()
FDIR='/home/claude/work/merge/ext/f/'
mode=sys.argv[1] if len(sys.argv)>1 else 'full5'
failraw=set(sys.argv[2].split(',')) if len(sys.argv)>2 and sys.argv[2] else set()
save=subprocess.check_output(['python3','-I','/home/claude/tools/mksave.py',mode]).decode()
s=json.loads(save); s['tut']={'k':1,'t':1}; s['settings']['story']=False
N=secrets.token_hex(8)
CSP=f"connect-src 'none'; script-src 'nonce-{N}' 'wasm-unsafe-eval'; frame-src 'none'; object-src 'none'; style-src * 'unsafe-inline'; default-src 'none'; img-src * data: blob:; font-src * data: blob:; media-src * data: blob:; base-uri 'none';"
mock="""
window.__store={sweet_merge_cafe_save:%s}; window.__btns=[];
window.__idb=(()=>{try{indexedDB.open('x');return 'ok'}catch(e){return 'blocked: '+e.name}})();
window.__ls=(()=>{try{localStorage.getItem('x');return 'ok'}catch(e){return 'blocked: '+e.name}})();
window.Risuai={pluginStorage:{getItem:async k=>window.__store[k]??null,setItem:async(k,v)=>{window.__store[k]=v}},
 getLocalPluginStorage:async()=>({getItem:async()=>null,setItem:async()=>{}}),
 registerButton:async(o,cb)=>{window.__btns.push(cb);return{id:'x'}},registerSetting:async()=>({id:'y'}),
 addRisuScriptHandler:async()=>{},onUnload:async()=>{},showContainer:async()=>{},hideContainer:async()=>{},
 nativeFetch:async()=>({status:403,arrayBuffer:async()=>new ArrayBuffer(0)})};
""" % json.dumps(json.dumps(s))
src=f'<!doctype html><html><head><meta charset=utf-8><meta http-equiv="Content-Security-Policy" content="{CSP}"></head><body style="margin:0"><script nonce="{N}">{mock}</script><script nonce="{N}">(async()=>{{{PLUG}\n}})();</script></body></html>'
outer='<!doctype html><html><body style="margin:0"><iframe id=f style="border:0;width:412px;height:860px"></iframe><script>const f=document.getElementById("f");f.sandbox.add("allow-scripts");f.sandbox.add("allow-modals");f.srcdoc=window.SRC;</script></body></html>'
stats={'raw':0,'cdn':0,'fail':0}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']); pg=await b.new_page(viewport={'width':412,'height':860},device_scale_factor=1.5)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.on('console',lambda c: errs.append('console: '+c.text) if 'fail' in c.text.lower() or 'error' in c.text.lower() else None)
        async def raw(route):
            u=route.request.url; fn=u.rsplit('/',1)[1]
            if fn in failraw or 'ALL' in failraw: stats['fail']+=1; return await route.fulfill(status=404,body='no')
            stats['raw']+=1
            fp=FDIR+fn
            if not os.path.exists(fp): stats['fail']+=1; return await route.fulfill(status=404,body='no')
            await route.fulfill(status=200,body=open(fp,'rb').read(),headers={'content-type':'image/png' if fn.endswith('.png') else 'image/webp','access-control-allow-origin':'*','cache-control':'max-age=300'})
        async def cdn(route):
            fn=route.request.url.rsplit('/',1)[1]; stats['cdn']+=1
            await route.fulfill(status=200,body=open(FDIR+fn,'rb').read(),headers={'content-type':'image/png' if fn.endswith('.png') else 'image/webp'})
        await pg.route('https://raw.githubusercontent.com/**',raw)
        await pg.route('https://cdn.jsdelivr.net/**',cdn)
        async def bg(route):
            fn=route.request.url.rsplit('/',1)[1]; stats['bgm']=stats.get('bgm',0)+1
            await route.fulfill(status=200,body=open('/home/claude/work/merge/bgm/'+fn,'rb').read(),headers={'content-type':'audio/mpeg','access-control-allow-origin':'*'})
        await pg.route('https://raw.githubusercontent.com/shakeit08/risu-plugins/main/sweet_merge_cafe_bgm/**',bg)
        await pg.add_init_script('window.SRC='+json.dumps(src))
        await pg.goto('about:blank'); await pg.set_content(outer); await pg.wait_for_timeout(2500)
        fr=pg.frames[1]
        print('idb:',await fr.evaluate('window.__idb'),'| localStorage:',await fr.evaluate('window.__ls'))
        await fr.evaluate('window.__btns[0]()'); await pg.wait_for_timeout(2000)
        for t in ('확인','닫기'):
            l=fr.get_by_text(t,exact=True)
            if await l.count():
                try: await l.first.click(timeout=800)
                except Exception: pass
        await fr.click('#mc-cafeb'); await pg.wait_for_timeout(5000)
        await pg.screenshot(path='/tmp/sbx/town_%s.png'%mode)
        bad=await fr.evaluate("""()=>{const r=[];document.querySelectorAll('img').forEach(i=>{if(i.complete&&!i.naturalWidth&&i.getAttribute('src'))r.push(i.getAttribute('src').slice(-30))});return {n:document.querySelectorAll('img').length,svgimg:document.querySelectorAll('image').length,bad:r.slice(0,5),badn:r.length}}""")
        print('town imgs',bad)
        await pg.mouse.click(300,500); await pg.wait_for_timeout(1500)
        print('ctx',await fr.evaluate("typeof AudioContext"))
        await fr.click('[data-tw="album"]'); await pg.wait_for_timeout(2500)
        await pg.screenshot(path='/tmp/sbx/album_%s.png'%mode)
        print('stats',stats,'errs',errs[:5])
        await b.close()
asyncio.run(main())
