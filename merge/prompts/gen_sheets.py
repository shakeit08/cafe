G={
'bakery':('빵 (토스트기 계열)',['a small pink pop-up toaster','a countertop toaster oven with a bread loaf inside','a tall double-deck oven with two glass doors','a bread display cart with shelves of loaves','a big brick bakery oven with a little chimney','a grand golden bakery oven with a tiny crown on top']),
'coffee':('커피 (모카포트 계열)',['a stovetop moka pot','a drip coffee maker with a glass carafe','a compact single-group espresso machine with one cup','a wide double-group espresso machine with two cups','a coffee cart with a striped awning','a grand golden espresso bar counter with a tiny crown on top']),
'berry':('딸기 (화분 계열)',['a strawberry plant in a small pot','a long wooden planter box of strawberries','a two-tier strawberry stand','a strawberry market cart with an awning','a small greenhouse full of strawberries','a grand strawberry gazebo with a heart sign and a tiny crown']),
'choco':('초콜릿 (카카오 계열)',['a cacao seedling in a small pot','a cacao bean roasting drum','a chocolate melting pot with a whisk','a chocolate fountain','a chocolate tempering machine with a mold tray','a grand golden chocolate machine with a tiny crown on top']),
'tea':('허브차 (허브 화분 계열)',['a herb plant in a small pot','a wooden drying rack with hanging herb bundles','a shelf of glass tea jars','a small herb greenhouse','a tea stand with a steaming teapot set','a grand tea pavilion with a golden roof and a tiny crown']),
'icecream':('아이스크림 (아이스크림 메이커 계열)',['a hand-crank ice cream churn','a soft-serve ice cream machine','a double soft-serve machine with two cones','an ice cream freezer display case','an ice cream cart with a parasol','a grand ice cream parlor counter with a giant cone sign and a tiny crown']),
'candy':('사탕 (사탕 기계 계열)',['a small glass candy jar','a round gumball machine','a cotton candy machine with a pink cloud','a candy shelf stall with rows of jars','a lollipop cart with a big swirl lollipop','a grand candy castle stand with a tiny crown']),
'fish':('붕어빵 (붕어빵 틀 계열)',['a single fish-shaped bungeoppang iron pan with a long handle','a tabletop iron with three fish-shaped molds','a griddle station with six fish-shaped molds','a fish bread griddle stall with a striped awning','a bungeoppang street cart with wheels','a grand golden bungeoppang shop stand with a tiny crown']),
'pie':('애플파이 (사과 바구니 계열)',['a woven basket of red apples','a small countertop oven with a pie inside','a cooling rack with three pies','a brick oven with a pie inside','a pie stall cart with an awning','a grand golden pie oven with a tiny crown on top']),
}
POS=['Top-left','Top-middle','Top-right','Bottom-left','Bottom-middle','Bottom-right']
COL=['soft pink','mint green','sky blue','lavender','butter yellow','gold with little sparkles']
T=("Cute cozy cafe mobile game sprite sheet, 2 rows x 3 columns grid of six separate item-generator sprites, one upgrade line from level 1 to level 6, soft pastel cozy game icon style. {items} "
 "Each level must look clearly different at a glance: a different silhouette, a bigger size, and more parts than the level before, so no two levels look alike. "
 "Each level also uses its own trim color on its base or frame, in this order: level 1 soft pink, level 2 mint green, level 3 sky blue, level 4 lavender, level 5 butter yellow, level 6 gold with little sparkles. "
 "Every sprite has a small cute simple face (two dot eyes, tiny smile, blush). Front view, all six drawn at the same scale feeling, each centered in its own cell with empty space around it, never touching the others. "
 "Soft flat pastel colors with gentle simple cel shading, thin warm dark brown outline (#5b3a32), simple shapes, no tiny details, no text, no numbers, no letters. Transparent background, PNG.")
for k,(ko,items) in G.items():
    it=' '.join(f"{POS[i]}: level {i+1}, {d} ({COL[i]} trim)." for i,d in enumerate(items))
    print(f"**{ko}**\n```\n{T.format(items=it)}\n```\n")
