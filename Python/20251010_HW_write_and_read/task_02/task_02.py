# Уровень 2: Средний
# Задача: напишите программу, которая создаёт текстовый файл и позволяет пользователю добавлять в него данные построчно. Каждая введённая строка должна добавляться в конец файла. После завершения программы (ввод команды «exit») программа должна вывести полный текст файла.


data = input('Введите строчку: ')

class addText():
    def __init__(self, data):
        self.data = data
        with open('data.txt', '+a', encoding='utf-8') as f:
            while data != 'exit':
                f.write(data + '\n')
                data = input('Введите строчку: ')
            else:
                with open('data.txt', 'r', encoding='utf-8') as out:
                    lines = out.readlines()
    
programm = addText(data)