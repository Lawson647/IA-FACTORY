# Fiches récap — Créer ton premier agent IA

## Fiche 1 — Les 3 critères d'une bonne tâche à automatiser

| Critère | Description | Exemple |
|---------|-------------|---------|
| **Répétitive** | Tu la fais plusieurs fois par semaine | Qualifier des demandes de devis |
| **Structurée** | Le processus est prévisible | Questions-réponses standards |
| **À forte valeur** | Gagner du temps ou améliorer un résultat | Mieux qualifier = plus de ventes |

## Fiche 2 — Architecture d'un agent IA simple

```
DÉCLENCHEUR → TRAITEMENT IA → ACTION
    ↓              ↓             ↓
Email reçu    Prompt structuré   Envoi d'email,
Formulaire    Rôle + contexte   Création ligne
Webhook       Format de sortie  Notification Slack
```

## Fiche 3 — Prompt type pour un agent

```
Tu es [rôle].
Voici la donnée reçue : {{$json["champ"]}}
Ta mission : [action à faire]
Format de sortie attendu :
1. [Élément 1]
2. [Élément 2]
3. [Élément 3]
```

## Fiche 4 — Connecteurs essentiels dans n8n

| Outil | Usage | Noeud n8n |
|-------|-------|-----------|
| Gmail | Lire/envoyer des emails | Gmail |
| Google Sheets | Stocker des données | Google Sheets |
| Airtable | Base de données avancée | Airtable |
| Slack | Notifications | Slack |
| Typeform / Tally | Formulaires entrants | Typeform / HTTP Request |
| OpenAI / Anthropic | Traitement IA | OpenAI Chat Model |

## Fiche 5 — Checklist avant mise en production

- [ ] L'agent est testé manuellement avec 3 exemples réels
- [ ] Les credentials sont configurés et valides
- [ ] Le prompt retourne un format stable
- [ ] Les cas d'erreur sont gérés
- [ ] Une notification de fallback est configurée
- [ ] L'onglet "Executions" est consultable
- [ ] Le workflow est activé

## Fiche 6 — Routine d'amélioration hebdomadaire

**15 minutes le vendredi :**
1. Vérifier les exécutions de la semaine
2. Identifier 1 ou 2 cas limites
3. Ajuster le prompt
4. Relancer le test
5. Réactiver l'agent

## Fiche 7 — Idées d'agents par métier

### Indépendant / Freelance
- Qualification de demandes de devis
- Relance de factures impayées
- Résumé de veille hebdomadaire

### Commercial
- Scoring automatique des leads
- Série d'emails de relance
- Briefing avant appel client

### Formateur / Coach
- Classement des inscriptions
- Génération de fiches de cours
- Sondage post-formation

### TPE / PME
- Réponse aux questions fréquentes
- Compte-rendu de réunion
- Rapport hebdomadaire simplifié

## Fiche 8 — Glossaire

| Terme | Définition |
|-------|------------|
| **Workflow** | Suite d'étapes automatisées |
| **Déclencheur** | Événement qui lance l'agent |
| **Noeud** | Bloc de traitement dans n8n |
| **Credential** | Identifiant sécurisé pour connecter un outil |
| **Webhook** | URL qui reçoit des données d'une autre application |
| **Prompt système** | Instruction générale donnée à l'IA |

---

IA Factory — Formation "Créer ton premier agent IA"
