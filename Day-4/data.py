class Subject:
    def __init__(self, name, score, max_score=100):
        self.name = name
        self.score = score
        self.max_score = max_score


class Student:

    def __init__(self, name, rollno, subjects = None):
        self.name = name
        self.rollno = rollno
        self.subjects = subjects if subjects is not None else []

    def total_marks(self):
        return sum(subject.score for subject in self.subjects)


    def pass_fail(self, pass_marks = 40):
        if not self.subjects:
            return "No Subjects"

        for subject in self.subjects:
            if subject.score < pass_marks:
                return "Fail"
            else:
                return "Pass"

    def getcgpa(self):
        if not self.subjects:
            return 0.0

        total_possible = sum(subject.max_score for subject in self.subjects)
        obtained = self.total_marks()

        percentage = (obtained / total_possible) * 100
        return round(percentage / 9.5, 2)

    def add_subject(self, subject_name, score):
        self.subjects.append(Subject(subject_name, score))