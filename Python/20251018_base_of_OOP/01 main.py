class Student:
    def __init__(self, name):
        self.name = name
        self.grade = []
    
    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if self.grades:
            return sum(self.add_grade)/len(self.grade)
        return 0.0
    
class Classroom:
    def __init__(self):
        self.studens = []

    def add_student(self, student):
        self.students.append(student)

    def add_grade_to_students(self, name, grade):
        for student in self.studens:
            if student.name == name:
                student.add_grade(grade)
            return f"Оценка {grade} добавлена для {name}"
        return f'Ученик с именем {name} не найден'
    
    def show_student(self):
        if not self.studens:
            print('Список учеников пуст.')
        else:
            print('Список учеников:')
            for students in self.studens:
                print(f'{students.name} - средний балл: {student.average_grade():.2f}')