import re,sys
src,ver,outdir=sys.argv[1],sys.argv[2],sys.argv[3]
s=open(src,encoding='utf-8').read()
i=s.index("const VER = '%s';\n"%ver); main=s[i+len("const VER = '%s';\n\n"%ver):]
main=re.sub(r"[A-Za-z0-9+/]{20000,}={0,2}","__FONT__",main,count=1)
a=s.index("const ART = (() => {\n")+len("const ART = (() => {\n"); b=s.index("return { CHAINS, CHAIN_KEYS")
art=s[a:b]
art=art[art.index("\n",art.index("const __mcR"))+1:]
for name,ph in [('OVR_B64','__OVR__'),('PAINT_D','__PAINT__'),('TOWN_BG_D','__TOWNBG__'),('TOWN_BG2_D','__TOWNBG2__'),('ST_DIM','__STDIM__'),('EXT_FILES','__EXTFILES__')]:
    art=re.sub(r"(const %s = )(?:__mcR\()?\{.*?\}\)?;\n"%name, lambda m: m.group(1)+ph+';\n', art, count=1, flags=re.S)
open(outdir+'/main.js','w').write(main); open(outdir+'/art.js','w').write(art)
