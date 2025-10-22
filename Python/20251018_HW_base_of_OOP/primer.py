class Student:
    def __init__(self, name, course=None, grade=None):
        self.name = name
        self.course = course
        self.grade = grade
        self.data = {} # Словарь для хранения информацииdef process_data(self):
    if self.name:
        self.data[self.name] = {}
        if self.course:
            if self.grade:
                self.data[self.name][self.course] = self.grade


def __str__(self):
    # Формирование таблицы для вывода
    header = "| Name | Course | Grade |\n"
    separator = "|------|--------|-------|\n"
    rows = []

    for name, course_data in self.data.items():
        for course, grade in course_data.items():
            rows.append(f"| {name} | {course} | {grade} |\n")

    return header + separator + "".join(rows)

            # Пример использования
student = Student("Alice", "Math", "A")
student.process_data()
print(student)

student2 = Student("Bob")
student2.process_data()
print(student2)

student3 = Student("Charlie", "History")
student3.process_data()
print(student3)
