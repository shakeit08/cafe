STYLE = ("Cute cozy kawaii mobile game art in the exact style of the reference image: thick dark brown outlines (#5b3a32), "
         "soft pastel colors, flat cel shading with one soft shade per color and small soft highlights, clean simple rounded shapes, no texture, no grain.")
BG = ("Background, identical in all four panels: a sunny white harbor town by the sea. A light blue sky with a few round puffy white clouds, "
      "a calm deep blue sea with a straight horizon line behind the building, a few small white houses with round blue domed roofs on a gentle hill far behind, "
      "two round green cypress trees at the left and right edges, and a pale cream stone quay running horizontally across the bottom of every panel.")
NOTXT = "No text, no letters, no numbers, no logos, no watermark, no frame or border."

shops = [
 dict(no=1, k='gelato', ratio='about 2 to 1 (twice as wide as tall)', mount='its own wall bracket arm on top', name='몽돌 젤라또 가게', who='수달 몽돌',
  bld="a small whitewashed cube-shaped shop with a flat roof and a small round blue dome on the right corner, a wide glass counter window on the left half and a blue arched door on the right half",
  ruin="cracked grey peeling whitewash, a faded broken dome with missing tiles, a dusty cracked empty counter window, a torn faded awning hanging loose, dry leaves piled at the door",
  plain="clean fresh white walls, a plain white dome, a plain wooden door, the counter window empty and dark",
  paint="white walls with pastel mint trim, a sky blue dome, a short pink and white striped awning over the counter window, a small ice cream cone emblem above the door, the counter window still empty and dark",
  win1="a simple glass counter with three plain metal gelato tubs and one stack of cones",
  win2="the same glass counter full of colorful gelato tubs in pink, mint, lemon and chocolate, each topped with fruit, cones in a holder and a string of tiny round lights along the top",
  sign_pos="hanging from a small bracket on the right side, beside the door",
  sign1="a plain round wooden board with the Korean word \"젤라또\" in dark brown",
  sign2="the same round board painted mint with a pink scalloped border, a tiny gelato cone on top and two small lemons on the bottom corner",
  g=[("a gelato cart","a plain small white push cart with one closed lid","the same cart with a pink striped umbrella, open lids showing colorful gelato and a cone holder on the side"),
     ("a cafe table","a plain small round white table with one chair","the same table with a mint tablecloth, two gelato cups with spoons and a tiny vase of flowers"),
     ("a lemon tree pot","a small lemon sapling in a plain clay pot","a bigger lemon tree full of yellow lemons in a blue painted pot")]),
 dict(no=2, k='post', ratio='about 6 to 5 (almost square, only a little wider than tall)', mount='no hanging tabs, no hooks, no rings, no chains, no bracket: a flat plate mounted directly on the wall', name='파랑 지붕 우체국', who='퍼핀 또박',
  bld="a small two-story white post office with a pointed blue gabled roof, a round clock in the gable, a wide arched window on the left of the ground floor and a double door on the right",
  ruin="cracked grey walls, a faded roof with missing blue tiles, a stopped broken clock with no hands, a cracked empty arched window, scattered old papers on the steps",
  plain="clean white walls, a plain grey roof, a plain clock face with hands, the arched window empty and dark",
  paint="white walls with navy trim, a bright sky blue roof, a small gold horn emblem above the door, a cream clock face with gold hands, the arched window still empty and dark",
  win1="a simple wooden sorting shelf with a few plain cream envelopes and one small parcel",
  win2="the same sorting shelf full of letters and parcels tied with string, a neat row of cream envelopes sealed with little pink seashells, and a small brass postal scale",
  sign_pos="mounted flat on the wall at the top center, above the arched window and the door",
  sign1="a plain long cream board with the Korean word \"우체국\" in dark brown",
  sign2="the same long board painted navy with the same Korean word in white, a small gold horn on the left and a tiny envelope on the right",
  g=[("a mailbox","a plain round white mailbox on a short post","the same mailbox painted sky blue with a gold horn and a letter sticking out of the slot"),
     ("a parcel cart","a plain wooden hand cart with one box","the same cart piled with parcels tied with string and blue ribbons"),
     ("a bicycle","a plain white bicycle with an empty front basket","the same bicycle painted blue with a front basket full of letters and a small flower")]),
 dict(no=3, k='market', ratio='about 4 to 1 (a long, very wide and low strip)', mount='two short rope loops on top only', name='뱃고동 수산시장', who='바다표범 뽀글',
  bld="a wide open-front harbor market stall building with a rounded arched roof, a long wide counter opening across the middle, and two wooden posts at the front corners",
  ruin="cracked grey boards, a sagging arched roof with holes, a torn faded canopy flap, an empty broken counter, a tipped-over wooden crate and a tangled old net",
  plain="clean natural wood walls, a plain grey arched roof, the counter opening empty and dark",
  paint="white walls with red and white striped canopy edge, a deep red arched roof, a small fish emblem on the roof center, the counter opening still empty and dark",
  win1="a simple long counter of crushed ice with three plain silver fish lying on it",
  win2="the same ice counter full of colorful fish, shrimp, little piles of clams, lemon halves and green herb sprigs, with a row of hanging lanterns at the top",
  sign_pos="hanging across the top of the roof edge at the center, above the counter",
  sign1="a plain long wooden board with the Korean words \"수산시장\" in dark brown",
  sign2="the same long board painted white with a red border, the same Korean words, a small fish on the left and a tiny anchor on the right",
  g=[("a fish crate stack","one plain wooden crate with ice","a stack of two crates full of ice and colorful fish with a lemon on top"),
     ("a hanging scale","a plain brass hanging scale on a short stand","the same scale with a small basket of clams and a red ribbon"),
     ("a net barrel","a plain wooden barrel","the same barrel with a fishing net draped over it, a float and a starfish")]),
 dict(no=4, k='sail', ratio='about 5 to 3 (a little wider than tall; the opening has its two top corners cut off diagonally, so keep the top corners plain dark wall)', mount='a single short rope loop on top only, no wooden beam, no bracket, no pulley wheel (the building already has the beam and pulley)', name='돛천 수선소', who='문어 문문',
  bld="a tall narrow wooden workshop with a pointed roof, a wide loft window on the upper floor, a door on the ground floor at the left, and a small wooden pulley beam sticking out from the top of the roof",
  ruin="faded cracked grey boards, a broken pulley beam with a frayed rope, a cracked empty loft window, a torn grey sail drooping from the roof, loose boards at the door",
  plain="clean natural wood walls, a whole plain pulley beam with a neat rope, the loft window empty and dark",
  paint="cream walls with soft coral trim, a teal roof, the rope from the pulley beam hanging down empty with only a small empty hook at its end (no cloth, no sail, nothing hanging on it), a small needle and thread emblem above the door, the loft window still empty and dark",
  win1="a simple sewing table with one roll of plain white sailcloth and a big spool of thread",
  win2="the same table full of colorful striped sailcloth rolls, spools of thread, a round embroidery hoop showing a little island map, and a string of small pennant flags at the top",
  sign_pos="hanging from the pulley beam at the top right, beside the loft window",
  sign1="a plain wooden board shaped like a small triangle sail with the Korean words \"돛 수선\" in dark brown",
  sign2="the same sail-shaped board painted cream with a coral stripe, the same Korean words, and a tiny needle and thread tied with a bow",
  g=[("a spool stack","one plain big wooden thread spool","a stack of three spools wound with coral, teal and yellow thread"),
     ("a sail bundle","a plain rolled white sail tied with rope","the same rolled sail with blue and white stripes, a rope bow and a tiny flag"),
     ("a sewing basket","a plain small woven basket","the same basket overflowing with colorful fabric scraps, a pincushion and scissors")]),
 dict(no=5, k='museum', ratio='about 7 to 5 (a little wider than tall)', mount='no hanging tabs, no hooks, no rings, no chains: a flat plate mounted directly on the wall', name='옛 등대 전시관', who='알바트로스 훨훨',
  bld="a small old stone museum building with a short round lighthouse-shaped tower attached on its left side, a big arched display window in the middle and a little wooden door on the right",
  ruin="crumbling grey stone with missing blocks, a cracked dark tower lamp room with broken glass, a cracked empty arched window, ivy and dry seaweed on the walls",
  plain="clean pale stone walls, a whole tower with a plain unlit lamp room, the arched window empty and dark",
  paint="cream stone walls with navy trim, the tower painted with red and white stripes and a gold lamp room roof, a small gold star emblem above the door, the arched window still empty and dark",
  win1="a simple display shelf with one old brass lantern",
  win2="the same shelf with the brass lantern glowing softly, a framed old picture of a lighthouse on a small island with no characters, a ship in a bottle and a brass compass",
  sign_pos="mounted flat on the wall at the top center, above the arched window",
  sign1="a plain wooden board with the Korean word \"전시관\" in dark brown",
  sign2="the same board painted navy with gold letters, a tiny gold lighthouse on the left and a tiny gold compass on the right",
  g=[("a lighthouse lamp","a plain old glass lamp on a short stone pedestal","the same lamp polished gold and glowing warm with a small navy ribbon"),
     ("a ship's wheel","a plain wooden ship's wheel on a stand","the same wheel polished with brass caps and a little flower garland"),
     ("an old logbook crate","one plain wooden crate with a closed old book","the same crate with a stack of old logbooks, a rolled sea chart and a quill")]),
 dict(no=6, k='ferry', ratio='about 6 to 5 (almost square, only a little wider than tall)', mount='two short rope loops on top only', name='하얀 여객선 부두', who='물개 첨벙',
  bld="a ferry terminal building on the quay, with a ticket window on the left, a wide entrance in the middle, a small clock tower on the right, and the round red funnel of a white ferry boat peeking up behind the building",
  ruin="grey weathered walls, a stopped broken clock tower, a cracked empty ticket window, a rusty faded funnel behind, loose cracked stones on the quay",
  plain="clean white walls, a plain clock tower, a plain white funnel behind, the ticket window empty and dark",
  paint="white walls with sky blue trim, a blue roof, a small gold ship wheel emblem above the entrance, a red funnel with a white stripe behind, the ticket window still empty and dark",
  win1="a simple ticket window with a plain counter and a small brass bell",
  win2="the same ticket window with a rolled sea map, a stack of ferry tickets, a small potted palm and a little gold lamp",
  sign_pos="hanging over the entrance at the top center",
  sign1="a plain oval wooden board framed with rope, with the Korean word \"여객선\" in dark brown",
  sign2="the same rope-framed oval board painted sky blue with white letters and two tiny red and white pennant flags at the sides; no ship wheel on the sign (the building already has a ship wheel emblem right above it)",
  g=[("a bollard","a plain iron mooring bollard","the same bollard painted navy with a coiled rope and a small flag"),
     ("a luggage cart","a plain metal luggage cart","the same cart with two suitcases, a straw hat and a flower lei"),
     ("a timetable board","a plain blank wooden board on two legs","the same board painted blue with a small drawn ship and a palm tree picture, no words")]),
]

OWL = "built like the round owl in the second reference image (round body, no separate neck, face toward the viewer in three-quarter view)"
LEGWALK = ("a walk cycle seen from the side, walking to the right. The two {legs} must be two different shades so they are easy to tell apart: the NEAR {leg} (closest to the viewer) is the normal bright {c}, the FAR {leg} is clearly darker {c} and partly hidden behind the body. "
           "Frame (1): the bright near {leg} is stepping FORWARD (on the right, toward the walking direction) and the dark far {leg} is BEHIND (on the left). "
           "Frame (2): both {legs} together under the body, mid-step. "
           "Frame (3): the exact opposite of frame (1): the dark far {leg} is stepping FORWARD (on the right) and the bright near {leg} is BEHIND (on the left). "
           "Frames (1) and (3) must clearly look different, like left-right-left steps, never the same pose twice. The {arm} swing opposite to the {legs}")
walkers = [
 dict(n='몽돌', k='otter', d="a round chubby sea otter standing upright on two short legs, deep dark chocolate brown fur all over the body, a pale silver-grey face and head with a cream round muzzle (clearly darker and cooler colored than a light tan otter), small round ears, short whiskers, a thick flat tail, short paw arms, a little pink and white striped apron and a small mint bandana on the head. Simple animal anatomy, no human hands.",
      walk=LEGWALK.format(c='brown', arm='arms', leg='leg', legs='legs'),
      wave="holding up a small gelato cone in one paw and waving the other", think="holding a round pebble to its chin with both paws, thinking"),
 dict(n='또박', k='puffin', d=f"a round chubby puffin, {OWL}, a black back and head top, a white face and belly, a big triangular beak with orange, yellow and blue-grey stripes, bright orange webbed feet, small black wings that act as hands, a little sky blue postman cap and a small brown mail satchel across the body. Simple bird anatomy, no arms, no human hands.",
      walk=LEGWALK.format(c='orange', arm='wings', leg='foot', legs='feet'),
      wave="holding up a cream envelope in one wing and waving the other", think="tapping one wing tip on its beak, looking curious"),
 dict(n='뽀글', k='seal', d="a round chubby harbor seal with deep slate blue-grey fur and small silver-white spots, a pale blue-grey belly (clearly darker than a white or light grey seal), a round head with no ear flaps, big round black eyes, short whiskers, two front flippers that act as hands and a small tail flipper at the back, a little yellow fisherman's rain hat and a red neckerchief. It moves by bouncing on its belly. Simple animal anatomy, no legs, no human hands.",
      walk="a bounce cycle seen from the side, moving to the right: (1) the body stretched forward low with the front flippers reaching ahead; (2) the body bunched up with the back curved up; (3) the body pushing off with the tail flipper lifted",
      wave="sitting up and clapping both front flippers", think="sitting up with one front flipper on its chin, thinking"),
 dict(n='문문', k='octopus', d="a soft round chubby octopus, a big round soft coral-pink head that is also the body, two round black eyes with white highlights, rosy cheeks and a small smile on the lower front of the head, six short soft curly tentacles underneath, all round and simple with a few pale round suckers only on the underside, a tiny round pincushion hat with a pin on top and a measuring tape draped over one tentacle. No extra eyes, no spikes, no human body.",
      walk="sliding to the right on its tentacles, the front tentacles curling forward; standing still mid-step with tentacles gathered; sliding with the back tentacles pushing",
      wave="waving two tentacles up happily", think="tapping one tentacle on its cheek, looking curious"),
 dict(n='훨훨', k='albatross', d=f"an old round chubby albatross sailor, {OWL}, white body feathers, long soft grey-brown wings folded at the sides that act as hands, a pale pink hooked beak, small round glasses, a few fluffy white feathers like a little beard under the beak, short pale pink webbed feet, a faded navy sailor cap. Gentle kind old face. Simple bird anatomy, no arms, no human hands.",
      walk=LEGWALK.format(c='pink', arm='wings', leg='foot', legs='feet'),
      wave="spreading one long wing out in a slow warm wave", think="pushing up its glasses with one wing tip, thinking"),
 dict(n='첨벙', k='sealion', d="a round chubby brown sea lion standing upright on its back flippers, sleek warm brown fur, small ear flaps, a round nose with long whiskers, a cream muzzle, front flippers that act as hands, a navy ferry captain jacket with gold buttons and a navy captain cap with a small gold ship wheel badge, a tiny silver whistle on a cord. Simple animal anatomy, no human hands.",
      walk="a walk cycle seen from the side: (1) the near back flipper, closest to the viewer, stepping forward to the right and the far one behind; (2) both back flippers together under the body, mid-step; (3) the opposite of (1): the far back flipper stepping forward and the near one behind. The far flipper is always drawn in a slightly darker brown and partly behind the near one, and frames (1) and (3) must clearly differ. The front flippers swing opposite",
      wave="saluting with one front flipper at the cap", think="holding a small brass spyglass to one eye, looking far away"),
]
WHITE = {'또박', '훨훨'}
OWLREF = {'또박', '훨훨'}

out = []
P = out.append
P("# 6장 하얀 항구 — 그림 프롬프트\n")
P("레퍼런스는 5장 때 쓴 ref_A~H 그대로입니다(ch5/refs). 메뉴 Lv.11~13만 ch6/refs의 ref_M1~M9를 씁니다. 프롬프트마다 넣을 레퍼런스를 적어 두었습니다.\n")
P("크기: 메뉴 시트와 지도 풍경 띠·바닥 타일을 빼고 모두 1536×1024 (가로 3:2).\n")
P("\n## 1. 가게 바탕 시트 (6장, 레퍼런스: ref_A)\n")
for s in shops:
    P(f"\n### 1-{s['no']}. {s['name']}\n```")
    P(f"{STYLE}\nA 2x2 grid sheet of four equal panels. All four panels show the exact same building, {s['bld']}, "
      "from the exact same straight front view, at the exact same position and size, with the same camera, centered and filling about 60% of the panel width, "
      "standing on the stone quay. Only the building changes between panels.\n"
      f"Panel 1 (top left): abandoned and ruined: {s['ruin']}.\n"
      f"Panel 2 (top right): repaired: {s['plain']}. No sign, no decorations, no props.\n"
      f"Panel 3 (bottom left): finished: {s['paint']}. No sign, no decorations, no props.\n"
      f"Panel 4 (bottom right): the same as panel 3, plus the window filled with its decorated version ({s['win2'].replace('the same ','a ',1)}), and a sign {s['sign_pos']}: {s['sign2'].replace('the same ','a ',1)}.\n"
      f"The window opening has the exact same shape, size and position in every panel.\n{BG}\n"
      "No characters, no animals, no extra objects in front of the building. The sign in panel 4 shows exactly the same Korean word as written above and no other letters. No watermark, no frame lines between panels other than the clean split of the grid.\n```")
P("\n## 2. 창문·간판 시트 (6장, 레퍼런스: 방금 뽑은 그 가게의 바탕 시트 + ref_B)\n")
for s in shops:
    P(f"\n### 2-{s['no']}. {s['name']}\n```")
    P(f"{STYLE}\nUse the attached base sheet of this shop as the exact reference. Draw four separate parts on a plain flat white background, "
      "arranged in a 2x2 grid with clear space between them, each part complete and not cut off.\n"
      "Top left: window level 1 inside view. Draw only what is seen through the empty window opening of panel 3, as a flat rectangular picture with no window frame, no sill, no posts and no outline border around it, filled edge to edge, with the same width-to-height ratio as that opening. "
      f"IMPORTANT: this picture must be {s['ratio']}, matching the window opening of this building, not the usual 2 to 1. "
      f"It will be shown very small, so use only two or three large simple objects with big clear shapes, a plain flat dark back wall and no small details: {s['win1']}.\n"
      f"Top right: window level 2 inside view, the exact same size and ratio as top left ({s['ratio']}), also with no frame and no border, the same large simple shapes plus a few more decorations: {s['win2']}.\n"
      f"Bottom left: sign level 1, {s['sign1']}, with {s['mount']}. It goes {s['sign_pos']}, so it must fit that spot on the building in the base sheet and must not repeat any emblem the building already has.\n"
      f"Bottom right: sign level 2, the exact same outline, size and mounting as bottom left ({s['mount']}): {s['sign2']}.\n"
      "Front view, no shadows on the ground, no background scenery. The signs show exactly the Korean word given above and no other letters. No watermark, no frame or border.\n```")
P("\n## 3. 바닥 소품 시트 (6장, 레퍼런스: 그 가게의 바탕 시트 + ref_B)\n")
for s in shops:
    a, b, c = s['g']
    P(f"\n### 3-{s['no']}. {s['name']}\n```")
    P(f"{STYLE}\nThree small ground props for the front of this shop, matching its colors in the attached base sheet. Draw six separate objects on a plain flat white background, "
      "in a grid of 3 columns and 2 rows with clear space between them, each object complete and not cut off, all seen from the same slight front view and at a consistent scale.\n"
      f"Top row, level 1 (plain): 1) {a[1]}; 2) {b[1]}; 3) {c[1]}.\n"
      f"Bottom row, level 2 (decorated), each directly under its level 1 version with the same base shape and size: 1) {a[2]}; 2) {b[2]}; 3) {c[2]}.\n"
      "Each object sits on a tiny patch of pale stone pavement. No characters. " + NOTXT + "\n```")
P("\n## 4. 이웃 걷기 시트 (6장, 레퍼런스: ref_C — 화풍과 칸 배치만 참고, 몸 구조는 프롬프트대로. 또박·훨훨은 ref_H 부엉이도 두 번째 레퍼런스로 함께 넣기)\n")
for w in walkers:
    bg = "a plain flat light mint background (#dff3ea)" if w['n'] in WHITE else "a plain flat white background"
    P(f"\n### 4. {w['n']} ({w['k']})\n```")
    P(f"{STYLE}\nA character sprite sheet of one cute kawaii character: {w['d']} "
      "Use the first reference image only for the art style, line weight and the grid layout, not for the body shape. "
      "Six poses of the same character in a grid of 3 columns and 2 rows, all facing right, all at the same size and on the same baseline, with clear space between them, none cut off:\n" +
      (f"Top row, {w['walk']}.\n" if w['walk'].startswith('a ') else f"Top row: {w['walk']}.\n") +
      f"Bottom row: standing still with a gentle smile; {w['wave']}, with closed happy eyes and three small yellow sparkle marks; {w['think']}.\n"
      f"On {bg}. No shadows, no props, no background objects. " + NOTXT + "\n```")
P("\n## 5. 이웃 얼굴 시트 (1장, 레퍼런스: ref_D + 걷기 시트 6장)\n```")
P(f"{STYLE}\nSix round face icons of six different animal characters, matching the attached character sheets exactly, in a grid of 3 columns and 2 rows with clear space between them. "
  "Each is only the head, front view, closed happy eyes, a small open smiling mouth and rosy cheeks.\n"
  "Top row: " + "; ".join(f"{i+1}) {w['d']}" for i, w in enumerate(walkers[:3])) + "\n"
  "Bottom row: " + "; ".join(f"{i+4}) {w['d']}" for i, w in enumerate(walkers[3:])) + "\n"
  "On a plain flat light mint background (#dff3ea). " + NOTXT + "\n```")
street = [
 ('lemon', '레몬나무 화분', 'a small lemon tree in a plain round clay pot', 'the same tree full of yellow lemons in a blue and white painted pot'),
 ('olive', '올리브나무 화분', 'a small olive tree in a plain square stone planter', 'the same olive tree with small olives, a string of tiny lights and white flowers in the planter'),
 ('bougain', '부겐빌레아 아치', 'a plain white stone arch', 'the same arch covered with bright pink bougainvillea flowers'),
 ('hydrangea', '수국 화분', 'a plain green bush in a plain pot', 'the same bush covered with round blue and purple hydrangea flowers in a white pot'),
 ('cafetable', '노천 카페 테이블', 'a plain small round table with two chairs', 'the same table with a blue checkered cloth, two lemonade glasses and a small parasol'),
 ('stonebench', '하얀 돌 벤치', 'a plain white stone bench', 'the same bench with blue cushions and a small pot of flowers at one end'),
 ('bollard', '밧줄 계류 기둥', 'a plain short iron mooring post', 'the same post painted navy with a thick coiled rope and a little seagull feather tucked in'),
 ('crates', '생선 상자 더미', 'one plain empty wooden crate', 'a stack of crates with ice, silver fish and a lemon'),
 ('netrack', '그물 걸이', 'a plain wooden rack with a plain grey net', 'the same rack with a blue net, round glass floats and a starfish'),
 ('barrels', '오크통', 'one plain wooden barrel', 'two barrels with a potted herb and a small lantern on top'),
 ('handcart', '짐 손수레', 'a plain empty wooden hand cart', 'the same cart with sacks, a crate of oranges and a small flag'),
 ('rowboat', '쪽배 화단', 'a plain old small rowboat on the ground', 'the same rowboat painted blue and white and filled with flowers'),
 ('harborlamp', '항구 가로등', 'a plain black lamp post, unlit', 'the same lamp post lit warm with a hanging flower basket and a small anchor charm'),
 ('clockpost', '항구 시계 기둥', 'a plain post with a round blank clock face', 'the same clock post painted blue with gold hands and a small ribbon'),
 ('bunting', '깃발 줄 기둥', 'two plain posts with a plain rope between them', 'the same posts with a row of small colorful pennant flags on the rope'),
 ('signpost', '항구 이정표', 'a plain wooden arrow sign post with no words', 'the same sign post painted white with blue arrows, a small shell and a tiny lighthouse charm, no words'),
 ('bicycle', '자전거', 'a plain white bicycle parked on a stand', 'the same bicycle painted sky blue with a basket of lemons and flowers'),
 ('sherbet', '레몬 셔벗 수레', 'a plain small wooden cart', 'the same cart with a bowl of yellow sherbet, lemons and a striped umbrella'),
 ('fountain', '돌고래 분수', 'a plain round stone fountain basin with no water', 'the same fountain with a cute round stone dolphin spouting water'),
 ('vane', '갈매기 풍향계', 'a plain metal weathervane on a post', 'the same weathervane with a little seagull on top, painted white and gold'),
 ('bell', '항구 종', 'a plain small brass bell hanging on a wooden frame', 'the same bell polished gold with a navy rope and a flower garland'),
 ('steps', '파란 계단 화분', 'three plain white stone steps', 'the same steps with blue painted edges and small flower pots on each step'),
 ('crane', '작은 짐 기중기', 'a plain small wooden harbor crane with a rope and hook', 'the same crane painted red with a net of colorful parcels hanging from the hook'),
 ('lhmodel', '작은 등대 모형', 'a plain small white lighthouse model on a stone base', 'the same lighthouse model painted with red and white stripes, its tiny lamp glowing warm'),
]
P("\n## 6. 거리 소품 시트 (6장, 레퍼런스: ref_E)\n")
for i in range(6):
    part = street[i*4:(i+1)*4]
    P(f"\n### 6-{i+1}. " + ", ".join(x[1] for x in part) + "\n```")
    P(f"{STYLE}\nSmall street props for a sunny white harbor town. Draw eight separate objects on a plain flat white background, in a grid of 4 columns and 2 rows with clear space between them, "
      "each complete and not cut off, all seen from the same slight front view at a consistent scale, each sitting on a tiny patch of pale stone pavement.\n"
      "Top row, level 1 (plain): " + "; ".join(f"{j+1}) {x[2]}" for j, x in enumerate(part)) + ".\n"
      "Bottom row, level 2 (decorated), each directly under its level 1 version with the same base shape and size: " + "; ".join(f"{j+1}) {x[3]}" for j, x in enumerate(part)) + ".\n"
      "No characters. " + NOTXT + "\n```")
P("\n## 7. 마을 지도 소품 (3장, 레퍼런스: ref_F)\n")
P("\n### 7-1. 지도 장식 16개\n```")
P(f"{STYLE}\nSixteen small decoration sprites for a sunny white harbor town map, on a plain flat white background, in a grid of 4 columns and 4 rows with clear space between them, each complete and not cut off, all at a consistent small scale, seen from a slight front view, each sitting on a tiny patch of pale stone pavement:\n"
  "1) a tall slim cypress tree, 2) a round olive tree, 3) a small lemon tree, 4) a pink bougainvillea bush, 5) a tiny white house with a blue dome, 6) a tiny white house with a flat roof and a blue door, 7) a short white stone wall piece, 8) a few white stone steps, "
  "9) a small wooden rowboat, 10) a wooden barrel, 11) a small stack of crates, 12) an iron mooring post with rope, 13) a pot of blue flowers, 14) a small grey rock pair, 15) a coil of rope, 16) a fishing net with two floats.\n"
  "No characters. " + NOTXT + "\n```")
P("\n### 7-2. 지도 위쪽 풍경 띠\n```")
P(f"{STYLE}\nA wide horizontal scenery strip for the top edge of a harbor town map, very wide panoramic format about 3:1. A light blue sky fading to pale at the bottom with a few round puffy clouds, "
  "a calm deep blue sea with a straight horizon, a small white ferry and two little sailboats far away, a tiny lighthouse island very far on the horizon, and along the bottom edge a gentle hill of tiny white houses with blue domes, "
  "the bottom edge fading into plain pale cream stone so it can blend into a stone ground. Simple and flat. " + NOTXT + "\n```")
P("\n### 7-3. 돌길 바닥 타일\n```")
P(f"{STYLE}\nA seamless tileable square ground texture of pale cream stone pavement, 1:1, viewed from straight above. Very subtle and flat: soft rounded pale cream and light warm grey paving stones with very faint thin joints, "
  "low contrast so it stays calm behind map objects. It must tile seamlessly on all four edges. No objects, no strong outlines. " + NOTXT + "\n```")

ILL = ("Simple cute flat illustration in the exact style of the first reference image (a kawaii mobile game): chubby chibi animal characters with big heads and small bodies, thick dark brown outlines (#5b3a32), soft pastel colors, flat coloring with only one soft shade per color, no texture, no grain. "
       "The background is very simple and minimal like a sticker or a children's picture book: big flat color areas, a plain sky with a few round puffy clouds, round lollipop-shaped trees, smooth rounded shapes, only a few large background elements, no small clutter, no tiny details, no complex perspective. "
       "The characters are large in the foreground and clearly the focus. Wide landscape composition, 3:2 (1536x1024).")
END = "Seen from the viewpoint of the unseen cafe owner: the characters look toward the viewer. No humans, no text, no letters, no numbers, no logos, no watermark, no frame or border."
P("\n## 8. 이벤트 일러스트 (3장, 레퍼런스는 장면마다 적은 순서대로. 첫 번째는 항상 ref_G)\n")
ev = [
 ('ev14 · 하얀 항구 도착', 'ref_G → walk_flamingo → walk_otter(몽돌 걷기 시트) → gelato_base → post_base',
  "The second and third reference images are the character sheets of the flamingo and the otter: draw them exactly like that. The fourth and fifth reference images are shop sheets: draw those two shops exactly like their abandoned version in the top left panel (faded, cracked, empty), small in the background. The bear and the bunny look exactly like the bear and the bunny in the first reference image.",
  "a quiet white harbor town in the soft morning: a calm blue sea, a straight horizon, a gentle hill of small white houses with blue domes, and behind the characters along the pale stone quay the two abandoned shops from the shop sheets, a small faded gelato shop and a faded post office with a stopped clock. The small white yacht with a navy striped sail is tied at the quay. In the foreground, a pink flamingo in a little white captain hat steps off the yacht with a graceful wave; a chubby brown bear with a cream muzzle, holding the honey-pot notebook, looks around with wide curious eyes; a white bunny with long upright ears and pink inner ears hops beside him; a round dark chocolate brown sea otter with a silver-grey face and a striped apron peeks out shyly from behind a crate, holding a pebble."),
 ('ev15 · 우체국 편지 기록', 'ref_G → walk_puffin(또박 걷기 시트) → post_base',
  "The second reference image is the character sheet of the puffin: draw it exactly like that. The third reference image is the post office sheet: draw the inside of that same post office in its finished colors (white walls, navy trim, sky blue accents, gold horn emblem). The bear and the bunny look exactly like the bear and the bunny in the first reference image.",
  "the cozy inside of the small harbor post office with tall wooden pigeonhole shelves full of letters. On the counter lies a big open old ledger, and spread around it are many small cream envelopes, every one sealed with the same little pink seashell. A round puffin with a sky blue postman cap points a wing at the envelopes with a surprised face; a chubby brown bear with a cream muzzle holds up the honey-pot notebook next to one of the envelopes to compare, with sparkling surprised eyes; a white bunny with long upright ears covers her mouth with both paws in amazement. Warm light from a round window."),
 ('ev16 · 여객선 출항', 'ref_G → walk_sealion(첨벙 걷기 시트) → walk_albatross(훨훨 걷기 시트) → ferry_base',
  "The second and third reference images are the character sheets of the sea lion and the albatross: draw them exactly like that. The fourth reference image is the ferry terminal sheet: draw the terminal exactly like its finished version in the bottom left panel (white walls, sky blue trim, blue roof, gold ship wheel emblem) and the white ferry with the red funnel with a white stripe. The bear and the bunny look exactly like the bear and the bunny in the first reference image.",
  "a sunny stone quay with the white ferry with a red funnel ready to leave, little pennant flags fluttering, and the finished ferry terminal from the sheet behind. On the quay, a brown sea lion in a navy captain jacket and cap salutes cheerfully; an old round albatross with small round glasses and a faded sailor cap points a long wing south across the sea; a chubby brown bear with a cream muzzle holds the honey-pot notebook open to a page with a small hand-drawn island map; a white bunny with long upright ears waves excitedly. Far across the calm sea, a small green tropical island with tall palm trees sits on the horizon."),
]
for t, refs, rl, sc in ev:
    P(f"\n### {t}\n레퍼런스 순서: {refs}\n```")
    P(f"{ILL}\n{rl}\nScene: {sc}\n{END}\n```")

MENU = [
 ('M1', '베이커리', ['프렌치토스트 탑', '크루아상 탑', '브런치 보드'],
  ['a tall stack of thick golden French toast slices with whipped cream, berries and maple syrup dripping', 'a pyramid tower of golden croissants tied with a cream ribbon', 'a wooden brunch board with a croissant, mini sandwiches, a sunny side up egg, fruit and a little jam jar']),
 ('M2', '커피', ['아포가토 세트', '모카 롤케이크', '커피 디저트 트레이'],
  ['an affogato set: a glass cup of vanilla ice cream with espresso poured over it on a small tray with a biscotti', 'a mocha roll cake on a plate with one slice cut showing the coffee cream spiral, topped with chocolate curls', 'a two-tier dessert tray with mini tiramisu cups, coffee macarons and cream puffs']),
 ('M3', '딸기', ['딸기 탕후루 다발', '딸기 밀푀유', '딸기 3단 케이크'],
  ['a bouquet of glossy candied strawberry skewers wrapped in pink paper with a ribbon', 'a tall strawberry mille-feuille with layers of flaky pastry, cream and strawberries, dusted with sugar', 'a three-tier strawberry cream cake covered with strawberries and small white flowers']),
 ('M4', '초콜릿', ['초코 에클레어 탑', '초코 3단 케이크', '초콜릿 정원'],
  ['a pyramid tower of chocolate glazed eclairs with gold sprinkles', 'a three-tier chocolate cake with chocolate drips, berries and chocolate curls', 'a round chocolate cake made like a little garden, with chocolate flowers, chocolate mushrooms and a tiny chocolate fence']),
 ('M5', '꽃차', ['꽃 젤리 케이크', '정원 티파티 세트', '꽃 롤케이크'],
  ['a round clear jelly cake with real-looking flowers suspended inside', 'a garden tea party set on a tray: a floral teapot, two tea cups and small flower cakes', 'a pastel roll cake decorated with pressed flower petals on the outside and a cream swirl inside']),
 ('M6', '아이스크림', ['아이스크림 와플', '아이스크림 3단 케이크', '무지개 콘 꽃다발'],
  ['a square waffle topped with three ice cream scoops, fruit and syrup', 'a three-tier ice cream cake with colorful scoop layers, wafers and cherries', 'a bouquet of rainbow ice cream cones wrapped in paper with a big ribbon']),
 ('M7', '사탕', ['사탕 열기구', '사탕 회전목마', '사탕 기차'],
  ['a little hot air balloon made of a big round striped lollipop with a candy basket full of sweets', 'a small candy carousel with lollipop poles, gummy horses and a striped candy roof', 'a cute candy train with a locomotive and two cars made of candies, carrying gumdrops']),
 ('M8', '붕어빵', ['초코 바나나 붕어빵', '미니 붕어빵 꼬치', '붕어빵 파르페'],
  ['a fish-shaped bread split open showing chocolate and banana slices inside', 'a skewer of five mini fish-shaped breads drizzled with chocolate and sprinkles', 'a tall parfait glass with ice cream, cream and fruit topped with two mini fish-shaped breads']),
 ('M9', '애플파이', ['캐러멜 사과 꼬치', '사과 롤케이크', '3단 파이 탑'],
  ['a bundle of three glossy caramel apples on sticks with nuts and a ribbon', 'an apple roll cake on a plate with apple slices on top and a caramel drizzle', 'a tower of three stacked lattice apple pies with apple slices and a small flag on top']),
]
MT = ("Cute cozy cafe mobile game item icon sheet, 1 row x 3 columns of three separate dessert item icons, levels 11 to 13 of one merge chain, each one bigger and fancier than the one before. "
      "Left (level 11): {a}. Middle (level 12): {b}. Right (level 13): {c}. "
      "Match the art style of the attached reference exactly (it shows levels 8 to 10 of the same chain): rich warm glossy colors with soft cel shading and small white highlights, thick warm dark brown outline (#5b3a32), simple chunky shapes, slightly top-down front view, no faces. "
      "Each icon centered in its own cell with empty space around it, never touching the others. No text, no numbers, no letters. Transparent background, PNG.")
P("\n## 9. 메뉴 Lv.11~13 시트 (9장, 레퍼런스: ch6/refs의 그 계열 ref_M 한 장, 크기 1536×512 또는 3:1)\n")
P("6장에선 Lv.11만 열지만, 그림 느낌을 맞추려고 Lv.11~13을 한 장에 같이 뽑습니다(Lv.12는 7장, Lv.13은 8장에서 열기).\n")
for k, ko, nm, it in MENU:
    P(f"\n### 9-{k[1:]}. {ko}: {' → '.join(nm)}\n레퍼런스: ref_{k}_{ko}_Lv8-10.png\n```")
    P(MT.format(a=it[0], b=it[1], c=it[2]) + "\n```")

txt = "\n".join(out)
open('/home/claude/ch6/ch6_prompts.md', 'w').write(txt)
print(len(txt), "chars", txt.count('```') // 2, "blocks")
