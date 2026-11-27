import json,subprocess,re,sys
s=json.loads(subprocess.check_output(['python3','-I','/home/claude/work/merge/tools/ch6/max6.py',sys.argv[1]]).decode())
src=open('/home/claude/work/merge/main.js').read()
a=src[src.index('const AREAS7'):src.index('const STREET_TALK7')]
full=len(sys.argv)<3
for k in re.findall(r"sp\('(\w+)'",a): s['decor'][k]=2 if full else 0
for k in re.findall(r"\{ k: '(\w+)', ch: 7",a):
    if full: s['areaDone'][k]=True
for k in re.findall(r"\['(\w+)', '[^']*', [.\d]+\]",a[a.index('const STREET7'):]): s['street']['c7_'+k]=3 if full else 0
if full: s['stBeat']['7']=99
print(json.dumps(s))
