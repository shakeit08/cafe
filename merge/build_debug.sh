#!/bin/sh
# 디버그용 웹앱 (다 깬 저장 상태) -> /home/claude/webapp_debug  (build_app.sh 먼저 실행)
set -e
VER=$(grep '^VER=' build.sh | cut -d= -f2)
O=/home/claude/webapp_debug; A=/home/claude/webapp
rm -rf $O; mkdir -p $O/story
cp $A/story/* $O/story/
mkdir -p $O/bgm && cp bgm/*.mp3 $O/bgm/
# 아티팩트는 .bin을 못 올려서 디버그용만 .webp 이름으로
mkdir -p $O/img && for f in $A/img/*.bin; do cp "$f" "$O/img/$(basename $f).webp"; done
python3 -I - "$VER" "$A/game.js" "$O" <<'PY'
import sys, json, subprocess
ver, gj, out = sys.argv[1], sys.argv[2], sys.argv[3]
src = open(gj, encoding='utf-8').read()
import re as _re
src = _re.sub(r'(\.[0-9a-f]{10}\.bin)"', r'\1.webp"', src)
N = 3; L = len(src); parts = []
for i in range(N):
    fn = f'game{i + 1}.txt'; open(f'{out}/{fn}', 'w', encoding='utf-8').write(src[i * L // N:(i + 1) * L // N]); parts.append(fn)
maxed = subprocess.check_output(['python3', '-I', '/home/claude/work/merge/tools/ch6/max6.py', ver]).decode()
h = open('app_debug.html', encoding='utf-8').read().replace('__MAXED__', maxed.strip()).replace('__PARTS__', json.dumps(parts))
open(f'{out}/index.html', 'w', encoding='utf-8').write(h)
PY
ls -la $O
