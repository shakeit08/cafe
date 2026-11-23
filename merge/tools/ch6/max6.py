import json,subprocess,re,sys
s=json.loads(subprocess.check_output(['python3','-I','/home/claude/tools/maxsave.py',sys.argv[1]]).decode())
src=open('/home/claude/work/merge/main.js').read()
a=src[src.index('const AREAS6'):src.index('const STREET_TALK6')]
for k in re.findall(r"sp\('(\w+)'",a): s['decor'][k]=2
for k in re.findall(r"\{ k: '(\w+)', ch: 6",a): s['areaDone'][k]=True
for k in re.findall(r"\['(\w+)', '[^']*', [.\d]+\]",a[a.index('const STREET6'):]): s['street']['c6_'+k]=3
s['stBeat']['6']=99
for c in s['disc']: s['disc'][c]=list(range(1,14))
s['tut']={'k':1,'t':1}; s.setdefault('settings',{})['story']=False
print(json.dumps(s))
