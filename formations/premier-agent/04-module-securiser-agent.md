# Module 4 — Sécuriser et fiabiliser l'agent (8 minutes)

## Contexte visuel
Screencast avec des exemples d'erreurs et de solutions.

## Script

Un agent IA qui fonctionne bien, c'est bien. Un agent IA qui ne fait pas de bêtises, c'est mieux.

Dans ce module, on va ajouter 3 sécurités essentielles.

### Sécurité 1 : les limites de l'agent

Définis clairement ce que l'agent ne doit PAS faire.

Par exemple :
- Il ne doit pas promettre des prix sans ton accord.
- Il ne doit pas s'engager sur des délais.
- Il ne doit pas répondre à des questions hors sujet.

Dans ton prompt système, ajoute :
"Tu ne dois jamais promettre un prix ou un délai. Si le prospect demande un chiffre, réponds que tu transmets la demande et qu'un conseiller recontactera sous 24h."

### Sécurité 2 : la gestion des erreurs

Dans n8n ou Make, ajoute un nœud "Error Handler". Si l'IA ne répond pas, ou si l'email ne part pas, l'agent doit t'avertir immédiatement.

Configuration simple :
- Si erreur → envoyer un email à toi-même avec les détails
- Si succès → continuer normalement

### Sécurité 3 : quand faire intervenir un humain

L'agent ne doit pas tout faire seul. Il doit savoir quand te passer la main.

Ajoute cette règle dans ton prompt :
"Si la demande du prospect est complexe, urgente, ou sort de ton périmètre, réponds poliment que la demande sera transmise à un conseiller et qu'il sera recontacté sous 24h."

### Monitoring simple

Une fois par semaine, regarde :
- Combien de fois l'agent s'est déclenché
- Combien d'emails ont bien été envoyés
- Combien d'erreurs sont survenues
- Quelles réponses méritent ton intervention

N'essaye pas d'automatiser 100 % dès le début. Commence avec 70 %, puis améliore progressivement.

Dans le dernier module, on déploie l'agent et on mesure le temps gagné.
