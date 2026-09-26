from data import Student
from data import Subject


class Teacher:

    def __init__(self):
        self.students = {
            "101":Student("Arman", [
                Subject("Math", 88),
                Subject("Stats", 68),
                Subject("Python", 78)
            ] )
        }
    def add_student(self, name, rollno, subjects_dict):

        if rollno in self.students:
            print(f"Error: Roll Number {rollno} already exists.")
            return

        subject_objects = [Subject(name, mark) for name, mark in subjects_dict.items()]
        new_student = Student(name, rollno, subject_objects)
        self.students[rollno] = new_student
        print(f"Student {name} (Roll No: {rollno})  added successfully.")

    

    def get_student(self,rollno):
        if rollno in self.students:
            print()
        else:
            print(f"No student with this {rollno} Rollno Exists")


    def remove_student(self, rollno):
        if rollno in self.students:
            removed = self.students.pop(rollno)
            print(f"Removed student: {removed.name}")
        else:
            print(f"Roll number {rollno} not found.")

    def display_all(self):
        print("\n--- STUDENT RECORDS ---")
        for rollno, student in self.students.items():
            print(f"Roll No: {rollno} | Name : {student.name}")
            print(f"Total Marks: {student.total_marks()}")
            print(f" CGPA: {student.getcgpa()}")
            print(f" Status: {student.pass_fail()}")
            print("_" * 25)
        
