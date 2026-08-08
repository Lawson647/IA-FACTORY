# Module 3 — Construire l'agent pas à pas (12 minutes)

## Contexte visuel
Screencast de n8n ou Make, avec l'avatar en bas à droite. Démonstration en direct.

## Script

On y est. On va construire un agent simple pas à pas.

Pour cet exemple, on va créer un agent qui qualifie une demande de devis.

**Scénario :** une personne remplit un formulaire sur ton site. L'agent reçoit les informations, pose 3 questions supplémentaires par email, analyse les réponses et t'envoie un récapitulatif avec une recommandation.

### Étape 1 : choisir l'outil

Pour commencer sans coder, je recommande **n8n** (gratuit en auto-hébergement) ou **Make** (très visuel). Zapier fonctionne aussi mais est plus cher.

Tu peux aussi commencer avec un simple **prompt système** dans ChatGPT que tu réutilises manuellement.

Dans cet exemple, on utilise n8n.

### Étape 2 : créer le déclencheur

Le déclencheur est l'événement qui lance l'agent.

Ici, le déclencheur est : "Quand un nouveau formulaire est soumis sur le site."

Dans n8n, tu choisis le nœud "Webhook" ou "Form Submission".

### Étape 3 : connecter l'IA

Tu ajoutes un nœud "OpenAI" ou "Anthropic" avec ton API key.

Tu écris le prompt système suivant :

"Tu es un assistant commercial pour IA Factory. Tu viens de recevoir une demande de devis. Voici les informations : [nom, email, besoin].

Rédige un email de 100 mots maximum à ce prospect pour :
1. Le remercier
2. Lui poser 3 questions précises pour qualifier son besoin
3. Lui proposer un créneau d'appel de 15 minutes

Ton : professionnel et chaleureux."

### Étape 4 : envoyer l'email au prospect

Tu ajoutes un nœud "Send Email" qui prend la réponse de l'IA et l'envoie au prospect.

### Étape 5 : te notifier

Tu ajoutes un deuxième nœud "Send Email" qui t'envoie un récapitulatif :
"Nouveau lead : [nom]. Besoin : [besoin]. L'IA a envoyé les 3 questions. En attente de réponse."

### Étape 6 : tester

Tu remplis toi-même le formulaire. Tu vérifies que l'email part bien, que les questions sont pertinentes, et que tu reçois bien ton récap.

Si ce n'est pas parfait, tu ajustes le prompt.

Et voilà. Tu as créé ton premier agent IA opérationnel.

Dans le prochain module, on va voir comment le sécuriser et le fiabiliser.
