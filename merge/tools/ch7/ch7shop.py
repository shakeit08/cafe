import sys,os,json; sys.path.insert(0,'/home/claude/tools')
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
src=open('/home/claude/tools/shop6.py').read()
exec(src.split("SRC={'hpost'")[0])   # panels, maskimg, cells, biggest, winpic(old)
exec(src[src.index('def opening'):src.index("PRE={")])  # opening, signbox
exec(open('/home/claude/tools/gridcut.py').read())
G='/home/claude/work/ch7/got/'
SRC={}
SEED={'coconut':(310,274),'lei':(320,288),'mango':(340,308),'hammock':(380,288),'radio':(320,318),'raft':(225,298)}
TOL={'radio':14}
SIGNBOX={'mango':(247,176,212,58),'hammock':(522,198,200,127),'radio':(222,171,235,57)}
PRE={'coconut':'cc','lei':'le','mango':'mg','hammock':'hm','radio':'rd','raft':'rf'}
GK={'coconut':['cccart','cctable','ccpalm'],'lei':['lebask','lestand','leperch'],'mango':['mgshaver','mgcrate','mgstool'],
    'hammock':['hmstand','hmpillow','hmlamp'],'radio':['rdspeaker','rdconch','rdcrate'],'raft':['rfpaddle','rfbarrel','rfscope']}
HANG={'coconut','lei','hammock','raft'}
GX={k:(.13,.87,.58) for k in SEED}
_panels=panels
def _trimpanels(path):
    a=np.array(Image.open(path).convert('RGB')); H,W=a.shape[:2]; h,w=H//2,W//2
    out=[]
    for (y0,y1) in ((0,h),(h,2*h)):
        for c in (0,1):
            p=a[y0:y1,c*w:(c+1)*w]
            n=0
            while n<12:
                r=p[-1-n].astype(int); bl=((r[:,2]-r[:,0])>40).mean()
                if bl>.3 or r.mean()<120: n+=1
                else: break
            if n: p=p[:len(p)-n]
            ph,pw=p.shape[:2]; tgt=round(pw*3/4); extra=tgt-ph
            if extra>0:
                k=20; strip=p[-k-1:-1]
                ext=np.concatenate([strip[::-1] if j%2==0 else strip for j in range(extra//k+1)],0)[:extra]
                p=np.concatenate([p,ext],0)[:tgt]
            else: p=p[:tgt]
            out.append(p)
    return out
def _edgefix(ps):
    out=[]
    for p in ps:
        p=p.copy()
        for x in range(3):
            if np.abs(p[:,x].astype(int)-p[:,4].astype(int)).mean()>15: p[:,x]=p[:,4]
            if np.abs(p[:,-1-x].astype(int)-p[:,-5].astype(int)).mean()>15: p[:,-1-x]=p[:,-5]
        out.append(p)
    return out
def _pavefix(ps):
    from skimage import color
    ref=_edgefix(_trimpanels(G+'base_lei.png'))[2]
    R=color.rgb2lab(ref[470:].astype(np.float64)/255).reshape(-1,3); rm,rs=R.mean(0),R.std(0)
    out=[]
    for p in ps:
        L=color.rgb2lab(p.astype(np.float64)/255); h=p.shape[0]
        Z=L[470:].reshape(-1,3); zm,zs=Z.mean(0),Z.std(0)
        T=(L-zm)/(zs+1e-6)*rs+rm
        w=np.clip((np.arange(h)-452)/12,0,1)[:,None,None]
        M=L*(1-w)+T*w
        q=(np.clip(color.lab2rgb(M),0,1)*255).round().astype(np.uint8)
        out.append(q)
    return out
def panels(path):
    ps=_edgefix(_panels7(path))
    return _pavefix(ps) if 'base_coconut' in path else ps
def _panels7(path):
    if 'base_coconut' not in path: return _trimpanels(path)
    a=np.array(Image.open(path).convert('RGB')); H,W=a.shape[:2]; w=W//2
    rows=[(0,504),(512,1017)]
    import tempfile
    out=[]
    for (y0,y1) in rows:
        for c in (0,1):
            p=a[y0:y1,c*w:(c+1)*w]; ph,pw=p.shape[:2]; tgt=round(pw*3/4); extra=tgt-ph
            if extra>0:
                k=20; strip=p[-k-1:-1]
                ext=np.concatenate([strip[::-1] if j%2==0 else strip for j in range(extra//k+1)],0)[:extra]
                p=np.concatenate([p,ext],0)[:tgt]
            else: p=p[:tgt]
            out.append(p)
    return out
def tcells(path,cols,rows):
    g=gridcut(path,cols,rows); return [g[(r,c)] for r in range(rows) for c in range(cols)]
def build(k,gx,gh=.17):
    ps=panels(G+f'base_{k}.png'); ph,pw=ps[0].shape[:2]; S=2; W,H=pw*S,ph*S
    om=opening(k,ps[2]); ys,xs=np.where(om); ob=(xs.min(),ys.min(),xs.max()+1,ys.max()+1)
    wc=tcells(G+f'ws_{k}.png',2,2); wins=[wc[0],wc[1]]; signs=[biggest(wc[2]),biggest(wc[3])]
    grc=tcells(G+f'gr_{k}.png',3,2)
    pre=PRE[k]; wk,sk=pre+'win',pre+'sign'; g=GK[k]
    P={'W':W,'H':H,'baseKey':pre+'wall','order':[wk,sk]+g,'ground':list(g),'rect':{},'open':{},'fill':[],'behind':[],'p':{'1':{},'2':{}}}
    mcrop=om[ob[1]:ob[3],ob[0]:ob[2]]
    for lv,wim in zip(('1','2'),wins):
        mm=Image.fromarray((mcrop*255).astype(np.uint8)).resize(wim.size,Image.LANCZOS)
        w2=wim.copy(); a=np.minimum(np.array(w2)[...,3],np.array(mm)); w2.putalpha(Image.fromarray(a)); P['p'][lv][wk]=w2
        P['rect'].setdefault(wk,{})[lv]=[ob[0]*S,ob[1]*S,(ob[2]-ob[0])*S,(ob[3]-ob[1])*S]
    sx,sy,sw,sh=SIGNBOX.get(k) or signbox(k,ps,om); s=sw*S/signs[1].width; cx=(sx+sw/2)*S
    for lv,im in zip(('1','2'),signs):
        w,h=im.width*s,im.height*s
        if lv=='1' and w>signs[1].width*s*.85: f=signs[1].width*s*.85/w; w,h=w*f,h*f
        y=sy*S if k in HANG else (sy+sh)*S-h
        P['rect'].setdefault(sk,{})[lv]=[round(cx-w/2,1),round(y,1),round(w,1),round(h,1)]; P['p'][lv][sk]=im
    bm=maskimg(ps[2]); bys,bxs=np.where(bm); x0,x1,yb=bxs.min(),bxs.max(),bys.max()
    base_y=min(ph-8,yb+.035*ph)*S
    for j,sp in enumerate(g):
        im1,im2=grc[j],grc[j+3]; s=gh*H/im1.height; cxj=gx[j]*W
        for lv,im in (('1',im1),('2',im2)):
            w,h=im.width*s,im.height*s
            P['rect'].setdefault(sp,{})[lv]=[round(cxj-w/2,1),round(base_y-h,1),round(w,1),round(h,1)]; P['p'][lv][sp]=im
    P['_bases']=[Image.fromarray(ps[i].astype(np.uint8)) for i in range(3)]; P['_bm']=[maskimg(ps[i]) for i in range(3)]
    P['_sb']=(sx,sy,sw,sh); P['_ob']=ob
    return P
def preview(P,lv):
    W,H=P['W'],P['H']; c=P['_bases'][2 if lv else 0].resize((W,H),Image.LANCZOS).convert('RGBA')
    if lv:
        for sp in P['order']:
            x,y,w,h=P['rect'][sp][str(lv)]; im=P['p'][str(lv)][sp].resize((max(1,round(w)),max(1,round(h))),Image.LANCZOS)
            c.alpha_composite(im,(round(x),round(y)))
    return c.resize((W//3,H//3),Image.LANCZOS)
if __name__=='__main__':
    os.makedirs('/tmp/c7/shop',exist_ok=True)
    for k in (sys.argv[1:] or SEED):
        P=build(k,GX[k]); print(k,P['W'],P['H'],'win',P['_ob'],'sign',P['_sb'])
        a=preview(P,1); b=preview(P,2); c=Image.new('RGBA',(a.width*2,a.height)); c.paste(a,(0,0)); c.paste(b,(a.width,0)); c.save(f'/tmp/c7/shop/{k}.png')
