from books import Book


class LibraryManager:

    def __init__(self):
        self.books = {
            "101": Book("Hands on Python", "O reilly", "101"),
            "102": Book("Hands on Machine Learning", "O stewart", "102"),
            "103": Book("Hands on CV", "Nitish", "103"),
            "104": Book("Agentic AI", "Krish", "104"),
            "105": Book("Conquer DSA", "Aditya singh", "105"),
        }

    def add_book(self, title: str, author: str, isbn: str):
        if isbn in self.books:
            print(f"Error: A book with ISBN {isbn} already exists.")
            return

        new_book = Book(title, author, isbn)
        self.books[isbn] = new_book
        print(f"Success: '{title}' added to the library.")

    def display_all_books(self):
        if not self.books:
            print("The library catalogue is currently empty.")
            return

        print("\n--- Library Catalog ---")
        for book in self.books.values():
            print(book)
        print("----------------------")

    def search_book(self, query: str):
        query = query.lower()
        results = [
            book
            for book in self.books.values()
            if query in book.title.lower() or query in book.author.lower()
        ]

        if not results:
            print(f"No books found matching '{query}'.")
        else:
            print(f"\n--- Search Results for '{query}' ---")
            for book in results:
                print(book)

    def issue_book(self, isbn: str):
        if isbn in self.books:
            self.books[isbn].borrow()
        else:
            print(f"Error: Book with ISBN {isbn} not found.")

    def return_book(self, isbn: str):
        if isbn in self.books:
            self.books[isbn].return_book()
        else:
            print(f"Error: Book with ISBN {isbn} not found.")