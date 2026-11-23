exec(open('/home/claude/tools/shop6.py').read())
def mask2(A,gap=3,thin=5):
    bar=A.mean(2)<95; bar=ndimage.binary_dilation(bar,iterations=gap)
    lab,n=ndimage.label(~bar); edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    m=~np.isin(lab,list(edge)); m=ndimage.binary_fill_holes(m|ndimage.binary_dilation(m,iterations=gap+1)&bar)
    body=ndimage.binary_opening(m,iterations=thin)
    lab2,n2=ndimage.label(body); sz=ndimage.sum(body,lab2,range(1,n2+1)); body=lab2==(np.argmax(sz)+1)
    m=m&ndimage.binary_dilation(body,iterations=thin+3)
    lab2,n2=ndimage.label(m); sz=ndimage.sum(m,lab2,range(1,n2+1)); m=lab2==(np.argmax(sz)+1)
    return ndimage.binary_fill_holes(m)
def mask3(A,gap=12,thin=5):
    dark=A.mean(2)<95
    bar=ndimage.binary_dilation(dark,iterations=gap)
    lab,n=ndimage.label(~bar); edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    core=~np.isin(lab,list(edge))&~bar
    ext=ndimage.binary_dilation(core,iterations=gap)&~dark
    outl=dark&ndimage.binary_dilation(core,iterations=gap+9)
    m=ndimage.binary_fill_holes(ext|outl)
    body=ndimage.binary_opening(m,iterations=thin)
    lab2,n2=ndimage.label(body); sz=ndimage.sum(body,lab2,range(1,n2+1)); body=lab2==(np.argmax(sz)+1)
    m=m&ndimage.binary_dilation(body,iterations=thin+3)
    lab2,n2=ndimage.label(m); sz=ndimage.sum(m,lab2,range(1,n2+1)); m=lab2==(np.argmax(sz)+1)
    return ndimage.binary_fill_holes(m)
def mask_post(A):
    m=mask2(A,gap=12)
    band=m&~ndimage.binary_erosion(m,iterations=16)
    Ai=A.astype(int); blu=(Ai[...,2]>Ai[...,0]+12)&(Ai.mean(2)>120)
    green=(Ai[...,1]>Ai[...,0]+10)&(Ai[...,1]>Ai[...,2])
    m=m&~(band&(blu|green))
    m=ndimage.binary_opening(m,iterations=1)
    lab2,n2=ndimage.label(m); sz=ndimage.sum(m,lab2,range(1,n2+1)); m=lab2==(np.argmax(sz)+1)
    return ndimage.binary_fill_holes(m)
