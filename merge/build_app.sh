#!/bin/sh
# web app (PWA) build -> /home/claude/webapp
set -e
VER=$(grep '^VER=' build.sh | cut -d= -f2)
O=/home/claude/webapp
# 마을·가게 그림은 게임 파일에서 빼서 img/ 묶음 파일로 (게임 파일이 너무 커서 폰에서 무거움)
rm -rf $O/img; mkdir -p $O/img
{
echo "(async () => {"
echo "const ART = (() => {"
MC_RAW=1 MC_EXT=1 MC_NO_STORY=1 MC_EXT_DIR=$O/img python3 embed.py
echo "return { CHAINS, CHAIN_KEYS, XMAS_CHAINS, XMAS_ART, SKIN_FACE, ART_ITEMS, ART_GENS, ANIMALS, UI, iconItem, iconGen, genName, hasGenArt, iconBag, iconAnimal, cafeScene, areaScene, lockedScene, SPOT_BOX, CAFE_BOX, paintBox, spotPos, HOUSE, townLot, townFence, TOWN_BG, TOWN_BG2, WALK, ST_IMG, DEB_IMG, ST_DIM, MAP, ART_TOOLS, WHEEL, EXT_FILES, extFill, STORY_IMG, iconRes, iconChest };"
echo "})();"
echo "const VER = '$VER';"
python3 font.py
echo "})();"
} > $O/game.js
sed "s/__VER__/$VER/g" app_index.html > $O/index.html
sed "s/__VER__/$VER/g" app_sw.js > $O/sw.js
cp app_manifest.webmanifest $O/manifest.webmanifest
mkdir -p $O/story && cp story/ev*.webp story/t_ev*.webp $O/story/ 2>/dev/null || true
mkdir -p $O/bgm && cp bgm/*.mp3 $O/bgm/
ls -la $O
