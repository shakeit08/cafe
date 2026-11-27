import sys,json,os; sys.path.insert(0,'/home/claude/tools'); sys.path.insert(0,'/home/claude/work/pipeline/walk')
import numpy as np
from PIL import Image
from scipy import ndimage
from cut import anchor
exec(open('/home/claude/tools/gridcut.py').read())
G='/home/claude/work/ch7/got/'; O='/home/claude/ch7/cut/'
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
W7=['monkey','parrot','hippo','sloth','toucan','frog']
for k in W7:
    g=gridcut(G+f'walk_{k}.png',3,2)
    assert len(g)==6,(k,len(g))
    fr=norm([g[(r,c)] for r in range(2) for c in range(3)])
    for i,f in enumerate(fr): f.save(O+f'walk/{k}_{i}.png')
    print(k,fr[0].size)
def sq(im):
    s=max(im.size); c=Image.new('RGBA',(s,s),(0,0,0,0)); c.alpha_composite(im,((s-im.width)//2,(s-im.height)//2)); return c
for fn,suf in (('faces.png',''),('faces_dot.png','_dot')):
    g=gridcut(G+fn,3,2); assert len(g)==6,(fn,len(g))
    for i,k in enumerate(W7): sq(g[(i//3,i%3)]).save(O+f'face/{k}{suf}.png')
ST=[['palmpot','banana','hibiscus','monstera'],['bamboobench','tiki','cocopile','pineapple'],['canoe','chime','fence','swing'],
    ['bamboolamp','islandsign','flowerarch','perch'],['fruitcart','bamboofountain','lilypond','shelllamp'],['conchhorn','mangotree','sandbed','raftbed']]
for i,row in enumerate(ST):
    g=gridcut(G+f'street_6-{i+1}.png',4,2); assert len(g)==8,(i,len(g),sorted(g))
    for j,k in enumerate(row):
        for lv in (0,1): g[(lv,j)].save(O+f'st/c7_{k}_{lv}.png')
g=gridcut(G+'map_deco7.png',4,4); assert len(g)==16,len(g)
for i in range(16): g[(i//4,i%4)].save(O+f'map/d7_{i:02d}.png')
print('ok')
