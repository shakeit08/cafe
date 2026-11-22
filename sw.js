const CACHE_PREFIX = 'sweet-merge-cafe-';
const V = CACHE_PREFIX + '2.21.51';
const FILES = ['./', './index.html', './game.js?v=2.21.51', './manifest.webmanifest', './icon-192.png', './icon-512.png', './icon-maskable-512.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(cache => cache.addAll(
    FILES.map(path => new Request(new URL(path, self.registration.scope), { cache: 'reload' }))
  )).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys
    .filter(key => key === 'mc-2.21.48' || (key.startsWith(CACHE_PREFIX) && key !== V))
    .map(key => caches.delete(key)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const request = e.request;
  const url = new URL(request.url);
  if (request.method !== 'GET' || !url.href.startsWith(self.registration.scope)) return;
  if (request.headers.has('range') || url.pathname.includes('/bgm/')) return;
  e.respondWith(caches.open(V).then(async cache => {
    const cached = await cache.match(request);
    if (cached) return cached;
    let response;
    try {
      response = await fetch(request);
    } catch {
      if (request.mode === 'navigate') return (await cache.match('./index.html')) || Response.error();
      return Response.error();
    }
    if (response.ok) {
      try { await cache.put(request, response.clone()); } catch { /* 캐시가 쓰이지 않아도 받은 응답은 사용 */ }
    }
    return response;
  }));
});
