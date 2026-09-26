from teacher import Teacher


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
            rollno = int(input("Enter student rollno to search: ")).strip()
            if rollno:
                Teacher.get_student(rollno)
            else:
                print("Search query cannot be empty.")

        elif choice == "3":
            name = input("Enter student Name: ").strip()
            rollno = input("Enter Rollno: ").strip()

            if not name or not rollno:
                print("Error: Name and Roll Number cannot be empty.")
                continue


            subjects_input = input("Enter Subjects (separated by commas): ").strip()
            marks_input = input("Enter Marks (separated by commas): ").strip()

            subjects_list = [s.strip() for s in subjects_input.split(",") if s.strip()]
            marks_list = [m.strip() for m in marks_input.split(",") if m.strip()]


            if len(subjects_list) != len(marks_list):
                print("Error: The number of subjects and marks must watch!")
                continue


            try:
                subjects_dict = {
                    subj: float(mark) for subj, mark in zip(subjects_list, marks_list)

                }
                Teacher.add_student(name, rollno, subjects_dict)

            except ValueError:
                print("Error: Marks must be valid numbers.")

            

        elif choice == "4":
            rollno = input("Enter student rollno to remove: ").strip()
            if rollno:
                Teacher.remove_student(rollno)
            else:
                print("Roll number cannot be empty.")

        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()