import sys, json, numpy as np
sys.path.insert(0,'/home/claude/tools')
from PIL import Image, ImageFilter
from scipy import ndimage
exec(open('/home/claude/tools/walk6.py').read().split('def norm')[0])  # cell_cut
G='/home/claude/work/ch6/got/'; OUT='/home/claude/ch6/shop/'
def panels(path):
    a=np.array(Image.open(path).convert('RGB')); H,W=a.shape[:2]; h,w=H//2,W//2
    ps=[a[:h,:w],a[:h,w:2*w],a[h:2*h,:w],a[h:2*h,w:2*w]]
    out=[]
    for p in ps:
        ph,pw=p.shape[:2]; tgt=round(pw*3/4); extra=tgt-ph
        if extra>0:
            k=20; strip=p[-k-4:-4]
            ext=np.concatenate([strip[::-1] if j%2==0 else strip for j in range(extra//k+1)],0)[:extra]
            p=np.concatenate([p[:-4],p[-4:-4] if False else p[-4:],ext],0)[:tgt]
        elif extra<0: p=p[:tgt]
        out.append(p)
    return out
def maskimg(A,thr=95):
    bar=A.mean(2)<thr; bar=ndimage.binary_dilation(bar,iterations=1)
    lab,n=ndimage.label(~bar); edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    m=~np.isin(lab,list(edge)); lab2,n2=ndimage.label(m); sz=ndimage.sum(m,lab2,range(1,n2+1)); m=lab2==(np.argmax(sz)+1)
    m=ndimage.binary_fill_holes(m); return ndimage.binary_dilation(m,iterations=1)
def cells(path,cols,rows,cut=True,pad=4,holes=True):
    a=np.array(Image.open(path).convert('RGB')); H,W=a.shape[:2]; cw,ch=W//cols,H//rows; out=[]
    for r in range(rows):
        for c in range(cols):
            cc=a[r*ch+pad:(r+1)*ch-pad,c*cw+pad:(c+1)*cw-pad]
            im=cell_cut(cc,holes) if cut else Image.fromarray(cc).convert('RGBA')
            out.append(im.crop(im.getbbox()))
    return out
def biggest(im):
    a=np.array(im); A=a[...,3]>40; lab,n=ndimage.label(A); sz=ndimage.sum(A,lab,range(1,n+1)); m=lab==(np.argmax(sz)+1)
    m=ndimage.binary_dilation(m,iterations=2); a[...,3]=np.where(m,a[...,3],0); o=Image.fromarray(a,'RGBA'); return o.crop(o.getbbox())
def winpic(path,i):
    # 창문 속 그림: 흰 배경 위 직사각형 그림 → 흰 테두리만 잘라냄
    a=np.array(Image.open(path).convert('RGB')); H,W=a.shape[:2]; cw,ch=W//2,H//2
    c=a[:ch,i*cw:(i+1)*cw].astype(int); nw=(c.min(2)<235)
    lab,n=ndimage.label(nw); sz=ndimage.sum(nw,lab,range(1,n+1)); m=lab==(np.argmax(sz)+1)
    ys,xs=np.where(m); return Image.fromarray(c[ys.min():ys.max()+1,xs.min():xs.max()+1].astype(np.uint8)).convert('RGBA')
SRC={'hpost':'post'}
SEED={'gelato':(292,307),'hpost':(281,330),'market':(384,340),'sail':(394,224),'museum':(366,324),'ferry':(216,334)}
TOL={'market':60,'museum':75}
def opening(k,p,tol=None,cl=1):
    tol=tol or TOL.get(k,40)
    A=p.astype(np.float32); sx,sy=SEED[k]
    c=np.median(A[sy-6:sy+6,sx-6:sx+6].reshape(-1,3),0)
    d=np.sqrt(((A-c)**2).sum(-1)); m=d<tol
    m=ndimage.binary_closing(m,iterations=cl)
    lab,_=ndimage.label(m); m=lab==lab[sy,sx]
    m=ndimage.binary_fill_holes(m); m=ndimage.binary_opening(m,iterations=3)
    lab,_=ndimage.label(m); m=lab==lab[sy,sx]
    return m

def signbox(k,ps,om):
    A=ps[2].astype(np.float32); B=ps[3].astype(np.float32)
    d=np.sqrt(((A-B)**2).sum(-1))>45
    d&=~ndimage.binary_dilation(om,iterations=12)
    d=ndimage.binary_opening(d,iterations=2); d=ndimage.binary_closing(d,iterations=6)
    lab,n=ndimage.label(d); sz=ndimage.sum(d,lab,range(1,n+1)); m=lab==(np.argmax(sz)+1)
    ys,xs=np.where(m); return (xs.min(),ys.min(),xs.max()-xs.min()+1,ys.max()-ys.min()+1)
PRE={'gelato':'gl','hpost':'ps','market':'mk','sail':'sa','museum':'ms','ferry':'fr'}
GK={'gelato':['glcart','gltable','gllemon'],'hpost':['psbox','pscart','psbike'],'market':['mkcrate','mkscale','mkbarrel'],
    'sail':['saspool','saroll','sabask'],'museum':['mslamp','mswheel','mslog'],'ferry':['frpost','frcart','frboard']}
HANG={'gelato','sail'}
def build(k,gx=(None,None,None),gh=.17):
    ps=panels(G+f'base_{SRC.get(k,k)}.png'); ph,pw=ps[0].shape[:2]; S=2; W,H=pw*S,ph*S
    om=opening(k,ps[2]); ys,xs=np.where(om); ob=(xs.min(),ys.min(),xs.max()+1,ys.max()+1)
    wsf=G+('ws_sail_window.png' if k=='sail' else f'ws_{SRC.get(k,k)}.png'); sgf=G+('ws_sail_signonly.png' if k=='sail' else f'ws_{SRC.get(k,k)}.png')
    wins=[winpic(wsf,i) for i in (0,1)]
    sc=cells(sgf,2,2,holes=False); signs=[biggest(sc[2]),biggest(sc[3])]
    grc=cells(G+f'gr_{SRC.get(k,k)}.png',3,2)
    pre=PRE[k]; wk,sk=pre+'win',pre+'sign'; g=GK[k]
    P={'W':W,'H':H,'baseKey':pre+'wall','order':[wk,sk]+g,'ground':list(g),'rect':{},'open':{},'fill':[],'behind':[],'p':{'1':{},'2':{}}}
    # 창문: 구멍 모양대로 잘라 넣음
    mcrop=om[ob[1]:ob[3],ob[0]:ob[2]]
    for lv,wim in zip(('1','2'),wins):
        mm=Image.fromarray((mcrop*255).astype(np.uint8)).resize(wim.size,Image.LANCZOS)
        w2=wim.copy(); w2.putalpha(mm); P['p'][lv][wk]=w2
        P['rect'].setdefault(wk,{})[lv]=[ob[0]*S,ob[1]*S,(ob[2]-ob[0])*S,(ob[3]-ob[1])*S]
    # 간판
    sx,sy,sw,sh=signbox(k,ps,om); s=sw*S/signs[1].width; cx=(sx+sw/2)*S
    for lv,im in zip(('1','2'),signs):
        w,h=im.width*s,im.height*s
        if lv=='1' and w>signs[1].width*s*.85: f=signs[1].width*s*.85/w; w,h=w*f,h*f
        y=sy*S if k in HANG else (sy+sh)*S-h
        P['rect'].setdefault(sk,{})[lv]=[round(cx-w/2,1),round(y,1),round(w,1),round(h,1)]; P['p'][lv][sk]=im
    # 바닥 소품
    bm=maskimg(ps[2]); bys,bxs=np.where(bm); x0,x1,yb=bxs.min(),bxs.max(),bys.max()
    base_y=min(ph-8,yb+.035*ph)*S
    dx=[x0+.02*pw, x1-.02*pw, (x0+x1)/2+.18*(x1-x0)]
    for j,sp in enumerate(g):
        im1,im2=grc[j],grc[j+3]; s=gh*H/im1.height
        cxj=(gx[j] if gx[j] is not None else dx[j]/pw)*W
        for lv,im in (('1',im1),('2',im2)):
            w,h=im.width*s,im.height*s
            P['rect'].setdefault(sp,{})[lv]=[round(cxj-w/2,1),round(base_y-h,1),round(w,1),round(h,1)]; P['p'][lv][sp]=im
    P['_bases']=[Image.fromarray(ps[i].astype(np.uint8)) for i in range(3)]
    P['_panels']=ps; P['_bm']=[maskimg(ps[i]) for i in range(3)]
    return P
def preview(P,lv):
    W,H=P['W'],P['H']; c=P['_bases'][2 if lv else 0].resize((W,H),Image.LANCZOS).convert('RGBA')
    if lv:
        for sp in P['order']:
            x,y,w,h=P['rect'][sp][str(lv)]; im=P['p'][str(lv)][sp].resize((max(1,round(w)),max(1,round(h))),Image.LANCZOS)
            c.alpha_composite(im,(round(x),round(y)))
    return c.resize((W//3,H//3),Image.LANCZOS)

GX={'gelato':(.14,.86,.55),'hpost':(.15,.86,.29),'market':(.12,.88,.62),'sail':(.14,.86,.62),'museum':(.09,.91,.57),'ferry':(.1,.9,.42)}
