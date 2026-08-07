export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const token = process.env.AIRTABLE_TOKEN;
  const baseId = 'appZFtopEQ92W8zLl';
  const tableId = 'tblpyIJjmTX2Z7Ble';

  const { email, prenom, source, statut, notes } = req.body;

  if (!email) {
    return res.status(400).json({ error: 'Email requis' });
  }

  const fields = {
    email: email,
    nom: prenom || '',
    source: source || 'site',
  };

  if (statut) {
    fields.statut = statut;
  }

  if (notes) {
    fields.notes = notes;
  }

  try {
    const response = await fetch(`https://api.airtable.com/v0/${baseId}/${tableId}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ fields })
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Airtable error:', errorText);
      return res.status(response.status).json({ 
        error: 'Erreur Airtable', 
        details: errorText 
      });
    }

    const data = await response.json();
    return res.status(200).json({ 
      success: true, 
      id: data.id 
    });
  } catch (error) {
    console.error('Server error:', error);
    return res.status(500).json({ error: error.message });
  }
}