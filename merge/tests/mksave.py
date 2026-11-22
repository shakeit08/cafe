import re, json, sys
src=open('/home/claude/work/merge/main.js',encoding='utf-8').read()
i=src.index('const AREAS'); j=src.index("{ const pi = AREAS.findIndex",i); seg=src[i:j]
areas=[]; 
for part in seg.split("\n  { k: '")[1:]:
    k=part.split("'")[0]; spots=re.findall(r"sp\('(\w+)'",part) or ['sign','awning','window','door','planter','lamp','terrace','wall']
    areas.append((k,spots))
def save(done_upto, extra=None):
    decor={}; ad={}
    for k,sp in areas:
        if k=='plaza': continue
        if k in done_upto:
            ad[k]=True
            for x in sp: decor[x]=2
    if extra:
        for x,v in extra.items(): decor[x]=v
    seen={k:True for k in ['intro','cafe','flower','ice','park','post','book','station','ch2_start','photo','store','bath','dock','teahouse','tackle','ch3_start','chestnut','mushroom','pie','library','camp','honey','nightcandy','maple','ch4_start','hotteok','knit','cocoa','musichall','skate','cablecar']}
    return {'board':[{'g':'bakery'},None,None,None,None,{'g':'coffee'}]+[None]*57,'level':40,'xp':0,'coins':99999,'energy':100,'eTs':0,'rows':6,'savedAt':9e12,
      'stars':9999,'chains':['bakery','coffee','berry','choco','tea','icecream','candy','fish','pie'],'decor':decor,'areaDone':ad,
      'story':{'intro':True,'seen':seen},'orders':[],'nextId':10,'seenVer':'2.21.1','settings':{'story':True}}
S4=[k for k,_ in areas if k not in ('plaza','parasol','melon','shell','surf','castle','yacht')]
mode=sys.argv[1]
if mode=='new5': s=save(S4)
elif mode=='mid5':
    s=save(S4+['parasol','melon'],{'slwall':2,'slwin':1}); s['story']['seen'].update({'ch5_invite':True,'ch5_start':True,'parasol':True,'melon':True})
    s['street']={f'c5_{k}':v for k,v in zip(['palm','ball','starrock','tower','lounger','hammock','shells','buoy'],[3,3,2,3,2,3,1,2])}
elif mode=='full5':
    s=save(S4+['parasol','melon','shell','surf','castle','yacht']); s['story']['seen'].update({k:True for k in ['ch5_invite','ch5_start','parasol','melon','shell','surf','castle','yacht']})
    s['street']={f'c5_{k}':3 for k in ['palm','ball','starrock','tower','lounger','hammock','shells','buoy','shavedice','lei','path','tiki','coconut','towels','bottle','driftwood','gullpost','pinwheel','trap','shellmail','rose','tidepool','scope','lamp']}
elif mode in ('gate','gate5'):
    import re as _r
    seg=src[src.index('const STREET = {'):src.index('const STEP_NAMES')]
    parts=_r.split(r"\n  (\d): \[|\nSTREET\[(\d)\] = \[", seg)[1:]
    parts=[x for x in parts]
    st={}; last4=None
    trip=[(a or b,c) for a,b,c in zip(parts[0::3],parts[1::3],parts[2::3])]
    for ch,body in trip:
        if ch=='5': continue
        for nm in _r.findall(r"\['(\w+)', '", body):
            st[f'c{ch}_{nm}']=3
            if ch=='4': last4=f'c4_{nm}'
    if mode=='gate': st[last4]=2
    s=save(S4); s['street']=st
s.setdefault('tut',{'k':1,'t':1})
print(json.dumps(s))
