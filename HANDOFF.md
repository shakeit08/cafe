# 달콤 머지 카페 — 작업 인수인계 (v2.21.48, 2026-11-22)

새 채팅에서는 **GitHub `shakeit08/cafe` 저장소의 `assets-src` 브랜치**를 받으면 바로 이어서 작업할 수 있습니다(웹앱 사이트는 main만 쓰므로 이 브랜치는 사이트에 영향 없음).

```
# add_repo로 shakeit08/cafe 를 access: push 로 붙인 뒤
git clone --branch assets-src --single-branch https://github.com/shakeit08/cafe /home/claude/work
```
브랜치 안: 이 문서, Jua.ttf, `merge/`(코드·빌드 스크립트·그림 데이터 ovr.json/paint.json·이야기 그림·BGM·테스트). 압축 캐시(*_c.json, .cache_c.json)와 빌드 결과(ext/, sweet_merge_cafe.js)는 빠져 있어서 첫 빌드가 조금 오래 걸립니다. 브랜치로 다시 빌드하면 배포본과 똑같은 플러그인이 나오는 것까지 확인했습니다.

작업 자료가 더 필요할 때만 zip으로 따로 받습니다.

| zip | 내용 |
|---|---|
| `3_작업자료.zip` | ch4/, ch3b/, ch3_prompts/, prompts/, pipeline/, res/(아이콘 원본·자르기), intro/(소개글·제목 이미지) — 그림·소개글 작업할 때 |
| `4_5장그림_1.zip`, `5_5장그림_2.zip` | ch5/ 확정 그림·레퍼런스·프롬프트 — 6장 이후 그림 작업할 때 |

`/home/claude/work/`에 풀면 `merge/`와 나란히 `ch5/` 등이 생깁니다. (브랜치를 못 쓸 때의 예비: `1_소스코드.zip` + `2_그림데이터.zip`(merge/ 안에 풀기))

소스를 고쳤으면 배포할 때 `assets-src` 브랜치에도 같이 커밋해 두기(그래야 다음 채팅이 최신 소스를 받음).

## 0. 작업 규칙 (사용자가 정한 것)

- 존댓말로 말하기. 생각은 영어로 해도 되고, 보고는 쉬운 한국어로(영어 용어 남발 금지 — "한글로 설명하라"고 화낸 적 있음).
- 요청한 것만 바꾸기. 요청 안 한 구조·크기·문구는 건드리지 않기. 시키지 않은 기능 넣지 않기(예전에 생산기에서 주스·금화 나오게 했다가 크게 혼남).
- 요청하지 않은 안내·고지 문구를 결과물에 넣지 않기.
- 사용자가 직접 해야 하는 작업은 단계를 빠뜨리지 말고 처음부터 안내하기.
- 빌드할 때마다 `build.sh`의 `VER=`를 올리기. 단, 사용자가 "버전 업 하지 마"라고 하면 올리지 않음(그 경우 리스는 업데이트 버튼이 안 뜸 → 다음 업데이트 때 같이 전달됨).
- 인게임 업데이트 내역(NOTES)은 "로그 올려"라고 할 때만 추가. 리스 전용 내용은 `...(APP ? [] : [...])`로 웹앱에서 숨김. 큰 업데이트만 쓰기.
- **iOS 확대(줌) 관련 수정(2.21.42/43)은 앞으로 어떤 업데이트 로그에도 언급 금지.**
- **저장소 push는 "업데이트해"라고 할 때만.** 대상도 말한 대로("양쪽", "리스만" 등). 그 전에는 빌드·테스트·디버그 미리보기까지만.
- 미리 보여 달라고 하면 디버그 아티팩트(아래 1절)에만 올리기.
- 웹앱 파일 자체는 요청할 때만 사용자에게 주기.
- 프롬프트는 복사해서 바로 쓸 수 있게 전체 블록으로 주기.
- 스토리: 느릿 할머니의 정체(바다 할미 거북)는 10장에서만 밝히기.
- 인수인계 문서는 사용자가 "채팅 옮긴다"고 할 때만 갱신.

## 1. 배포 상태

| 대상 | 버전 | 위치 |
|---|---|---|
| 리스 플러그인 | 2.21.48 | `shakeit08/risu-plugins` → `sweet_merge_cafe.js`(약 2.37MB) + `sweet_merge_cafe_img/f/*.webp|png`(그림 1,082장) + `sweet_merge_cafe_bgm/*.mp3` + `sweet_merge_cafe_mail.json`(개발자 편지) |
| 웹앱(PWA) | 2.21.48 | `shakeit08/cafe` 루트 → https://shakeit08.github.io/cafe/ (`img/*.bin` 묶음, `story/`, `bgm/`) |
| 디버그(다 깬 저장) | 2.21.48 + 미리보기용 | 아티팩트 slug `63799f4c-ab43-4ea3-a780-a83a1e334d3a` (https://claude.ai/artifact/DHT4HobawKcczwbRJdrPRj) |

- 두 저장소 모두 `add_repo`(access: push)로 붙여서 clone 후 push. 다른 채팅 커밋이 섞이므로 항상 `git pull --rebase` 후 push.
- 커밋 메시지: `달콤 머지 카페 2.21.xx: <요약>` + Co-Authored-By/Claude-Session 줄.
- `sweet_merge_cafe_img/`의 예전 `.bin` 묶음은 지우지 않음(예전 버전 사용자용). 새 파일은 `cp --update=none`으로 추가만.
- push 뒤 `curl https://raw.githubusercontent.com/shakeit08/risu-plugins/main/sweet_merge_cafe.js | head -4`로 버전 확인. GitHub Pages(shakeit08.github.io)는 작업 환경에서 접속이 막혀 있어 raw로 sw.js 확인.

### 리스 플러그인 환경에서 알아낸 것 (중요)
- 리스 v3 플러그인은 `<iframe sandbox="allow-scripts">` 안에서 돔. CSP: `connect-src 'none'; img-src * data: blob:; media-src * data: blob:`.
  - → IndexedDB·localStorage·fetch 전부 막힘. 저장은 `Risuai.pluginStorage`만. 인터넷은 `Risuai.nativeFetch`만(웹 리스는 프록시 하나를 거쳐서 브라우저 캐시가 엉뚱한 응답을 돌려주는 문제 있음).
  - → 그래서 2.21.44부터 마을·이야기 그림과 BGM은 **깃허브 주소를 `<img>`/`<audio>`에 바로 넣는 방식**(raw.githubusercontent, 실패하면 jsDelivr `imgAlt()`로 한 번 더). 브라우저 캐시가 알아서 기억.
- 리스는 `//@version`이 올라가야 업데이트 버튼을 띄움(compareVersions). 리스는 자동 업데이트 안 함 → 제보자가 예전 버전일 수 있음.
- 리스 소스 확인: `git clone --depth 1 https://github.com/kwaroran/RisuAI` (src/ts/plugins/apiV3/factory.ts 등).

## 2. 소스 구조

```
merge/
  main.js        게임 로직 전부 (AREAS, STREET, STORY, TALK, NOTES, 주문, 상점, 앨범, 우편함, 튜토리얼, BGM, 머지 힌트 모션…)
  art.js         CHAINS, GEN, ANIMALS, 장면 그리기(paintScene/propSvg), rectOf, P.twin(창문 두 개 가게)
  ovr.json       그림: 아이템·생산기·이웃·거리 소품·도구·마을 장식·r_en/r_co(주스·금화 6단계)·r_box(선물 상자 3단계)·ui(bolt/coin/star)·tool.mail
  paint.json     가게 장면: base, p{1,2}{소품}, rect, rectW, twin(반대쪽 창문), order, behind, fg, cut
  stdim.json, townbg.json, townbg2.json
  build.sh       플러그인 빌드 → sweet_merge_cafe.js (VER= 여기). MC_EXT=1 MC_EXT_URL=1 → 그림을 ext/f/<sha1 12자리>.webp로 한 장씩
  embed.py       그림 넣기. URL 모드에선 '~이름' 문자열 → art.js 머리의 __mcR()가 IMG_BASE 주소로 바꿈
  compress.py    빌드 때 그림 압축 → *_c.json, .cache_c.json (zip엔 빠져 있음: 첫 빌드가 오래 걸림)
  build_app.sh   웹앱 빌드 → /home/claude/webapp (MC_RAW=1 MC_EXT=1 MC_NO_STORY=1, img/*.bin 묶음 + story/ + bgm/)
  build_debug.sh 디버그 빌드 → /home/claude/webapp_debug (build_app.sh 먼저! game1~3.txt로 나눔, bin은 .bin.webp 이름)
  app_index.html / app_debug.html / app_sw.js / app_manifest.webmanifest   웹앱 껍데기 (sw는 bgm·Range 요청은 안 건드림)
  story/         이야기 일러스트 ev01~ev13.webp + 썸네일 t_ev*.webp + story_script.md
  bgm/           cafe1.0c711031.mp3, cafe2.e5b77f07.mp3 (주방, 번갈아), town1.ee1e87ef.mp3 (마을). 이름의 해시는 sha1 앞 8자리
  tests/         mksave.py, maxsave.py, srv.sh, Playwright 테스트들(아래 5절)
  tools/         ph2.html·blank.html(예전 하네스), cutsrv.py, snowfill.py 등
  sweet_merge_cafe_mail.json   개발자 편지 원본(저장소에 올라가는 것)
```

새 환경 준비(한 번):
```
mkdir -p /home/claude/font && cp /home/claude/work/Jua.ttf /home/claude/font/
pip install --break-system-packages brotli playwright && playwright install chromium
mkdir -p /home/claude/webapp
cp /home/claude/work/merge/tests/{mksave.py,maxsave.py,srv.sh} /home/claude/tools/   # 테스트 스크립트가 이 경로를 씀
```

빌드:
```
cd /home/claude/work/merge
sh build.sh                 # 플러그인 → sweet_merge_cafe.js, 그림 → ext/f/
sh build_app.sh             # 웹앱 → /home/claude/webapp
sh build_debug.sh           # 디버그 → /home/claude/webapp_debug (미리보기 때만)
```
주의: build_app.sh는 /home/claude/webapp을 덮어씀. "미리보기만" 할 때는 webapp을 백업해 두고 디버그 빌드 후 되돌리기(배포본과 섞이지 않게).

배포(지시 있을 때만):
- 플러그인: `cp sweet_merge_cafe.js` + `cp --update=none ext/f/* sweet_merge_cafe_img/f/` + (새 곡이면) `sweet_merge_cafe_bgm/` → commit/push.
- 웹앱: webapp의 `game.js index.html sw.js` + `img/ story/ bgm/`(--update=none) → cafe 저장소 루트 → commit/push.
- 디버그: `publish_files`로 index.html, game1~3.txt(+새 파일) 다시 올림. base_version은 get_artifact/list_files로 확인.

## 3. 게임 현재 내용 (2.21.48)

- **마을:** VILLAGES = 사계절 마을(1~4장: 구름언덕·강가 거리·가을 숲·눈꽃 언덕) / 반짝 바닷가 마을(5장 햇살 모래사장 완성). 앞 마을 거리 꾸미기까지 다 해야 다음 장·마을이 열림(chOpen, stFull). 완성한 마을은 앨범 카드 → 다시 둘러보기(pastView).
- **메뉴:** 9계열 Lv1~10(Lv8~10은 3장 마지막 단풍 산장역 완성 = 4장 열릴 때, hiOpen). 생산기 Lv5 → 그 뒤 Lv8.
- **주문(2.21.46~):** Lv.8 이상은 한 주문에 최대 1개, 18% 확률(ORD_HI=8, ORD_HI_P=.18). 높은 단계 2개 이상 든 옛 주문은 불러올 때 새로 뽑음.
- **에너지·재화:** 에너지 주스(r_en)·금화(r_co) 6단계 합치기, 선물 상자 3단계(레벨업 1단계 / 가게 완성 2단계 / 마을 완성 3단계 / 룰렛·뽑기). 보관함 10칸 시작 → 코인으로 50칸.
- **우편함:** 마을 화면 오른쪽. 아침·저녁 주민 편지(에너지·코인 랜덤), 우체국 소포, 개발자 편지(mail.json). 2.21.46: 읽은 편지 지우기 버튼. 2.21.47: X 버튼 창에 고정.
- **가이드(튜토리얼):** 처음에 버튼 위 말풍선. Lv → 설정 → 가이드 다시 보기.
- **머지 단계 창(openEvoIt):** 생산품·생산기·주스·금화·상자·보따리 설명칸 그림을 누르면 단계 보기. 설명은 주민 이야기식(ITEM_DESC, GEN_DESC…).
- **룰렛:** 칸 지날 때마다 "또로록" 효과음(sfx 'tick').
- **머지 힌트 모션(2.21.47):** 재료를 고르면 같이 합칠 수 있는 것들이 분홍 테두리 + 젤리처럼 살짝 끌려감(pullTo 세기 .06/.075), 5초 가만히 있으면 한 쌍이 서로 당김. 설정에서 켜기/끄기(mhint). 띠용(한쪽 고정) 버전은 사용자가 별로라 취소함.
- **상점 연타 방지(2.21.47):** 에너지 0에서 생산기 연타로 열린 상점은 연타가 0.5초 멈출 때까지 버튼이 안 눌림(오른쪽 위 생산기 자리가 "에너지 +100" 버튼과 겹쳐 코인이 빠지던 제보). 구매 알림 +100으로 수정.
- **창문(2.21.47):** 단풍 산장역(snwin)·타닥 숲속 캠핑장(cpwin)은 창문이 양쪽 → paint.json `twin`으로 반대쪽에도 같은 장식, 크기도 창문에 맞춤.
- **배경 음악(2.21.48):** 주방 2곡 번갈아, 마을 1곡, 곡 끝·화면 전환 때 서서히 겹침. 설정 → 배경 음악 켜기/끄기 + 음량 슬라이더(bgm, bgmV 기본 .5). WebAudio GainNode로 음량(iOS 대응), 오디오는 crossOrigin anonymous. 첫 터치에 재생 시작. 게임 창 닫거나 화면 숨기면 멈춤.
- 이야기: 꿀단 할머니 레시피 수첩 → 바닷가 등대지기 초대장. ev11~13까지 일러스트.

## 4. 남은 일 / 아이디어

- 반짝 바닷가 마을 6~10장(하얀 항구 → 야자수 열대섬 → 물빛 조개 동굴 → 노을 온천 → 별빛 등대섬). 기획은 예전 문서 그대로: 일반 가게는 1회 보상, 장 마지막 건물만 작은 영구 보너스. 이야기 단서 순서는 ch5/ch5_prompts.md 참고, 거북 정체는 10장.
- 메뉴 Lv11~15 이름 계획: prompts/prod_sheets.py NAMES.
- 소개글: 아카 플러그인 소개글(intro/post/), 웹앱 소개글(intro/web/, 제목 0_제목_웹앱.png는 보석 십자수 부록 스티커). 사이트(라이믹스) HTML은 그라데이션·flex·transform·position·svg·details·class/style 태그가 지워짐 → 쓰지 말 것. 아카는 `white-space:nowrap`이 지워지고 U+2060 같은 보이지 않는 문자는 "금지된 문구"로 막힘 → 줄바꿈 막을 땐 `&nbsp;`만.

## 5. 테스트 방법

- 저장 만들기: `python3 -I tests/mksave.py <new5|mid5|full5|gate|gate5>`, `python3 -I tests/maxsave.py <VER>` (다 깬 상태). 둘 다 튜토리얼 끝난 상태로 만듦.
- 웹앱: `cd /home/claude/webapp && python3 -m http.server 8765` (또는 `srv.sh <명령>`) 후 Playwright로 localStorage `mc_sweet_merge_cafe_save`에 저장 넣고 열기.
- 리스 플러그인 진짜 환경 흉내: `tests/sandbox_plugin_test.py <모드> [실패시킬파일|ALL]` — 리스와 같은 sandbox+CSP iframe에 플러그인을 넣고, raw.githubusercontent·jsDelivr 요청을 로컬 ext/f로 돌려줌. IndexedDB가 막히는지, 깨진 그림 수, 예비 주소 전환까지 출력. `sandbox_plugin_bgm_test.py`는 BGM 요청까지.
- 기타: shop_tapthrough_test.py(상점 연타), bgm_test.py(곡 전환·켜기/끄기), mail_spin_test.py(우편 지우기·룰렛 소리), order_test.py(옛 주문 정리). 포트·경로가 하드코딩돼 있으니 열어 보고 맞춰 쓰기.
- 파이썬 http.server는 Range를 지원 안 해서 오디오 되감기 시험은 안 됨('ended' 이벤트로 대신 시험).

## 6. 그림 작업에서 배운 것 (반복 실수 방지)

- 이웃 걷기 시트는 종마다 몸 구조·움직임을 따로. "먼 쪽 다리 살짝 어둡게, (1)·(3)칸 다리 반대" 명시. 흰 동물은 배경 연민트(#dff3ea).
- 창문 소품은 "안쪽만, 테두리 없이, 큼직한 물건 2~3개". 창문이 두 개인 건물은 양쪽 다 덮을 것(twin).
- 간판 글자는 간판 시트 것을 씀. 흰 물체는 누끼 때 속이 비기 쉬움 → tools/snowfill.py. 투명 구멍(하이라이트)은 흰색으로 채우기.
- 기존 캐릭터를 그대로 따라 그리지 않기(느낌만). 펠리컨 같은 새는 특징 문단 따로.
- 버튼 아이콘은 1024×1024, 40px에서도 보이게 큰 모양, 흰 배경, 기존 아이콘을 레퍼런스로.
