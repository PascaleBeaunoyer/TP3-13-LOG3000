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

### Flux de contribution
▪ Une section sur le flux de contribution (branches, PR, issues). 

## Structure du projet
- `app.py` : point d’entrée de l’application Flask
- `operators.py` : fonctions d’opérations mathématiques
- `templates/index.html` : page HTML de l’interface utilisateur
- `static/style.css` : styles de l’application

  





