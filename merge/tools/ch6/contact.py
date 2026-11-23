import sys,os,glob
from PIL import Image, ImageDraw
src,out=sys.argv[1],sys.argv[2]; cols=int(sys.argv[3]) if len(sys.argv)>3 else 8
fs=sorted(f for f in glob.glob(src+'/*.png'))
tw=200; c=Image.new('RGB',(cols*tw,((len(fs)+cols-1)//cols)*(tw+14)),(190,220,245)); d=ImageDraw.Draw(c)
for i,f in enumerate(fs):
    im=Image.open(f).convert('RGBA'); im.thumbnail((tw-8,tw-8),Image.LANCZOS)
    x,y=(i%cols)*tw,(i//cols)*(tw+14); c.paste(im,(x+4,y+4),im); d.text((x+3,y+tw),os.path.basename(f)[:-4],fill='black')
c.save(out)
