# TP3-13 - LOG3000

## Nom du projet
Calculatrice web simple

## Objectif
Ce projet a pour but de créer une application web permettant d’effectuer des calculs simples à partir d’une expression saisie par l’utilisateur. L’interface est réalisée avec Flask et les opérations mathématiques sont gérées dans un module dédié.

## Description
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

## Installation
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
Pour démarrer l’application :

```bash
python app.py
```

Ensuite, ouvrir dans le navigateur :

```text
http://127.0.0.1:5000/
```

## Structure du projet
- `app.py` : point d’entrée de l’application Flask
- `operators.py` : fonctions d’opérations mathématiques
- `templates/index.html` : page HTML de l’interface utilisateur
- `static/style.css` : styles de l’application

## Fonctionnement
L’utilisateur entre une expression dans le formulaire web. La route principale récupère la saisie, valide le format et effectue le calcul. En cas d’erreur, un message est affiché à l’écran.

## Remarques
Ce projet est une base de travail pour un exercice de programmation avec Flask. Il peut être enrichi avec des validations supplémentaires, une meilleure gestion des erreurs et des opérations plus avancées.