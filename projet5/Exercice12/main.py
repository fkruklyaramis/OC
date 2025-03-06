class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                return

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                return

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrow_books]


mylibrary = Library()
book = Book("Harry Potter", "J.K. Rowling", 1997)
mylibrary.add_book(book)
print(f"available books: {mylibrary.available_books()}")
print(f"Borrowed books: {mylibrary.borrowed_books()}")
print("Borrow book")
mylibrary.borrow_book("Harry Potter")
print(f"available books: {mylibrary.available_books()}")
print(mylibrary.borrowed_books())
print("return book")
mylibrary.return_book("Harry Potter")
print(f"available books: {mylibrary.available_books()}")
print("Remove book")
mylibrary.remove_book("Harry Potter")
print(f"available books: {mylibrary.available_books()}")
