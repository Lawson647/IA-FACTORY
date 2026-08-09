# Module 4 — Connecter l'agent à tes outils (8 minutes)

## Contexte visuel
Screencast n8n. Connexions aux services : Gmail, Airtable, Slack. Avatar en bas à droite.

## Script

Maintenant qu'on a construit la base de l'agent, on va le rendre utile dans ta vraie vie professionnelle.

Un agent qui tourne dans le vide ne sert à rien. Il faut qu'il puisse lire tes emails, écrire dans tes tableaux, t'envoyer des messages.

Dans ce module, on connecte l'agent à tes outils.

### Étape 1 : connecter Gmail

Dans n8n, ajoute un noeud "Gmail".
Clique sur "Create new credential".
Connecte-toi avec ton compte Google.
Autorise n8n à lire et envoyer des emails.

Ton agent peut maintenant :
- Déclencher une action quand un email arrive
- Envoyer un email automatiquement
- Lire les pièces jointes

### Étape 2 : connecter Airtable

Ajoute un noeud "Airtable".
Crée une nouvelle connexion avec ton token Airtable.
Sélectionne ta base et ta table.

Ton agent peut maintenant :
- Créer une nouvelle ligne avec les infos qualifiées
- Mettre à jour un statut
- Lire des données existantes

### Étape 3 : connecter Slack

Ajoute un noeud "Slack".
Connecte ton workspace.
Choisis le canal où tu veux recevoir les notifications.

Ton agent peut maintenant t'envoyer un message avec le récap du lead.

### Exemple d'agent complet : qualification de demande de devis

Voici le scénario :
1. Un prospect envoie un email à contact@tonsite.com avec sa demande.
2. L'agent lit l'email avec un noeud IA.
3. Il pose 3 questions complémentaires automatiquement.
4. Quand le prospect répond, l'agent crée une ligne dans Airtable.
5. Il t'envoie un récap sur Slack avec un score de qualité.

Résultat : tu ouvres Slack le matin, tu vois directement les bons leads, et tu ignores le bruit.

### Gérer les erreurs

Un agent ne fonctionne pas parfaitement du premier coup. Prévois :
- Un noeud "IF" pour vérifier si l'email contient bien les infos nécessaires
- Un noeud "Error Trigger" pour être alerté si ça plante
- Un message de fallback si l'IA ne comprend pas

Teste chaque étape séparément avant d'activer l'agent en production.

## Éléments à l'écran

- Capture d'écran des credentials n8n (masquer les tokens)
- Schéma de l'agent complet
- Exemple de notification Slack

## Exercice
Connecte au moins un outil à n8n et fais un test simple : envoie-toi un email ou crée une ligne dans Airtable.

## Références
- n8n credentials docs
- Airtable token personal access
- Slack app creation
