class Book:

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isborrowed = False

    def borrow(self):
        if self.isborrowed:
            print(f"Sorry, '{self.title}' is already borrowed.")
        else:
            self.isborrowed = True
            print(f"You have successfully borrowed '{self.title}'.")

    def return_book(self):
        if not self.isborrowed:
            print(f"'{self.title}' was not checked out.")
        else:
            self.isborrowed = False
            print(f"You have successfully returned '{self.title}'.")

    def __repr__(self):
        status = "Borrowed" if self.isborrowed else "Available"
        return f"[{status}] {self.title} by {self.author} (ISBN: {self.isbn})"