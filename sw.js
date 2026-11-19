const V = 'mc-2.21.22';
const FILES = ['./', './index.html', './game.js?v=2.21.22', './manifest.webmanifest', './icon-192.png', './icon-512.png', './icon-maskable-512.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(c => Promise.all(FILES.map(u => fetch(new Request(u, { cache: 'reload' })).then(r => c.put(u, r))))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.open(V).then(c => c.match(e.request).then(r => r || fetch(e.request).then(res => { if (res.ok && new URL(e.request.url).origin === location.origin) c.put(e.request, res.clone()); return res; }).catch(() => c.match('./index.html')))));
});
