import json,base64,io,sys
import numpy as np
from PIL import Image
from scipy import ndimage
def dec(s): return Image.open(io.BytesIO(base64.b64decode(s.split(',')[-1]))).convert('RGBA')
def snow_holes(im):
    a=np.array(im); al=a[:,:,3]>40
    f=ndimage.binary_fill_holes(al)&~al
    lab,k=ndimage.label(f); res=np.zeros(al.shape,bool); info=[]
    rgb=a[:,:,:3].astype(int); mn=rgb.min(2); bl=(rgb[:,:,2]-rgb[:,:,0])
    for i in range(1,k+1):
        h=lab==i; n=h.sum()
        if n<60: continue
        ring=ndimage.binary_dilation(h,iterations=3)&~h&al
        light=((mn>205)|((mn>170)&(bl>15)))&ring
        fr=light.sum()/max(1,ring.sum())
        info.append((int(n),round(fr,2)))
        if fr>0.42: res|=h
    return res,info
