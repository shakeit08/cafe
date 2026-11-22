import asyncio, json, sys
from playwright.async_api import async_playwright
src = open('sweet_merge_cafe.js').read()
MOCK = """
window.__store = JSON.parse(localStorage.getItem('mock_store')||'{}');
window.__btns=[]; window.__handlers={};
window.Risuai = {
  pluginStorage:{ getItem: async k=>window.__store[k]??null, setItem: async (k,v)=>{if(localStorage.getItem('mock_lock')){localStorage.removeItem('mock_lock');return;} window.__store[k]=v; localStorage.setItem('mock_store', JSON.stringify(window.__store));} },
  getLocalPluginStorage: async()=>({ getItem: async k=>null, setItem: async()=>{} }),
  registerButton: async (o,cb)=>{window.__btns.push(cb); return {id:'x'}},
  registerSetting: async ()=>({id:'y'}),
  addRisuScriptHandler: async (m,f)=>{window.__handlers[m]=f},
  onUnload: async()=>{},
  showContainer: async()=>{document.body.classList.add('shown')},
  hideContainer: async()=>{document.body.classList.remove('shown')},
};
"""
HTML = """<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"></head><body style="margin:0;background:linear-gradient(#334,#556)"><script>"""+MOCK+"""
(async()=>{ """ + src + """ })();
</script></body></html>"""
open('harness.html','w').write(HTML)
