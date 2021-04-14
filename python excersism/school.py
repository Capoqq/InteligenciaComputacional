class School:
    __slots__ = ['students']
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade
        self.students = {k:v for k,v in sorted(self.students.items(), key=lambda i:(i[1], i[0]))}

    def roster(self):
        return list(self.students.keys())

    def grade(self, grade_number):
        return sorted([k for k,v in self.students.items() if v == grade_number])