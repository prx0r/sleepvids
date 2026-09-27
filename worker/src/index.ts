export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname.replace('/', '');
    
    const object = await env.BUCKET.get(path);
    if (object) {
      const headers = new Headers();
      object.writeHttpMetadata(headers);
      headers.set('etag', object.httpEtag);
      headers.set('Access-Control-Allow-Origin', '*');
      return new Response(object.body, { headers });
    }
    
    if (!path || path === '') {
      const index = await env.BUCKET.get('longhaul.html');
      if (index) {
        return new Response(index.body, {
          headers: { 'Content-Type': 'text/html', 'Access-Control-Allow-Origin': '*' }
        });
      }
    }
    
    return new Response('Not found', { status: 404 });
  }
};
