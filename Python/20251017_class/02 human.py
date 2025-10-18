class Human:
    def __init__(self, name, father_name, born_date, second_name=None):
        self.second_name = second_name
        self.name = name
        self.father_name = father_name
        self.born_date = born_date

    def __str__(self):
        return('Тут ответ')

human = Human('Pupsikov', 'Valera', 'Agafonov', '1999')
print(human)