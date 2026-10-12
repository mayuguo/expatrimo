// Starts the GitHub login for the /admin editor (Decap CMS).
// Needs the Vercel environment variables GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET.
const crypto = require('crypto');

module.exports = (req, res) => {
  const clientId = process.env.GITHUB_CLIENT_ID;
  if (!clientId) {
    res.statusCode = 500;
    res.end('GITHUB_CLIENT_ID is not set in the Vercel project settings.');
    return;
  }
  const state = crypto.randomBytes(16).toString('hex');
  const host = req.headers['x-forwarded-host'] || req.headers.host;
  const params = new URLSearchParams({
    client_id: clientId,
    redirect_uri: `https://${host}/api/callback/`,
    scope: 'repo,user',
    state,
  });
  res.setHeader('Set-Cookie', `decap_oauth_state=${state}; Path=/api; HttpOnly; Secure; SameSite=Lax; Max-Age=600`);
  res.statusCode = 302;
  res.setHeader('Location', `https://github.com/login/oauth/authorize?${params}`);
  res.end();
};
