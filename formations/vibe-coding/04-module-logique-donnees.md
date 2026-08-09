# Module 4 — Ajouter la logique et les données (12 minutes)

## Contexte visuel
Screencast Lovable + Supabase/Airtable. Avatar en bas à droite.

## Script

Une belle interface sans données, c'est juste une maquette.

Dans ce module, on connecte une base de données pour que ton application stocke et récupère des informations.

### Option 1 : Supabase

Supabase est une base de données gratuite très populaire avec Lovable.

1. Crée un compte sur supabase.com
2. Crée un nouveau projet
3. Copie l'URL et la clé API
4. Dans Lovable, va dans les paramètres et connecte Supabase

### Option 2 : Airtable

Si tu préfères quelque chose de plus simple, Airtable peut aussi servir de base de données.

### Ce qu'on va créer

Prenons l'exemple d'un CRM simple pour indépendants :
- Table "Prospects" avec nom, email, statut, date de relance
- Formulaire pour ajouter un prospect
- Page dashboard qui liste les prospects
- Bouton pour supprimer un prospect

### Tester les parcours

Une fois connectée, teste chaque action :
- Ajouter un prospect
- Voir la liste
- Modifier un statut
- Supprimer un prospect

Si un parcours ne fonctionne pas, demande à Lovable de le corriger avec un prompt précis.

### Gérer l'authentification

Pour une vraie application, ajoute une page de connexion. Lovable peut générer l'authentification avec Supabase Auth en quelques clics.

