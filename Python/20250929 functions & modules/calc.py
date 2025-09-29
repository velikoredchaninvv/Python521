# Создание калькулятора для математических операций
# add, subtrack, muliplay, divide


class Calc():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x-self.y

    def multiplay(self):
        return self.x*self.y

    def divide(self):
        return self.x/self.y

    def __str__(self):
        return f'''
        Результат сложения {self.add()}
        Результат вычитания {self.subtract()}
        Результат умножения {self.multiplay()}
        Результат деления {self.divide():.02f}
        '''

x = int(input('Введите значение X: '))
y = int(input('Введите значение Y: '))

answer = Calc(x,y)
out = print(answer)