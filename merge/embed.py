import json, sys, os, re, base64, hashlib
def pre(v):
    if isinstance(v, str): return 'data:image/webp;base64,' + v if len(v) > 200 and not v.startswith('data:') else v
    if isinstance(v, list): return [pre(x) for x in v]
    if isinstance(v, dict): return {k: pre(x) for k, x in v.items()}
    return v
C = lambda f: (f[:-5] + '_c.json') if os.path.exists(f[:-5] + '_c.json') and not os.environ.get('MC_RAW') else f
L = lambda f: json.load(open(C(f)))
O, P, T1, T2 = L('ovr.json'), L('paint.json'), L('townbg.json'), L('townbg2.json')
EXT = {}

# ---- MC_EXT=1 (리스 플러그인): 마을·가게 그림을 장별 묶음 파일로 빼고 토큰(@번호)으로 바꿔 둠
if os.environ.get('MC_EXT'):
    OUT = os.environ.get('MC_EXT_DIR', 'ext')
    main = open('main.js').read(); art = open('art.js').read()
    area_ch = {k: int(c) for k, c in re.findall(r"k: '(\w+)', ch: (\d+)", main)}
    shop_ch = lambda a: area_ch.get(a, 1)
    walk_ch = {k: shop_ch(a) for k, a in re.findall(r"key: '(\w+)', name: '[^']*', art: [^,]+, ch2: '(\w+)'", art)}
    groups, n = {}, [0]
    # MC_EXT_URL=1: 묶음 파일 대신 그림을 한 장씩 파일로 두고, 주소('~이름')를 바로 씀
    URLMODE = os.environ.get('MC_EXT_URL')
    FDIR = os.path.join(OUT, 'f')
    if URLMODE: os.makedirs(FDIR, exist_ok=True)
    def one(b):
        f = hashlib.sha1(b).hexdigest()[:12] + ('.png' if b[:4] == b'\x89PNG' else '.webp')
        fp = os.path.join(FDIR, f)
        if not os.path.exists(fp): open(fp, 'wb').write(b)
        return '~' + f
    def take(s, g):
        if g == 'common' or not (isinstance(s, str) and len(s) > 200): return s
        b = base64.b64decode(s.split(',')[-1])
        if URLMODE: return one(b)
        n[0] += 1; t = '@%d' % n[0]
        groups.setdefault(g, []).append((t, b))
        return t
    def deep(v, g):
        if isinstance(v, list): return [deep(x, g) for x in v]
        if isinstance(v, dict): return {k: deep(x, g) for k, x in v.items()}
        return take(v, g)
    for a in list(P): P[a] = deep(P[a], 'ch%d' % shop_ch(a))
    O['walk'] = {k: deep(v, 'ch%d' % walk_ch.get(k, 1)) for k, v in O['walk'].items()}
    O['st'] = {k: deep(v, 'ch%s' % (re.match(r'c(\d+)_', k).group(1) if re.match(r'c(\d+)_', k) else 1)) for k, v in O['st'].items()}
    # 마을 화면에서만 쓰는 그림(길·풀·물 무늬, 사계절 카드, 잔해, 룰렛·뽑기·앨범 아이콘)도 묶음 파일로
    O['map'] = {k: deep(v, 'ch%s' % m.group(1) if (m := re.search(r'(\d+)$', k)) else 'town') for k, v in O['map'].items()}
    O['deb'] = deep(O['deb'], 'town')
    if 'wheel' in O: O['wheel'] = deep(O['wheel'], 'town')
    # 안 쓰는 옛 마을 배경은 플러그인에서 뺌
    T1 = {k: ('' if isinstance(v, str) and len(v) > 200 else v) for k, v in T1.items()}
    T2 = {k: ('' if isinstance(v, str) and len(v) > 200 else v) for k, v in T2.items()}
    # 이야기 일러스트 (앨범·이야기 장면)
    O['story'] = {}
    for f in ([] if os.environ.get('MC_NO_STORY') else sorted(os.listdir('story'))):
        if not f.endswith('.webp'): continue
        if URLMODE:
            raw = open(os.path.join('story', f), 'rb').read()
            if re.match(r'ev(1[4-9]|[2-9]\d)\.webp$', f):  # 6장부터: 웹앱은 무손실 원본, 리스 플러그인용은 화질 95 (크기 그대로)
                import io
                from PIL import Image
                bb = io.BytesIO(); Image.open(io.BytesIO(raw)).save(bb, 'WEBP', quality=95, method=6); raw = bb.getvalue()
            O['story'][f[:-5]] = one(raw); continue
        n[0] += 1; t = '@%d' % n[0]
        groups.setdefault('story', []).append((t, open(os.path.join('story', f), 'rb').read()))
        O['story'][f[:-5]] = t
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.endswith('.bin'): os.remove(os.path.join(OUT, f))
    # 웹리스 중계 서버가 큰 응답(약 2MB 이상)을 중간에 끊어서, 600KB 이하 조각으로 나눠 둠
    PART = 600 * 1024
    for g, items in sorted(groups.items()):
        parts, cur, sz = [], [], 0
        for t, b in items:
            if cur and sz + len(b) > PART: parts.append(cur); cur, sz = [], 0
            cur.append((t, b)); sz += len(b)
        if cur: parts.append(cur)
        for pi, part in enumerate(parts, 1):
            idx, off, body = [], 0, b''
            for t, b in part:
                mime = 'image/png' if b[:4] == b'\x89PNG' else 'image/webp'
                idx.append([t, mime, off, len(b)]); off += len(b); body += b
            head = json.dumps(idx, separators=(',', ':')).encode()
            data = b'MCB1' + len(head).to_bytes(4, 'little') + head + body
            name = '%s-%d.%s.bin' % (g, pi, hashlib.sha1(data).hexdigest()[:10])
            open(os.path.join(OUT, name), 'wb').write(data)
            EXT['%s-%d' % (g, pi)] = name
            print('ext', name, len(part), 'imgs', len(data) // 1024, 'KB', file=sys.stderr)

J = lambda d: json.dumps(pre(d), separators=(',', ':'))
HEAD = ''
if os.environ.get('MC_EXT') and os.environ.get('MC_EXT_URL'):
    # '~이름' → 깃허브 주소 (리스 플러그인 안에서는 파일 받기·저장이 막혀 있어도 그림 주소는 바로 띄울 수 있음)
    HEAD = ("const IMG_BASE = globalThis.__MC_IMG_BASE || 'https://raw.githubusercontent.com/shakeit08/risu-plugins/main/sweet_merge_cafe_img/f/';\n"
            "const __mcR = o => { if (typeof o === 'string') return o[0] === '~' ? IMG_BASE + o.slice(1) : o; if (Array.isArray(o)) return o.map(__mcR); if (o && typeof o === 'object') { for (const k in o) o[k] = __mcR(o[k]); } return o; };\n")
    J0 = J; J = lambda d: '__mcR(' + J0(d) + ')'
s = HEAD + open('art.js').read().replace('__OVR__', J(O)).replace('__PAINT__', J(P)).replace('__TOWNBG__', J(T1)).replace('__TOWNBG2__', J(T2)).replace('__STDIM__', open('stdim.json').read()).replace('__EXTFILES__', json.dumps(EXT))
sys.stdout.write(s)
