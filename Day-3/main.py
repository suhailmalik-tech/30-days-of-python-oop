from manager import LibraryManager


def main():
    manager = LibraryManager()

    while True:
        print(
            """
===============================
    Library Management System
===============================
1. Display All Books
2. Search for a Book
3. Add a New Book
4. Issue a Book
5. Return a Book
6. Exit
"""
        )

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            manager.display_all_books()

        elif choice == "2":
            query = input("Enter book title or author to search: ").strip()
            if query:
                manager.search_book(query)
            else:
                print("Search query cannot be empty.")

        elif choice == "3":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            isbn = input("Enter ISBN Number: ").strip()

            if title and author and isbn:
                manager.add_book(title, author, isbn)
            else:
                print("Error: All fields (title, author, ISBN) are required.")

        elif choice == "4":
            isbn = input("Enter ISBN of the book to issue: ").strip()
            manager.issue_book(isbn)

        elif choice == "5":
            isbn = input("Enter ISBN of the book to return: ").strip()
            manager.return_book(isbn)

        elif choice == "6":
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 6.")


if __name__ == "__main__":
    main()