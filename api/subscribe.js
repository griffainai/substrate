// Reading Room newsletter — subscribe endpoint.
// The homepage form POSTs { email } here; we add the contact to a Resend Audience
// using the server-side API key (never exposed to the browser).
// Env vars (set in Vercel → Project → Settings → Environment Variables):
//   RESEND_API_KEY      — from resend.com/api-keys
//   RESEND_AUDIENCE_ID  — from resend.com/audiences (create one called "Reading Room")
module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });

  const { email } = req.body || {};
  const ok = typeof email === 'string' && /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
  if (!ok) return res.status(400).json({ error: 'invalid_email' });

  if (!process.env.RESEND_API_KEY || !process.env.RESEND_AUDIENCE_ID) {
    return res.status(500).json({ error: 'not_configured' });
  }

  try {
    const r = await fetch(
      `https://api.resend.com/audiences/${process.env.RESEND_AUDIENCE_ID}/contacts`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email.trim().toLowerCase(), unsubscribed: false })
      }
    );

    // 201 = created. Already-subscribed can come back 409/422 — treat as success (idempotent).
    if (r.ok || r.status === 409 || r.status === 422) {
      return res.status(200).json({ ok: true });
    }

    const err = await r.json().catch(() => ({}));
    console.error('Resend contacts error:', r.status, err);
    return res.status(502).json({ error: 'provider_error' });
  } catch (err) {
    console.error('subscribe handler error:', err);
    return res.status(500).json({ error: 'server_error' });
  }
};
