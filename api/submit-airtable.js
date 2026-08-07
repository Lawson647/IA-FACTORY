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

  const { email, prenom, nom, source, statut, business } = req.body;

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

  // Statut optionnel : envoyé seulement si la valeur correspond à une option existante dans Airtable
  const statutValue = statut || business || '';
  if (statutValue) {
    // Normaliser les valeurs pour correspondre aux options Airtable
    const normalized = statutValue.toString().trim();
    fields.statut = normalized;
  }

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

      // Si l'erreur vient du champ statut (option non autorisée), on réessaie sans le statut
      const errorMsg = errorData.error?.message || '';
      if (statutValue && errorMsg.includes('select option')) {
        delete fields.statut;
        const retryResponse = await fetch(`https://api.airtable.com/v0/${AIRTABLE_BASE_ID}/${AIRTABLE_TABLE_ID}`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${AIRTABLE_TOKEN}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ fields })
        });

        if (retryResponse.ok) {
          const retryData = await retryResponse.json();
          return res.status(200).json({
            success: true,
            id: retryData.id,
            note: 'Inscription enregistrée sans le statut. Vérifiez les options du champ statut dans Airtable.'
          });
        }
      }

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
