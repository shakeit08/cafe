import sys; sys.path.insert(0,'/home/claude/work/pipeline/walk')
from cut import anchor
from PIL import Image, ImageFilter
import numpy as np
from scipy import ndimage
def cell_cut(rgb,holes=True):
    A=rgb.astype(np.float32)
    corner=np.median(np.concatenate([A[:6,:6].reshape(-1,3),A[:6,-6:].reshape(-1,3),A[-6:,:6].reshape(-1,3),A[-6:,-6:].reshape(-1,3)]),0)
    d=np.sqrt(((A-corner)**2).sum(-1)); bgc=d<22
    lab,n=ndimage.label(bgc)
    edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    bg=np.isin(lab,list(edge))
    sz0=ndimage.sum(bgc,lab,range(1,n+1))
    hmin=250 if holes is True else (holes or 10**9)
    bg|=np.isin(lab,[i+1 for i,s in enumerate(sz0) if s>hmin and (i+1) not in edge])
    fg=~bg; lab2,n2=ndimage.label(fg); sz=ndimage.sum(fg,lab2,range(1,n2+1))
    keep=np.isin(lab2,[i+1 for i,s in enumerate(sz) if s>=0.002*sz.max()])
    al=Image.fromarray((keep*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.7))
    out=Image.fromarray(rgb.astype(np.uint8)).convert('RGBA'); out.putalpha(al); return out
def sheet(fn):
    a=np.array(Image.open(fn).convert('RGB')); H,W=a.shape[:2]; cw,ch=W//3,H//2
    return [cell_cut(a[r*ch+4:(r+1)*ch-4,c*cw+4:(c+1)*cw-4]) for r in range(2) for c in range(3)]
def norm(frames):
    anc=[anchor(f) for f in frames]
    L=max(ax for ax,_ in anc); R=max(f.width-ax for f,(ax,_) in zip(frames,anc)); T=max(b for _,b in anc)
    outs=[]
    for f,(ax,b) in zip(frames,anc):
        c=Image.new('RGBA',(int(L+R),int(T)+4),(0,0,0,0)); c.alpha_composite(f,(int(L-ax),int(T-b))); outs.append(c)
    bb=None
    for c in outs:
        b=c.getbbox(); bb=b if bb is None else (min(bb[0],b[0]),min(bb[1],b[1]),max(bb[2],b[2]),max(bb[3],b[3]))
    return [c.crop(bb) for c in outs]
for k in ['otter','puffin','seal','octopus','albatross','sealion']:
    fr=norm(sheet(f'/home/claude/work/ch6/got/walk_{k}.png'))
    for i,f in enumerate(fr): f.save(f'/home/claude/ch6/cut/walk/{k}_{i}.png')
    print(k,fr[0].size)
