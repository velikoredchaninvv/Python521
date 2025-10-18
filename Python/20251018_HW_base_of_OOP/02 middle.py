# Напишите программу, которая:
# Добавляет нового ученика.
# Позволяет добавлять оценки ученику.
# Показывает список всех учеников и их средние оценки.

# {self.name:{self.course:self.grade}}

class Student:
    def __init__(self, name, course=None, grade=None):
        self.name = name
        self.course = course
        self.grade = grade
        self.data = {} # по типу {self.name:{self.course:self.grade}}

    def process_data(self):

        # создаю словарь по имени
        if self.name:
            self.data[self.name] = {}    

            # если изначально ввели, то создаю имя курса
            if self.course:
                    
                    # если изначально ввели, то задаю оценку
                    if self.grade:
                        self.data[self.name][self.course] = self.grade
                
        # Если ученика нет, то создаю ученика
        # Запрашиваю дисциплину
        # Ставлю оценку
        return self.data

    def average_grade(self):
        # запрашиваю имя ученика
        pass

    def __str__(self):
        #формирование таблицы для вывода
        header = "| Name | Course | Grade |\n"
        separator = "|------|------|------|"
        rows = []

        for name, course_data in self.data.items():
             for course, grade in course_data.items():
                rows.append(f"| {name} | {course} | {grade} |\n")

        return header + separator + "".join(rows)

# Запуск программы
student = Student("Иван", "Python", 5)
print(student.process_data())
# student.add_grade(4)
# student.add_grade(5)
# print("Средний балл: ", student.average_grade()) # Вывод: Средний балл: 4.5