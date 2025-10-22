class Student:
    def __init__(self, name, course, grade):
        self.name = name
        self.course = course
        self.grade = grade
        self.grades = []
        self.data = {} # seld.data = {self.name: {self.course: self.grade}} // Словарь в словаре

    def data_process(self):
        if self.name:
            self.data[self.name] = {}
            
            if self.course:
                self.data[self.name] = {self.course:None}

                if self.grade:
                    
                    self.grades.append(self.grade)
                self.data[self.name][self.course] = self.grades
                return self.grades

    def __str__(self):
        return f'Имя: {self.name}, Курс: {self.course}, Оценки: {self.grade}'


student = Student('Слава', 'Python', 10)
print(student)