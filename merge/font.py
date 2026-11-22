import base64, subprocess, sys
src=open('main.js').read()+open('art.js').read()
chars=set(c for c in src if 0xAC00<=ord(c)<=0xD7A3)|set(chr(c) for c in range(0x20,0x7f))|set('…·✓×→←‹›♪♥★☆！？～')
open('/home/claude/font/chars.txt','w').write(''.join(sorted(chars)))
subprocess.run(['pyftsubset','/home/claude/font/Jua.ttf','--text-file=/home/claude/font/chars.txt','--flavor=woff2','--output-file=/home/claude/font/jua_sub.woff2','--layout-features=*','--no-hinting'],check=True)
f=base64.b64encode(open('/home/claude/font/jua_sub.woff2','rb').read()).decode()
sys.stdout.write(src[:0]+open('main.js').read().replace('__FONT__',f))
