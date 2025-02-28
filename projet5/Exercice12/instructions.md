# Instruction - Exercice 12

Vous devez créer un programme pour gérer une bibliothèque. Une bibliothèque peut contenir plusieurs livres. Chaque livre a un titre, un auteur et une année de publication. Les utilisateurs de la bibliothèque peuvent emprunter des livres, les rendre et afficher la liste des livres disponibles.

1. Créez une classe `Book` avec les attributs `title`, `author`, et `year`.
2. Créez une classe `Library` avec deux attributs `books` (livres disponibles dans la bibliothèque) et  `borrowed_books` (livres empruntés)
3. Ajoutez les méthodes suivantes à la classe `Library` :
   - `add_book(self, book)`: Ajoute un livre à la bibliothèque.
   - `remove_book(self, book_title)`: Supprime un livre de la bibliothèque en utilisant le titre du livre comme argument.
   - `borrow_book(self, book_title)`: Emprunte un livre de la bibliothèque en utilisant le titre du livre comme argument. Le livre doit être retiré de la liste des livres disponibles et ajouté dans la liste des livres empruntés.
   - `return_book(self, book_title)`: Rend un livre emprunté à la bibliothèque en utilisant le titre du livre comme argument. Le livre doit être retiré de la liste des livres empruntés et ajouté dans la liste des livres disponibles.
   - `available_books(self)`: Renvoie une liste contenant les titres des livres disponibles dans la bibliothèque.
   - `borrowed_books(self)`: Renvoie une liste contenant les titres des livres empruntés de la bibliothèque.
