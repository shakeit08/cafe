import numpy as np
from PIL import Image
from scipy import ndimage
def gridcut(path,cols,rows,thr=10):
    im=Image.open(path).convert('RGBA'); a=np.array(im); A=a[...,3]>thr
    lab,n=ndimage.label(A); H,W=A.shape
    cm=ndimage.center_of_mass(A,lab,range(1,n+1)); sz=ndimage.sum(A,lab,range(1,n+1))
    cells={}
    for i,((y,x),s) in enumerate(zip(cm,sz),1):
        if s<30: continue
        c=min(cols-1,int(x*cols/W)); r=min(rows-1,int(y*rows/H)); cells.setdefault((r,c),[]).append(i)
    out={}
    for (r,c),ids in cells.items():
        m=np.isin(lab,ids); ys,xs=np.where(m)
        crop=a[ys.min():ys.max()+1,xs.min():xs.max()+1].copy()
        crop[...,3]=np.where(m[ys.min():ys.max()+1,xs.min():xs.max()+1],crop[...,3],0)
        out[(r,c)]=Image.fromarray(crop,'RGBA')
    return out
