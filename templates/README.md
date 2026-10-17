
## Rôle du module

Le répertoire `templates` contient les modèles HTML utilisés par l’application Flask pour présenter l’interface de la calculatrice et afficher les résultats.

## Fichiers principaux

- `index.html` : définit l’interface de la calculatrice et ses boutons. Le modèle affiche la valeur transmise par l’application dans le champ de résultat.
- `README.md` : décrit le rôle du répertoire et les dépendances de ses modèles.

## Dépendances et hypothèses

- `index.html` est rendu par Flask avec le moteur de modèles Jinja. Il dépend de la route `/`, qui transmet la variable `result`.
- Le formulaire envoie son champ `display` à cette route avec la méthode `POST`.
- La feuille de style `static/style.css` est servie par l’application Flask.