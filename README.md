# TP3-13 - LOG3000

## Nom du projet
Calculatrice web simple

## Objectif
Ce projet a pour but de créer une application web permettant d’effectuer des calculs simples à partir d’une expression saisie par l’utilisateur. L’interface est réalisée avec Flask et les opérations mathématiques sont gérées dans un module dédié.

## Description
▪ Une description complète du but et de la portée du projet.

L’application reçoit une expression du type :

- 12 + 3
- 8 - 2
- 5 * 4
- 20 / 2

Elle vérifie ensuite la validité de l’expression, extrait les opérandes et applique l’opération demandée.

## Prérequis
Avant de lancer le projet, il faut avoir installé :

- Python 3.x
- pip
- Flask
Donc il faut lancer cette commande: ``pip install -r requirements.txt``

## Installation
▪ Un guide d’installation clair (étape par étape).  

1. Ouvrir un terminal dans le dossier du projet.


2. Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   ```
3. Activer l’environnement virtuel :
   - Windows :
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/macOS :
     ```bash
     source .venv/bin/activate
     ```
4. Installer les dépendances :
   ```bash
   pip install flask
   ```

## Lancement
▪ Des instructions d’utilisation détaillées (comment lancer l’app, comment 
utiliser ses fonctionnalités).  

Pour démarrer l’application :

```bash
python app.py
```

Ensuite, ouvrir dans le navigateur :

```text
http://127.0.0.1:5000/
```

### Utilisation des fonctionnalités
▪ Une section sur les tests (comment exécuter les tests que vous ajouterez 
plus tard).  

### Test
1. Commande d’exécution depuis la racine : ``python -m pytest tests/ -v``
2. La liste des tests s'afficheront dans le terminal (échoue ou réussite)
Pour plus de détails, voir le README.md sous le répertoire /tests

### Flux de contribution

1. **Ouvrir une issue** pour signaler un bogue. Décrire le problème, les étapes pour le reproduire, le résultat attendu/obtenu et les tests concernés.
2. **Créer une branche dédiée** à partir de la branche principale à jour. Utiliser un nom explicite, par exemple `issue-1-nom_du_problème` pour une correction.
3. **Effectuer des changements ciblés** et ajouter ou modifier les tests pertinents. Avant de soumettre la contribution, exécuter la suite de tests depuis la racine du projet :

   ```bash
   python -m pytest tests/ -v
   ```

4. **Ouvrir une pull request (PR)** vers la branche principale. Résumer les changements, indiquer l’issue associée et préciser les vérifications effectuées.
5. **Fusionner la PR** après approbation lorsque les vérifications passent et mettre à jour la branche.

## Structure du projet
- `app.py` : 
Rôle du module: point d’entrée et contrôleur de l’application Flask. Il définit la route `/`, reçoit les expressions envoyées par le formulaire, valide et découpe une expression contenant deux opérandes et un opérateur, puis appelle la fonction mathématique correspondante. Il transmet le résultat ou le message d’erreur au modèle `templates/index.html`.
Dépendances et hypothèses: 
   - `app.py` dépend de Flask (`Flask`, `request` et `render_template`) et importe les fonctions du module local `operators.py`. Flask doit être installé à partir des dépendances du projet.
   - L’application suppose que l’expression saisie contient exactement deux opérandes numériques séparés par un seul opérateur parmi `+`, `-`, `*` et `/`. Les espaces sont retirés avant l’analyse; les opérandes sont convertis en nombres décimaux (`float`).
- `operators.py` : 
Rôle du module: module de logique mathématique. Il définit les fonctions `add`, `subtract`, `multiply` et `divide`, appelées par `app.py` pour effectuer les opérations.
Dépendances et hypothèses:
   - `operators.py` ne dépend que des opérations arithmétiques intégrées de Python et suppose que ses arguments sont des nombres compatibles avec ces opérations. 
   - Nous supposons que la division doit agir comme une vraie calculatrice, soit ne pas faire une division entiere par plancher, mais bien une division qui peut donner un nombre à virgule.  
- `templates/index.html` : page HTML de l’interface utilisateur
- `static/style.css` : styles de l’application

