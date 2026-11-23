# 원본 시트에서 저장된 작은 그림 위치를 찾아 원본 해상도로 다시 자르기
import numpy as np, cv2, io, base64
from PIL import Image
from scipy import ndimage
def dec(s): return Image.open(io.BytesIO(base64.b64decode(s.split(',')[-1]))).convert('RGBA')
def enc(im):
    b=io.BytesIO(); im.save(b,'WEBP',lossless=True,quality=70,method=4,exact=True); return base64.b64encode(b.getvalue()).decode()
_cache={}
def sheet_scaled(path,f):
    k=(path,round(f,4))
    if k not in _cache:
        im=_cache.get((path,'o'))
        if im is None: im=np.array(Image.open(path).convert('RGB')); _cache[(path,'o')]=im
        h,w=im.shape[:2]; _cache[k]=cv2.resize(im,(max(8,round(w*f)),max(8,round(h*f))),interpolation=cv2.INTER_AREA).astype(np.float32)
    return _cache[k]
def score(path,f,T,m3,msum):
    B=sheet_scaled(path,f)
    if T.shape[0]>=B.shape[0] or T.shape[1]>=B.shape[1]: return None
    r=cv2.matchTemplate(B,T,cv2.TM_SQDIFF,mask=m3)/msum
    mn,_,loc,_=cv2.minMaxLoc(r); return mn,loc
def find(S,sheets,fmin=.2,fmax=.8,step=.02):
    A=np.array(S).astype(np.float32); T=A[...,:3].copy(); m=(A[...,3]>220).astype(np.float32); m3=np.dstack([m]*3); msum=m.sum()*3
    best=None
    for p in sheets:
        for f in np.arange(fmin,fmax,step):
            r=score(p,f,T,m3,msum)
            if r and (best is None or r[0]<best[0]): best=(r[0],p,f,r[1])
    sc,p,f0,_=best
    for f in np.arange(f0-step,f0+step,step/10):
        r=score(p,f,T,m3,msum)
        if r and r[0]<best[0]: best=(r[0],p,f,r[1])
    return best
def recut(S,best,band=1.6):
    sc,p,f,(x,y)=best
    O=Image.open(p).convert('RGB'); w,h=S.size
    X,Y,W,H=x/f,y/f,w/f,h/f
    X0,Y0=round(X),round(Y); W1,H1=round(W),round(H)
    C=np.array(O.crop((X0,Y0,X0+W1,Y0+H1))).astype(np.float32)
    # 배경색: 시트 네 귀퉁이
    a=np.array(O); bg=np.median(np.concatenate([a[:8,:8].reshape(-1,3),a[:8,-8:].reshape(-1,3),a[-8:,:8].reshape(-1,3),a[-8:,-8:].reshape(-1,3)]),0)
    Aup=np.array(S.getchannel('A').resize((W1,H1),Image.LANCZOS)).astype(np.float32)/255
    k=1/f; r=max(2,int(round(k*band)))
    core=ndimage.binary_erosion(Aup>.5,iterations=r)
    region=ndimage.binary_dilation(Aup>.05,iterations=r)
    d=np.sqrt(((C-bg)**2).sum(-1)); abg=np.clip((d-10)/30,0,1)
    alpha=np.where(core,1.0,np.where(region,abg,0.0))
    out=np.dstack([C,alpha*255]).clip(0,255).astype(np.uint8)
    return Image.fromarray(out,'RGBA'),(X0,Y0,W1,H1,f,sc)
def find_fast(S,sheets,fmin=.18,fmax=.72):
    # 1차: 절반 크기로 거칠게 → 2차: 고른 시트에서 원래 크기로 정밀
    h=S.resize((max(4,S.width//2),max(4,S.height//2)),Image.LANCZOS)
    A=np.array(h).astype(np.float32); T=A[...,:3].copy(); m=(A[...,3]>220).astype(np.float32); m3=np.dstack([m]*3); msum=m.sum()*3
    best=None
    for p in sheets:
        for f in np.arange(fmin,fmax,.03):
            r=score(p,f/2,T,m3,msum)
            if r and (best is None or r[0]<best[0]): best=(r[0],p,f)
    _,p,f0=best
    return find(S,[p],f0-.04,f0+.04,.01)
