#!/bin/sh
set -e
VER=2.21.70
python3 compress.py >&2
{
cat <<H
//@name sweet_merge_cafe
//@display-name 🧁 달콤 머지 카페
//@api 3.0
//@version $VER
//@update-url https://raw.githubusercontent.com/shakeit08/risu-plugins/main/sweet_merge_cafe.js

// 달콤 머지 카페 — 리스 채팅 중에 즐기는 디저트 카페 머지 게임
H
echo "const ART = (() => {"
MC_EXT=1 MC_EXT_URL=1 python3 embed.py
echo "return { CHAINS, CHAIN_KEYS, XMAS_CHAINS, XMAS_ART, SKIN_FACE, ART_ITEMS, ART_GENS, ANIMALS, UI, iconItem, iconGen, genName, hasGenArt, iconBag, iconAnimal, cafeScene, areaScene, lockedScene, SPOT_BOX, CAFE_BOX, paintBox, spotPos, HOUSE, townLot, townFence, TOWN_BG, TOWN_BG2, WALK, ST_IMG, DEB_IMG, ST_DIM, MAP, ART_TOOLS, WHEEL, EXT_FILES, extFill, STORY_IMG, iconRes, iconChest };"
echo "})();"
echo "const VER = '$VER';"
echo
python3 font.py
} > sweet_merge_cafe.js
