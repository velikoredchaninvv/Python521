from datetime import date

class Task:

    def __init__(self, description, year, month, day):
        self.dt             = date.now()
        self.deadline       = date(year, month, day)
        self.description    = description
        self.done           = False

t = Task('Написать классы Автомобиль, Человек, Одежда, Товар')
# Исправить класс! Добавить параметры, часть сделать по умолчанию
