# Book Scraper

Ce projet est un scraper qui extrait des données de livres depuis le site [Books to Scrape](http://books.toscrape.com). Il collecte des informations telles que le titre, le prix, la description, la catégorie et les images des livres, puis les enregistre dans des fichiers CSV.
Les images des livres sont également enregistrées.

## Structure du Projet

Voici la structure des fichiers et dossiers du projet :
```
/app/
├── functions.py          # Fonctions utilitaires
├── classes.py            # Définition des classes et méthodes
├── code_scrap_book.py    # Logique de scraping des livres
│
/csv/                     # Dossier pour stocker les fichiers CSV générés
/pictures/                # Dossier pour stocker les images des livres
main.py                   # Fichier principal à exécuter
requirements.txt          # Liste des dépendances
```

## Installation

Assurez-vous d'avoir Python installé sur votre machine. Ensuite, installez les dépendances nécessaires en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

## Utilisation

Pour exécuter le scraper, lancez le fichier principal :

```bash
python main.py
```

Le scraper va parcourir toutes les catégories de livres, récupérer les informations de chaque livre et les enregistrer dans des fichiers CSV dans le dossier `csv/`. Les images des livres seront également téléchargées dans le dossier `pictures/`.


### Fonctionnalités

- **Scraping des livres** : Extrait les informations des livres à partir des pages de catégories.
- **Téléchargement des images** : Télécharge les images des livres et les enregistre localement.
- **Export CSV** : Les données des livres sont enregistrées dans des fichiers CSV par catégorie.

### Exemple de Données

Les fichiers CSV contiendront les colonnes suivantes pour chaque livre :

- `product_page_url`
- `universal_product_code`
- `title`
- `price_including_tax`
- `price_excluding_tax`
- `number_available`
- `product_description`
- `category`
- `review_rating`
- `image_url`

Les images téléchargées seront nommées de cette façon : `universal_product_code` + `_` + `title`

## Contributeurs

Si vous souhaitez contribuer à ce projet, n'hésitez pas à faire des suggestions ou à soumettre des pull requests.

## Licence

Ce projet n'est pas sous licence
