// Receives GitHub's answer and hands the access token back to the /admin editor window.
module.exports = async (req, res) => {
  const host = req.headers['x-forwarded-host'] || req.headers.host;
  const url = new URL(req.url, `https://${host}`);
  const code = url.searchParams.get('code');
  const state = url.searchParams.get('state');
  const cookie = (req.headers.cookie || '').split(';').map(s => s.trim()).find(s => s.startsWith('decap_oauth_state='));
  const expected = cookie ? cookie.split('=')[1] : null;

  let status = 'error';
  let content = { error: 'Connexion refusée.' };
  if (!code || !state || state !== expected) {
    content = { error: 'Session de connexion expirée ou invalide. Réessayez depuis /admin/.' };
  } else {
    try {
      const r = await fetch('https://github.com/login/oauth/access_token', {
        method: 'POST',
        headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify({
          client_id: process.env.GITHUB_CLIENT_ID,
          client_secret: process.env.GITHUB_CLIENT_SECRET,
          code,
          redirect_uri: `https://${host}/api/callback/`,
        }),
      });
      const data = await r.json();
      if (data.access_token) {
        status = 'success';
        content = { token: data.access_token, provider: 'github' };
      } else {
        content = { error: data.error_description || data.error || 'Jeton GitHub manquant.' };
      }
    } catch (e) {
      content = { error: 'Impossible de joindre GitHub.' };
    }
  }

  const message = `authorization:github:${status}:${JSON.stringify(content)}`;
  const origin = `https://${host}`;
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.setHeader('Set-Cookie', 'decap_oauth_state=; Path=/api; Max-Age=0');
  res.end(`<!doctype html><html><body><p>Connexion…</p><script>
(function () {
  var message = ${JSON.stringify(message)};
  var origin = ${JSON.stringify(origin)};
  function receive(e) {
    if (e.origin !== origin) return;
    window.opener.postMessage(message, origin);
    window.removeEventListener('message', receive, false);
    setTimeout(function () { window.close(); }, 500);
  }
  window.addEventListener('message', receive, false);
  window.opener && window.opener.postMessage('authorizing:github', origin);
})();
</script></body></html>`);
};
