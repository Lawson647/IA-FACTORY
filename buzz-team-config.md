# 🤖 Équipe d'agents Hermes sur Buzz — IA Factory

## Agents recommandés

| Agent | Rôle | Modèle | Spécialité | Channel préféré |
|-------|------|--------|-----------|-----------------|
| **Hermes IA Factory** | Agent généraliste / chef d'orchestre | qwen2.5-coder:32b | Exécution de commandes, vérification, déploiement | #general |
| **Hermes Content** | Rédaction et marketing | qwen2.5-coder:32b | Posts LinkedIn, emails, scripts vidéo, contenu Skool | #content |
| **Hermes Dev** | Développement web | qwen2.5-coder:32b | Modification HTML/CSS, Vercel, GitHub, Airtable | #dev |
| **Hermes QA** | Tests et qualité | qwen2.5-coder:14b | Vérification des liens, captures d'écran, recettage | #qa |

---

## Configuration commune

| Paramètre | Valeur |
|-----------|--------|
| Provider | Ollama (ou Custom OpenAI-compatible) |
| Base URL | `http://2.24.15.63:32768` |
| API Key | laisser vide |

---

## Prompts système par agent

### Hermes Content

```
Tu es Hermes Content, agent spécialisé en marketing et rédaction pour IA Factory.

Mission : créer du contenu percutant pour promouvoir IA Factory : posts LinkedIn, emails de vente, scripts vidéo, descriptions de cours Skool, annonces communautaires.

Règles :
1. Rédige en français, ton professionnel mais chaleureux.
2. Cible : indépendants, freelances, formateurs, coaches, dirigeants de TPE/PME en France.
3. Utilise les offres existantes : Pack IA Factory 149 €, formations 79 €, service création de site web 990–4 900 €.
4. Rends le contenu prêt à publier : pas de placeholder, pas de jargon inutile.
5. Propose toujours 3 variantes quand on te demande un post ou un email.
6. Termine chaque réponse par un CTA clair.

Contexte projet : IA Factory aide les indépendants et TPE à gagner du temps avec l'IA grâce à des formations pratiques, des agents IA et une communauté Skool.
```

### Hermes Dev

```
Tu es Hermes Dev, agent développeur web pour IA Factory.

Mission : modifier le site statique IA Factory, déployer sur Vercel, connecter les formulaires Airtable, générer des PDFs, maintenir la cohérence technique.

Règles :
1. Travaille dans `/workspace/ia-factory/`.
2. Le site est statique HTML/CSS/JS avec Tailwind inline.
3. Avant toute modification, lis le fichier visé.
4. Vérifie que les balises HTML (div, main, nav, section) restent équilibrées.
5. Préserve les formulaires vers `/api/submit-airtable.js`.
6. Ne supprime pas les liens Skool et les offres existantes.
7. Mets à jour `sitemap.xml` si tu ajoutes une page.
8. Après modification, teste avec `python -m http.server 8080` ou vérifie l'URL Vercel.
9. Ne commite pas sans demander la confirmation.
10. N'expose aucune clé API.

Contexte : site en ligne sur https://ia-factory-seven.vercel.app/, repo GitHub Lawson647/IA-FACTORY.
```

### Hermes QA

```
Tu es Hermes QA, agent de recettage pour IA Factory.

Mission : vérifier la qualité du site, détecter les bugs, tester les liens, les formulaires et l'affichage mobile.

Règles :
1. Utilise curl, python requests ou un navigateur headless pour tester.
2. Vérifie les codes HTTP 200 sur les pages principales.
3. Détecte les liens internes cassés.
4. Teste les formulaires avec des données fictives.
5. Signale les problèmes avec : page, sévérité, description, suggestion de correction.
6. Ne modifie jamais le code toi-même ; passe la main à Hermes Dev.

Site à tester : https://ia-factory-seven.vercel.app/
```

---

## Channels Buzz recommandés

| Channel | Usage |
|---------|-------|
| #general | Questions générales, missions transverses |
| #content | Rédaction, marketing, posts, scripts |
| #dev | Code, déploiement, bugfix |
| #qa | Recettage, tests, rapports de bugs |

---

## Missions type à copier-coller

### Mission Content — 3 posts LinkedIn
```
@Hermes Content crée 3 posts LinkedIn pour promouvoir le Pack IA Factory (149 €). 1 post pédagogique, 1 post storytelling, 1 post CTA direct. Prêt à copier-coller.
```

### Mission Dev — vérifier les liens
```
@Hermes Dev vérifie tous les liens internes du site https://ia-factory-seven.vercel.app/ et donne-moi le nombre de liens cassés avec leur URL.
```

### Mission QA — test formulaire
```
@Hermes QA teste le formulaire de https://ia-factory-seven.vercel.app/atelier-gratuit.html avec une donnée fictive et dis-moi s'il répond correctement.
```

### Mission Orchestrateur — créer une nouvelle page
```
@Hermes IA Factory crée une nouvelle page /workspace/ia-factory/formation-automatiser-linkedin.html en copiant le style de formation-10-prompts.html. Prix 79 €, 5 modules, FAQ, CTA vers le Pack IA Factory. Vérifie les balises et mets à jour sitemap.xml.
```

---

## Sécurité

- Aucune clé API ne doit être envoyée dans les messages Buzz.
- Les tokens sont dans `.env` du VPS et dans les variables Vercel.
- L'agent Dev ne doit pas exposer le token Airtable ou GitHub.

## Si l'agent ne répond pas dans Buzz

### ✅ Option rapide — PC Windows

Quand ton PC Windows est allumé, l'agent fonctionne.

1. Ouvre **PowerShell**
2. Tape :
   ```powershell
   hermes
   ```
3. Attends 10–20 secondes
4. Rafraîchis Buzz : **Hermes IA Factory** passe au vert ✅

### 🔧 Option avancée — VPS 24/7 (fonctionnel)

Objectif : faire tourner l'agent dans le container Docker `hermes-agent` du VPS pour ne pas dépendre du PC Windows.

**⚠️ Important :** le gateway Hermes tourne sous l'utilisateur **`hermeswebui`**, pas `root`. La config doit être créée dans `/home/hermeswebui/.hermes/config.yaml`.

**Commandes :**

```bash
# 1. Se connecter au container hermes-agent en root
docker exec -it hermes-agent bash

# 2. Tuer le gateway actuel pour le relancer avec la nouvelle config
ps aux | grep hermes
# repérer le PID de "hermes gateway run --replace"
kill -9 <PID>

# 3. Créer la config en tant qu'hermeswebui
su - hermeswebui -c "cat > /home/hermeswebui/.hermes/config.yaml << 'EOF'
model:
  default_model: qwen2.5-coder:32b
  default_provider: ollama

providers:
  ollama:
    base_url: http://2.24.15.63:33227/v1
    api_key: ""

gateway:
  enabled: true
  workspace: factory-ia
  relay_url: wss://factory-ia.communities.buzz.xyz

surfaces: {}
plugins: {}
tools:
  defaults: []
EOF"

# 4. Relancer le gateway en tant qu'hermeswebui
su - hermeswebui -c 'nohup hermes gateway run > /tmp/hermes-gateway.log 2>&1 &'

# 5. Vérifier les logs
tail -50 /tmp/hermes-gateway.log
```

**Vérification dans Buzz :**
- Aller dans **Agents**
- **Hermes IA Factory** doit être vert
- Lui envoyer `salut` pour tester

**Logs du gateway :**
```bash
tail -f /tmp/hermes-gateway.log
```

**Redémarrer le gateway si besoin :**
```bash
ps aux | grep hermes
kill -9 <PID>
su - hermeswebui -c 'nohup hermes gateway run > /tmp/hermes-gateway.log 2>&1 &'
```

### ❌ Erreurs à éviter

- Ne pas créer la config dans `/root/.hermes/config.yaml` : le gateway ne la voit pas.
- Ne pas lancer `hermes` sans argument : c'est un chat interactif, pas un gateway.
- Lancer `hermes gateway run` (pas `hermes` seul).

---

## URLs importantes

| Ressource | Lien |
|---|---|
| Buzz workspace | `factory-ia` |
| Relay URL | `wss://factory-ia.communities.buzz.xyz` |
| Ollama VPS | `http://2.24.15.63:33227/v1` |
| Site IA Factory | https://ia-factory-seven.vercel.app/ |
| Repo GitHub | https://github.com/Lawson647/IA-FACTORY |

---

IA Factory — Configuration équipe d'agents Buzz
