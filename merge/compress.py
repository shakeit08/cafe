# re-encode embedded art smaller -> *_c.json (cached)
import json, base64, io, hashlib, os
from multiprocessing import Pool
from PIL import Image
CF='.cache_c.json'
def job(a):
    s, q, aq, tgt = a
    im = Image.open(io.BytesIO(base64.b64decode(s.split(',')[-1]))); im.load()
    if tgt and max(im.size) > tgt:
        k = tgt / max(im.size); im = im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)
    b = io.BytesIO(); kw = dict(quality=q, method=6)
    if im.mode == 'RGBA': kw['alpha_quality'] = aq
    im.save(b, 'WEBP', **kw); n = base64.b64encode(b.getvalue()).decode()
    return n if len(n) < len(s) else s
def main():
    cache = json.load(open(CF)) if os.path.exists(CF) else {}
    jobs = {}
    def want(s, q, aq=70, tgt=0):
        k = hashlib.sha1(f'{q},{aq},{tgt},'.encode() + s.encode()).hexdigest()
        if k not in cache: jobs[k] = (s, q, aq, tgt)
        return k
    P = json.load(open('paint.json')); O = json.load(open('ovr.json'))
    plan = []  # (setter, key)
    for ar, v in P.items():
        sc = 434 * 3 / v['W']
        for i, s in enumerate(v['base']): plan.append((v['base'], i, want(s, 60)))
        for lv, d in v['p'].items():
            for sp, s in d.items():
                if not s: continue
                r = v['rect'][sp][str(lv)] if str(lv) in v['rect'][sp] else v['rect'][sp][int(lv)]
                plan.append((d, sp, want(s, 70, 70, round(max(r[2], r[3]) * sc))))
        for c in v.get('cut', []): plan.append((c, 'u', want(c['u'], 74)))
        for c in v.get('fg', []): plan.append((c, 'u', want(c['u'], 62)))
    def walk(node, q, aq=70):
        if isinstance(node, list):
            for i, s in enumerate(node):
                if isinstance(s, str) and len(s) > 200: plan.append((node, i, want(s, q, aq)))
                else: walk(s, q, aq)
        elif isinstance(node, dict):
            for k, s in node.items():
                if isinstance(s, str) and len(s) > 200: plan.append((node, k, want(s, q, aq)))
                else: walk(s, q, aq)
    QS = {'walk': 66, 'st': 70, 'deb': 70, 'map': 72}
    for k, v in O.items():
        if k == 'map':
            for mk, mv in v.items():
                if mk in ('top1', 'top2', 'top3'): plan.append((v, mk, want(mv, 66)))
                elif mk.startswith('d'): walk(mv, 72)
        else: walk(v, QS.get(k, 76), 75 if k not in QS else 70)
    if jobs:
        with Pool(os.cpu_count()) as pool:
            for k, r in zip(jobs, pool.map(job, list(jobs.values()), chunksize=4)): cache[k] = r
        json.dump(cache, open(CF, 'w'))
    for cont, key, k in plan: cont[key] = cache[k]
    json.dump(P, open('paint_c.json', 'w')); json.dump(O, open('ovr_c.json', 'w'))
    print('paint', os.path.getsize('paint.json') // 1024, '->', os.path.getsize('paint_c.json') // 1024, 'ovr', os.path.getsize('ovr.json') // 1024, '->', os.path.getsize('ovr_c.json') // 1024, 'new jobs', len(jobs))
if __name__ == '__main__': main()
