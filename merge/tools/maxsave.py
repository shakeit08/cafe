import re, json, sys
src=open('main.js',encoding='utf-8').read(); art=open('art.js',encoding='utf-8').read()
VER=sys.argv[1]
i=src.index('const AREAS'); j=src.index("{ const pi = AREAS.findIndex",i); seg=src[i:j]
decor={}; ad={}
for part in seg.split("\n  { k: '")[1:]:
    k=part.split("'")[0]; spots=re.findall(r"sp\('(\w+)'",part) or ['sign','awning','window','door','planter','lamp','terrace','wall']
    ad[k]=True
    for x in spots: decor[x]=2
street={}
a=src.index('const STREET = {'); b=src.index('const STEP_NAMES')
for m in re.finditer(r"(?:^|\n)\s*(?:(\d): \[|STREET\[(\d)\] = \[)(.*?)\]\],?", src[a:b], re.S):
    ch=m.group(1) or m.group(2)
    for k in re.findall(r"\['(\w+)', '[^']*', [.\d]+\]", m.group(3)+']'): street[f'c{ch}_{k}']=3
a=src.index('const STORY = {'); b=src.index('\n};',a)
seen={k:True for k in re.findall(r"\n  (\w+): \[", src[a:b])}
chains=['bakery','coffee','berry','choco','tea','icecream','candy','fish','pie']
ci=art.index('const CHAINS'); cseg=art[ci:art.index('};',ci)]
disc={}
for m in re.finditer(r"(\w+): \{\s*name: '[^']+'.*?items: \[([^\]]+)\]", cseg, re.S): disc[m.group(1)]=list(range(1,len(re.findall(r"'[^']+'",m.group(2)))+1))
board=[None]*63
for n,c in enumerate(chains): board[n if n<7 else 7+(n-7)]={'g':c,'gl':8}
store=[{'tool':'cut','n':99},{'tool':'up','n':99}]+[None]*8
s={'v':1,'savedAt':9e12,'level':60,'xp':0,'coins':999999,'energy':500,'eTs':0,'board':board,'rows':9,'chains':chains,'orders':[],'disc':disc,
   'gdisc':{c:8 for c in chains},'decor':decor,'areaDone':ad,'street':street,'stBeat':{str(c):99 for c in range(1,6)},
   'stars':99999,'snow':9999,'coll':{'xmas':True},'story':{'intro':True,'seen':seen},'settings':{'chatE':3,'sfx':2,'story':True},
   'store':store,'storeN':10,'tools':{'cut':0,'up':0},'seenVer':VER,'nextId':100,'stats':{'merges':0,'orders':0,'made':0}}
print(json.dumps(s,ensure_ascii=False))
