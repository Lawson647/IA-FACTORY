# Tutoriel — Installer MoneyPrinterTurbo pour IA Factory

## Qu'est-ce que MoneyPrinterTurbo ?

MoneyPrinterTurbo est un outil **open-source** qui génère automatiquement des vidéos courtes (Shorts/Reels/TikTok) à partir d'un sujet ou d'un script.

Il fait tout seul :
- Écrit le script
- Génère la voix off
- Trouve des images/vidéos de stock
- Ajoute des sous-titres
- Ajoute une musique de fond
- Rend une vidéo 9:16 prête à publier

---

## 🎯 Cas d'usage pour IA Factory

| Usage | Comment |
|---|---|
| Shorts YouTube | Extraire les moments clés des vidéos longues |
| Reels Instagram | Adapter le format 9:16 |
| TikTok | Même workflow, même export |
| Faceless channel | Vidéos sans montrer son visage |
| Test viral | Produire beaucoup de contenu vite |

---

## ⚙️ Installation sur le VPS Hostinger

### Prérequis

- Docker et Docker Compose installés ✅ (déjà présents sur le VPS)
- Au moins 4 Go de RAM libres
- 10 Go d'espace disque

### Étape 1 : cloner le repo

```bash
cd /opt
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
cd MoneyPrinterTurbo
```

### Étape 2 : configurer les clés API

Copie le fichier d'exemple :

```bash
cp config.example.toml config.toml
```

Édite `config.toml` avec les clés nécessaires :

```toml
[llm]
provider = "openai"
api_key = "sk-..."
model = "gpt-4o-mini"

[proxy]
# Laisse vide si pas de proxy

[pexels]
api_key = "votre_cle_pexels"  # gratuit sur pexels.com/api

[pexels.video]
# Laisse par défaut
```

### Étape 3 : lancer avec Docker

```bash
docker-compose up -d
```

### Étape 4 : ouvrir l'interface web

```
http://2.24.15.63:8080
```

(Le port exact dépend de la configuration Docker. Vérifie avec `docker ps`.)

---

## 🛠️ Installation locale sur Windows

### Prérequis

- Python 3.10+
- Git
- FFmpeg (télécharger sur https://ffmpeg.org/download.html)

### Étapes

1. **Cloner le repo**
   ```powershell
   git clone https://github.com/harry0703/MoneyPrinterTurbo.git
   cd MoneyPrinterTurbo
   ```

2. **Créer un environnement virtuel**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configurer**
   ```powershell
   copy config.example.toml config.toml
   notepad config.toml
   ```

5. **Lancer**
   ```powershell
   python app.py
   ```

6. **Ouvrir** http://localhost:8080

---

## 📝 Utilisation pour IA Factory

### 1. Générer un Short depuis un sujet

Dans l'interface web :
- **Video Subject** : "5 agents IA pour freelances"
- **Video Language** : French
- **Video Length** : 30-60 seconds
- **Aspect Ratio** : 9:16
- Clique sur **Generate Video**

### 2. Utiliser son propre script

- Active **"Use custom script"**
- Colle un script court et percutant
- Génère la vidéo

### 3. Exemple de script pour un Short IA Factory

```
Tu passes 2 heures par jour à gérer tes emails ?
Moi aussi. Jusqu'à ce que je teste cet agent IA.
En 5 minutes, il lit mes emails, répond aux simples, et classe le reste.
Résultat : je gagne 1h30 chaque jour.
Lien en description pour tester.
```

---

## 🔗 Intégration avec le workflow IA Factory

### Workflow recommandé

1. **Publier la vidéo longue** sur YouTube
2. **Télécharger** la vidéo (via YouTube Studio ou yt-dlp)
3. **Utiliser `shorts_generator.py`** pour extraire les moments forts
4. **Pousser les clips** dans MoneyPrinterTurbo pour ajouter voix/sous-titres/musique
5. **Publier** sur YouTube Shorts, Instagram Reels, TikTok

### Automatisation avancée avec n8n

Voir le fichier `n8n-workflow-youtube-shorts.json` pour un workflow qui :
- Déclenche sur nouvelle vidéo YouTube
- Télécharge la vidéo
- Lance `shorts_generator.py`
- Upload les Shorts sur YouTube

---

## ⚠️ Limites à connaître

| Limite | Explication |
|---|---|
| Qualité variable | Les assets de stock sont parfois génériques |
| Risque de doublon | Beaucoup d'utilisateurs utilisent les mêmes vidéos stock |
| Pas de personnalité | Difficile de créer un vrai lien avec l'audience |
| Dépendance API | Nécessite OpenAI + Pexels |

### Mon conseil

Utilise MoneyPrinterTurbo pour les **Shorts**, mais garde les **vidéos longues** en screencast/test direct pour l'autorité et la confiance.

---

## 📦 Alternative : notre script `shorts_generator.py`

Si MoneyPrinterTurbo est trop lourd, utilise le script Python plus léger dans :
```
/workspace/ia-factory/scripts/shorts_generator.py
```

Il extrait les meilleurs moments d'une vidéo longue et génère des Shorts avec sous-titres et CTA.

---

IA Factory — Tutoriel MoneyPrinterTurbo
Créé le 2026-08-12
