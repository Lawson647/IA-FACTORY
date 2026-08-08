# Fiches récap — Créer ton premier agent IA

## IA Factory — Formation pratique

---

## Les 3 composants d'un agent IA

1. **Déclencheur** : quand l'agent doit agir ?
   - Email reçu
   - Formulaire rempli
   - Heure fixe (tous les matins)
   - Nouveau lead

2. **Traitement** : quelle logique appliquer ?
   - Un prompt système précis
   - Des données à analyser
   - Des règles de décision

3. **Action** : que fait l'agent ?
   - Envoie un email
   - Crée une tâche
   - Envoie une notification
   - Alimente un CRM

---

## Les 5 critères d'une bonne première tâche

1. **Répétitive** : tu la fais souvent
2. **Règles simples** : on peut l'expliquer en 3 étapes
3. **Données structurées** : formulaire, email, fichier
4. **Valeur immédiate** : gain de temps visible
5. **Risque limité** : une erreur n'est pas critique

---

## Idées d'agents rapides à créer

| Tâche | Déclencheur | Action |
|-------|-------------|--------|
| Qualification de devis | Formulaire soumis | Email récap + alerte |
| Relance de leads | Lead inact depuis 7 jours | Email personnalisé |
| Compte-rendu de réunion | Upload de transcription | Résumé + actions |
| FAQ automatique | Question reçue | Réponse + redirection |
| Briefing client | RDV dans 24h | Fiche de préparation |

---

## Template de prompt système

```
Tu es [rôle].
Ta mission : [tâche à accomplir].
Données reçues : [liste des champs].
Traitement : [règles en 3 étapes maximum].
Format de sortie : [email / tableau / liste / JSON].
Ton : [professionnel / chaleureux / direct].
Contraintes : [limites importantes].
```

---

## Checklist de mise en production

- [ ] Agent testé sur 5 cas réels
- [ ] Cas d'erreur gérés (données manquantes, format incorrect)
- [ ] Notification en cas d'échec
- [ ] Documentation de 5 lignes maximum
- [ ] Point de contrôle humain pour les cas sensibles
- [ ] Mesure du temps gagné la première semaine

---

## Rappel important

Un agent IA ne remplace pas le jugement humain.  
Il accélère les tâches répétitives.  
Il doit toujours avoir une "issue de secours" vers un humain.
