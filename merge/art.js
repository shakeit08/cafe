// ===================== ART =====================
const O = '#5b3a32';
const svg = (inner, vb = '0 0 64 64') => `<svg viewBox="${vb}" xmlns="http://www.w3.org/2000/svg" stroke-linejoin="round" stroke-linecap="round">${inner}</svg>`;
const p = (d, f) => `<path d="${d}" fill="${f}"/>`;
const po = (d, f = 'none', w = 3) => `<path d="${d}" fill="${f}" stroke="${O}" stroke-width="${w}"/>`;
const sl = (d, c, w = 2.5) => `<path d="${d}" fill="none" stroke="${c}" stroke-width="${w}"/>`;
const e = (cx, cy, rx, ry, f) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${f}"/>`;
const eo = (cx, cy, rx, ry, f = 'none', w = 3) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${f}" stroke="${O}" stroke-width="${w}"/>`;
const g = (t, inner) => `<g transform="${t}">${inner}</g>`;
const lay = (d, base, extras, w = 3) => po(d, base, w) + extras + po(d, 'none', w);
const SH = e(32, 58, 17, 3.2, 'rgba(91,58,50,.16)');

// ---- shared parts ----
const grain = (x, y, r) => g(`translate(${x} ${y}) rotate(${r})`,
  eo(0, 0, 4.6, 7.6, '#f4c45c') + e(1.5, 1.8, 2.6, 5, '#e38b46') + e(-1.6, -2.6, 1.3, 2.2, '#fff3a6') + eo(0, 0, 4.6, 7.6));
const bean = (x, y, s, r, mood = -1) => g(`translate(${x} ${y}) rotate(${r}) scale(${s})`,
  eo(0, 0, 11, 15, '#94603c') + e(3.5, 3.5, 6.5, 10, '#5f3044') + e(-4.5, -6, 2.4, 3.6, '#c99060') + eo(0, 0, 11, 15) +
  (mood < 0 ? po('M0 -13 Q-5 -4 0 0 Q5 4 0 13') : po('M-2 -13 Q-5 -10 -4 -7', 'none', 2.4) + kface(0, 2, .78, mood, true, -r)));
const BD = 'M0 -9 Q11 -12 12 -1 Q11 11 0 16 Q-11 11 -12 -1 Q-11 -12 0 -9 Z';
const berry = (x, y, s, r, mood = -1) => g(`translate(${x} ${y}) rotate(${r}) scale(${s})`,
  lay(BD, '#ff5d73',
    p('M5 -9 Q12 -9 12 -1 Q11 11 0 16 Q9 5 5 -9 Z', '#c93468') + e(-6, -2, 2.4, 4, '#ff9e8e') +
    (mood < 0 ? e(-5, 5, 1, 1.5, '#ffe58a') + e(0, 9, 1, 1.5, '#ffe58a') + e(5, 4, 1, 1.5, '#ffe58a') + e(0, 1, 1, 1.5, '#ffe58a') + e(-7, -3, 1, 1.4, '#ffe58a') + e(6, -4, 1, 1.4, '#ffe58a')
      : e(-3, -6, .9, 1.3, '#ffe58a') + e(4, -6.5, .9, 1.3, '#ffe58a') + e(-6, 9, .9, 1.3, '#ffe58a') + e(5, 9, .9, 1.3, '#ffe58a') + e(0, 12.5, .9, 1.3, '#ffe58a'))) +
  (mood < 0 ? '' : kface(0, 2.5, .62, mood)) +
  po('M0 -8 L-10 -12 L-4 -9 L-7 -16 L0 -11 L7 -16 L4 -9 L10 -12 Z', '#6cc46a', 2.6) + po('M0 -11 L1 -18', 'none', 3));
const face = (x, y, s = 1) => g(`translate(${x} ${y}) scale(${s})`,
  e(-6, 0, 1.9, 2.5, O) + e(6, 0, 1.9, 2.5, O) + e(-5.4, -0.9, .7, .8, '#fff') + e(6.6, -0.9, .7, .8, '#fff') +
  e(-10, 3.5, 2.6, 1.5, 'rgba(255,120,150,.55)') + e(10, 3.5, 2.6, 1.5, 'rgba(255,120,150,.55)') +
  po('M-2.2 2.4 Q0 4.6 2.2 2.4', 'none', 2));
const kface = (x, y, s = 1, mood = 0, dark = false, rot = 0) => {
  const ec = dark ? '#22100d' : O;
  let eyes, mouth;
  if (mood === 0) {
    eyes = e(-5.5, 0, 1.8, 2.3, ec) + e(5.5, 0, 1.8, 2.3, ec) + e(-5, -.9, .65, .75, '#fff') + e(6, -.9, .65, .75, '#fff');
    mouth = `<path d="M-2 2.6 Q0 4.6 2 2.6" fill="none" stroke="${ec}" stroke-width="1.7" stroke-linecap="round"/>`;
  } else if (mood === 1) {
    eyes = e(-5.6, -.2, 2.2, 2.8, ec) + e(5.6, -.2, 2.2, 2.8, ec) + e(-4.9, -1.2, .95, 1, '#fff') + e(6.3, -1.2, .95, 1, '#fff') + e(-6.2, .9, .45, .45, '#fff') + e(5, .9, .45, .45, '#fff');
    mouth = `<path d="M-2.4 2.3 Q0 6 2.4 2.3 Z" fill="#d9475f" stroke="${ec}" stroke-width="1.4" stroke-linejoin="round"/>`;
  } else {
    eyes = `<path d="M-8 1 Q-5.6 -2.6 -3.2 1 M3.2 1 Q5.6 -2.6 8 1" fill="none" stroke="${ec}" stroke-width="1.9" stroke-linecap="round"/>`;
    mouth = `<path d="M-3 2 Q0 7.6 3 2 Z" fill="#d9475f" stroke="${ec}" stroke-width="1.4" stroke-linejoin="round"/>` + e(0, 4.6, 1.3, .8, '#ff9db0');
  }
  const blush = e(-9.6, 3.4, 2.6, 1.5, dark ? 'rgba(255,140,170,.85)' : 'rgba(255,120,150,.6)') + e(9.6, 3.4, 2.6, 1.5, dark ? 'rgba(255,140,170,.85)' : 'rgba(255,120,150,.6)');
  return g(`translate(${x} ${y}) rotate(${rot}) scale(${s})`, blush + eyes + mouth);
};
const spark = (x, y, s = 1, c = '#ffd75a') => g(`translate(${x} ${y}) scale(${s})`, `<path d="M0 -6 Q.9 -.9 6 0 Q.9 .9 0 6 Q-.9 .9 -6 0 Q-.9 -.9 0 -6Z" fill="${c}" stroke="${O}" stroke-width="1.6" stroke-linejoin="round"/>`);
const SPK6 = spark(55, 9, .8) + spark(9, 16, .5, '#fff');
const SPK7 = spark(55, 9, 1) + spark(8, 18, .7, '#fff') + spark(57, 30, .5, '#ffb3c1');
const handle = (d, c) => `<path d="${d}" fill="none" stroke="${O}" stroke-width="9"/><path d="${d}" fill="none" stroke="${c}" stroke-width="3.4"/>`;
const heart = (x, y, s, f) => g(`translate(${x} ${y}) scale(${s})`, po('M0 6 Q-8 1 -8 -3 Q-8 -8 -4 -8 Q-1 -8 0 -5 Q1 -8 4 -8 Q8 -8 8 -3 Q8 1 0 6 Z', f, 2.5));

// ---- chains ----
const CHAINS = {
  bakery: {
    name: '베이커리', gen: '빵 봉투', color: '#f4c45c',
    items: ['밀 이삭', '밀가루', '말랑 반죽', '모닝빵', '식빵', '크루아상', '빵 바구니', '과일 샌드위치', '클럽 샌드위치 탑', '샌드위치 케이크', '프렌치토스트 탑', '크루아상 탑', '브런치 보드'],
  },
  coffee: {
    name: '커피', gen: '원두 봉투', color: '#94603c',
    items: ['커피 원두', '원두 한 줌', '원두 봉투', '에스프레소', '아메리카노', '카페라떼', '크림 프라페', '아인슈페너', '티라미수', '커피 젤리 파르페', '아포가토 세트', '모카 롤케이크', '커피 디저트 트레이'],
  },
  berry: {
    name: '딸기', gen: '딸기 씨앗', color: '#ff5d73',
    items: ['딸기 꽃', '딸기', '딸기 두 알', '딸기 바구니', '딸기잼', '딸기 타르트', '딸기 케이크', '딸기 파르페', '딸기 크레페', '딸기 2단 케이크', '딸기 탕후루 다발', '딸기 밀푀유', '딸기 3단 케이크'],
  },
  choco: {
    name: '초콜릿', gen: '카카오 나무', color: '#7a4630',
    items: ['카카오 열매', '카카오 빈', '초콜릿 조각', '판 초콜릿', '초코칩 쿠키', '초코 컵케이크', '하트 봉봉 상자', '초코 퐁당 케이크', '브라우니 탑', '초콜릿 하우스', '초코 에클레어 탑', '초코 3단 케이크', '초콜릿 정원'],
  },
  tea: {
    name: '꽃차', gen: '허브 다발', color: '#9cc36b',
    items: ['허브 새싹', '캐모마일', '꽃잎 봉투', '꽃무늬 틴', '꽃잎 허브티', '찻주전자 세트', '애프터눈 티', '꽃잎 마카롱 탑', '꽃 티케이크', '꽃 화과자 세트', '꽃 젤리 케이크', '정원 티파티 세트', '꽃 롤케이크'],
  },
  icecream: {
    name: '아이스크림', gen: '와플콘', color: '#ff9fb8',
    items: ['우유병', '생크림', '딸기 스쿱', '콘 아이스크림', '트리플 콘', '선데', '아이스크림 케이크', '바나나 스플릿', '과일 빙수', '파르페 타워', '아이스크림 와플', '아이스크림 3단 케이크', '무지개 콘 꽃다발'],
  },
  candy: {
    name: '사탕', gen: '사탕 봉투', color: '#9fd8b5',
    items: ['각설탕', '알사탕', '막대사탕', '젤리 컵', '솜사탕', '사탕 병', '사탕 꽃다발', '젤리 케이크', '젤리 어항', '사탕 화관', '사탕 열기구', '사탕 회전목마', '사탕 기차'],
  },
  fish: {
    name: '붕어빵', gen: '밀가루 자루', color: '#f4b860',
    items: ['반죽 그릇', '팥앙금', '붕어빵', '붕어빵 봉투', '붕어빵 접시', '붕어빵 바구니', '붕어빵 선물 상자', '딸기 슈크림 붕어빵', '자색 고구마 붕어빵', '말차 팥 붕어빵', '초코 바나나 붕어빵', '미니 붕어빵 꼬치', '붕어빵 파르페'],
  },
  pie: {
    name: '애플파이', gen: '사과나무', color: '#e8574a',
    items: ['빨간 사과', '사과잼', '애플파이', '사과파이 조각', '아이스크림 파이', '파이 바구니', '파이 선물 상자', '타르트 타탱', '사과 크럼블', '사과 장미 타르트', '캐러멜 사과 꼬치', '사과 롤케이크', '3단 파이 탑'],
  },
  xmas: {
    name: '크리스마스', gen: '쿠키 오븐', color: '#d84a4a',
    items: ['진저 반죽', '진저브레드맨', '아이싱 진저맨', '크리스마스 쿠키', '크리스마스 쿠키 틴', '과자 집', '크리스마스 케이크'],
  },
  xmasCocoa: {
    name: '크리스마스 핫초코', gen: '핫초코 디스펜서', color: '#edada8',
    items: ['코코아 가루', '초콜릿 베이스', '우유를 데운 핫초코', '따뜻한 핫초코', '마시멜로 핫초코', '크리스마스 핫초코 두 잔'],
  },
  xmasCandy: {
    name: '크리스마스 캔디케인', gen: '캔디 롤러', color: '#b9dfc6',
    items: ['설탕 시럽', '두 가지 색의 사탕 반죽', '줄무늬 사탕 막대', '캔디케인', '캔디케인 묶음'],
  },
};
const XMAS_CHAINS = ['xmas', 'xmasCocoa', 'xmasCandy'];
const CHAIN_KEYS = Object.keys(CHAINS);

const ART_ITEMS = {
  bakery: [
    // 1 wheat
    SH + po('M30 60 Q31 40 36 8') +
    lay('M31 50 Q17 46 13 31 Q26 36 31 47 Z', '#b5cc5c', p('M31 50 Q22 46 19 38 Q26 42 31 48 Z', '#6f9a4f')) +
    grain(29.8, 36, -32) + grain(38.2, 36, 34) + grain(30.6, 27, -30) + grain(38.8, 27, 34) + grain(31.4, 18, -26) + grain(39.4, 18, 30) + g('translate(35.6 8.5) rotate(6) scale(1.55)', eo(0, 0, 4.6, 6.4, '#f4c45c', 2) + e(1.6, 1.8, 2.4, 3.8, '#e38b46') + e(-1.6, -2.4, 1.2, 1.6, '#fff3a6') + eo(0, 0, 4.6, 6.4, 'none', 2)) ,
    // 2 flour sack
    SH + lay('M17 26 Q13 42 17 54 Q32 59 47 54 Q51 42 47 26 Q32 30 17 26 Z', '#f6ecd9',
      p('M40 28 Q47 27 47 27 Q50 42 46 54 Q40 56 35 56 Q43 42 40 28Z', '#dcbcb2') + p('M20 32 Q18 42 21 50 Q23 42 23 32Z', '#fffdf7')) +
    lay('M20 27 Q24 19 22 13 Q32 16 42 13 Q40 19 44 27 Q32 30 20 27Z', '#f6ecd9', p('M36 15 Q42 13 42 13 Q40 19 44 27 Q40 28 37 28 Q40 20 36 15Z', '#dcbcb2')) +
    eo(27, 12, 4.5, 4, '#fff') + eo(39, 12, 4.5, 4, '#fff') + eo(33, 10, 5.5, 5, '#fff') +
    po('M19 25 Q32 30 45 25 L45 30 Q32 35 19 30 Z', '#ff8fa3', 2.6) + eo(26, 28.5, 4, 3, '#ff8fa3', 2.4) + eo(38, 28.5, 4, 3, '#ff8fa3', 2.4) + eo(32, 30, 2.6, 2.6, '#ff6b81', 2.4) +
    eo(32, 43, 8, 7, '#fff8e8', 2.4) + sl('M32 49 L32 38', '#e38b46') + sl('M32 41 L28 38 M32 44 L28 41 M32 41 L36 38 M32 44 L36 41', '#e38b46', 2),
    // 3 dough in bowl
    SH + lay('M13 38 Q12 21 32 19 Q52 21 51 38 Z', '#f9dfb2', p('M40 22 Q51 27 51 38 L39 38 Q45 30 40 22Z', '#e6ab84') + e(23, 27, 5, 3, '#fff6de')) +
    e(26, 33, 1.3, 1.3, '#e6ab84') + e(34, 30, 1.2, 1.2, '#e6ab84') +
    lay('M8 37 L56 37 Q54 57 32 57 Q10 57 8 37 Z', '#a2dccb', p('M43 37 L56 37 Q54 55 35 57 Q48 49 43 37Z', '#5ea7ad') + p('M13 41 Q15 49 22 53 Q17 47 17 41Z', '#d9f5ea')) +
    po('M6 35 Q32 39 58 35 L57 40 Q32 44 7 40 Z', '#c6efe1', 2.6) + heart(32, 48, .55, '#ff8fa3'),
    // 4 bun
    SH + lay('M10 44 Q10 18 32 17 Q54 18 54 44 Q54 51 32 52 Q10 51 10 44 Z', '#e9a252',
      p('M41 21 Q54 27 54 44 Q54 51 32 52 Q49 42 41 21Z', '#c0603f') + p('M11 44 Q32 49 53 44 Q52 51 32 52 Q12 51 11 44Z', '#f6d29a') + p('M17 31 Q21 22 32 21 Q23 26 21 35Z', '#ffd98e')) +
    g('translate(25 29) rotate(-25)', e(0, 0, 1.4, 2.6, '#fff4dc')) + g('translate(33 26)', e(0, 0, 1.4, 2.6, '#fff4dc')) + g('translate(41 30) rotate(25)', e(0, 0, 1.4, 2.6, '#fff4dc')) + g('translate(29 35) rotate(10)', e(0, 0, 1.4, 2.6, '#fff4dc')) + g('translate(37 35) rotate(-10)', e(0, 0, 1.4, 2.6, '#fff4dc')),
    // 5 bread slice + butter
    SH + lay('M14 55 L14 31 Q7 17 21 13 Q32 8 43 13 Q57 17 50 31 L50 55 Q32 58 14 55 Z', '#d98a45', p('M44 15 Q57 18 50 31 L50 55 Q46 56 43 56 L43 29 Q49 19 44 15Z', '#a94f3c')) +
    `<path d="M19 51 L19 30 Q14 20 24 18 Q32 14 40 18 Q50 20 45 30 L45 51 Q32 53 19 51Z" fill="#fbe6bc" stroke="#c4773f" stroke-width="2"/>` +
    p('M39 32 L44 31 L44 50 Q38 51 34 52 Q41 44 39 32Z', '#f0cb98') +
    g('rotate(-8 32 30)', lay('M24 25 L40 25 L40 35 L24 35 Z', '#ffe27a', p('M34 25 L40 25 L40 35 L34 35Z', '#f2b54a') + p('M26 27 h5 v2 h-5z', '#fff6c4')) + po('M28 35 Q28 40 30.5 40 Q33 40 33 35', '#ffe27a', 2.4)),
    // 6 croissant
    SH + [[11, 44, 5, 7, -55], [53, 44, 5, 7, 55], [19, 37, 7, 10, -35], [45, 37, 7, 10, 35], [32, 33, 9.5, 13.5, 0]].map(([x, y, rx, ry, r]) =>
      g(`translate(${x} ${y}) rotate(${r})`, eo(0, 0, rx, ry, '#eba44e') + e(rx * .15, ry * .38, rx * .75, ry * .45, '#bf5f3a') + e(-rx * .32, -ry * .42, rx * .32, ry * .22, '#ffd57c') + eo(0, 0, rx, ry))).join('') + SPK6,
    // 7 bread basket
    SH + g('rotate(-38 34 22)', lay('M14 22 Q14 16 22 16 L48 16 Q55 16 55 22 Q55 28 48 28 L22 28 Q14 28 14 22 Z', '#e3a052', p('M16 25 Q32 28 53 25 Q52 28 48 28 L22 28 Q17 28 16 25Z', '#b45d3a') + p('M22 18 h18 v2 h-18z', '#ffd98e')) + sl('M27 18 L24 26 M36 18 L33 26 M45 18 L42 26', O, 2.4)) +
    g('translate(20 27) scale(.5) translate(-32 -34)', lay('M10 44 Q10 18 32 17 Q54 18 54 44 Q54 51 32 52 Q10 51 10 44 Z', '#e9a252', p('M41 21 Q54 27 54 44 Q54 51 32 52 Q49 42 41 21Z', '#c0603f') + p('M17 31 Q21 22 32 21 Q23 26 21 35Z', '#ffd98e'), 5)) +
    g('translate(45 29) scale(.42) translate(-32 -36)', [[11, 44, 5, 7, -55], [53, 44, 5, 7, 55], [19, 37, 7, 10, -35], [45, 37, 7, 10, 35], [32, 33, 9.5, 13.5, 0]].map(([x, y, rx, ry, r]) =>
      g(`translate(${x} ${y}) rotate(${r})`, eo(0, 0, rx, ry, '#eba44e', 6) + e(rx * .15, ry * .38, rx * .75, ry * .45, '#bf5f3a') + eo(0, 0, rx, ry, 'none', 6))).join('')) +
    lay('M7 34 L57 34 L51 57 L13 57 Z', '#d99b5b', p('M44 34 L57 34 L51 57 L42 57 Q46 46 44 34Z', '#a8613f')) +
    sl('M10 42 L54 42 M12 49 L52 49', '#a8613f', 2.2) + sl('M20 35 L22 56 M32 35 L32 56 M44 35 L42 56', '#c27f4a', 2) +
    po('M5 31 h54 a2 2 0 0 1 2 2 v3 a2 2 0 0 1 -2 2 h-54 a2 2 0 0 1 -2 -2 v-3 a2 2 0 0 1 2 -2 z', '#ecb878', 2.6) +
    `<path d="M5 34.5 h54" stroke="#ff8fa3" stroke-width="2.4" stroke-dasharray="3 3"/>` + heart(32, 47, .7, '#ff8fa3') + SPK7,
  ],
  coffee: [
    SH + bean(32, 32, 1.25, 25),
    SH + bean(22, 39, .85, -22) + bean(43, 39, .85, 32) + bean(32, 22, .85, 6),
    SH + lay('M15 21 L49 21 L52 57 L12 57 Z', '#dba96d', p('M41 21 L49 21 L52 57 L43 57 Z', '#ac6c4f') + p('M18 25 L22 25 L19 51 L16 51Z', '#f1cf96')) +
    po('M13 14 L51 14 L49 22 L15 22 Z', '#c8925a', 2.6) + po('M25 10 h14 v7 h-14z', '#ff7d93', 2.6) +
    eo(32, 40, 10.5, 10.5, '#fff6e6', 2.5) + bean(32, 40, .45, 20),
    // espresso
    SH + eo(32, 51, 24, 6.5, '#fffdf6') + e(32, 51.5, 17, 3.6, '#d3d8ee') +
    handle('M43 34 Q53 33 52 39 Q51 44 42 43', '#fffdf6') +
    lay('M17 31 L47 31 Q46 49 32 49 Q18 49 17 31 Z', '#fffdf6', p('M39 32 L47 31 Q46 48 33 49 Q43 43 39 32Z', '#cdd3ec') + p('M18.4 37 L45.6 37 L45 40.5 L19 40.5Z', '#ff9db0')) +
    eo(32, 31, 15, 4.2, '#6a3826') + e(29.5, 30.6, 8.5, 2.1, '#c98a52'),
    // americano mug
    SH + `<path d="M24 12 Q20 8 24 3 M32 11 Q28 7 32 2 M40 12 Q36 8 40 3" fill="none" stroke="#d8c7c0" stroke-width="3"/>` +
    handle('M46 26 Q56 26 56 36 Q56 46 46 45', '#ffb6c4') +
    lay('M15 19 L47 19 L47 51 Q47 56 42 56 L20 56 Q15 56 15 51 Z', '#ffb6c4', p('M39 19 L47 19 L47 51 Q47 56 42 56 L36 56 Q42 40 39 19Z', '#d97a9e') + p('M19 24 h4 v26 h-4z', '#ffdbe3')) +
    eo(31, 19, 16, 4.2, '#5b2e22') + heart(31, 38, .75, '#fff'),
    // latte
    SH + eo(32, 52, 26, 6.5, '#fffdf6') + e(32, 52.5, 19, 3.6, '#d3d8ee') +
    handle('M51 30 Q60 30 59 37 Q58 44 48 42', '#a9e4d0') +
    lay('M9 26 L55 26 Q53 51 32 51 Q11 51 9 26 Z', '#a9e4d0', p('M44 27 L55 26 Q53 50 34 51 Q48 42 44 27Z', '#5fa9ab') + p('M14 30 Q16 42 23 47 Q19 40 19 30Z', '#dcf6ec')) +
    eo(32, 26, 22, 7, '#c48b5c') + e(32, 25, 17, 4.6, '#d9a172') + p('M32 31 Q21 24 26.5 20.5 Q30 19 32 22.5 Q34 19 37.5 20.5 Q43 24 32 31Z', '#fff3e0') + SPK6,
    // frappe
    SH + `<path d="M37 24 L47 3" stroke="${O}" stroke-width="8" fill="none"/><path d="M37 24 L47 3" stroke="#ff7d93" stroke-width="3.5" fill="none"/>` +
    po('M17 25 L47 25 L43 58 L21 58 Z', '#eef6ff') +
    p('M19 34 L45 34 L43.2 56.5 L20.8 56.5Z', '#c48b5c') + p('M20.2 45 L43.8 45 L43.2 56.5 L20.8 56.5Z', '#8a5136') +
    sl('M20 34 Q26 38 32 34 Q38 38 44 34', '#7a4630', 2.4) + p('M22 29 L25.5 29 L24 53 L22.4 53Z', 'rgba(255,255,255,.8)') + po('M17 25 L47 25 L43 58 L21 58 Z') +
    lay('M13 27 Q11 19 19 18 Q21 9 32 9 Q43 9 45 18 Q53 19 51 27 Z', '#fffaf3', p('M15 24 Q32 29 50 24 Q51 26 51 27 L13 27 Q13 25 15 24Z', '#f1cfd8') + e(26, 14, 4, 2.4, '#fff')) +
    sl('M18 20 Q22 24 26 19 Q30 24 34 18 Q38 24 42 19 Q45 22 47 21', '#7a4630', 2.4) +
    po('M37 5 Q38 1 42 0', 'none', 2.4) + eo(36, 7, 4.5, 4.3, '#ff5d73', 2.6) + e(34.6, 5.6, 1.3, 1, '#ffb1a8') + SPK7,
  ],
  berry: [
    // flower
    SH + po('M32 44 L32 58') +
    lay('M32 48 Q20 46 13 56 Q26 60 32 50Z', '#6cc46a', p('M32 50 Q24 56 16 56 Q26 59 32 51Z', '#2f8a6b')) +
    lay('M32 48 Q44 46 51 56 Q38 60 32 50Z', '#6cc46a', p('M32 50 Q40 56 48 56 Q38 59 32 51Z', '#2f8a6b')) +
    [-90, -18, 54, 126, 198].map(a => {
      const r = a * Math.PI / 180, x = 32 + Math.cos(r) * 12, y = 29 + Math.sin(r) * 12;
      return g(`translate(${x.toFixed(1)} ${y.toFixed(1)}) rotate(${a + 90})`, eo(0, 0, 9, 9.5, '#fffaf6') + e(0, 4, 6, 4, '#f6cad8') + eo(0, 0, 9, 9.5));
    }).join('') +
    eo(32, 29, 7.5, 7.5, '#ffd75a') + e(34, 31, 4, 4, '#ea9a3f') + e(30, 27, 2, 1.6, '#fff4b0') + eo(32, 29, 7.5, 7.5),
    SH + berry(32, 33, 1.55, 0),
    SH + po('M23 22 Q28 10 33 8 Q37 12 42 19') + berry(23, 37, 1.1, -14) + berry(42, 34, 1.1, 16),
    // punnet
    SH + berry(21, 26, .9, -22) + berry(43, 26, .9, 22) + berry(32, 21, .95, 0) + berry(27, 30, .9, -6) + berry(37, 30, .9, 8) +
    lay('M10 33 L54 33 L49 57 L15 57 Z', '#93d8bd', p('M44 33 L54 33 L49 57 L41 57 Q46 45 44 33Z', '#4d9c96')) +
    sl('M14 37 L22 56 M24 34 L32 56 M36 34 L42 56 M18 56 L28 34 M30 56 L38 34 M41 56 L49 36', '#5fb3a6', 2) +
    po('M8 30 h48 a2 2 0 0 1 2 2 v3 a2 2 0 0 1 -2 2 h-48 a2 2 0 0 1 -2 -2 v-3 a2 2 0 0 1 2 -2 z', '#b7ecd8', 2.6),
    // jam
    SH + lay('M14 27 Q14 22 19 22 L45 22 Q50 22 50 27 L50 50 Q50 57 43 57 L21 57 Q14 57 14 50 Z', '#e8475f',
      p('M41 22 L45 22 Q50 22 50 27 L50 50 Q50 57 43 57 L38 57 Q45 42 41 22Z', '#b92a5c') + p('M18 27 h4 v24 h-4z', 'rgba(255,255,255,.55)')) +
    po('M19 34 h26 a2 2 0 0 1 2 2 v12 a2 2 0 0 1 -2 2 h-26 a2 2 0 0 1 -2 -2 v-12 a2 2 0 0 1 2 -2 z', '#fff6e6', 2.4) + berry(32, 42, .4, 0) +
    lay('M10 18 Q12 9 32 9 Q52 9 54 18 L50 25 Q32 28 14 25 Z', '#ff9db0', sl('M18 11 L16 24 M26 9.6 L25 26 M34 9.4 L34 27 M42 10 L43 26 M49 12 L50 24', 'rgba(255,255,255,.75)', 2.4) + sl('M11 15 Q32 11 53 15 M12 20 Q32 17 52 20', 'rgba(255,255,255,.75)', 2.4)) +
    handle('M14 24 Q32 29 50 24', '#ffd75a'),
    // tart
    SH + lay('M7 36 Q32 43 57 36 L52 51 Q32 57 12 51 Z', '#e8ad62', p('M46 39 L56 37 L52 51 Q46 53 42 54 Q47 47 46 39Z', '#b8673e') + p('M11 40 L15 50 L13 41Z', '#f6cf8c')) +
    sl('M15 41 L17 52 M22 42 L23 54 M29 43 L29 55 M36 43 L35 55 M43 42 L41 54 M50 41 L47 52', '#b8673e', 1.8) +
    po('M7 36 Q32 29 57 36 Q32 43 7 36 Z', '#fff0b5', 2.6) +
    berry(19, 30, .55, -20) + berry(32, 27, .6, 0) + berry(45, 30, .55, 20) + berry(25, 35, .55, -8) + berry(39, 35, .55, 10) +
    e(30, 24, 1.2, .8, '#fff') + e(43, 28, 1, .7, '#fff') + SPK6,
    // cake
    SH + eo(32, 53, 27, 6, '#bfe3f2') + e(32, 53, 20, 3.4, '#9fd0e8') +
    lay('M12 30 L52 30 L52 49 Q32 55 12 49 Z', '#fffaf3',
      p('M12 38 L52 38 L52 44 Q32 48 12 44Z', '#f7d27c') + p('M12 40 L52 40 L52 42.2 Q32 46.2 12 42.2Z', '#ff5d73') + p('M44 30 L52 30 L52 49 Q48 51 44 52Z', 'rgba(220,170,190,.45)')) +
    eo(32, 30, 20, 6, '#fffaf3') + [[15, 31], [23, 34], [32, 35], [41, 34], [49, 31]].map(([x, y]) => eo(x, y, 3.6, 3, '#fffaf3', 2.4)).join('') +
    berry(21, 24, .55, -12) + berry(43, 24, .55, 12) + berry(32, 21, .62, 0) + SPK7,
  ],
  choco: [
    SH + g('rotate(28 32 34)', lay('M32 8 Q48 14 48 34 Q48 54 32 60 Q16 54 16 34 Q16 14 32 8 Z', '#f2a04c',
      p('M38 12 Q48 18 48 34 Q48 54 32 60 Q44 44 38 12Z', '#c4553f') + p('M21 22 Q19 34 22 46 Q24 34 25 22Z', '#ffd480')) +
      sl('M32 11 Q29 34 32 57 M24 14 Q20 34 24 54 M40 14 Q44 34 40 54', '#c4553f', 2) + po('M32 8 L32 2', 'none', 4)),
    SH + lay('M7 31 Q9 57 32 57 Q55 57 57 31 Z', '#f2a04c', p('M44 33 L57 31 Q55 55 34 57 Q49 47 44 33Z', '#c4553f')) +
    eo(32, 31, 25, 7.5, '#fff3e6') +
    [[20, 29, -20], [32, 27, 0], [44, 29, 20], [26, 33, -10], [38, 33, 10]].map(([x, y, r]) => g(`translate(${x} ${y}) rotate(${r})`, eo(0, 0, 5, 3.4, '#8a4f5c', 2.4) + e(-1.5, -1, 1.6, .9, '#c48a90'))).join('') +
    g('translate(52 54) rotate(-25)', eo(0, 0, 5, 3.4, '#8a4f5c', 2.4) + e(-2, -1, 1.7, .9, '#c48a90')),
    SH + lay('M13 20 Q13 15 18 15 L40 15 L44 20 L48 18 L51 24 L50 47 Q50 52 45 52 L18 52 Q13 52 13 47 Z', '#7a4630',
      p('M44 20 L48 18 L51 24 L50 47 Q50 52 45 52 L40 52 Q46 40 44 20Z', '#4e2638') + p('M16 19 h22 v3 h-22z', '#a86b42')) +
    po('M20 23 h10 v10 h-10 z', '#8e5536', 2.2) + po('M34 23 h9 v10 h-9 z', '#8e5536', 2.2) + po('M20 37 h10 v10 h-10 z', '#8e5536', 2.2) + po('M34 37 h9 v10 h-9 z', '#8e5536', 2.2) +
    p('M21 24 h8 v2 h-8z', '#b77a4a') + p('M35 24 h7 v2 h-7z', '#b77a4a') + p('M21 38 h8 v2 h-8z', '#b77a4a') + p('M35 38 h7 v2 h-7z', '#b77a4a') +
    g('translate(53 12) rotate(20)', po('M-3 -2 L3 -3 L4 2 L-2 3 Z', '#7a4630', 2.2)) + g('translate(56 54) rotate(-10)', po('M-3 -2 L3 -3 L3 2 L-2 3 Z', '#4e2638', 2.2)),
    SH + g('rotate(-12 32 34)',
      po('M17 7 h30 a3 3 0 0 1 3 3 v28 h-36 v-28 a3 3 0 0 1 3 -3 z', '#7a4630') +
      [[18, 10], [32, 10], [18, 22], [32, 22]].map(([x, y]) => p(`M${x} ${y} h12 v10 h-12z`, '#8e5536') + p(`M${x} ${y} h12 v2.5 h-12z`, '#b77a4a') + p(`M${x + 9.5} ${y} h2.5 v10 h-2.5z`, '#5e3040')).join('') +
      po('M13 33 L51 33 L51 59 L13 59 Z', '#ff8fa3') + p('M42 33 L51 33 L51 59 L42 59Z', '#d9628e') +
      po('M13 31 L19 35 L25 31 L32 35 L39 31 L45 35 L51 31 L51 37 L13 37 Z', '#e1e8f6', 2.4) + heart(32, 47, .9, '#fff')),
    SH + lay('M32 13 Q50 12 53 30 Q55 48 36 54 Q16 57 11 40 Q8 18 32 13 Z', '#e4a75c', p('M44 17 Q54 24 53 34 Q52 50 36 54 Q50 40 44 17Z', '#b8673e') + p('M18 24 Q15 32 17 38 Q20 30 23 25Z', '#f8cf8a')) +
    [[22, 23, 0], [38, 19, 30], [46, 30, 10], [17, 37, -20], [44, 45, 40], [27, 49, 0]].map(([x, y, r]) => g(`translate(${x} ${y}) rotate(${r})`, po('M-3 -2 L2 -3 L4 1 L0 3.5 L-3.5 1.5 Z', '#5a2f3a', 2))).join(''),
    SH + lay('M16 37 L48 37 L44 58 L20 58 Z', '#ff9fb5', p('M40 37 L48 37 L44 58 L38 58Z', '#d9628e')) + sl('M23 38 L25 57 M30 38 L31 57 M37 38 L37 57 M43 38 L41 57', '#d9628e', 2) + SPK6 +
    lay('M12 39 Q9 31 17 29 Q15 19 25 19 Q27 9 36 11 Q45 13 42 21 Q52 22 50 30 Q56 35 50 41 Q32 45 14 41 Z', '#7a4630',
      p('M42 21 Q52 22 50 30 Q56 35 50 41 Q42 43 36 43 Q50 34 42 21Z', '#4e2638') + p('M20 26 Q24 22 30 22 Q24 25 22 30Z', '#a86b42') + p('M28 15 Q31 13 35 14 Q31 16 30 18Z', '#a86b42')) +
    sl('M16 33 Q30 38 46 31 M20 26 Q30 29 40 24', '#4e2638', 2) +
    p('M18 34 l3 -1 l.6 1.6 l-3 1z', '#ffe58a') + p('M38 35 l3 1 l-.5 1.6 l-3 -1z', '#9fe3c9') + p('M26 27 l2.6 -1.8 l1 1.3 l-2.6 1.8z', '#ff9db0') + p('M41 27 l2.8 .8 l-.5 1.6 l-2.8 -.8z', '#fff') + p('M31 33 l.5 -3 l1.7 .3 l-.5 3z', '#ffe58a') +
    po('M35 8 Q36 3 40 2', 'none', 2.4) + eo(34, 10, 4.3, 4.1, '#ff5d73', 2.6) + e(32.8, 8.8, 1.2, .9, '#ffb1a8'),
    // heart bonbon box
    SH + p('M32 59 Q8 45 8 29 Q8 15 20 15 Q28 15 32 23 Q36 15 44 15 Q56 15 56 29 Q56 45 32 59 Z', '#a52a55') + po('M32 59 Q8 45 8 29 Q8 15 20 15 Q28 15 32 23 Q36 15 44 15 Q56 15 56 29 Q56 45 32 59 Z') +
    lay('M32 54 Q8 40 8 25 Q8 11 20 11 Q28 11 32 19 Q36 11 44 11 Q56 11 56 25 Q56 40 32 54 Z', '#ff6b8a',
      p('M44 13 Q56 13 56 25 Q56 40 32 54 Q50 36 44 13Z', '#c8336b') + p('M14 20 Q15 15 20 14 Q16 18 17 24Z', '#ffb3c1')) +
    handle('M13 37 Q30 26 50 15', '#ffd75a') +
    g('translate(22 20)', eo(-6, -2, 6, 4, '#ffd75a', 2.6) + eo(6, 2, 6, 4, '#ffd75a', 2.6) + eo(0, 0, 3, 3, '#f2b03a', 2.6)) + SPK7,
  ],
};

const ART_GENS = {
  bakery: SH +
    po('M12 54 l0 4 h6 v-4 M46 54 l0 4 h6 v-4', '#8f6a5e', 2.6) +
    lay('M10 20 h44 a5 5 0 0 1 5 5 v26 a5 5 0 0 1 -5 5 h-44 a5 5 0 0 1 -5 -5 v-26 a5 5 0 0 1 5 -5 z', '#ffb98c',
      p('M48 20 h6 a5 5 0 0 1 5 5 v26 a5 5 0 0 1 -5 5 h-8 Q50 40 48 20Z', '#e07a6a') + p('M9 24 h3 v28 h-3z', '#ffd9bf')) +
    po('M13 36 h38 a2 2 0 0 1 2 2 v12 a2 2 0 0 1 -2 2 h-38 a2 2 0 0 1 -2 -2 v-12 a2 2 0 0 1 2 -2 z', '#ffcf6a', 2.6) + p('M40 38 h11 v12 h-15 Q42 44 40 38Z', '#ff9a5a') +
    po('M22 49 Q22 42 32 42 Q42 42 42 49 Z', '#e9a252', 2.4) +
    eo(15, 27.5, 3, 3, '#fff6e6', 2.4) + eo(49, 27.5, 3, 3, '#fff6e6', 2.4) + face(32, 27.5, .8) +
    lay('M21 21 L21 15 Q14 15 15 9 Q16 3 23 4.5 Q26 -.5 32 2 Q38 -.5 41 4.5 Q48 3 49 9 Q50 15 43 15 L43 21 Z', '#fff', p('M38 4 Q48 3 49 9 Q50 15 43 15 L43 21 L38 21 Q44 12 38 4Z', '#dfe3f3')),
  coffee: SH +
    po('M8 52 h48 a2 2 0 0 1 2 2 v3 a2 2 0 0 1 -2 2 h-48 a2 2 0 0 1 -2 -2 v-3 a2 2 0 0 1 2 -2 z', '#8f6a5e', 2.6) +
    lay('M14 6 h36 a4 4 0 0 1 4 4 v42 h-44 v-42 a4 4 0 0 1 4 -4 z', '#ffb3c4',
      p('M44 6 h6 a4 4 0 0 1 4 4 v42 h-8 Q48 30 44 6Z', '#d9779c') + p('M13 10 h3 v40 h-3z', '#ffdbe3')) +
    po('M10 4 h44 v7 h-44 z', '#fff6e6', 2.6) + face(32, 19, .85) +
    po('M21 28 h22 v5 h-22 z', '#cfd6ea', 2.6) + po('M24 33 h16 l-2 4 h-12 z', '#9aa3c4', 2.4) + po('M24 34.5 L12 35', 'none', 4) +
    po('M18 38 h28 v14 h-28 z', '#7a5a50', 2.4) +
    handle('M37 45 Q42 45 41 48 Q40 51 36 50.5', '#fff') + po('M25 42 L39 42 Q38.5 52 32 52 Q25.5 52 25 42Z', '#fff', 2.6) + e(32, 42.5, 6, 1.2, '#6a3826'),
  berry: SH +
    lay('M32 36 Q18 30 10 16 Q24 14 32 32 Z', '#6cc46a', p('M32 36 Q22 30 14 18 Q24 24 32 34Z', '#2f8a6b')) +
    lay('M32 36 Q46 30 54 16 Q40 14 32 32 Z', '#6cc46a', p('M32 36 Q42 30 50 18 Q40 24 32 34Z', '#2f8a6b')) +
    lay('M32 37 Q24 22 32 6 Q40 22 32 37 Z', '#7fd47a', p('M32 37 Q38 22 32 8 Q41 22 32 37Z', '#3f9a74')) +
    po('M20 32 Q16 36 15 40') + berry(14, 44, .55, 10) + po('M44 32 Q49 36 50 40') + berry(50, 44, .55, -10) +
    g('translate(43 17) scale(.42)', [-90, -18, 54, 126, 198].map(a => { const r = a * Math.PI / 180; return eo(Math.cos(r) * 10, Math.sin(r) * 10, 8, 8, '#fffaf6', 4); }).join('') + eo(0, 0, 6, 6, '#ffd75a', 4)) +
    lay('M15 38 L49 38 L45 58 L19 58 Z', '#e98a5a', p('M40 38 L49 38 L45 58 L38 58 Q42 48 40 38Z', '#b85a48')) +
    po('M12 34 h40 a2 2 0 0 1 2 2 v3 a2 2 0 0 1 -2 2 h-40 a2 2 0 0 1 -2 -2 v-3 a2 2 0 0 1 2 -2 z', '#f5a77c', 2.6) + face(32, 48, .8),
  choco: SH +
    po('M29 40 L29 24 L35 24 L35 40 Z', '#a5683e') + po('M32 30 L40 24', 'none', 3) +
    lay('M10 24 Q6 12 18 10 Q22 2 33 3 Q44 2 47 10 Q59 12 55 24 Q51 31 32 30 Q13 31 10 24 Z', '#7fcf7a',
      p('M44 8 Q58 12 55 24 Q51 31 32 30 Q52 22 44 8Z', '#3f9a74') + p('M16 14 Q20 8 28 8 Q20 12 19 18Z', '#c4ec8a')) +
    g('translate(19 23) rotate(15)', eo(0, 0, 4, 6, '#f2a04c', 2.6) + e(1.4, 1.5, 2, 3.5, '#c4553f') + eo(0, 0, 4, 6, 'none', 2.6)) +
    g('translate(44 24) rotate(-15)', eo(0, 0, 4, 6, '#f2a04c', 2.6) + e(1.4, 1.5, 2, 3.5, '#c4553f') + eo(0, 0, 4, 6, 'none', 2.6)) +
    g('translate(32 16) rotate(5)', eo(0, 0, 3.5, 5, '#ffd480', 2.6)) +
    lay('M15 40 L49 40 L45 58 L19 58 Z', '#9cc9ef', p('M40 40 L49 40 L45 58 L38 58 Q42 48 40 40Z', '#5f86c4')) +
    po('M12 36 h40 a2 2 0 0 1 2 2 v3 a2 2 0 0 1 -2 2 h-40 a2 2 0 0 1 -2 -2 v-3 a2 2 0 0 1 2 -2 z', '#c4e0f7', 2.6) + face(32, 49.5, .8),
};

const ANIMALS = [
  { key: 'bear', name: '보리', art: eo(14, 18, 8, 8, '#c88a5a') + e(14, 18, 4, 4, '#f3c9a6') + eo(50, 18, 8, 8, '#c88a5a') + e(50, 18, 4, 4, '#f3c9a6') +
    lay('M32 15 Q54 15 54 36 Q54 57 32 57 Q10 57 10 36 Q10 15 32 15 Z', '#c88a5a', p('M44 18 Q54 24 54 36 Q54 57 32 57 Q52 44 44 18Z', '#9a5a46')) +
    eo(32, 44, 9, 7, '#f5dcbc', 2.6) + e(32, 41, 3, 2.2, O) + face(32, 35, .95) },
  { key: 'rabbit', name: '솜이', art: lay('M18 24 Q12 2 20 1 Q28 2 27 21 Z', '#fffaf6', p('M20 20 Q16 6 20 5 Q24 6 24 19Z', '#ffc2cf')) + lay('M46 24 Q52 2 44 1 Q36 2 37 21 Z', '#fffaf6', p('M44 20 Q48 6 44 5 Q40 6 40 19Z', '#ffc2cf')) +
    lay('M32 18 Q54 18 54 38 Q54 58 32 58 Q10 58 10 38 Q10 18 32 18 Z', '#fffaf6', p('M44 21 Q54 26 54 38 Q54 58 32 58 Q52 46 44 21Z', '#ead4de')) +
    face(32, 38, .95) + e(32, 42, 2.2, 1.6, '#ff8fa3') },
  { key: 'cat', name: '치즈', art: lay('M11 30 L13 6 L29 19 Z', '#ffc985', p('M15 24 L16 12 L24 19Z', '#ffb0a0')) + lay('M53 30 L51 6 L35 19 Z', '#ffc985', p('M49 24 L48 12 L40 19Z', '#ffb0a0')) +
    lay('M32 16 Q55 16 55 37 Q55 57 32 57 Q9 57 9 37 Q9 16 32 16 Z', '#ffc985', p('M45 19 Q55 25 55 37 Q55 57 32 57 Q53 44 45 19Z', '#e8955f')) +
    sl('M32 18 L32 25 M25 19 L27 25 M39 19 L37 25', '#e8955f', 3) + face(32, 37, .95) + e(32, 41, 2, 1.4, '#ff8fa3') +
    sl('M8 40 L17 41 M8 45 L17 44 M56 40 L47 41 M56 45 L47 44', O, 1.6) },
  { key: 'dog', name: '콩떡', art: lay('M32 15 Q54 15 54 36 Q54 57 32 57 Q10 57 10 36 Q10 15 32 15 Z', '#f7e4c4', p('M44 18 Q54 24 54 36 Q54 57 32 57 Q52 44 44 18Z', '#dbb48f') + e(23, 32, 7, 6, '#e8c49a')) +
    lay('M14 18 Q2 22 5 40 Q11 46 17 34 Z', '#a5683e', p('M8 30 Q8 40 11 42 Q9 34 12 28Z', '#7a4630')) + lay('M50 18 Q62 22 59 40 Q53 46 47 34 Z', '#a5683e', p('M56 30 Q56 40 53 42 Q55 34 52 28Z', '#7a4630')) +
    eo(32, 44, 9, 7, '#fff6e6', 2.6) + e(32, 40.5, 3.4, 2.4, O) + face(32, 34, .95) + po('M30 47 Q32 52 34 47', '#ff8fa3', 2) },
  { key: 'hamster', name: '쿠키', art: eo(15, 20, 6, 6, '#f6b46a') + e(15, 20, 3, 3, '#ffc2cf') + eo(49, 20, 6, 6, '#f6b46a') + e(49, 20, 3, 3, '#ffc2cf') +
    lay('M32 17 Q57 17 57 39 Q57 58 32 58 Q7 58 7 39 Q7 17 32 17 Z', '#f6b46a', p('M46 20 Q57 26 57 39 Q57 58 32 58 Q55 46 46 20Z', '#d9824f')) +
    e(19, 46, 9, 7, '#fff6ea') + e(45, 46, 9, 7, '#fff6ea') + p('M32 22 Q35 30 32 34 Q29 30 32 22Z', '#fff6ea') + face(32, 38, .9) + e(32, 42, 2, 1.4, '#ff8fa3') },
  { key: 'penguin', name: '펭구', art: lay('M32 14 Q55 14 55 37 Q55 58 32 58 Q9 58 9 37 Q9 14 32 14 Z', '#46557a', p('M45 17 Q55 24 55 37 Q55 58 32 58 Q52 45 45 17Z', '#2f3a5a')) +
    po('M32 28 Q24 20 18 26 Q13 34 16 44 Q22 56 32 56 Q42 56 48 44 Q51 34 46 26 Q40 20 32 28 Z', '#fff', 2.6) +
    face(32, 37, .95) + po('M28 42 L36 42 L32 47 Z', '#ffb347', 2.4) },
];
ANIMALS.push({ key: 'fox', name: '단풍', art: ANIMALS[0].art, ch2: 'photo' }, { key: 'tanuki', name: '도토리', art: ANIMALS[0].art, ch2: 'store' },
  { key: 'sheep', name: '몽실', art: ANIMALS[0].art, ch2: 'bath' }, { key: 'duck', name: '퐁당', art: ANIMALS[0].art, ch2: 'dock' },
  { key: 'otter', name: '찰랑', art: ANIMALS[0].art, ch2: 'teahouse' }, { key: 'beaver', name: '뚝딱', art: ANIMALS[0].art, ch2: 'tackle' },
  { key: 'squirrel', name: '알밤', art: ANIMALS[0].art, ch2: 'chestnut' }, { key: 'mole', name: '꼼지', art: ANIMALS[0].art, ch2: 'mushroom' },
  { key: 'hedgehog', name: '새콤', art: ANIMALS[0].art, ch2: 'pie' }, { key: 'owl', name: '소곤', art: ANIMALS[0].art, ch2: 'library' },
  { key: 'badger', name: '타닥', art: ANIMALS[0].art, ch2: 'camp' }, { key: 'deer', name: '살랑', art: ANIMALS[0].art, ch2: 'maple' },
  { key: 'redpanda', name: '꿀떡', art: ANIMALS[0].art, ch2: 'honey' }, { key: 'bat', name: '반짝', art: ANIMALS[0].art, ch2: 'nightcandy' },
  { key: 'polarbear', name: '포근', art: ANIMALS[0].art, ch2: 'hotteok' }, { key: 'alpaca', name: '몽글', art: ANIMALS[0].art, ch2: 'knit' },
  { key: 'ermine', name: '따끈', art: ANIMALS[0].art, ch2: 'cocoa' }, { key: 'seal', name: '도레', art: ANIMALS[0].art, ch2: 'musichall' },
  { key: 'husky', name: '쌩쌩', art: ANIMALS[0].art, ch2: 'skate' }, { key: 'reindeer', name: '사뿐', art: ANIMALS[0].art, ch2: 'cablecar' });
ANIMALS.push({ key: 'crab', name: '집게', art: ANIMALS[0].art, ch2: 'parasol' }, { key: 'pelican', name: '꿀꺽', art: ANIMALS[0].art, ch2: 'melon' },
  { key: 'hermit', name: '또르', art: ANIMALS[0].art, ch2: 'shell' }, { key: 'turtle', name: '느릿', art: ANIMALS[0].art, ch2: 'surf' },
  { key: 'gull', name: '끼룩', art: ANIMALS[0].art, ch2: 'castle' }, { key: 'flamingo', name: '산들', art: ANIMALS[0].art, ch2: 'yacht' });
ANIMALS.push({ key: 'seaotter', name: '몽돌', art: ANIMALS[0].art, ch2: 'gelato' }, { key: 'puffin', name: '또박', art: ANIMALS[0].art, ch2: 'hpost' },
  { key: 'hseal', name: '뽀글', art: ANIMALS[0].art, ch2: 'market' }, { key: 'octopus', name: '문문', art: ANIMALS[0].art, ch2: 'sail' },
  { key: 'albatross', name: '훨훨', art: ANIMALS[0].art, ch2: 'museum' }, { key: 'sealion', name: '첨벙', art: ANIMALS[0].art, ch2: 'ferry' });
ANIMALS.push({ key: 'monkey', name: '대롱', art: ANIMALS[0].art, ch2: 'coconut' }, { key: 'parrot', name: '재잘', art: ANIMALS[0].art, ch2: 'lei' },
  { key: 'hippo', name: '통통', art: ANIMALS[0].art, ch2: 'mango' }, { key: 'sloth', name: '꾸벅', art: ANIMALS[0].art, ch2: 'hammock' },
  { key: 'toucan', name: '쫑긋', art: ANIMALS[0].art, ch2: 'radio' }, { key: 'frog', name: '폴짝', art: ANIMALS[0].art, ch2: 'raft' });

const UI = {
  bolt: svg(po('M27 5 L45 5 L36 26 L50 26 L22 60 L28 37 L14 37 Z', '#ffd75a', 3.5) + p('M36 26 L50 26 L22 60 L28 37 Z', 'rgba(242,155,58,.55)') + e(31, 11, 3.2, 1.8, '#fff3b0') + po('M27 5 L45 5 L36 26 L50 26 L22 60 L28 37 L14 37 Z', 'none', 3.5)),
  coin: svg(eo(32, 33, 26, 26, '#f2b03a', 3.5) + eo(32, 30, 26, 26, '#ffd75a', 3.5) + eo(32, 30, 18, 18, 'none', 2.5) + heart(32, 31, 1.3, '#f2b03a') + e(20, 18, 4, 2.5, '#fff3b0')),
  star: svg(po('M29.4 11.4 Q32.0 6.5 34.6 11.4 L39.5 20.8 Q40.5 22.8 42.7 23.1 L53.2 24.9 Q58.6 25.8 54.8 29.8 L47.3 37.4 Q45.8 39.0 46.1 41.2 L47.7 51.7 Q48.5 57.2 43.5 54.7 L34.0 50.0 Q32.0 49.0 30.0 50.0 L20.5 54.7 Q15.5 57.2 16.3 51.7 L17.9 41.2 Q18.2 39.0 16.7 37.4 L9.2 29.8 Q5.4 25.8 10.8 24.9 L21.3 23.1 Q23.5 22.8 24.5 20.8 Z', '#ffd75a', 3.5) + e(26, 25, 3, 2, '#fff3b0')),
  lock: svg(po('M22 28 V20 Q22 10 32 10 Q42 10 42 20 V28', 'none', 5) + po('M14 28 h36 a4 4 0 0 1 4 4 v20 a4 4 0 0 1 -4 4 h-36 a4 4 0 0 1 -4 -4 v-20 a4 4 0 0 1 4 -4 z', '#ffd75a', 3.5) + eo(32, 40, 4, 4, O, 2) + po('M32 42 L32 48', 'none', 3.5)),
  gift: svg(po('M10 26 h44 v10 h-44 z', '#ff8fa3', 3) + po('M13 36 h38 v20 h-38 z', '#ffb3c1', 3) + po('M29 26 h6 v30 h-6 z', '#ffd75a', 2.6) + eo(25, 20, 7, 5, '#ffd75a', 3) + eo(39, 20, 7, 5, '#ffd75a', 3)),
};

// ---- image overrides (painted item sheets) ----
const OVR_B64 = __OVR__;
const toUrl = s => { if (!s) return s; if (s[0] === '@' || s.startsWith('http')) return s; const d = s.startsWith('data:') ? s : 'data:image/webp;base64,' + s; return globalThis.__mcBlob ? globalThis.__mcBlob(d) : d; };
// 리스 플러그인: 마을·가게 그림은 묶음 파일(EXT_FILES)에서 받아 '@번호' 자리를 채움
const EXT_FILES = __EXTFILES__;
function extFill(m) {
  const walk = o => { for (const k in o) { const v = o[k]; if (typeof v === 'string') { if (v[0] === '@' && m[v]) o[k] = m[v]; } else if (v && typeof v === 'object') walk(v); } };
  walk(OVR); walk(PAINT); walk(TOWN_BG); walk(TOWN_BG2);
}
const OVR = Object.fromEntries(Object.entries(OVR_B64).map(([k, v]) => [k, Array.isArray(v) ? v.map(toUrl) : Object.fromEntries(Object.entries(v).map(([c, arr]) => [c, Array.isArray(arr) ? arr.map(toUrl) : toUrl(arr)]))]));
// 에너지·코인·별 아이콘은 그림으로 (SVG로 감싸서 쓰던 크기·위치 그대로)
{
  const blobOf = u => { try { if (!u.startsWith('data:')) return u; const [h, b] = u.split(','), bin = atob(b), arr = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) arr[i] = bin.charCodeAt(i); return URL.createObjectURL(new Blob([arr], { type: h.slice(5, h.indexOf(';')) })); } catch (_) { return u; } };
  if (OVR.ui) for (const k of ['bolt', 'coin', 'star']) if (OVR.ui[k]) UI[k] = svg(`<image href="${blobOf(OVR.ui[k])}" x="0" y="0" width="64" height="64"/>`);
}
const XMAS_ART = globalThis.__MC_APP ? 'img/christmas/' : 'https://raw.githubusercontent.com/shakeit08/risu-plugins/main/sweet_merge_cafe_img/christmas/';
const oldXmasCocoa = OVR.xmas[4];
OVR.xmas[4] = XMAS_ART + 'cookie-tin.webp';
for (const c of XMAS_CHAINS.slice(1)) {
  OVR[c] = CHAINS[c].items.map((_, i) => c === 'xmasCocoa' && i === 4 ? oldXmasCocoa : `${XMAS_ART}${c}-${i + 1}.webp`);
}
const GEN_IDX = { bakery: 0, coffee: 1, berry: 2, choco: 3, tea: 4, icecream: 5 };
const imgTag = src => `<img src="${src}" alt="" draggable="false">`;
// 에너지·코인 아이템 그림 (상자는 그림이 오기 전까지 선물 아이콘)
const iconChest = x => OVR.r_box ? `<img src="${OVR.r_box[x - 1]}" alt="" draggable="false">` : UI.gift;
const iconRes = (r, l) => OVR['r_' + r] ? `<img src="${OVR['r_' + r][l - 1]}" alt="" draggable="false">` : (r === 'en' ? UI.bolt : UI.coin);
const iconItem = (c, l) => OVR[c] ? `<img src="${OVR[c][l - 1]}" alt="" draggable="false">` : svg(ART_ITEMS[c][l - 1]);
const GEN_LV_NAMES = {
  bakery: ['빵 봉투', '토스트기', '반죽 믹서', '토스터 오븐', '빵 수레', '2단 오븐', '빵 노점', '빵집'],
  coffee: ['원두 봉투', '커피 그라인더', '모카포트', '드립 커피 머신', '에스프레소 머신', '커피 수레', '로스터기', '커피 바'],
  berry: ['딸기 씨앗', '물뿌리개', '새싹 화분', '딸기 화분', '딸기 상자', '딸기 텃밭', '딸기 온실', '딸기 가판대'],
  choco: ['카카오 나무', '카카오 자루', '맷돌 그라인더', '초콜릿 냄비', '초콜릿 분수', '봉봉 진열장', '초콜릿 기계', '초콜릿 가게'],
  tea: ['허브 다발', '허브 화분', '찻잎 병', '찻주전자', '화로 주전자', '티 카트', '허브 건조대', '찻집'],
  candy: ['사탕 봉투', '사탕 통', '사탕 병', '검볼 머신', '솜사탕 기계', '사탕 디스펜서', '사탕 노점', '사탕 집'],
  fish: ['밀가루 자루', '반죽 볼', '팥소 냄비', '붕어빵 팬', '붕어빵 틀', '붕어빵 수레', '붕어빵 노점', '붕어빵 가게'],
  pie: ['사과나무', '사과 바구니', '사과 수레', '밀대와 반죽', '파이 틀', '오븐', '벽돌 화덕', '파이 가게'],
  icecream: ['와플콘', '아이스크림 통', '아이스크림 메이커', '소프트콘 기계', '아이스바 냉동고', '아이스크림 수레', '젤라토 쇼케이스', '아이스크림 가게'],
};
const iconGen = (c, gl = 1) => XMAS_CHAINS.indexOf(c) > 0 ? imgTag(`${XMAS_ART}${c}-gen.webp`) : (OVR.genLv && OVR.genLv[c]) ? imgTag(OVR.genLv[c][Math.min(gl, OVR.genLv[c].length) - 1]) : (OVR.genOne && OVR.genOne[c]) ? imgTag(OVR.genOne[c]) : svg(ART_GENS[c]);
const hasGenArt = c => !!(OVR.genLv && OVR.genLv[c]);
const genName = (c, gl = 1) => (GEN_LV_NAMES[c] && OVR.genLv && OVR.genLv[c]) ? GEN_LV_NAMES[c][gl - 1] : CHAINS[c].gen;
const WALK = OVR.walk || {};
const ST_IMG = OVR.st || {}, DEB_IMG = OVR.deb || [];
const ST_DIM = __STDIM__;
const MAP = OVR.map || {};
const ART_TOOLS = OVR.tool || null;
const WHEEL = OVR.wheel || null;
const STORY_IMG = OVR.story || null;
const iconBag = (s) => OVR.bag ? imgTag(OVR.bag[s - 1]) : '🎁';
// 입고 있는 옷(스킨)이 있으면 그 얼굴로 바꿔 보여 줌: SKIN_FACE[이웃 번호] = 옷 얼굴 번호
const SKIN_FACE = {};
const iconAnimal = (i, happy = true) => (i = SKIN_FACE[i] ?? i, OVR.animal) ? imgTag((!happy && OVR.animalDot && OVR.animalDot[i]) ? OVR.animalDot[i] : OVR.animal[i]) : svg(ANIMALS[i].art);

// ===================== CAFE SCENE =====================
const SW = 2.5;
const txt = (x, y, s, fill, t, extra = '') => `<text x="${x}" y="${y}" font-size="${s}" text-anchor="middle" font-family="Jua, sans-serif" fill="${fill}" ${extra}>${t}</text>`;
const itemAt = (c, l, x, y, s) => OVR[c] ? `<image href="${OVR[c][l - 1]}" x="${x + 6 * s}" y="${y + 6 * s}" width="${(52 * s).toFixed(1)}" height="${(52 * s).toFixed(1)}"/>` : g(`translate(${x} ${y}) scale(${s})`, ART_ITEMS[c][l - 1].replace(SH, ''));
const flower = (x, y, c) => g(`translate(${x} ${y})`, [0, 72, 144, 216, 288].map(a => { const r = a * Math.PI / 180; return eo((Math.cos(r) * 3).toFixed(1), (Math.sin(r) * 3).toFixed(1), 2.6, 2.6, c, 1.4); }).join('') + eo(0, 0, 1.8, 1.8, '#ffd75a', 1.2));
const bulbs = (pts, cols) => pts.map(([x, y], i) => eo(x, y, 2.6, 2.6, cols[i % cols.length], 1.4)).join('');

function sceneParts(L) {
  const parts = {};
  const wallC = ['#d6cec6', '#fff1dc', '#fff1dc'][L.wall], trim = ['#aea398', '#f6b8a0', '#8fd6b9'][L.wall];
  const corn = ['#b3a79c', '#ffb3a0', '#ff9db0'][L.wall], roof = ['#9b8e84', '#e98a5a', '#ff6b81'][L.wall];
  // wall + roof
  parts.wall =
    po('M48 34 Q160 2 272 34 Z', roof, SW) + sl('M80 28 Q160 10 240 28 M110 22 Q160 12 210 22', 'rgba(91,58,50,.35)', 1.6) +
    eo(160, 22, 7, 7, L.wall ? '#e3f4fb' : '#bfc9cc', 2.2) + sl('M160 15 V29 M153 22 H167', O, 1.4) +
    po('M60 46 H260 V200 H60 Z', wallC, SW) + p('M244 48 H258 V198 H244Z', 'rgba(91,58,50,.07)') +
    (L.wall === 0 ? sl('M74 58 L80 68 L76 78 L82 86 M246 148 L238 158 L244 168 M120 186 L128 194', O, 1.5) + p('M222 60 h16 v10 h-16z', '#c7bdb3') + sl('M222 60 h16 v10 h-16z', O, 1.2) : '') +
    (L.wall === 2 ? p('M61 160 H259 V199 H61Z', '#f7a8b2') +
      [170, 180, 190].map((y, k) => sl(`M61 ${y} H259`, '#d9707f', 1.3) + Array.from({ length: 13 }, (_, j) => sl(`M${70 + j * 16 + (k % 2) * 8} ${y - 10} V${y}`, '#d9707f', 1.3)).join('')).join('') +
      po('M60 156 H260 V162 H60Z', trim, 2) : '') +
    (L.wall === 1 ? po('M60 191 H260 V200 H60Z', trim, 2) : '') +
    po('M52 33 H268 V48 H52 Z', corn, SW) +
    (L.wall ? Array.from({ length: 13 }, (_, j) => e(60 + j * 16.7, 48, 5, 3.4, corn) + `<path d="M${55 + j * 16.7} 48 a5 3.4 0 0 0 10 0" fill="none" stroke="${O}" stroke-width="1.6"/>`).join('') : sl('M52 40 H268', 'rgba(91,58,50,.3)', 1.4)) +
    // right small window frame
    po('M216 114 H252 V150 H216 Z', L.wall ? '#fff' : '#a99c90', 2.2) + p('M220 118 H248 V146 H220Z', L.wall ? '#e3f4fb' : '#c3cccf') + sl('M234 118 V146 M220 132 H248', O, 1.6) + p('M222 120 l6 0 l-6 8z', 'rgba(255,255,255,.7)');
  // sign
  parts.sign = [
    g('rotate(-5 160 64)', po('M124 55 h72 v18 h-72 z', '#c2a487', SW) + sl('M124 61 H196 M124 67 H196', 'rgba(91,58,50,.25)', 1.2) + e(129, 58, 1.4, 1.4, O) + e(191, 58, 1.4, 1.4, O) + txt(160, 69, 11, '#8d7a6c', 'CAFE')) +
      sl('M200 66 Q204 70 200 74 M118 60 L112 56', '#aaa', 1.2),
    po('M118 51 h84 a8 8 0 0 1 8 8 v10 a8 8 0 0 1 -8 8 h-84 a8 8 0 0 1 -8 -8 v-10 a8 8 0 0 1 8 -8 z', '#fffaf3', SW) +
      sl('M120 55 h80 a5 5 0 0 1 5 5 v8 a5 5 0 0 1 -5 5 h-80 a5 5 0 0 1 -5 -5 v-8 a5 5 0 0 1 5 -5 z', '#ff8fa3', 1.4) +
      txt(160, 69, 14, O, '달콤 카페') + heart(119, 64, .32, '#ff8fa3') + heart(201, 64, .32, '#ff8fa3'),
    po('M102 78 V62 Q102 49 115 49 H205 Q218 49 218 62 V78 Z', '#ff8fa3', SW) +
      sl('M107 75 V63 Q107 54 116 54 H204 Q213 54 213 63 V75 Z', '#ffd75a', 1.8) +
      bulbs([[112, 52], [126, 50], [140, 50], [154, 50], [168, 50], [182, 50], [196, 50], [210, 52]], ['#ffe27a', '#fff', '#9fe3c9']) +
      txt(160, 71, 15, '#fff', '달콤 카페', `stroke="${O}" stroke-width="3" paint-order="stroke"`) +
      g('translate(160 40) scale(.32) translate(-32 -40)', ART_ITEMS.choco[5].replace(SH, '')),
  ][L.sign];
  // awning
  const scallops = (c1, c2) => Array.from({ length: 12 }, (_, j) => `<path d="M${64 + j * 16} 98 a8 8 0 0 0 16 0 Z" fill="${j % 2 ? c2 : c1}" stroke="${O}" stroke-width="2"/>`).join('');
  const stripes = (c1, c2) => p('M64 82 H256 V98 H64Z', c2) + Array.from({ length: 12 }, (_, j) => j % 2 ? '' : p(`M${64 + j * 16} 82 h16 v16 h-16z`, c1)).join('') + po('M64 82 H256 V98 H64Z', 'none', SW) + po('M60 80 H260', 'none', 3.5);
  parts.awning = [
    po('M64 82 H256 V96 L246 103 L236 96 L224 104 L210 96 L196 101 L182 96 L170 104 L156 96 L140 102 L126 96 L112 104 L98 96 L86 101 L74 96 L64 100 Z', '#b0a9a1', SW) +
      e(150, 89, 4, 2.5, '#7d7268') + p('M96 86 q8 4 16 0 v4 q-8 3 -16 0z', 'rgba(91,58,50,.15)'),
    stripes('#ff8fa3', '#fff') + scallops('#ff8fa3', '#fff'),
    stripes('#ff8fa3', '#fff') + scallops('#ff8fa3', '#fff') +
      sl('M66 108 Q110 122 160 108 Q210 122 254 108', O, 1.4) +
      bulbs([[80, 112.5], [98, 116.5], [116, 117], [134, 114], [186, 114], [204, 117], [222, 116.5], [240, 112.5]], ['#ffe27a', '#ff8fa3', '#9fe3c9', '#fff']),
  ][L.awning];
  // display window
  parts.window = [
    po('M74 112 H154 V182 H74 Z', '#9c8b7e', SW) + p('M80 118 H148 V176 H80Z', '#c0c9cc') + e(96, 150, 6, 4, 'rgba(120,110,100,.3)') + e(132, 130, 8, 5, 'rgba(120,110,100,.25)') +
      sl('M114 118 V176 M80 147 H148', O, 1.8) + sl('M80 118 l12 8 M80 118 l4 12 M84 124 l6 -2', '#eee', 1) +
      g('rotate(-14 114 147)', po('M74 141 H154 V151 H74 Z', '#b0906f', 2.2) + e(80, 146, 1.2, 1.2, O) + e(148, 146, 1.2, 1.2, O)),
    po('M74 112 H154 V182 H74 Z', '#fff', SW) + p('M80 118 H148 V176 H80Z', '#e3f4fb') + p('M84 122 l14 0 l-14 22z', 'rgba(255,255,255,.8)') +
      itemAt('bakery', 4, 82, 136, .38) + itemAt('berry', 7, 101, 134, .42) + itemAt('coffee', 6, 122, 138, .36) +
      po('M80 162 H148', 'none', 2) + sl('M114 118 V128', O, 1.6) + po('M70 180 H158 V186 H70Z', '#f6b8a0', 2),
    po('M74 182 V130 Q74 108 114 108 Q154 108 154 130 V182 Z', '#fff', SW) + p('M80 176 V131 Q80 114 114 114 Q148 114 148 131 V176Z', '#e3f4fb') +
      itemAt('berry', 7, 92, 124, .48) + itemAt('bakery', 6, 80, 148, .32) + itemAt('choco', 7, 126, 146, .34) + itemAt('coffee', 7, 132, 122, .3) +
      po('M80 166 H148', 'none', 2) +
      po('M80 131 Q80 114 98 114 Q92 140 84 150 Q80 148 80 140 Z', '#ff8fa3', 1.8) + po('M148 131 Q148 114 130 114 Q136 140 144 150 Q148 148 148 140 Z', '#ff8fa3', 1.8) +
      eo(84, 150, 3, 2, '#ffd75a', 1.4) + eo(144, 150, 3, 2, '#ffd75a', 1.4) + po('M70 180 H158 V186 H70Z', '#8fd6b9', 2),
  ][L.window];
  // door
  const frame = po('M164 114 H210 V200 H164Z', L.wall ? trim : '#aea398', 2.2);
  parts.door = frame + [
    po('M169 120 H205 V200 H169Z', '#a08778', SW) + sl('M178 120 V200 M187 120 V200 M196 120 V200', 'rgba(91,58,50,.35)', 1.3) + e(199, 162, 2, 2, O) +
      sl('M180 132 L187 126 L194 132', O, 1) + po('M178 132 h18 v9 h-18z', '#e8e2dc', 1.4) + txt(187, 139.5, 6, '#8d7a6c', 'CLOSED'),
    po('M169 120 H205 V200 H169Z', '#8fd6b9', SW) + po('M174 125 h26 v28 h-26z', '#e3f4fb', 2) + p('M176 127 l8 0 l-8 12z', 'rgba(255,255,255,.8)') +
      po('M174 160 h26 v34 h-26z', 'none', 1.6) + eo(199, 163, 2.4, 2.4, '#ffd75a', 1.4) +
      sl('M181 140 L187 133 L193 140', O, 1) + po('M178 140 h18 v9 h-18z', '#ff8fa3', 1.4) + txt(187, 147.5, 6.5, '#fff', 'OPEN'),
    po('M168 200 V138 Q168 118 187 118 Q206 118 206 138 V200Z', '#ff9db0', SW) + po('M174 160 V140 Q174 126 187 126 Q200 126 200 140 V160Z', '#e3f4fb', 2) +
      `<circle cx="187" cy="143" r="9" fill="none" stroke="${O}" stroke-width="5.5"/><circle cx="187" cy="143" r="9" fill="none" stroke="#6cc46a" stroke-width="3"/>` +
      [[180, 137], [194, 139], [181, 150], [193, 149], [187, 134]].map(([x, y]) => e(x, y, 1.6, 1.6, '#ff5d73')).join('') + eo(187, 153, 3, 2, '#ff5d73', 1.3) +
      eo(201, 172, 2.4, 2.4, '#ffd75a', 1.4) + po('M164 122 Q164 116 170 116', 'none', 1.4) + po('M166 122 Q170 128 174 122 Z', '#ffd75a', 1.4) +
      po('M164 200 H210 V205 H164Z', '#f2b03a', 2),
  ][L.door];
  // planter
  parts.planter = [
    po('M224 186 H240 L238 200 H226 Z', '#b98b6e', 2.2) + sl('M232 186 Q228 176 222 180 M232 186 Q236 174 242 178 M232 186 Q232 178 230 172', '#a68a5c', 1.8) +
      po('M214 150 H254 V158 H214Z', '#a99c90', 2) + sl('M226 150 L232 158', O, 1.2),
    po('M214 150 H254 V159 H214Z', '#f6b8a0', 2) + [[220, 146, '#ff8fa3'], [229, 144, '#fff'], [238, 146, '#ff8fa3'], [247, 144, '#fff']].map(([x, y, c]) => flower(x, y, c)).join('') +
      po('M224 186 H242 L240 200 H226 Z', '#e98a5a', 2.2) + e(233, 181, 9, 6, '#6cc46a') + sl('M233 181 m-9 0 a9 6 0 0 1 18 0', O, 2) + flower(229, 179, '#ff8fa3') + flower(238, 180, '#fff'),
    po('M214 150 H254 V159 H214Z', '#8fd6b9', 2) +
      sl('M218 158 Q214 170 220 182 M250 158 Q256 172 249 186', '#3f9a74', 1.8) + [[216, 166], [219, 176], [253, 168], [251, 180]].map(([x, y]) => eo(x, y, 2.6, 1.8, '#7fd47a', 1.2)).join('') +
      [[219, 145, '#ff8fa3'], [226, 143, '#ffd75a'], [233, 145, '#fff'], [240, 143, '#ff8fa3'], [248, 145, '#b9a6ff']].map(([x, y, c]) => flower(x, y, c)).join('') +
      [222, 248].map(x => po(`M${x - 4} 168 V184`, 'none', 2) + eo(x - 4, 166, 8, 8, '#7fd47a', 2.2) + p(`M${x - 1} 160 a6 6 0 0 1 3 9 a8 8 0 0 0 -3 -9z`, '#3f9a74') + po(`M${x - 11} 186 H${x + 3} L${x + 1} 200 H${x - 9} Z`, '#fffaf3', 2.2) + p(`M${x - 10} 190 H${x + 2} V193 H${x - 10}Z`, '#ff8fa3')).join(''),
  ][L.planter];
  // lamp
  const post = c => po('M27 98 H33 V200 H27Z', c, 2.2) + po('M23 200 H37 L35 194 H25Z', c, 2) + po('M30 98 Q30 86 22 86', 'none', 2.4);
  parts.lamp = [
    g('rotate(-4 30 204)', post('#9a948e') + po('M14 86 H30 L27 96 H17Z', '#9a948e', 2) + eo(22, 99, 4, 3.4, '#cfcac4', 1.6)),
    e(22, 98, 20, 20, 'rgba(255,236,150,.45)') + post('#46557a') + po('M14 86 H30 L27 96 H17Z', '#46557a', 2) + eo(22, 99, 4.2, 3.6, '#ffe27a', 1.6),
    e(22, 98, 22, 22, 'rgba(255,236,150,.5)') + post('#46557a') + po('M14 86 H30 L27 96 H17Z', '#46557a', 2) + eo(22, 99, 4.2, 3.6, '#ffe27a', 1.6) +
      po('M33 112 H46 M44 112 V118', 'none', 1.8) + po('M36 120 H52 Q51 130 44 130 Q37 130 36 120Z', '#d99b5b', 2) + flower(40, 118, '#ff8fa3') + flower(47, 117, '#fff') + sl('M37 124 Q36 132 38 138', '#3f9a74', 1.6) +
      po('M33 140 H50 L46 147 L50 154 H33Z', '#ff8fa3', 2) + heart(40, 147, .26, '#fff'),
  ][L.lamp];
  // terrace
  const chair = (x, flip) => po(`M${x} 186 h12 v3 h-12z`, '#8fd6b9', 1.8) + po(`M${x + (flip ? 10 : 0)} 189 v14 M${x + (flip ? 0 : 10)} 189 v14`, 'none', 1.8) + po(`M${x + (flip ? 12 : 0)} 186 V170`, 'none', 2.2) + po(`M${x + (flip ? 12 : 0) - 1.5} 170 h3 v8 h-3z`, '#8fd6b9', 1.6);
  const table = po('M288 174 V202 M282 202 H294', 'none', 2.2) + eo(288, 172, 15, 3.6, '#fffaf3', 2.2);
  parts.terrace = [
    po('M268 184 H292 V202 H268Z', '#c49a6c', 2.2) + sl('M268 190 H292 M268 196 H292', 'rgba(91,58,50,.4)', 1.2) +
      sl('M300 202 l-3 -8 M303 202 l0 -10 M306 202 l3 -7 M312 202 l-2 -6 M315 202 l2 -7', '#8fae5a', 1.6) + eo(306, 200, 4, 2.4, '#bdb5ad', 1.4),
    chair(266, false) + chair(298, true) + table + itemAt('coffee', 4, 280, 158, .22),
    po('M288 170 V126', 'none', 2.2) +
      po('M260 134 Q288 110 316 134 Z', '#fff', 2.2) + p('M270 128 Q280 118 288 116 L288 134 L270 134Z', '#ff8fa3') + p('M304 128 Q296 118 288 116 L288 116 L306 134 L304 134Z', '#ff8fa3') + po('M260 134 Q288 110 316 134 Z', 'none', 2.2) +
      chair(266, false) + chair(298, true) + table + itemAt('coffee', 6, 274, 157, .22) + itemAt('berry', 6, 287, 157, .24),
  ][L.terrace];
  return parts;
}

const SPOT_BOX = {
  sign: '100 36 120 46', awning: '58 74 204 52', wall: '44 2 232 202', window: '66 104 96 86',
  door: '158 110 58 98', planter: '208 108 52 96', terrace: '256 106 64 102', lamp: '6 76 52 132',
};
function cafeScene(L, vb = '0 0 320 240', anim = '') {
  const parts = sceneParts(L);
  const bg = `<rect width="320" height="240" fill="#d6f0fb"/>` +
    e(250, 22, 22, 9, '#fff') + e(268, 16, 14, 9, '#fff') + e(70, 18, 18, 7, '#fff') + e(84, 13, 11, 7, '#fff') +
    p('M0 150 Q40 120 80 140 Q120 118 160 138 Q200 120 240 140 Q280 122 320 140 V200 H0Z', '#c3e8cb') +
    p('M0 199 H320 V240 H0Z', '#f3e4d3') + sl('M0 220 H320', '#e2cdb6', 1.4) + Array.from({ length: 11 }, (_, j) => sl(`M${j * 32 + 8} 200 V220 M${j * 32 + 24} 220 V240`, '#e2cdb6', 1.4)).join('') + po('M0 199.5 H320', 'none', 2.4);
  const order = ['wall', 'window', 'door', 'planter', 'sign', 'awning', 'lamp', 'terrace'];
  return `<svg viewBox="${vb}" xmlns="http://www.w3.org/2000/svg" stroke-linejoin="round" stroke-linecap="round">${bg}${order.map(k => `<g data-spot="${k}" ${anim === k ? 'class="sp-new"' : ''}>${parts[k]}</g>`).join('')}</svg>`;
}
const HOUSE = svg(po('M10 30 L32 10 L54 30', 'none', 4) + po('M14 28 H50 V56 H14 Z', '#fff1dc', 3.5) + po('M12 30 L32 12 L52 30 Z', '#ff8fa3', 3.5) + po('M27 40 h10 v16 h-10 z', '#8fd6b9', 3) + po('M17 36 h7 v7 h-7 z', '#e3f4fb', 2.5) + po('M40 36 h7 v7 h-7 z', '#e3f4fb', 2.5) + po('M14 30 H50', 'none', 3));

// ===================== NEIGHBORHOOD AREAS =====================
const SCENE_BG = `<rect width="320" height="240" fill="#d6f0fb"/>` +
  e(250, 22, 22, 9, '#fff') + e(268, 16, 14, 9, '#fff') + e(70, 18, 18, 7, '#fff') + e(84, 13, 11, 7, '#fff') +
  p('M0 150 Q40 120 80 140 Q120 118 160 138 Q200 120 240 140 Q280 122 320 140 V200 H0Z', '#c3e8cb') +
  p('M0 199 H320 V240 H0Z', '#f3e4d3') + sl('M0 220 H320', '#e2cdb6', 1.4) + Array.from({ length: 11 }, (_, j) => sl(`M${j * 32 + 8} 200 V220 M${j * 32 + 24} 220 V240`, '#e2cdb6', 1.4)).join('') + po('M0 199.5 H320', 'none', 2.4);
const tulip = (x, y, c) => po(`M${x} ${y + 4} V${y + 12}`, 'none', 1.6) + po(`M${x - 3.5} ${y - 3} L${x - 3.5} ${y + 2} Q${x} ${y + 6} ${x + 3.5} ${y + 2} L${x + 3.5} ${y - 3} L${x + 1.5} ${y - 1} L${x} ${y - 4} L${x - 1.5} ${y - 1} Z`, c, 1.5);
const bucket = (x, c1, c2, n = 3) => po(`M${x - 8} 186 H${x + 8} L${x + 6} 204 H${x - 6} Z`, '#cfd6ea', 2) + sl(`M${x - 7} 191 H${x + 7}`, '#9aa3c4', 1.4) +
  Array.from({ length: n }, (_, j) => (j % 2 ? flower(x - 5 + j * 5, 180 - (j % 2) * 3, c2) : tulip(x - 5 + j * 5, 177 + (j === 1 ? -2 : 0), c1))).join('');
const roundTree = (cx, cy, r, c1, c2, c3) => po(`M${cx - r} ${cy} Q${cx - r} ${cy - r} ${cx} ${cy - r} Q${cx + r} ${cy - r} ${cx + r} ${cy} Q${cx + r} ${cy + r * .8} ${cx} ${cy + r * .8} Q${cx - r} ${cy + r * .8} ${cx - r} ${cy} Z`, c1, 2.4) +
  p(`M${cx + r * .3} ${cy - r * .8} Q${cx + r} ${cy - r * .5} ${cx + r} ${cy} Q${cx + r} ${cy + r * .8} ${cx} ${cy + r * .8} Q${cx + r * .8} ${cy} ${cx + r * .3} ${cy - r * .8}Z`, c2) + e(cx - r * .45, cy - r * .35, r * .25, r * .16, c3) +
  po(`M${cx - r} ${cy} Q${cx - r} ${cy - r} ${cx} ${cy - r} Q${cx + r} ${cy - r} ${cx + r} ${cy} Q${cx + r} ${cy + r * .8} ${cx} ${cy + r * .8} Q${cx - r} ${cy + r * .8} ${cx - r} ${cy} Z`, 'none', 2.4);

function flowerParts(L) {
  const P = {}, wl = L.fwall;
  const wall = ['#d6cec6', '#efe3ff', '#efe3ff'][wl], roof = ['#9b8e84', '#7fcf9a', '#5fbf8a'][wl], trim = ['#aea398', '#fff', '#fff'][wl];
  P.fwall = po('M54 62 L160 14 L266 62 Z', roof, SW) +
    (wl ? sl('M86 50 L234 50 M112 38 L208 38 M136 27 L184 27', 'rgba(255,255,255,.4)', 2) : sl('M90 50 L110 48 M200 40 L214 44', 'rgba(91,58,50,.35)', 1.6)) +
    (wl === 2 ? Array.from({ length: 12 }, (_, j) => `<path d="M${62 + j * 17} 62 a8.5 5 0 0 0 17 0" fill="#5fbf8a" stroke="${O}" stroke-width="1.8"/>`).join('') : '') +
    eo(160, 42, 7, 7, wl ? '#e3f4fb' : '#bfc9cc', 2.2) + sl('M160 35 V49 M153 42 H167', O, 1.3) +
    po('M72 60 H248 V200 H72 Z', wall, SW) + p('M234 62 H246 V198 H234Z', 'rgba(91,58,50,.07)') +
    (wl === 0 ? sl('M84 70 L90 80 L86 90 M236 150 L228 160 L234 170', O, 1.5) + p('M200 76 h14 v10 h-14z', '#c7bdb3') : '') +
    (wl === 2 ? p('M73 170 H247 V199 H73Z', '#f5d7b0') + Array.from({ length: 10 }, (_, j) => sl(`M${82 + j * 17} 171 V199`, '#d9a86c', 1.4)).join('') + po('M72 166 H248 V171 H72Z', '#b993d6', 2) : '') +
    (wl === 1 ? po('M72 192 H248 V200 H72Z', '#b993d6', 2) : '') +
    po('M166 112 H210 V200 H166Z', trim, 2.2) +
    (wl === 2 ? po('M170 200 V132 Q170 116 188 116 Q206 116 206 132 V200Z', '#ff9db0', SW) + po('M176 150 V134 Q176 124 188 124 Q200 124 200 134 V150Z', '#e3f4fb', 2) + heart(188, 168, .5, '#fff') + eo(200, 176, 2.3, 2.3, '#ffd75a', 1.4)
      : po('M170 116 H206 V200 H170Z', wl ? '#8fd6b9' : '#a08778', SW) + (wl ? po('M175 122 h26 v24 h-26z', '#e3f4fb', 2) + eo(200, 166, 2.3, 2.3, '#ffd75a', 1.4) : sl('M179 116 V200 M188 116 V200 M197 116 V200', 'rgba(91,58,50,.35)', 1.3) + e(200, 164, 1.8, 1.8, O)));
  P.fsign = [
    sl('M140 60 V66 M180 60 V66', O, 1.6) + g('rotate(-6 160 76)', po('M128 66 h64 v18 h-64 z', '#c2a487', SW) + txt(160, 79, 9, '#8d7a6c', 'FLOWER')),
    sl('M140 60 V68 M180 60 V68', O, 1.6) + eo(160, 79, 34, 12, '#fffaf3', SW) + `<ellipse cx="160" cy="79" rx="30" ry="9" fill="none" stroke="#b993d6" stroke-width="1.4"/>` + txt(160, 83.5, 11, O, '꽃집 봄날') + tulip(122, 77, '#ff8fa3') + tulip(198, 77, '#ffd75a'),
    sl('M140 60 V66 M180 60 V66', O, 1.6) + eo(160, 79, 36, 13, '#b993d6', SW) + `<ellipse cx="160" cy="79" rx="31" ry="9.5" fill="none" stroke="#fff" stroke-width="1.4"/>` +
      txt(160, 83.5, 11.5, '#fff', '꽃집 봄날', `stroke="${O}" stroke-width="2.6" paint-order="stroke"`) +
      Array.from({ length: 11 }, (_, j) => { const a = Math.PI + j * Math.PI / 10; return flower((160 + Math.cos(a) * 38).toFixed(1), (79 + Math.sin(a) * 15).toFixed(1), ['#ff8fa3', '#fff', '#ffd75a'][j % 3]); }).join(''),
  ][L.fsign];
  P.fwindow = [
    po('M84 98 H152 V168 H84 Z', '#9c8b7e', SW) + p('M90 104 H146 V162 H90Z', '#c0c9cc') + sl('M118 104 V162 M90 133 H146', O, 1.8) +
      g('rotate(16 118 133)', po('M80 128 H156 V137 H80 Z', '#b0906f', 2.2)) + sl('M90 104 l10 7 M90 104 l3 10', '#eee', 1),
    po('M84 98 H152 V168 H84 Z', '#fff', SW) + p('M90 104 H146 V162 H90Z', '#e3f4fb') + p('M93 107 l12 0 l-12 18z', 'rgba(255,255,255,.8)') + sl('M118 104 V140', O, 1.6) +
      [98, 118, 138].map((x, j) => po(`M${x - 6} 152 H${x + 6} L${x + 4} 162 H${x - 4} Z`, '#e98a5a', 1.8) + (j === 1 ? flower(x, 146, '#ff8fa3') + flower(x - 4, 149, '#fff') : po(`M${x} 152 Q${x - 6} 144 ${x - 3} 140 M${x} 152 Q${x + 5} 143 ${x + 2} 139`, 'none', 1.6) + eo(x - 3, 140, 3, 2, '#7fd47a', 1.4) + eo(x + 2, 139, 3, 2, '#7fd47a', 1.4))).join('') +
      po('M80 166 H156 V172 H80Z', '#8fd6b9', 2),
    po('M84 168 V118 Q84 96 118 96 Q152 96 152 118 V168 Z', '#fff', SW) + p('M90 162 V119 Q90 102 118 102 Q146 102 146 119 V162Z', '#e3f4fb') +
      [100, 136].map(x => sl(`M${x} 104 V112`, O, 1.2) + po(`M${x - 7} 112 H${x + 7} Q${x + 6} 120 ${x} 120 Q${x - 6} 120 ${x - 7} 112Z`, '#d99b5b', 1.6) + sl(`M${x - 5} 120 Q${x - 7} 130 ${x - 4} 138 M${x + 4} 120 Q${x + 6} 132 ${x + 3} 140`, '#3f9a74', 1.5) + eo(x - 4, 130, 2, 1.4, '#7fd47a', 1) + eo(x + 5, 132, 2, 1.4, '#7fd47a', 1) + flower(x - 3, 111, '#ff8fa3') + flower(x + 3, 110, '#fff')).join('') +
      po('M80 166 H156 V178 H80Z', '#d99b5b', 2) + [86, 96, 106, 116, 126, 136, 146].map((x, j) => flower(x, 164, ['#ff8fa3', '#fff', '#ffd75a', '#b9a6ff'][j % 4])).join(''),
  ][L.fwindow];
  P.fstand = [
    po('M214 188 H236 V204 H214Z', '#c49a6c', 2.2) + sl('M214 194 H236 M214 199 H236', 'rgba(91,58,50,.4)', 1.2) + g('rotate(-12 246 198)', po('M238 192 H256 V204 H238Z', '#c49a6c', 2.2)) + po('M226 186 L244 182', 'none', 2.4),
    bucket(218, '#ff8fa3', '#fff') + bucket(236, '#ffd75a', '#ff8fa3') + bucket(254, '#b9a6ff', '#fff'),
    po('M212 204 V196 H260 V204 M218 196 V186 H254 V196 M224 186 V176 H248 V186', '#d99b5b', 2) +
      [218, 236, 254].map((x, j) => g(`translate(0 ${j === 1 ? -10 : 0})`, bucket(x, ['#ff8fa3', '#ffd75a', '#b9a6ff'][j], '#fff'))).join('') + g('translate(0 -20)', bucket(236, '#ff5d73', '#fff')),
  ][L.fstand];
  P.ftree = [
    po('M24 204 L26 186 H42 L44 204Z', '#a5683e', 2.2) + eo(34, 186, 8, 2.6, '#d29763', 2) + sl('M34 186 Q36 178 40 176', '#6cc46a', 1.8) + eo(41, 175, 2.6, 1.6, '#7fd47a', 1.2),
    po('M30 204 L32 150 H38 L40 204Z', '#a5683e', 2.2) + roundTree(35, 128, 26, '#7fcf7a', '#3f9a74', '#c4ec8a'),
    po('M30 204 L32 150 H38 L40 204Z', '#a5683e', 2.2) + roundTree(35, 126, 30, '#ffc2d4', '#ff8fa3', '#fff') +
      [[20, 118], [44, 112], [30, 134], [50, 132], [14, 132]].map(([x, y]) => flower(x, y, '#fff')).join('') +
      [[10, 170], [56, 162], [22, 186], [60, 190]].map(([x, y]) => e(x, y, 2.2, 1.4, '#ff9db0')).join(''),
  ][L.ftree];
  const bench = c => po('M266 176 H314 V184 H266Z', c, 2) + po('M264 188 H316 V193 H264Z', c, 2) + po('M268 193 V204 M312 193 V204 M270 184 V188 M310 184 V188', 'none', 2.2);
  P.fbench = [
    g('rotate(8 290 196)', po('M264 190 H312 V195 H264Z', '#b8a596', 2)) + po('M300 196 V204', 'none', 2.2) + g('rotate(-14 280 178)', po('M268 176 H300 V183 H268Z', '#b8a596', 2)) + sl('M306 200 l5 -4', O, 1.6),
    bench('#d99b5b'),
    bench('#d99b5b') + g('translate(286 180)', eo(0, 2, 10, 6, '#ffc985', 2) + po('M-9 -3 L-8 -10 L-3 -5 Z M-1 -5 L4 -10 L4 -3 Z', '#ffc985', 1.8) + eo(-3, -1, 7, 5.5, '#ffc985', 2) +
      sl('M-6 -1.4 q1 -1 2 0 M-1.5 -1.4 q1 -1 2 0', O, 1.2) + e(-7.5, 1, 1.4, .8, 'rgba(255,120,150,.6)') + e(1.5, 1, 1.4, .8, 'rgba(255,120,150,.6)') + sl('M9 4 Q14 2 12 -2', '#e8955f', 2.4)) +
      po('M304 180 H316 L314 188 H306Z', '#e98a5a', 1.8) + flower(310, 176, '#ff8fa3'),
  ][L.fbench];
  return P;
}

function iceParts(L) {
  const P = {}, wl = L.iwall;
  const roof = ['#b3a79c', '#ff9db0', '#ff8fa3'][wl];
  P.iwall = po('M84 90 Q160 50 236 90 Z', roof, SW) + (wl === 2 ? [[120, 76], [140, 70], [160, 68], [180, 70], [200, 76], [130, 82], [170, 80], [190, 84]].map(([x, y], j) => p(`M${x} ${y} l3 -1 l.6 1.5 l-3 1z`, ['#fff', '#ffe58a', '#9fe3c9'][j % 3])).join('') : '') +
    po('M92 92 H228 V200 H92 Z', wl ? '#fff' : '#d6cec6', SW) +
    (wl ? Array.from({ length: 6 }, (_, j) => p(`M${94 + j * 22} 94 h11 v105 h-11z`, '#a9e4d0')).join('') + po('M92 92 H228 V200 H92 Z', 'none', SW) : sl('M100 100 L106 112 L102 122 M220 170 L212 180', O, 1.5) + p('M196 104 h16 v12 h-16z', '#c7bdb3')) +
    po('M82 88 H238 V96 H82Z', wl ? '#ffd75a' : '#aea398', 2.4) +
    (wl === 2 ? Array.from({ length: 10 }, (_, j) => `<path d="M${82 + j * 15.6} 96 a7.8 5 0 0 0 15.6 0" fill="#ff8fa3" stroke="${O}" stroke-width="1.8"/>`).join('') : '');
  P.icounter = [
    po('M112 112 H208 V164 H112Z', '#b9b4ae', SW) + sl('M112 120 H208 M112 128 H208 M112 136 H208 M112 144 H208 M112 152 H208', 'rgba(91,58,50,.35)', 1.3) + po('M156 156 h8 v7 h-8z', '#8d7a6c', 1.6) + po('M108 164 H212 V172 H108Z', '#aea398', 2.2),
    po('M112 112 H208 V164 H112Z', '#fff6e6', SW) + [[124, '#ff9db0'], [144, '#7a4630'], [164, '#9fe3c9'], [184, '#ffe58a'], [200, '#fff']].map(([x, c]) => po(`M${x - 8} 160 Q${x - 8} 148 ${x} 148 Q${x + 8} 148 ${x + 8} 160Z`, c, 1.8)).join('') +
      p('M114 114 H206 V130 H114Z', 'rgba(255,255,255,.55)') + po('M108 164 H212 V172 H108Z', '#fff', 2.2),
    po('M112 112 H208 V164 H112Z', '#fff6e6', SW) + [[124, '#ff9db0'], [144, '#7a4630'], [164, '#9fe3c9'], [184, '#ffe58a'], [200, '#fff']].map(([x, c]) => po(`M${x - 8} 160 Q${x - 8} 148 ${x} 148 Q${x + 8} 148 ${x + 8} 160Z`, c, 1.8)).join('') +
      po('M108 164 H212 V172 H108Z', '#fff', 2.2) + p('M106 104 H214 V114 H106Z', '#fff') + Array.from({ length: 6 }, (_, j) => j % 2 ? '' : p(`M${106 + j * 18} 104 h18 v10 h-18z`, '#ff8fa3')).join('') + po('M106 104 H214 V114 H106Z', 'none', 2) +
      Array.from({ length: 6 }, (_, j) => `<path d="M${106 + j * 18} 114 a9 5 0 0 0 18 0" fill="${j % 2 ? '#fff' : '#ff8fa3'}" stroke="${O}" stroke-width="1.8"/>`).join('') +
      po('M196 156 L201 172 L206 156Z', '#e9b064', 1.6) + eo(201, 152, 5.5, 5, '#ff9db0', 1.6),
  ][L.icounter];
  const cone = (x, y, s, c) => g(`translate(${x} ${y}) scale(${s})`, po('M-10 0 L0 30 L10 0 Z', c, 2.4) + (c === '#e9b064' ? sl('M-6 4 L4 20 M2 2 L-4 16 M6 4 L-1 22', '#b8673e', 1.4) : sl('M-4 6 L2 14', O, 1.4)));
  P.isign = [
    g('rotate(-10 160 60)', cone(160, 34, 1, '#cfc6bd')),
    cone(160, 36, 1, '#e9b064') + eo(160, 30, 12, 10, '#ff9db0', SW) + p('M152 36 q2 5 4 0 q2 6 4 0', '#ff9db0') + e(155, 26, 3, 2, '#ffd0d8'),
    bulbs([[136, 60], [146, 46], [160, 40], [174, 46], [184, 60]], ['#ffe27a', '#fff', '#9fe3c9']) +
      cone(160, 40, 1, '#e9b064') + eo(160, 34, 12, 9, '#9fe3c9', SW) + eo(160, 22, 11, 8.5, '#ff9db0', SW) + eo(160, 11, 9.5, 7.5, '#7a4630', SW) +
      [[154, 20], [165, 23], [158, 26], [163, 33], [153, 34]].map(([x, y], j) => p(`M${x} ${y} l3 -1 l.6 1.5 l-3 1z`, ['#fff', '#ffe58a', '#ff5d73'][j % 3])).join('') + eo(160, 2, 3.6, 3.4, '#ff5d73', 2),
  ][L.isign];
  P.ifount = [
    po('M10 186 H82 V204 H10 Z', '#c9c2ba', 2.4) + eo(46, 186, 36, 5, '#bdb5ad', 2.4) + sl('M24 190 L30 198 M60 188 L56 196', O, 1.4) + po('M42 186 V168 H50 V186', '#c9c2ba', 2.2),
    po('M10 186 H82 V204 H10 Z', '#dfe6f5', 2.4) + eo(46, 186, 36, 5, '#9fdcf2', 2.4) + po('M42 186 V164 H50 V186', '#dfe6f5', 2.2) +
      `<path d="M46 162 Q30 160 24 182 M46 162 Q62 160 68 182" fill="none" stroke="#9fdcf2" stroke-width="3"/>` + e(46, 160, 4, 3, '#9fdcf2'),
    po('M8 186 H84 V204 H8 Z', '#dfe6f5', 2.4) + eo(46, 186, 38, 5.5, '#9fdcf2', 2.4) + po('M42 186 V158 H50 V186', '#dfe6f5', 2.2) + eo(46, 158, 16, 4, '#9fdcf2', 2.2) + po('M44 158 V146 H48 V158', '#dfe6f5', 1.8) +
      `<path d="M46 144 Q36 142 32 156 M46 144 Q56 142 60 156 M34 160 Q22 162 20 182 M58 160 Q70 162 72 182" fill="none" stroke="#9fdcf2" stroke-width="2.6"/>` + e(46, 143, 3, 2.4, '#bfeaf8') +
      [12, 22, 70, 80].map((x, j) => flower(x, 200, ['#ff8fa3', '#fff', '#ffd75a', '#ff8fa3'][j])).join('') +
      g('translate(66 152)', eo(0, 0, 4, 3, '#fff', 1.4) + p('M3 -1 l3 -1 l-1 2z', '#ffb347') + e(1.5, -1, .6, .6, O)),
  ][L.ifount];
  const cartBox = c => po('M248 168 H306 V192 H248Z', c, 2.2) + p('M249 176 H305 V182 H249Z', '#ff8fa3') + po('M248 168 H306 V192 H248Z', 'none', 2.2) + eo(258, 198, 6, 6, '#fff', 2.2) + eo(296, 198, 6, 6, '#fff', 2.2) + e(258, 198, 2, 2, O) + e(296, 198, 2, 2, O) + po('M306 172 L316 166', 'none', 2.6);
  P.icart = [
    g('rotate(4 280 190)', po('M248 170 H306 V192 H248Z', '#b9a99a', 2.2) + sl('M256 176 l6 4 M290 184 l8 -3', 'rgba(91,58,50,.4)', 1.4)) + eo(258, 198, 6, 6, '#a99c90', 2.2) + po('M290 202 Q296 196 302 202Z', '#a99c90', 2) + po('M306 176 L314 184', 'none', 2.6),
    po('M277 168 V120', 'none', 2) + po('M250 128 Q277 104 304 128 Z', '#fff', 2.2) + p('M262 122 Q270 113 277 111 V128 H262Z', '#9fe3c9') + p('M292 122 Q284 113 277 111 V111 L294 128 H292Z', '#9fe3c9') + po('M250 128 Q277 104 304 128 Z', 'none', 2.2) + cartBox('#fff'),
    po('M277 168 V120', 'none', 2) + po('M250 128 Q277 104 304 128 Z', '#fff', 2.2) + p('M262 122 Q270 113 277 111 V128 H262Z', '#9fe3c9') + p('M292 122 Q284 113 277 111 V111 L294 128 H292Z', '#9fe3c9') + po('M250 128 Q277 104 304 128 Z', 'none', 2.2) +
      sl('M246 168 Q240 140 236 116 M246 168 Q246 136 248 108 M246 168 Q252 142 258 120', O, 1.2) + eo(236, 110, 7, 8.5, '#ff8fa3', 2) + eo(248, 101, 7, 8.5, '#ffd75a', 2) + eo(259, 114, 7, 8.5, '#9fe3c9', 2) +
      cartBox('#fff') + po('M273 160 L277 174 L281 160Z', '#e9b064', 1.4) + eo(277, 157, 5, 4.5, '#ff9db0', 1.4),
  ][L.icart];
  return P;
}

function parkParts(L) {
  const P = {};
  P.plawn = [
    p('M0 166 Q80 158 160 164 Q240 158 320 166 V199 H0Z', '#d9c3a3') + sl('M30 190 l-2 -6 M33 190 l1 -7 M120 186 l-2 -5 M123 186 l2 -6 M250 192 l-2 -6 M253 192 l2 -5', '#8fae5a', 1.6) + e(200, 184, 10, 3, '#cdb48f') + e(70, 178, 8, 2.5, '#cdb48f'),
    p('M0 164 Q80 156 160 162 Q240 156 320 164 V199 H0Z', '#a8e08f') + [[30, 186, '#fff'], [96, 178, '#ff8fa3'], [226, 182, '#ffd75a'], [290, 176, '#fff']].map(([x, y, c]) => flower(x, y, c)).join(''),
    p('M0 162 Q80 154 160 160 Q240 154 320 162 V199 H0Z', '#a8e08f') +
      [[72, 188], [250, 188]].map(([x, y]) => eo(x, y, 22, 7, '#c9a27a', 2) + Array.from({ length: 7 }, (_, j) => flower(x - 15 + j * 5, y - 2 + (j % 2) * 3, ['#ff8fa3', '#fff', '#ffd75a', '#b9a6ff'][j % 4])).join('')).join('') +
      [[150, 192], [164, 184], [156, 176]].map(([x, y]) => eo(x, y, 6, 2.6, '#e6dfd6', 1.6)).join(''),
  ][L.plawn];
  const posts = c => [118, 142, 178, 202].map(x => po(`M${x - 3} 124 H${x + 3} V184 H${x - 3}Z`, c, 2)).join('');
  P.pgazebo = [
    po('M104 184 H216 V194 H104Z', '#c9c2ba', 2.2) + po('M115 124 H121 V184 H115Z', '#bdb5ad', 2) + po('M139 124 H145 V184 H139Z', '#bdb5ad', 2) + po('M175 124 H181 V184 H175Z', '#bdb5ad', 2) + g('rotate(18 204 170)', po('M199 150 H205 V184 H199Z', '#bdb5ad', 2)) +
      po('M100 124 L160 80 L190 102 L180 112 L196 124 Z', '#a99c90', 2.4) + sl('M196 124 L208 120 L220 124', O, 1.6),
    po('M104 184 H216 V194 H104Z', '#e6d3bd', 2.2) + posts('#fff') + po('M100 124 L160 80 L220 124 Z', '#ff9db0', 2.4) + po('M98 122 H222 V130 H98Z', '#fff', 2) + po('M160 80 V70', 'none', 2) + eo(160, 68, 3, 3, '#ffd75a', 1.6) +
      sl('M118 130 Q130 140 142 130 M178 130 Q190 140 202 130', O, 1.6),
    po('M104 184 H216 V194 H104Z', '#e6d3bd', 2.2) + posts('#fff') + po('M100 124 L160 80 L220 124 Z', '#ff8fa3', 2.4) + sl('M130 102 L190 102 M115 113 L205 113', 'rgba(255,255,255,.5)', 1.8) + po('M98 122 H222 V130 H98Z', '#fff', 2) + po('M160 80 V70', 'none', 2) + eo(160, 67, 3.4, 3.4, '#ffd75a', 1.6) +
      Array.from({ length: 13 }, (_, j) => flower(100 + j * 10, 131 + (j % 2) * 2, ['#ff8fa3', '#fff', '#ffd75a'][j % 3])).join('') +
      sl('M118 138 Q130 148 142 138 M178 138 Q190 148 202 138', O, 1.2) + bulbs([[124, 142], [136, 142], [184, 142], [196, 142]], ['#ffe27a', '#fff']) +
      [130, 190].map(x => po(`M${x} 130 V146`, 'none', 1.2) + po(`M${x - 4} 146 h8 v12 h-8z`, '#ff5d73', 1.6) + sl(`M${x - 4} 150 h8 M${x - 4} 154 h8`, '#ffd75a', 1)).join(''),
  ][L.pgazebo];
  const frame = c => po('M14 200 L30 120 L46 200 M50 200 L66 120 L82 200', 'none', 3.4) + po('M24 120 H72', 'none', 4) + sl('M14 200 L30 120 L46 200 M50 200 L66 120 L82 200 M24 120 H72', c, 1.8);
  P.pswing = [
    frame('#bdb5ad') + po('M40 120 V170', 'none', 1.6) + g('rotate(12 40 172)', po('M32 170 H48 V174 H32Z', '#b8a596', 1.8)) + po('M56 120 V138 Q60 146 54 150', 'none', 1.6),
    frame('#8fd6b9') + po('M36 120 V170 M50 120 V170', 'none', 1.6) + po('M33 170 H53 V175 H33Z', '#ff8fa3', 1.8),
    frame('#8fd6b9') + po('M36 120 V170 M50 120 V170', 'none', 1.6) + po('M33 170 H53 V175 H33Z', '#ff8fa3', 1.8) +
      po('M86 200 V146 M98 200 V146', 'none', 2) + po('M84 146 H100 V150 H84Z', '#ffd75a', 1.8) + po('M98 150 Q102 176 118 198 L110 200 Q96 178 92 150Z', '#9fe3c9', 2) + flower(20, 198, '#ff8fa3') + flower(70, 198, '#fff'),
  ][L.pswing];
  P.pbus = [
    g('rotate(-14 286 204)', po('M284 204 V144', 'none', 3) + eo(284, 140, 9, 9, '#cfcac4', 2.2) + txt(284, 143.5, 7, '#8d7a6c', '버스')) + g('rotate(10 260 196)', po('M244 192 H276 V196 H244Z', '#b8a596', 1.8)) + po('M252 197 V204', 'none', 2),
    po('M234 132 H312 V138 H234Z', '#46557a', 2.2) + po('M238 138 H308 V188 H238Z', 'rgba(227,244,251,.7)', 2) + po('M236 138 V204 M310 138 V204', 'none', 2.6) +
      po('M244 188 H302 V193 H244Z', '#d99b5b', 1.8) + po('M248 193 V204 M298 193 V204', 'none', 2) + po('M318 204 V130', 'none', 2.4) + eo(318, 124, 9, 9, '#8fd6b9', 2.2) + txt(318, 127.5, 7, '#fff', '버스'),
    po('M234 132 H312 V138 H234Z', '#46557a', 2.2) + e(273, 140, 4, 2.4, '#ffe27a') + po('M238 138 H308 V188 H238Z', 'rgba(227,244,251,.7)', 2) + po('M236 138 V204 M310 138 V204', 'none', 2.6) +
      po('M282 146 h20 v28 h-20z', '#ff9db0', 1.8) + heart(292, 158, .5, '#fff') + txt(292, 170, 5, '#fff', 'CAFE') +
      po('M244 188 H302 V193 H244Z', '#d99b5b', 1.8) + po('M248 193 V204 M298 193 V204', 'none', 2) + po('M318 204 V130', 'none', 2.4) + eo(318, 124, 9, 9, '#8fd6b9', 2.2) + txt(318, 127.5, 7, '#fff', '버스') +
      po('M242 178 H254 L252 188 H244Z', '#e98a5a', 1.6) + flower(248, 174, '#ff8fa3'),
  ].map(x => g('translate(-10 0)', x))[L.pbus];
  return P;
}
const PARK_BG = roundTree(30, 118, 26, '#9bd88a', '#5fae74', '#d0f0a0') + roundTree(292, 112, 28, '#9bd88a', '#5fae74', '#d0f0a0') + roundTree(150, 104, 18, '#b6e3a2', '#7cc08a', '#e0f6b8');

const AREA_ART = {
  cafe: { parts: L => sceneParts(L), order: ['wall', 'window', 'door', 'planter', 'sign', 'awning', 'lamp', 'terrace'], extra: '' },
  flower: { parts: flowerParts, order: ['fwall', 'fwindow', 'fsign', 'fstand', 'ftree', 'fbench'], extra: '' },
  ice: { parts: iceParts, order: ['iwall', 'icounter', 'isign', 'ifount', 'icart'], extra: '' },
  park: { parts: parkParts, order: ['plawn', 'pgazebo', 'pswing', 'pbus'], extra: PARK_BG },
};
Object.assign(SPOT_BOX, {
  fwall: '50 10 220 194', fsign: '118 58 84 40', fwindow: '76 90 84 92', fstand: '206 160 58 46', ftree: '2 92 64 114', fbench: '258 160 62 46',
  iwall: '78 46 164 158', icounter: '102 100 116 76', isign: '128 -4 64 74', ifount: '2 136 88 70', icart: '230 96 90 110',
  plawn: '0 150 320 52', pgazebo: '94 60 132 140', pswing: '6 112 116 94', pbus: '226 112 94 94',
});
// ---- painted area scenes (base by wall level + prop stickers) ----
const PAINT_D = __PAINT__;
const PAINT = {};
for (const [a, d] of Object.entries(PAINT_D || {})) {
  const m = o => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, toUrl(v)]));
  PAINT[a] = Object.assign({}, d, { behind: d.behind || [], fg: d.fg ? d.fg.map(f => Object.assign({}, f, { u: toUrl(f.u) })) : null, base: d.base.map(toUrl), cut: d.cut ? d.cut.map(c => Object.assign({}, c, { u: toUrl(c.u) })) : null, p: { 1: m(d.p[1]), 2: m(d.p[2]) }, K: d.W / 320 });
}
const CAFE_BOX = PAINT.cafe ? PAINT.cafe.box : null;
const PAINT_DEFS = '<defs><filter id="cfDs" x="-15%" y="-15%" width="130%" height="140%"><feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#5b3a32" flood-opacity=".28"/></filter><filter id="cfBl" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="7"/></filter></defs>';
function spotPos(area, k) {
  const P = PAINT[area]; if (!P) return null;
  if (k === P.baseKey) return [50, 10];
  const r = P.rect[k] && (P.rect[k][1] || P.rect[k]['1']); if (!r) return null;
  return [(r[0] + r[2] / 2) / P.W * 100, (r[1] + r[3] * .45) / P.H * 100];
}
// 벽 단계마다 창문 위치가 다른 가게용
function rectOf(P, sp, lv, wl) { const o = P.rectW && P.rectW[wl] && P.rectW[wl][sp]; return (o && o[lv]) || P.rect[sp][lv]; }
function paintBox(area, k) { const P = PAINT[area]; return P && P.box[k]; }
function paintScene(area, L, vb, anim) {
  const P = PAINT[area], v = vb.split(' ').map(n => (+n * P.K).toFixed(1)).join(' ');
  const wl = L[P.baseKey] || 0;
  let h = `<g data-spot="${P.baseKey}" ${anim === P.baseKey ? 'class="sp-new"' : ''}><image href="${P.base[wl]}" x="0" y="0" width="${P.W}" height="${P.H}" preserveAspectRatio="none"/></g>`;
  let fgDone = !P.fg;
  for (const sp of P.order) {
    const lv = L[sp] || 0;
    if (!fgDone && !P.behind.includes(sp)) { const f = P.fg[wl]; h += `<image href="${f.u}" x="${f.x}" y="${f.y}" width="${f.w}" height="${f.h}" preserveAspectRatio="none" pointer-events="none"/>`; fgDone = true; }
    if (!lv) continue;
    const [x, y, w, hh] = rectOf(P, sp, lv, wl);
    let inner = '';
    const op = P.open[sp];
    if (op && P.fill[wl]) inner += `<rect x="${op[0]}" y="${op[1]}" width="${op[2]}" height="${op[3]}" fill="${P.fill[wl]}"/>`;
    const ground = P.ground.includes(sp);
    if (ground) inner += `<ellipse cx="${(x + w / 2).toFixed(1)}" cy="${(y + hh).toFixed(1)}" rx="${(w * .42).toFixed(1)}" ry="13" fill="rgba(91,58,50,.3)" filter="url(#cfBl)"/>`;
    inner += `<image href="${P.p[lv][sp]}" x="${x}" y="${y}" width="${w}" height="${hh}" preserveAspectRatio="none"${ground ? '' : ' filter="url(#cfDs)"'}/>`;
    // 같은 장식을 반대쪽 창문에도 (창문이 두 개인 가게)
    const tw = P.twin && P.twin[sp] && P.twin[sp][lv];
    if (tw) inner += `<image href="${P.p[lv][sp]}" x="${tw[0]}" y="${tw[1]}" width="${tw[2]}" height="${tw[3]}" preserveAspectRatio="none"${ground ? '' : ' filter="url(#cfDs)"'}/>`;
    h += `<g data-spot="${sp}" ${anim === sp ? 'class="sp-new"' : ''}>${inner}</g>`;
  }
  return `<svg viewBox="${v}" xmlns="http://www.w3.org/2000/svg">${PAINT_DEFS}${h}</svg>`;
}
// ---- town (village overview) ----
const TOWN_BG_D = __TOWNBG__;
const TOWN_BG = { u: toUrl(TOWN_BG_D.u), w: TOWN_BG_D.w, h: TOWN_BG_D.h, p: toUrl(TOWN_BG_D.p), pt: TOWN_BG_D.pt, ph: TOWN_BG_D.ph };
const TOWN_BG2_D = __TOWNBG2__;
const TOWN_BG2 = { u: toUrl(TOWN_BG2_D.u), w: TOWN_BG2_D.w, h: TOWN_BG2_D.h, p: toUrl(TOWN_BG2_D.p), pt: TOWN_BG2_D.pt, ph: TOWN_BG2_D.ph };
function propSvg(P, sp, lv, wl, rect) {
  const [x, y, w, hh] = rect;
  let inner = '';
  const op = P.open[sp];
  if (op && P.fill[wl]) inner += `<rect x="${op[0]}" y="${op[1]}" width="${op[2]}" height="${op[3]}" fill="${P.fill[wl]}"/>`;
  const ground = P.ground.includes(sp);
  if (ground) inner += `<ellipse cx="${(x + w / 2).toFixed(1)}" cy="${(y + hh).toFixed(1)}" rx="${(w * .42).toFixed(1)}" ry="13" fill="rgba(91,58,50,.3)" filter="url(#cfBl)"/>`;
  inner += `<image href="${P.p[lv][sp]}" x="${x}" y="${y}" width="${w}" height="${hh}" preserveAspectRatio="none"${ground ? '' : ' filter="url(#cfDs)"'}/>`;
  const tw = P.twin && P.twin[sp] && P.twin[sp][lv];
  if (tw && rect === rectOf(P, sp, lv, wl)) inner += `<image href="${P.p[lv][sp]}" x="${tw[0]}" y="${tw[1]}" width="${tw[2]}" height="${tw[3]}" preserveAspectRatio="none"${ground ? '' : ' filter="url(#cfDs)"'}/>`;
  return inner;
}
function townLot(area, L) {
  const P = PAINT[area]; if (!P) return null;
  const wl = L[P.baseKey] || 0;
  let h = '';
  if (area === 'plaza') {
    if (!wl) return null;
    h += `<ellipse cx="750" cy="${P.gy - 70}" rx="620" ry="200" fill="${wl === 2 ? '#f4f8fc' : '#e9d6bf'}" stroke="#5b3a32" stroke-width="7"/><ellipse cx="750" cy="${P.gy - 84}" rx="540" ry="150" fill="${wl === 2 ? '#ffffff' : '#f1e2cf'}"/>`;
    for (const sp of P.order) { const lv = L[sp] || 0; if (lv) h += propSvg(P, sp, lv, wl, P.rect[sp][lv]); }
  } else if (area === 'park') {
    h += `<ellipse cx="720" cy="${1000}" rx="700" ry="110" fill="#a8d77a" stroke="#5b3a32" stroke-width="7"/><ellipse cx="720" cy="${990}" rx="640" ry="80" fill="#bfe28e"/>`;
    if (wl) h += [[300, 985], [560, 1010], [900, 1012], [1140, 985]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="16" fill="#ffb3c1" stroke="#5b3a32" stroke-width="5"/><circle cx="${x}" cy="${y}" r="6" fill="#ffd75a"/>`).join('');
    for (const sp of P.order) { const lv = L[sp] || 0; if (lv) h += propSvg(P, sp, lv, wl, P.townRect[sp][lv]); }
  } else {
    for (const sp of P.order) if (P.behind.includes(sp) && L[sp]) h += propSvg(P, sp, L[sp], wl, rectOf(P, sp, L[sp], wl));
    const c = P.cut[wl];
    h += `<image href="${c.u}" x="${c.x}" y="${c.y}" width="${c.w}" height="${c.h}" preserveAspectRatio="none"/>`;
    for (const sp of P.order) if (!P.behind.includes(sp) && L[sp]) h += propSvg(P, sp, L[sp], wl, rectOf(P, sp, L[sp], wl));
  }
  const [lx, ly, lw, lh] = P.lot;
  return { svg: `<svg viewBox="${lx} ${ly} ${lw} ${lh}" xmlns="http://www.w3.org/2000/svg" overflow="visible">${PAINT_DEFS}${h}</svg>`, lot: P.lot, ground: P.gy };
}
function townFence(name) {
  const K = 4.7;
  const svg = `<svg viewBox="14 92 292 116" xmlns="http://www.w3.org/2000/svg" stroke-linejoin="round" stroke-linecap="round" overflow="visible">` +
    Array.from({ length: 15 }, (_, j) => po(`M${24 + j * 19} 200 V146 L${31 + j * 19} 140 L${38 + j * 19} 146 V200 Z`, j % 2 ? '#e9c79a' : '#ddb886', 2)).join('') +
    po('M18 160 H302 M18 186 H302', 'none', 3) + sl('M18 160 H302 M18 186 H302', '#c49a6c', 1.4) +
    po('M110 96 h100 v40 h-100 z', '#ffd75a', SW) + sl('M114 100 h92 v32 h-92 z', O, 1.2) + txt(160, 116, 13, O, '공사 중') + txt(160, 130, 9, O, esc2(name)) + po('M130 136 V150 M190 136 V150', 'none', 3) +
    [[60, 204], [262, 204]].map(([x, y]) => po(`M${x - 9} ${y} L${x - 4} ${y - 22} H${x + 4} L${x + 9} ${y} Z`, '#ff9a5a', 2) + p(`M${x - 6} ${y - 9} H${x + 6} L${x + 6.6} ${y - 5} H${x - 6.6}Z`, '#fff') + po(`M${x - 12} ${y} H${x + 12}`, 'none', 2.4)).join('') + '</svg>';
  return { svg, lot: [14 * K, 92 * K, 292 * K, 116 * K], ground: 200 * K };
}
function areaScene(area, L, vb = '0 0 320 240', anim = '') {
  if (PAINT[area]) return paintScene(area, L, vb, anim);
  const A = AREA_ART[area], parts = A.parts(L);
  return `<svg viewBox="${vb}" xmlns="http://www.w3.org/2000/svg" stroke-linejoin="round" stroke-linecap="round">${SCENE_BG}${A.extra}${A.order.map(k => `<g data-spot="${k}" ${anim === k ? 'class="sp-new"' : ''}>${parts[k]}</g>`).join('')}</svg>`;
}
function lockedScene(name) {
  return `<svg viewBox="0 0 320 240" xmlns="http://www.w3.org/2000/svg" stroke-linejoin="round" stroke-linecap="round">${SCENE_BG}` +
    p('M20 150 H300 V199 H20Z', '#d9c3a3') +
    Array.from({ length: 15 }, (_, j) => po(`M${24 + j * 19} 200 V146 L${31 + j * 19} 140 L${38 + j * 19} 146 V200 Z`, j % 2 ? '#e9c79a' : '#ddb886', 2)).join('') +
    po('M18 160 H302 M18 186 H302', 'none', 3) + sl('M18 160 H302 M18 186 H302', '#c49a6c', 1.4) +
    po('M110 96 h100 v40 h-100 z', '#ffd75a', SW) + sl('M114 100 h92 v32 h-92 z', O, 1.2) + txt(160, 116, 13, O, '공사 중') + txt(160, 130, 9, O, esc2(name)) + po('M130 136 V150 M190 136 V150', 'none', 3) +
    [[60, 204], [262, 204]].map(([x, y]) => po(`M${x - 9} ${y} L${x - 4} ${y - 22} H${x + 4} L${x + 9} ${y} Z`, '#ff9a5a', 2) + p(`M${x - 6} ${y - 9} H${x + 6} L${x + 6.6} ${y - 5} H${x - 6.6}Z`, '#fff') + po(`M${x - 12} ${y} H${x + 12}`, 'none', 2.4)).join('') + '</svg>';
}
const esc2 = s => String(s).replace(/[&<>"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));
