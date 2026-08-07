export default async function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, prenom, nom, source, business } = req.body;

  if (!email) {
    return res.status(400).json({ error: 'Email requis' });
  }

  const AIRTABLE_BASE_ID = 'appZFtopEQ92W8zLl';
  const AIRTABLE_TABLE_ID = 'tblpyIJjmTX2Z7Ble';
  const AIRTABLE_TOKEN = process.env.AIRTABLE_TOKEN;

  if (!AIRTABLE_TOKEN) {
    return res.status(500).json({ error: 'Configuration Airtable manquante' });
  }

  const fields = {
    email: email,
    nom: prenom || nom || 'Non renseigné',
    source: source || 'site'
  };

  // Si un statut/activité est fourni et correspond à une option existante,
  // on pourrait l'ajouter ici. Pour l'instant on ne l'envoie pas pour éviter
  // les erreurs de permission sur le single select.

  try {
    const response = await fetch(`https://api.airtable.com/v0/${AIRTABLE_BASE_ID}/${AIRTABLE_TABLE_ID}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${AIRTABLE_TOKEN}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ fields })
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error('Airtable error:', errorData);
      return res.status(response.status).json({
        error: errorData.error?.message || 'Erreur Airtable'
      });
    }

    const data = await response.json();
    return res.status(200).json({ success: true, id: data.id });
  } catch (error) {
    console.error('Server error:', error);
    return res.status(500).json({ error: 'Erreur serveur' });
  }
}
