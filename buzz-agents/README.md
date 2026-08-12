# Créer les 3 agents Hermes dans Buzz — Instructions

## Agent 1 — Hermes Content

### Dans Buzz : Add agent

| Champ | Valeur |
|-------|--------|
| Name | Hermes Content |
| Description | Rédaction et marketing IA Factory |
| Harness | Buzz Agent (default) |
| LLM Provider | Ollama / Custom |
| Base URL | http://2.24.15.63:32768 |
| Model | qwen2.5-coder:32b |
| System prompt | Copier le contenu de hermes-content-prompt.txt |
| Channels | #content |

---

## Agent 2 — Hermes Dev

| Champ | Valeur |
|-------|--------|
| Name | Hermes Dev |
| Description | Développement web IA Factory |
| Harness | Buzz Agent (default) |
| LLM Provider | Ollama / Custom |
| Base URL | http://2.24.15.63:32768 |
| Model | qwen2.5-coder:32b |
| System prompt | Copier le contenu de hermes-dev-prompt.txt |
| Channels | #dev |

---

## Agent 3 — Hermes QA

| Champ | Valeur |
|-------|--------|
| Name | Hermes QA |
| Description | Recettage et tests IA Factory |
| Harness | Buzz Agent (default) |
| LLM Provider | Ollama / Custom |
| Base URL | http://2.24.15.63:32768 |
| Model | qwen2.5-coder:14b |
| System prompt | Copier le contenu de hermes-qa-prompt.txt |
| Channels | #qa |

---

## Configuration technique commune

| Paramètre | Valeur |
|-----------|--------|
| Provider | Ollama (ou Custom OpenAI-compatible) |
| Base URL | http://2.24.15.63:32768 |
| API Key | laisser vide |

---

## Prompts à copier

1. Ouvrir chaque fichier .txt ci-dessous
2. Ctrl+A puis Ctrl+C
3. Dans Buzz, coller dans le champ System prompt
4. Cliquer Add agent

Fichiers :
- /buzz-agents/hermes-content-prompt.txt
- /buzz-agents/hermes-dev-prompt.txt
- /buzz-agents/hermes-qa-prompt.txt

---

## Channels à créer dans Buzz

- #general
- #content
- #dev
- #qa

---

## Test rapide après création

Dans chaque channel, envoyer :

```
@Hermes Content salut
@Hermes Dev salut
@Hermes QA salut
```

Si les 3 répondent, l'équipe est opérationnelle.
