cd /home/claude/webapp_proto && python3 -m http.server 8766 >/dev/null 2>&1 & P1=$!
cd /home/claude/webapp && python3 -m http.server 8765 >/dev/null 2>&1 & P2=$!
sleep 1; cd /home/claude/tools; "$@"; R=$?; kill $P1 $P2; exit $R
