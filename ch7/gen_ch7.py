STYLE = ("Cute cozy kawaii mobile game art in the exact style of the reference image: thick dark brown outlines (#5b3a32), "
         "soft pastel colors, flat cel shading with one soft shade per color and small soft highlights, clean simple rounded shapes, no texture, no grain.")
BG = ("Background, identical in all four panels: a sunny tropical island village. A light blue sky with a few round puffy white clouds, "
      "a calm turquoise sea with a straight horizon line behind the building, a round green island hill with a tiny white waterfall far behind, "
      "two tall round palm trees at the left and right edges, and a pale warm sand strip with a row of pale pink rounded paving stones running horizontally across the bottom of every panel.")
NOTXT = "No text, no letters, no numbers, no logos, no watermark, no frame or border."
TRANS = "Transparent background (PNG with a real alpha channel), no background color, no white box behind the objects."

shops = [
 dict(no=1, k='coconut', wratio='about 5 to 2 (two and a half times as wide as tall)', ratio='about 2 to 1 (twice as wide as tall)', mount='its own wall bracket arm on top', name='대롱 코코넛 가게', who='원숭이 대롱',
  bld="a small round bamboo hut with a thick thatched palm leaf roof, a wide rectangular counter window on the left half and a round-topped bamboo door on the right half",
  ruin="faded grey cracked bamboo, a messy torn thatched roof with holes, a dusty broken empty counter window, a fallen broken shutter, dry palm leaves piled at the door",
  plain="clean natural bamboo walls, a neat plain thatched roof, a plain wooden door, the counter window empty and dark",
  paint="pale peach bamboo walls with mint trim, a neat golden thatched roof with a row of small pink hibiscus flowers along the edge, a small coconut emblem above the door, the counter window still empty and dark",
  win1="a simple wooden counter with three plain brown coconuts and one coconut cup with a straw",
  win2="the same counter full of coconut cups with colorful straws and little paper umbrellas, a pile of green coconuts, pineapple slices and a string of tiny shell lights along the top",
  sign_pos="hanging from a small bracket on the right side, beside the door",
  sign1="a plain round wooden board with the Korean word \"코코넛\" in dark brown",
  sign2="the same round board painted mint with a peach scalloped border, a tiny coconut with a straw on top and two small palm leaves on the bottom corner",
  g=[("a coconut cart","a plain small wooden push cart with one closed lid","the same cart with a striped mint umbrella, open lid showing coconut cups and a little flower garland"),
     ("a drink table","a plain small round bamboo table with one stool","the same table with a peach cloth, two coconut drinks with straws and a tiny hibiscus vase"),
     ("a coconut palm pot","a small palm sapling in a plain clay pot","a bigger palm in a painted mint pot with three small coconuts")]),
 dict(no=2, k='lei', wratio='about 2 to 1 (twice as wide as tall)', ratio='about 3 to 2 (a little wider than tall)', mount='two short rope loops on top only', name='재잘 꽃목걸이 공방', who='앵무새 재잘',
  bld="a small wooden workshop on short stilts with a pointed thatched roof, a wide open window with a flat sill in the middle and a short wooden step at the door on the right",
  ruin="faded grey cracked boards, a torn sagging thatched roof, a cracked empty window, a fallen broken flower basket and wilted petals on the step",
  plain="clean natural wood walls, a neat plain thatched roof, the window empty and dark",
  paint="soft lilac painted walls with cream trim, a golden thatched roof, a row of small flower garlands under the roof edge, a small hibiscus emblem above the door, the window still empty and dark",
  win1="a simple work table with one plain flower garland and a small basket of white flowers",
  win2="the same table full of colorful flower leis in pink, yellow and lilac, baskets of plumeria and hibiscus and a row of hanging flower crowns at the top",
  sign_pos="hanging under the roof edge at the top center, above the window",
  sign1="a plain long wooden board with the Korean word \"꽃목걸이\" in dark brown",
  sign2="the same long board painted cream with a lilac border, the same Korean word, and a tiny pink flower garland draped along the top edge",
  g=[("a flower basket","a plain small woven basket with a few white flowers","the same basket overflowing with pink, yellow and lilac flowers and a lei on the rim"),
     ("a garland stand","a plain wooden stand with one plain garland","the same stand hung with three colorful leis and a little flower crown"),
     ("a parrot perch","a plain wooden perch on a short pole","the same perch wrapped with a flower garland and a tiny water cup")]),
 dict(no=3, k='mango', ratio='about 2 to 1 (twice as wide as tall)', mount='no hanging tabs, no hooks, no rings, no chains, no bracket: a flat plate mounted directly on the wall', name='통통 망고 빙수 오두막', who='하마 통통',
  bld="a small chubby round hut with a big rounded palm leaf roof like a mushroom cap, a wide rectangular serving window in the middle and a small round door on the right",
  ruin="faded grey cracked walls, a torn drooping leaf roof with holes, a cracked empty serving window, a tipped-over broken stool and dry leaves",
  plain="clean pale cream walls, a neat plain leaf roof, the serving window empty and dark",
  paint="pastel yellow walls with soft pink trim, a fresh green leaf roof, a small mango emblem above the door, the serving window still empty and dark",
  win1="a simple counter with one bowl of plain shaved ice and a whole mango",
  win2="the same counter with tall bowls of mango shaved ice topped with mango cubes, cream and a mint leaf, a stack of bowls and a row of small paper lanterns at the top",
  sign_pos="mounted flat on the wall at the top center, above the serving window",
  sign1="a plain long cream board with the Korean word \"빙수\" in dark brown",
  sign2="the same long board painted soft pink with yellow letters, a tiny mango on the left and a tiny bowl of shaved ice on the right",
  g=[("an ice shaver","a plain small hand-crank ice shaver on a stand","the same ice shaver painted yellow with a bowl of mango shaved ice under it"),
     ("a mango crate","one plain wooden crate","the same crate full of ripe mangos with green leaves and a pink ribbon"),
     ("a round stool pair","one plain round wooden stool","two stools painted pink and yellow with small cushions")]),
 dict(no=4, k='hammock', wratio='about 3 to 1 (a long, wide and low strip)', ratio='about 5 to 3 (a little wider than tall)', mount='a single short rope loop on top only', name='꾸벅 해먹 쉼터', who='나무늘보 꾸벅',
  bld="a small open-sided bamboo rest pavilion with a low wide thatched roof, a wide rectangular back wall window in the middle and a short bamboo railing at the front",
  ruin="faded grey cracked bamboo poles, a torn sagging roof with holes, a cracked empty window, a torn faded hammock lying on the floor",
  plain="clean natural bamboo poles, a neat plain thatched roof, the window empty and dark",
  paint="pale mint bamboo poles with cream trim, a golden thatched roof, a small leaf emblem above the window, the window still empty and dark",
  win1="a simple view of one plain hammock hanging between two posts",
  win2="the same view with a colorful striped hammock with soft pillows, a small lantern and a few hanging green vines with flowers",
  sign_pos="hanging from the roof edge at the top right corner",
  sign1="a plain wooden board shaped like a small leaf with the Korean word \"쉼터\" in dark brown",
  sign2="the same leaf-shaped board painted mint with a cream border, the same Korean word, and a tiny sleeping moon and star",
  g=[("a hammock stand","a plain wooden hammock frame with an empty plain hammock","the same frame with a striped pastel hammock and a pillow"),
     ("a pillow pile","one plain round cushion","a pile of three soft pastel cushions with a tassel"),
     ("a vine lantern","a plain bamboo lantern post, unlit","the same lantern lit warm and wrapped with a green flowering vine")]),
 dict(no=5, k='radio', wratio='about 2 to 1 (twice as wide as tall)', ratio='about 6 to 5 (almost square, only a little wider than tall)', mount='no hanging tabs, no hooks, no rings, no chains: a flat plate mounted directly on the wall', name='쫑긋 소라 방송국', who='큰부리새 쫑긋',
  bld="a small round hut shaped like a giant spiral conch shell lying on its side, with a rectangular window on the left, a small arched door on the right and a short bamboo antenna on top",
  ruin="faded grey cracked shell walls, a broken bent antenna, a cracked empty window, loose seaweed on the walls and a toppled stool",
  plain="clean pale cream shell walls, a straight plain antenna, the window empty and dark",
  paint="pastel coral and cream striped shell walls, a gold antenna with a tiny star on top, a small sound wave emblem above the door, the window still empty and dark",
  win1="a simple desk with one old round radio and one big conch shell",
  win2="the same desk with the radio glowing softly, a big conch shell on a small cushion, a pair of headphones, a small microphone and a string of tiny shell lights at the top",
  sign_pos="mounted flat on the wall at the top center, above the window and the door",
  sign1="a plain wooden board with the Korean word \"방송국\" in dark brown",
  sign2="the same board painted coral with cream letters, a tiny conch shell on the left and a tiny music note on the right",
  g=[("a speaker post","a plain wooden post with a plain round horn speaker","the same post painted coral with a gold horn speaker and a small flag"),
     ("a conch stand","a plain big conch shell on a short stand","the same conch polished pink and cream on a stand with a flower garland"),
     ("a record crate","one plain wooden crate","the same crate full of pastel records and a small potted fern")]),
 dict(no=6, k='raft', wratio='about 3 to 2 (a little wider than tall)', ratio='about 6 to 5 (almost square, only a little wider than tall)', mount='two short rope loops on top only', name='폴짝 뗏목 나루터', who='청개구리 폴짝',
  bld="a small wooden explorers' hut on a short pier, with a rectangular map window on the left, a wide entrance in the middle and a small lookout platform on the right, and the tip of a little bamboo raft with a leaf sail peeking up behind the hut",
  ruin="grey weathered boards, a broken lookout platform, a cracked empty map window, a torn leaf sail behind, loose planks on the pier",
  plain="clean natural wood walls, a whole plain lookout platform, a plain leaf sail behind, the map window empty and dark",
  paint="pastel mint walls with sunny yellow trim, a soft teal roof, a small compass emblem above the entrance, a fresh green leaf sail behind, the map window still empty and dark",
  win1="a simple wall with one plain rolled map and a small brass compass",
  win2="the same wall with an open island map pinned up showing a small sea cave, a coil of rope, a little lantern and a small potted fern",
  sign_pos="hanging over the entrance at the top center",
  sign1="a plain oval wooden board framed with rope, with the Korean word \"나루터\" in dark brown",
  sign2="the same rope-framed oval board painted mint with yellow letters and two tiny leaf flags at the sides; no compass on the sign (the building already has a compass emblem right above it)",
  g=[("a paddle rack","a plain wooden rack with one plain paddle","the same rack with three pastel painted paddles and a small flag"),
     ("a supply barrel","a plain wooden barrel","the same barrel with a coil of rope, a lantern and a starfish on top"),
     ("a lookout scope","a plain brass spyglass on a short stand","the same spyglass polished gold on a mint stand with a tiny pennant")]),
]

OWL = "built like the round owl in the second reference image (round body, no separate neck, face toward the viewer in three-quarter view)"
LEGWALK = ("a walk cycle seen from the side, walking to the right. The two {legs} must be two different shades so they are easy to tell apart: the NEAR {leg} (closest to the viewer) is the normal bright {c}, the FAR {leg} is clearly darker {c} and partly hidden behind the body. "
           "Frame (1): the bright near {leg} is stepping FORWARD (on the right, toward the walking direction) and the dark far {leg} is BEHIND (on the left). "
           "Frame (2): both {legs} together under the body, mid-step. "
           "Frame (3): the exact opposite of frame (1): the dark far {leg} is stepping FORWARD (on the right) and the bright near {leg} is BEHIND (on the left). "
           "Frames (1) and (3) must clearly look different, like left-right-left steps, never the same pose twice. The {arm} swing opposite to the {legs}")
PASTEL = "Very cute, round and soft, with big sparkly eyes and rosy cheeks, in gentle pastel colors."
walkers = [
 dict(n='대롱', k='monkey', d="a round chubby little monkey standing upright on two short legs, soft pastel peach-tan fur, a pale cream heart-shaped face and cream round ears, a long thin curly tail, short arms, a small mint bandana around the neck and a tiny pink hibiscus flower behind one ear. Simple animal anatomy, no human hands.",
      walk=LEGWALK.format(c='peach', arm='arms', leg='leg', legs='legs'),
      wave="holding up a coconut cup with a straw in one paw and waving the other", think="hanging the curly tail in a loop and tapping its chin, thinking"),
 dict(n='재잘', k='parrot', d=f"a round chubby little parrot, {OWL}, soft pastel sky blue feathers with a pale yellow face and belly, a small curved peach beak, a tiny pastel pink crest of three feathers on the head, short pastel pink feet, small wings that act as hands, a little flower lei around the neck. Simple bird anatomy, no arms, no human hands.",
      walk=LEGWALK.format(c='pink', arm='wings', leg='foot', legs='feet'),
      wave="holding up a small flower lei in one wing and waving the other", think="tilting its head with one wing tip on its beak, looking curious"),
 dict(n='통통', k='hippo', d="a round chubby little hippo standing upright on two short stubby legs, soft pastel lavender-pink skin, a big round muzzle with two small nostrils, tiny round ears, a small round tail, short arms, a little yellow apron with a mango pocket and a white chef bandana. Simple animal anatomy, no human hands.",
      walk=LEGWALK.format(c='lavender', arm='arms', leg='leg', legs='legs'),
      wave="holding up a bowl of mango shaved ice in one hand and waving the other", think="holding a spoon to its chin, thinking"),
 dict(n='꾸벅', k='sloth', d="a round chubby little sloth standing upright on two short legs, soft pastel caramel-beige fur, a pale cream face with gentle dark brown eye patches around sleepy half-closed eyes, a tiny smile, long arms with three soft rounded claws, a small mint scarf and a little leaf tucked on the head. Simple animal anatomy, no human hands.",
      walk=LEGWALK.format(c='beige', arm='long arms', leg='leg', legs='legs') + ". It walks very slowly and sleepily",
      wave="waving one long arm slowly with a sleepy smile", think="hugging a small pillow and nodding off, thinking"),
 dict(n='쫑긋', k='toucan', d=f"a round chubby little toucan, {OWL}, soft pastel charcoal-lavender back and head top, a cream face and belly, a big rounded pastel rainbow beak in peach, yellow and mint (big but soft and round, not sharp), short pastel blue feet, small wings that act as hands, a pair of small pink headphones around the neck. Simple bird anatomy, no arms, no human hands.",
      walk=LEGWALK.format(c='blue', arm='wings', leg='foot', legs='feet'),
      wave="holding a small conch shell to its ear with one wing and waving the other", think="wearing the pink headphones on its head, moved up from the neck (so in this pose there are NO headphones around the neck, only one pair, on the head), pressing them with both wings, listening carefully"),
 dict(n='폴짝', k='frog', d="a round chubby little tree frog standing upright on two short legs, soft pastel mint green skin, a pale cream belly, big round shiny eyes on top of the head, rosy cheeks, short arms with round fingertips, a little yellow explorer hat and a small brown satchel across the body. Simple animal anatomy, no human hands.",
      walk=LEGWALK.format(c='mint', arm='arms', leg='leg', legs='legs'),
      wave="jumping up a little with both arms raised happily", think="holding a small rolled map to its chin, thinking"),
]
OWLREF = {'재잘', '쫑긋'}

out = []
P = out.append
P("# 7장 야자수 열대섬 — 그림 프롬프트\n")
P("레퍼런스는 5장 때 쓴 ref_A~H 그대로입니다(ch5/refs). 프롬프트마다 넣을 레퍼런스를 적어 두었습니다.\n")
P("크기: 지도 풍경 띠·바닥 타일을 빼고 모두 1536×1024 (가로 3:2). 메뉴 Lv.12는 6장 때 이미 받아서 이번엔 없습니다.\n")
P("가게 바탕 시트·이벤트 일러스트·풍경 띠·바닥 타일은 배경이 있는 그림이고, 나머지(창문·간판·바닥 소품·이웃·얼굴·거리 소품·지도 장식)는 모두 투명 배경으로 요청합니다.\n")
P("\n## 1. 가게 바탕 시트 (시트 6장, 레퍼런스: ref_A)\n")
for s in shops:
    P(f"\n### 1-{s['no']}. {s['name']}\n```")
    P(f"{STYLE}\nA 2x2 grid sheet of four equal panels. All four panels show the exact same building, {s['bld']}, "
      "from the exact same straight front view, at the exact same position and size, with the same camera, centered and filling about 60% of the panel width, "
      "standing on the sand path. Only the building changes between panels.\n"
      f"Panel 1 (top left): abandoned and ruined: {s['ruin']}.\n"
      f"Panel 2 (top right): repaired: {s['plain']}. No sign, no decorations, no props.\n"
      f"Panel 3 (bottom left): finished: {s['paint']}. No sign, no decorations, no props.\n"
      f"Panel 4 (bottom right): the same as panel 3, plus the window filled with its decorated version ({s['win2'].replace('the same ','a ',1)}), and a sign {s['sign_pos']}: {s['sign2'].replace('the same ','a ',1)}.\n"
      f"IMPORTANT: the window opening is a plain straight rectangle, {s['ratio']}, with a simple frame and a flat sill, and it has the exact same shape, size and position in every panel.\n{BG}\n"
      "No characters, no animals, no extra objects in front of the building. The sign in panel 4 shows exactly the same Korean word as written above and no other letters. No watermark, no frame lines between panels other than the clean split of the grid.\n```")
P("\n## 2. 창문·간판 시트 (시트 6장, 레퍼런스: 방금 뽑은 그 가게의 바탕 시트 + ref_B)\n")
for s in shops:
    P(f"\n### 2-{s['no']}. {s['name']}\n```")
    P(f"{STYLE}\nUse the attached base sheet of this shop as the exact reference. Draw four separate parts, "
      "arranged in a 2x2 grid with clear space between them, each part complete and not cut off.\n"
      "Top left: window level 1 inside view. Draw only what is seen through the empty window opening of panel 3, as a flat rectangular picture with no window frame, no sill, no posts and no outline border around it, filled edge to edge, with the same width-to-height ratio as that opening. "
      f"IMPORTANT: this picture must be {s.get('wratio', s['ratio'])}, exactly matching the window opening of this building in the base sheet. "
      f"It will be shown very small, so use only two or three large simple objects with big clear shapes, a plain flat dark back wall and no small details: {s['win1']}.\n"
      f"Top right: window level 2 inside view, the exact same size and ratio as top left ({s.get('wratio', s['ratio'])}), also with no frame and no border, the same large simple shapes plus a few more decorations: {s['win2']}.\n"
      f"Bottom left: sign level 1, {s['sign1']}, with {s['mount']}. It goes {s['sign_pos']}, so it must fit that spot on the building in the base sheet and must not repeat any emblem the building already has.\n"
      f"Bottom right: sign level 2, the exact same outline, size and mounting as bottom left ({s['mount']}): {s['sign2']}.\n"
      f"Front view, no shadows on the ground, no background scenery. {TRANS} The signs show exactly the Korean word given above and no other letters. No watermark, no frame or border.\n```")
P("\n## 3. 바닥 소품 시트 (시트 6장, 레퍼런스: 그 가게의 바탕 시트 + ref_B)\n")
for s in shops:
    a, b, c = s['g']
    P(f"\n### 3-{s['no']}. {s['name']}\n```")
    P(f"{STYLE}\nThree small ground props for the front of this shop, matching its colors in the attached base sheet. Draw six separate objects, "
      "in a grid of 3 columns and 2 rows with clear space between them, each object complete and not cut off, all seen from the same slight front view and at a consistent scale.\n"
      f"Top row, level 1 (plain): 1) {a[1]}; 2) {b[1]}; 3) {c[1]}.\n"
      f"Bottom row, level 2 (decorated), each directly under its level 1 version with the same base shape and size: 1) {a[2]}; 2) {b[2]}; 3) {c[2]}.\n"
      f"Each object sits on a tiny patch of pale sand. No characters. {TRANS} " + NOTXT + "\n```")
P("\n## 4. 이웃 걷기 시트 (시트 6장, 레퍼런스: ref_C — 화풍과 칸 배치만 참고, 몸 구조는 프롬프트대로. 재잘·쫑긋은 ref_H 부엉이도 두 번째 레퍼런스로 함께 넣기)\n")
for w in walkers:
    P(f"\n### 4. {w['n']} ({w['k']})\n```")
    P(f"{STYLE}\nA character sprite sheet of one cute kawaii character: {w['d']} {PASTEL} "
      "Use the first reference image only for the art style, line weight and the grid layout, not for the body shape. "
      "Six poses of the same character in a grid of 3 columns and 2 rows, all facing right, all at the same size and on the same baseline, with clear space between them, none cut off:\n"
      f"Top row, {w['walk']}.\n"
      f"Bottom row: standing still with a gentle smile; {w['wave']}, with closed happy eyes and three small yellow sparkle marks; {w['think']}.\n"
      + ("This is a bird: show every expression only with the beak (closed, or slightly open when happy or surprised). Never draw a separate mouth under the beak or on the face.\n" if w['n'] in OWLREF else "") +
      f"{TRANS} No shadows, no props, no background objects. " + NOTXT + "\n```")
P("\n## 5. 이웃 얼굴 시트 (시트 1장, 레퍼런스: ref_D + 걷기 시트 6장)\n```")
P(f"{STYLE}\nSix round face icons of six different animal characters, matching the attached character sheets exactly, in a grid of 3 columns and 2 rows with clear space between them. "
  "Each is only the head, front view, closed happy eyes, a small open smiling mouth and rosy cheeks. For the two birds (2 and 5) there is no mouth at all: the beak is slightly open in a happy smile instead, with nothing drawn under the beak.\n"
  "Top row: " + "; ".join(f"{i+1}) {w['d']}" for i, w in enumerate(walkers[:3])) + "\n"
  "Bottom row: " + "; ".join(f"{i+4}) {w['d']}" for i, w in enumerate(walkers[3:])) + "\n"
  f"{TRANS} " + NOTXT + "\n```")
street = [
 ('palmpot', '야자수 화분', 'a small palm tree in a plain round clay pot', 'the same palm in a mint painted pot with two small coconuts and a flower garland'),
 ('banana', '바나나 나무', 'a small banana plant with big plain green leaves', 'the same banana plant with a bunch of yellow bananas and a pink flower'),
 ('hibiscus', '히비스커스 덤불', 'a plain round green bush', 'the same bush covered with big pink and coral hibiscus flowers'),
 ('monstera', '몬스테라 화분', 'a small monstera plant in a plain pot', 'the same monstera with big leaves in a woven basket pot with a ribbon'),
 ('bamboobench', '대나무 벤치', 'a plain bamboo bench', 'the same bench with pastel striped cushions and a small coconut drink'),
 ('tiki', '티키 횃불', 'a plain bamboo torch post, unlit', 'the same torch lit with a soft warm flame and wrapped with a flower garland'),
 ('cocopile', '코코넛 더미', 'a small pile of three plain brown coconuts', 'a pile of green and brown coconuts with two coconut cups and paper umbrellas'),
 ('pineapple', '파인애플 화분', 'a small pineapple plant in a plain pot', 'the same plant with a golden pineapple in a yellow painted pot'),
 ('canoe', '카누 거치대', 'a plain wooden rack with one plain canoe', 'the same rack with a pastel painted canoe and two paddles'),
 ('chime', '조개 풍경', 'a plain bamboo frame with a few plain strings', 'the same frame hung with pastel seashells and tiny bells'),
 ('fence', '대나무 울타리', 'a short plain bamboo fence piece', 'the same fence wound with green vines and small flowers'),
 ('swing', '나무 그네', 'a plain wooden swing hanging from a short frame', 'the same swing with a flower garland on the ropes and a small cushion'),
 ('bamboolamp', '대나무 가로등', 'a plain bamboo lamp post, unlit', 'the same lamp post lit warm with a hanging flower basket and a small shell charm'),
 ('islandsign', '섬 이정표', 'a plain wooden arrow sign post with no words', 'the same sign post painted mint and peach with a tiny coconut and a starfish charm, no words'),
 ('flowerarch', '꽃 아치', 'a plain bamboo arch', 'the same arch covered with plumeria and hibiscus flowers'),
 ('perch', '앵무새 횃대', 'a plain wooden perch on a pole', 'the same perch with a flower garland, a small fruit cup and a tiny bell'),
 ('fruitcart', '열대 과일 손수레', 'a plain empty wooden hand cart', 'the same cart with mangos, pineapples, bananas and a striped umbrella'),
 ('bamboofountain', '대나무 물받이 분수', 'a plain stone basin with a plain bamboo spout and no water', 'the same basin with clear water flowing from the bamboo spout and floating flowers'),
 ('lilypond', '연잎 연못', 'a small round plain pond edge of stones with no water', 'the same pond with clear water, round lily pads and a pink lotus flower'),
 ('shelllamp', '조개 등불', 'a plain big shell on a short stand', 'the same shell glowing warm like a little lamp with a pink pearl'),
 ('conchhorn', '소라 나팔 받침', 'a plain big conch shell lying half buried in the sand, with no stand', 'the same conch polished pastel pink with a flower garland on the stand'),
 ('mangotree', '망고 나무', 'a small round plain green tree', 'the same tree full of ripe orange-yellow mangos'),
 ('sandbed', '모래 화단', 'a small plain round mound of piled sand with no stone border', 'the same sand bed with small tropical flowers, shells and a starfish'),
 ('raftbed', '작은 뗏목 화단', 'a plain small bamboo raft lying on the ground', 'the same raft filled with flowers and a tiny leaf sail'),
]
P("\n## 6. 거리 소품 시트 (시트 6장, 레퍼런스: ref_E)\n")
for i in range(6):
    part = street[i*4:(i+1)*4]
    P(f"\n### 6-{i+1}. " + ", ".join(x[1] for x in part) + "\n```")
    P(f"{STYLE}\nSmall street props for a sunny tropical island village. Draw eight separate objects, in a grid of 4 columns and 2 rows with clear space between them, "
      "each complete and not cut off, all seen from the same slight front view at a consistent scale, each sitting on a tiny patch of pale sand.\n"
      "Top row, level 1 (plain): " + "; ".join(f"{j+1}) {x[2]}" for j, x in enumerate(part)) + ".\n"
      "Bottom row, level 2 (decorated), each directly under its level 1 version with the same base shape and size: " + "; ".join(f"{j+1}) {x[3]}" for j, x in enumerate(part)) + ".\n"
      f"No characters. {TRANS} " + NOTXT + "\n```")
P("\n## 7. 마을 지도 소품 (시트 3장, 레퍼런스: ref_F)\n")
P("\n### 7-1. 지도 장식 16개\n```")
P(f"{STYLE}\nSixteen small decoration sprites for a sunny tropical island village map, in a grid of 4 columns and 4 rows with clear space between them, each complete and not cut off, all at a consistent small scale, seen from a slight front view, each sitting on a tiny patch of pale sand:\n"
  "1) a tall palm tree, 2) a short round palm tree, 3) a banana plant, 4) a pink hibiscus bush, 5) a tiny round thatched hut, 6) a tiny bamboo hut on stilts, 7) a short bamboo fence piece, 8) a few flat stepping stones, "
  "9) a small canoe, 10) a pile of coconuts, 11) a pineapple plant, 12) a tiki torch, 13) a pot of tropical flowers, 14) a small mossy rock pair, 15) a big seashell, 16) a starfish and two small shells.\n"
  f"No characters. {TRANS} " + NOTXT + "\n```")
P("\n### 7-2. 지도 위쪽 풍경 띠\n```")
P(f"{STYLE}\nA wide horizontal scenery strip for the top edge of a tropical island village map, very wide panoramic format about 3:1. A light blue sky fading to pale at the bottom with a few round puffy clouds, "
  "a calm turquoise sea with a straight horizon, the small white ferry far away, a round green island hill with a tiny white waterfall, a rocky cliff on one side with a small dark sea cave opening glowing faint blue, and along the bottom edge a row of round palm trees and tiny thatched huts, "
  "the bottom edge fading into plain pale warm sand so it can blend into a sand ground. Simple and flat. " + NOTXT + "\n```")
P("\n### 7-3. 모래길 바닥 타일\n```")
P(f"{STYLE}\nA seamless tileable square ground texture of a pale warm sand path, 1:1, viewed from straight above. Very subtle and flat: soft pale sand with a few very faint small flat round stepping stones and tiny faint shell dots, "
  "low contrast so it stays calm behind map objects. It must tile seamlessly on all four edges. No objects, no strong outlines. " + NOTXT + "\n```")

ILL = ("Simple cute flat illustration in the exact style of the first reference image (a kawaii mobile game): chubby chibi animal characters with big heads and small bodies, thick dark brown outlines (#5b3a32), soft pastel colors, flat coloring with only one soft shade per color, no texture, no grain. "
       "The background is very simple and minimal like a sticker or a children's picture book: big flat color areas, a plain sky with a few round puffy clouds, round lollipop-shaped trees, smooth rounded shapes, only a few large background elements, no small clutter, no tiny details, no complex perspective. "
       "The characters are large in the foreground and clearly the focus. Wide landscape composition, 3:2 (1536x1024).")
END = "Seen from the viewpoint of the unseen cafe owner: the characters look toward the viewer. No humans, no text, no letters, no numbers, no logos, no watermark, no frame or border."
P("\n## 8. 이벤트 일러스트 (시트 3장, 레퍼런스는 장면마다 적은 순서대로. 첫 번째는 항상 ref_G)\n")
ev = [
 ('ev17 · 야자수 열대섬 도착', 'ref_G → walk_sealion(첨벙 걷기 시트) → walk_monkey(대롱 걷기 시트) → coconut_base → lei_base',
  "The second and third reference images are the character sheets of the sea lion and the monkey: draw them exactly like that. The fourth and fifth reference images are shop sheets: draw those two shops exactly like their abandoned version in the top left panel (faded, torn, empty), small in the background. The bear and the bunny look exactly like the bear and the bunny in the first reference image.",
  "a quiet tropical island in the bright morning: a calm turquoise sea, a straight horizon, tall round palm trees, and behind the characters along the sand path the two abandoned shops from the shop sheets, a faded coconut hut and a faded flower workshop on stilts. The white ferry with a red funnel is tied at a small wooden pier. In the foreground, a brown sea lion in a navy captain jacket waves goodbye from the ferry; a chubby brown bear with a cream muzzle, holding the honey-pot notebook, steps onto the sand with wide happy eyes; a white bunny with long upright ears holds a straw hat on her head in the breeze; a round pastel peach monkey with a mint bandana hangs upside down from a palm tree by its curly tail, waving hello."),
 ('ev18 · 소라 방송국의 바다 소리', 'ref_G → walk_toucan(쫑긋 걷기 시트) → radio_base',
  "The second reference image is the character sheet of the toucan: draw it exactly like that. The third reference image is the shell radio station sheet: draw the inside of that same radio station in its finished colors (pastel coral and cream stripes, gold accents). The bear and the bunny look exactly like the bear and the bunny in the first reference image.",
  "the cozy round inside of the conch shell radio station, with curved striped walls, an old round radio glowing softly and a big pink conch shell on a cushion. A round toucan with pink headphones holds the big conch up so the others can listen, eyes closed in concentration; a chubby brown bear with a cream muzzle presses one ear to the conch with a surprised face, the honey-pot notebook in his other paw; a white bunny with long upright ears leans in with sparkling eyes. Through a round window behind them, far out on the calm sea, a small round grey rock island sits on the horizon with a faint wake of ripples behind it, as if it were slowly moving."),
 ('ev19 · 뗏목 출발', 'ref_G → walk_frog(폴짝 걷기 시트) → raft_base',
  "The second reference image is the character sheet of the tree frog: draw it exactly like that. The third reference image is the raft dock sheet: draw the explorers' hut exactly like its finished version in the bottom left panel (pastel mint walls, sunny yellow trim, teal roof, compass emblem) and the bamboo raft with the green leaf sail. The bear and the bunny look exactly like the bear and the bunny in the first reference image.",
  "a sunny small wooden pier with a bamboo raft with a green leaf sail ready to leave, and the finished explorers' hut behind. On the raft, a round pastel mint tree frog in a yellow explorer hat points a little arm across the sea; a chubby brown bear with a cream muzzle holds the honey-pot notebook open to a page with a small hand-drawn map of a sea cave; a white bunny with long upright ears holds a lantern and cheers. Across the calm turquoise sea, a rocky cliff with a sea cave opening glows soft blue, with a few pink seashells floating on the water toward it."),
]
for t, refs, rl, sc in ev:
    P(f"\n### {t}\n레퍼런스 순서: {refs}\n```")
    P(f"{ILL}\n{rl}\nScene: {sc}\n{END}\n```")

txt = "\n".join(out)
open('/home/claude/work/ch7/ch7_prompts.md', 'w').write(txt)
print(len(txt), "chars", txt.count('```') // 2, "blocks")
