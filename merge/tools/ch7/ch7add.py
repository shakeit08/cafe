import sys,os,json; sys.path.insert(0,'/home/claude/tools')
exec(open('/home/claude/tools/ch7shop.py').read().split("if __name__")[0])
from recut import enc
def F(v): return float(v) if isinstance(v,(np.floating,np.integer)) else v
def boxes(rects,W):
    K=W/320; out={}
    for sp,lv in rects.items():
        xs=[r[0] for r in lv.values()]; ys=[r[1] for r in lv.values()]; xe=[r[0]+r[2] for r in lv.values()]; ye=[r[1]+r[3] for r in lv.values()]
        x0,y0,x1,y1=min(xs),min(ys),max(xe),max(ye); s=max(x1-x0,y1-y0)*1.12; cx=(x0+x1)/2; cy=(y0+y1)/2
        out[sp]=' '.join(f'{v/K:.1f}' for v in (cx-s/2,cy-s/2,s,s))
    return out
PJ=json.load(open('paint.json'))
for k in SEED:
    P=build(k,GX[k]); W,H=P['W'],P['H']; S=2
    E={kk:P[kk] for kk in ('W','H','baseKey','order','ground','open','fill','behind')}
    E['rect']={sp:{lv:[F(v) for v in r] for lv,r in d.items()} for sp,d in P['rect'].items()}
    E['box']=boxes(E['rect'],W); E['box'][P['baseKey']]='0 0 320 240'
    E['base']=[enc(b.convert('RGBA')) for b in P['_bases']]
    E['p']={lv:{sp:enc(im) for sp,im in d.items()} for lv,d in P['p'].items()}
    cuts=[]
    for i in range(3):
        m=P['_bm'][i]; rgba=P['_bases'][i].convert('RGBA')
        rgba.putalpha(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.6)))
        bb=rgba.getbbox(); c=rgba.crop(bb)
        cuts.append({'u':enc(c),'x':bb[0]*S,'y':bb[1]*S,'w':(bb[2]-bb[0])*S,'h':(bb[3]-bb[1])*S})
    E['cut']=cuts
    xs=[c['x'] for c in cuts]; ys=[c['y'] for c in cuts]; xe=[c['x']+c['w'] for c in cuts]; ye=[c['y']+c['h'] for c in cuts]
    for sp,lv in E['rect'].items():
        for r in lv.values(): xs.append(r[0]); ys.append(r[1]); xe.append(r[0]+r[2]); ye.append(r[1]+r[3])
    E['lot']=[F(min(xs)),F(min(ys)),F(max(xe)-min(xs)),F(max(ye)-min(ys))]; E['gy']=F(max(c['y']+c['h'] for c in cuts))
    PJ[k]=E; print(k,flush=True)
s=json.dumps(PJ); open('paint.json.tmp','w').write(s); os.replace('paint.json.tmp','paint.json'); print('saved')
