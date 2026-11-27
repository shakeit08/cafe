import sys,json,os; sys.path.insert(0,'/home/claude/tools')
from recut import enc
from PIL import Image
C='/home/claude/ch7/cut/'; G='/home/claude/work/ch7/got/'
o=json.load(open('ovr.json')); s=json.load(open('stdim.json'))
W7=['monkey','parrot','hippo','sloth','toucan','frog']
assert len(o['animal'])==38
for k in W7:
    o['walk'][k]=[enc(Image.open(C+f'walk/{k}_{i}.png').convert('RGBA')) for i in range(6)]
    o['animal'].append(enc(Image.open(C+f'face/{k}.png').convert('RGBA')))
    o['animalDot'].append(enc(Image.open(C+f'face/{k}_dot.png').convert('RGBA')))
ST=['palmpot','banana','hibiscus','monstera','bamboobench','tiki','cocopile','pineapple','canoe','chime','fence','swing',
    'bamboolamp','islandsign','flowerarch','perch','fruitcart','bamboofountain','lilypond','shelllamp','conchhorn','mangotree','sandbed','raftbed']
for k in ST:
    ims=[Image.open(C+f'st/c7_{k}_{lv}.png').convert('RGBA') for lv in (0,1)]
    o['st']['c7_'+k]=[enc(im) for im in ims]; s['c7_'+k]=[list(im.size) for im in ims]
ds=[Image.open(C+f'map/d7_{i:02d}.png').convert('RGBA') for i in range(16)]
o['map']['d7']=[enc(im) for im in ds]; s['map']['d7']=[list(im.size) for im in ds]
t=Image.open(G+'map_top7.png').convert('RGBA'); o['map']['top7']=enc(t); s['map']['top7']=list(t.size)
o['map']['grass7']=enc(Image.open(G+'map_tile7.png').convert('RGBA'))
for fn,d in (('ovr.json',o),('stdim.json',s)):
    open(fn+'.tmp','w').write(json.dumps(d)); os.replace(fn+'.tmp',fn)
print(len(o['animal']),len(o['animalDot']))
