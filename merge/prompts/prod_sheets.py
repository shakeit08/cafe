# 생산품 Lv.8~15 계획 (Lv.8~10만 프롬프트)
P={
'bakery':('베이커리',['a fruit sandwich cut in half showing whipped cream with strawberry and kiwi slices','a tall three-layer club sandwich tower held with a little pick','a sandwich cake made of stacked bread layers frosted with cream and decorated with vegetables and egg slices']),
'coffee':('커피',['a tall glass of Einspanner coffee topped with a thick swirl of whipped cream','a square slice of tiramisu dusted with cocoa on a small plate','a coffee jelly parfait in a tall glass with coffee jelly cubes, cream and a wafer']),
'berry':('딸기',['a strawberry parfait in a tall glass with layers of cream and strawberries','a folded strawberry crepe filled with cream and strawberries','a two-tier strawberry cream cake with strawberries on top']),
'choco':('초콜릿',['a chocolate fondant cake with melted chocolate flowing out on a plate','a stacked tower of brownies with chocolate drizzle','a little chocolate house made of chocolate bars and candies']),
'tea':('꽃차',['a small tower of pastel macarons decorated with flower petals','a round flower tea cake topped with edible flowers','a wooden box set of flower-shaped Japanese wagashi sweets']),
'icecream':('아이스크림',['a banana split boat with three ice cream scoops and cherries','a big bowl of fruit shaved ice bingsu with ice cream on top','a tall ice cream parfait tower glass with many scoops, wafers and fruit']),
'candy':('사탕',['a wobbly layered jelly cake with gummy bears on top','a round glass bowl of rainbow jellies shaped like a little aquarium with gummy fish','a candy wreath made of lollipops, wrapped candies and a ribbon']),
'fish':('붕어빵',['a fish-shaped bread split open showing custard cream and strawberries inside','a purple sweet potato fish-shaped bread with purple filling and sweet potato pieces','a green matcha fish-shaped bread split open with red bean filling']),
'pie':('애플파이',['an upside-down caramel apple tarte tatin on a plate','a baked apple crumble in a small dish with a scoop of vanilla ice cream','an apple rose tart with thin apple slices arranged like roses']),
}
T=("Cute cozy cafe mobile game item icon sheet, 1 row x 3 columns of three separate dessert item icons, levels 8 to 10 of one merge chain, each one bigger and fancier than the one before. "
 "Left (level 8): {a}. Middle (level 9): {b}. Right (level 10): {c}. "
 "Match the art style of the attached reference: rich warm glossy colors with soft cel shading and small white highlights, thick warm dark brown outline (#5b3a32), simple chunky shapes, slightly top-down front view, no faces. "
 "Each icon centered in its own cell with empty space around it, never touching the others. No text, no numbers, no letters. Transparent background, PNG.")
for k,(ko,it) in P.items():
    print(f"**{ko}**\n```\n{T.format(a=it[0],b=it[1],c=it[2])}\n```\n")
# 이름 계획 Lv.8~15
NAMES={
'bakery':['과일 샌드위치','클럽 샌드위치 탑','샌드위치 케이크','프렌치토스트 탑','크루아상 탑','브런치 보드','빵 꽃다발','황금 빵 트로피'],
'coffee':['아인슈페너','티라미수','커피 젤리 파르페','아포가토 세트','모카 롤케이크','커피 디저트 트레이','티라미수 3단 케이크','황금 커피잔'],
'berry':['딸기 파르페','딸기 크레페','딸기 2단 케이크','딸기 탕후루 다발','딸기 밀푀유','딸기 3단 케이크','딸기 웨딩 케이크','황금 딸기'],
'choco':['초코 퐁당 케이크','브라우니 탑','초콜릿 하우스','초코 에클레어 탑','초코 3단 케이크','초콜릿 정원','초콜릿 성','황금 초콜릿'],
'tea':['꽃잎 마카롱 탑','꽃 티케이크','꽃 화과자 세트','꽃 젤리 케이크','정원 티파티 세트','꽃 롤케이크','꽃마차 티세트','황금 찻잔'],
'icecream':['바나나 스플릿','과일 빙수','파르페 타워','아이스크림 와플','아이스크림 3단 케이크','무지개 콘 꽃다발','아이스크림 성','황금 아이스크림'],
'candy':['젤리 케이크','젤리 어항','사탕 화관','사탕 열기구','사탕 회전목마','사탕 기차','솜사탕 성','황금 사탕'],
'fish':['딸기 슈크림 붕어빵','자색 고구마 붕어빵','말차 팥 붕어빵','초코 바나나 붕어빵','미니 붕어빵 꼬치','붕어빵 파르페','붕어빵 케이크','황금 잉어빵'],
'pie':['타르트 타탱','사과 크럼블','사과 장미 타르트','캐러멜 사과 꼬치','사과 롤케이크','3단 파이 탑','사과 정원 케이크','황금 사과 파이'],
}
