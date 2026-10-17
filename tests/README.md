# Tests

## But du dossier
Tester la logique de operators.py et les routes de app.py.

## Couverture des tests

- `test_app.py` vérifie que la page d’accueil répond correctement, que la feuille CSS est servie et que certaines requêtes POST (expression incomplète ou entrées non numériques) ne provoquent pas d’erreur serveur. Il contient aussi un cas d’addition.
- `test_operators.py` vérifie les résultats de l’addition, de la soustraction, de la multiplication ainsi que la division entière, la division avec résultat décimal et la division par zéro.
- `test_template.py` vérifie la présence des boutons numériques et des opérateurs avec leurs libellés, l’existence d’un libellé pour chaque bouton, le type de soumission du bouton `=`, et l’affichage initial vide.

### Limites connues

- Le cas d’addition POST de `test_app.py` envoie les champs `num1`, `num2` et `operation`, tandis que l’application actuelle lit le champ `display`. Ce test ne vérifie donc pas le résultat de l’addition via le formulaire actuel.

## Prérequis
- S'assurer d'avoir déjà fait la commande: ``pip install -r requirements.txt``

## Exécution
1. Commande d’exécution depuis la racine : ``python -m pytest tests/ -v``
2. La liste des tests s'afficheront dans le terminal (échoue ou réussite)
