
## Rôle du module

Le répertoire `static` contient les ressources statiques de l’application. Il fournit les styles visuels de l’interface de la calculatrice.

## Fichiers principaux

- `style.css` : définit la mise en page, les couleurs et les états interactifs de l’afficheur et des boutons de la calculatrice.
- `README.md` : décrit le rôle du répertoire et l’utilisation de ses ressources.

## Dépendances et hypothèses

- Flask sert les fichiers de ce répertoire comme ressources statiques. Le modèle `templates/index.html` charge `style.css` via `url_for('static', filename='style.css')`.
- Les règles CSS ciblent les éléments et sélecteurs utilisés dans `index.html`, notamment `.calculator`, `.buttons`, `.btn`, `.operator` et `#display`.
- Aucune compilation ni bibliothèque CSS externe n’est nécessaire.