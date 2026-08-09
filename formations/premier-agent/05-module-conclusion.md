# Module 5 — Mise en production et routine (5 minutes)

## Contexte visuel
Screencast n8n : bouton "Activate", exécutions, logs. Avatar en bas à droite.

## Script

Ton agent est construit, connecté et testé.

Maintenant, il faut le mettre en production.

### Activer l'agent

Dans n8n, clique sur le bouton "Activate Workflow" en haut à droite.

À partir de ce moment, l'agent tourne en continu. Dès que le déclencheur reçoit une nouvelle information, l'agent exécute tout le workflow.

### Surveiller les exécutions

Va dans l'onglet "Executions".
Tu vois toutes les exécutions passées :
- Les succès en vert
- Les échecs en rouge
- Le temps de traitement
- Les données entrantes et sortantes

Si une exécution est rouge, clique dessus pour voir exactement où ça a bloqué.

### Améliorer l'agent au fil du temps

Un bon agent IA n'est jamais parfait du premier coup. Voici comment l'améliorer :

1. **Regarde les cas réels** : quelles demandes l'agent a mal traitées ?
2. **Ajuste le prompt** : ajoute des exemples, des consignes, des exclusions.
3. **Ajoute des conditions** : si l'email est vide, envoie une relance. Si la demande est hors cible, classe-la différemment.
4. **Demande du feedback** : quand tu reçois un récap Slack, demande à l'agent de te demander si c'était pertinent.

### Routine hebdomadaire

Prends 15 minutes chaque vendredi pour :
- Vérifier les exécutions de la semaine
- Corriger 1 ou 2 cas limites
- Ajouter une petite amélioration au prompt

En 1 mois, ton agent deviendra très fiable.

### Prochaines étapes

Tu as maintenant un agent qui fonctionne. Tu peux :
- En construire un deuxième pour une autre tâche
- Rejoindre Les Ateliers IA sur Skool pour partager ton agent
- Passer au Pack IA Factory pour maîtriser prompts, agents et contenu

Tu vois : automatiser, ce n'est plus réservé aux développeurs. Avec un prompt clair et un outil no-code, tu peux déjà gagner des heures chaque semaine.

Bravo d'être arrivé jusqu'ici.

On se retrouve dans la communauté.

## Éléments à l'écran

- Capture du bouton "Activate" dans n8n
- Onglet "Executions" avec succès/échecs
- Exemple de log d'erreur
- CTA vers Skool et Pack IA Factory

## Exercice final
Active ton agent en production et note pendant 3 jours combien de temps il t'a fait gagner.
