from Teacher import Teacher


def main():
    Teacher = Teacher()

    while True:
        print(
            """
===============================
    Student Management System
===============================
1. Display All Students Data
2. Search for a Student
3. Add a New Student
4. Remove a Student
5. Exit
"""
        )

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            Teacher.display_all()

        elif choice == "2":
            query = int(input("Enter student rollno to search: "))
            if query:
                Teacher.self.students(query)
            else:
                print("Search query cannot be empty.")

        elif choice == "3":
            name = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            isbn = input("Enter ISBN Number: ").strip()

            if title and author and isbn:
                manager.add_book(title, author, isbn)
            else:
                print("Error: All fields (title, author, ISBN) are required.")

        elif choice == "4":
            print("Thank you for using the Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 6.")


if __name__ == "__main__":
    main()