class Main:
    def __init__(self, name):
        self.name = name

    def rename(self):
        self.name = self.name+'WOW'

    def __str__(self):
        return self.name

class Second:
    def __init__(self):
        self.steps = []

    def add_step(self,data):
        self.steps.append(data)

    def __str__(self):
        return f'Состояние списка: {self.steps}'

second = Second()
second.add_step(Main('Slava'))
print(second)