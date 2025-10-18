# Основа программы:
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        return 0.0
    
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def add_grade_to_student(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                return f"Оценка {grade} добавлена для {name}."
        return f'Ученик с именем {name} не найден.'
    
    def show_student(self):
        if not self.students:
            print('Список учеников пуст.')
        else:
            print('Список учеников:')
            for student in self.students:
                print(f'{student.name} - средний балл: {student.average_grade():.2f}')

# Программа для выполнения:
classroom = Classroom()

while True:
    command = input('Введите команду (add_student, add_grade, show, exit): ').strip().lower()
    if command == 'add_student':
        name = input('Введите имя ученика: ').strip()
        classroom.add_student(Student(name))
        print(f'Ученик {name} добавлен.')
    elif command == 'add_grade':
        name = input('Введите имя ученика: ').strip()
        grade = float(input('Введите оценку: '))
        print(classroom.add_grade_to_student(name, grade))
    elif command == 'show':
        classroom.show_student()
    elif command == 'exit':
        print('Программа завершена.')
        break
else:
    print('Неизвестная команда. Попробуйте снова.')