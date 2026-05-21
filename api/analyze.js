module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });

  const { q1, q2, q3, q4, q5, q6 } = req.body || {};

  if (!process.env.ANTHROPIC_API_KEY) {
    return res.status(500).json({ error: 'not_configured' });
  }

  if (!q1 || !q2 || !q3 || !q4 || !q5) {
    return res.status(400).json({ error: 'missing_answers' });
  }

  const safe = (s) => (s || '').replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n');

  const prompt = `You are conducting a Substrate Audit on behalf of the practice of Jayden Forshee (jaydenforshee.com). Substrate reads businesses at their structural layer — the implicit theory the company is actually running from — and installs AI operating architecture aligned with that reality.

The three layers this practice reads:
— The Substrate (Layer -1): The foundational ontology. What the business actually IS at its base level. The implicit theory governing all decisions, hiring, pricing, positioning — often invisible to the founder because it was never named.
— The Experience (Layer 0): What actually happens between the company and the people it touches. The lived reality vs. the narrated reality.
— The Strategy (Layer 1): The deliberate direction. What the founder says they're doing.

A fracture occurs when the narrated company diverges from the observed company. This divergence always has a substrate — a hidden theory governing behavior even when the founder believes they're running on a different one. Every operational decision made on top of an unexamined substrate deepens the cost of eventually correcting it.

A founder has just completed a self-conducted ontological audit. Here are their answers:

Q1 — What is your business at a foundational level? (Not what it does — what it IS)
"${safe(q1)}"

Q2 — What did you think this would be when you started? What is it now?
"${safe(q2)}"

Q3 — What is your customer actually buying?
"${safe(q3)}"

Q4 — Where do your decisions diverge from your stated strategy?
"${safe(q4)}"

Q5 — What is your company doing that you privately know is wrong?
"${safe(q5)}"

Q6 — If you had no memory of what this company was supposed to be, and observed it for a week — what would you say it is? (Optional)
${q6 ? '"' + safe(q6) + '"' : '(Not answered)'}

---

Your task: produce a deep, precise, highly personal structural reading. This is not business coaching. This is not encouragement. This is an ontological audit — name exactly what substrate this business is running from, what the fracture is, and what it actually costs to leave it unread.

Instructions for the reading:
— Use their actual words back at them. Speak directly to what these specific answers reveal about the structure underneath.
— Do not generalize. Every sentence should be impossible to apply to anyone else's business.
— Do not soften the reading. Precision is kindness here — the founder came for a structural reading, not reassurance.
— Read for what is NOT said as much as what is said. The gaps, the hedges, the places where the answer changes register — these are often the most important signals.
— The fracture name should be specific to this founder — not a generic archetype, but a name that captures the exact shape of their structural misalignment.
— The substrate reading should name the implicit theory that IS governing the business — not the stated one, not what they wish was true, but what the pattern of their answers reveals is actually running underneath.

Return ONLY a valid JSON object with exactly these fields. No preamble, no explanation, just the JSON:

{
  "fractureTitle": "A precise, evocative name for this founder's specific fracture — 3-7 words, names the exact structural shape of their misalignment",
  "fractureDesc": "5-7 sentences. Name the fracture precisely. Use their words. Show them exactly what you see in the structure. Do not soften. Do not use generic framing. Every sentence should land as a recognition, not a lesson.",
  "substrateReading": "3-4 sentences. Name the actual substrate — the implicit theory actually governing this business right now, beneath the one they stated. Be direct. Name what is running.",
  "founderSignal": "2-3 sharp sentences on what Q1 reveals beyond the surface answer — the tell in how they framed their own business, what it says about the substrate they're operating from",
  "driftSignal": "2-3 sentences on the Q2 gap — what the specific distance between their original vision and current reality reveals about how and why the substrate shifted",
  "customerSignal": "2-3 sentences on the gap between what's sold and what's bought — name the specific structural cost of this gap to the business",
  "decisionSignal": "2-3 sentences on what the specific decision divergence in Q4 reveals about the actual operating frame — what it shows about which substrate is actually running",
  "hiddenSignal": "3-4 sentences on Q5 — this is almost always the most important answer in the audit. Name what it reveals structurally, not just operationally. What has been carried without language, and what it costs.",
  "observerSignal": ${q6 ? '"2-3 sentences on what the Q6 outside-view reveals or confirms about the fracture — and the significance of the gap between narrated and observed"' : 'null'},
  "implication": "5-7 sentences. What is the actual structural cost of this specific fracture? What is already happening as a result that the founder may not be attributing to it? What becomes impossible or expensive to build on top of this unread substrate? What has to be named and corrected before any operating architecture is installed? Be specific to what you read.",
  "nextStep": "One direct, specific sentence naming a real first action — not a conversation, not a framework, but the exact thing this specific founder needs to do or write or name before anything else moves.",
  "urgency": "low or medium or high or critical"
}`;

  try {
    const apiResponse = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': process.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-opus-4-5',
        max_tokens: 2500,
        messages: [{ role: 'user', content: prompt }]
      })
    });

    if (!apiResponse.ok) {
      const errData = await apiResponse.json().catch(() => ({}));
      console.error('Anthropic API error:', errData);
      return res.status(500).json({ error: 'api_error', message: errData.error?.message });
    }

    const data = await apiResponse.json();
    const text = data.content?.[0]?.text || '';

    const match = text.match(/\{[\s\S]*\}/);
    if (!match) {
      console.error('No JSON in response:', text.slice(0, 300));
      return res.status(500).json({ error: 'parse_error' });
    }

    const analysis = JSON.parse(match[0]);
    return res.status(200).json(analysis);

  } catch (err) {
    console.error('Handler error:', err);
    return res.status(500).json({ error: 'server_error', message: err.message });
  }
};
