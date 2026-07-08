# Aggregation = one object contains references to other INDEPENDENT objects - "B has a A"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

lib = Library("NY Public Library")

book1 = Book("Harry Potter 1", "JK Rowling")
book2 = Book("The Hobbit", "JRR Tolkein")
book3 = Book("Colour of Magic", "Terry Pratchet")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

print(lib.name)

for book in lib.list_books():
    print(book)