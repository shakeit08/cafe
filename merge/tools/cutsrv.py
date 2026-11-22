import http.server, os, sys, re
MODE=sys.argv[1]; CUT=300*1024
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
    def do_GET(self):
        p=self.path.split('?')[0].lstrip('/')
        if not p.endswith('.bin'): return super().do_GET()
        d=open(p,'rb').read(); st=0
        m=re.match(r'bytes=(\d+)-', self.headers.get('Range',''))
        if m: st=int(m.group(1))
        part=d[st:]
        self.send_response(206 if m else 200)
        self.send_header('Access-Control-Allow-Origin','*')
        if MODE=='cl':  # 전체 길이를 알리고 중간에 끊음 → 브라우저 쪽에서 오류
            self.send_header('Content-Length',str(len(part))); self.send_header('Connection','close'); self.end_headers()
            self.wfile.write(part[:CUT]); self.wfile.flush(); self.close_connection=True; return
        self.send_header('Connection','close'); self.end_headers()  # 길이 없이 보내다 끊음 → 조용히 짧게 옴
        self.wfile.write(part[:CUT]); self.close_connection=True
os.chdir('/tmp/gm/srv3'); http.server.ThreadingHTTPServer(('',8767),H).serve_forever()
