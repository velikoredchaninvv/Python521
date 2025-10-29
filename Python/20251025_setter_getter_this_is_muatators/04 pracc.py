# Написать свойства для человека и для студента.
# Для студента создать свойство для среднего, а человеку - для возраста, не создавая отдельных полей для хранения!

from datetime import datetime

class Human:
    def __init__(self, birth_year):
        pass
        self._birth_year = birth_year

    def get_age(self):
        current_year = 2025 #datetime
        return current_year - self._birth_year
    
    def set_age(self, age):
        current_year = 2025 #datetime
        if age < 0:
            raise ValueError('Возраст не может быть отрицательным')
        self._birth_year = current_year - age

    age = property(get_age, set_age) # Создаём свойство age

    def __str__(self):
        return f'Человек, возраст: {self.age}'


class Student:
    def __init__(self):
        def __init__(self, grades):
            self.grades = grades

        def get_average_grade(self):
            pass
