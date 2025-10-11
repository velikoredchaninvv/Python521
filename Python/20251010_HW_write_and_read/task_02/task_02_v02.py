# Уровень 2: Средний
# Задача: напишите программу, которая создаёт текстовый файл и позволяет пользователю добавлять в него данные построчно. Каждая введённая строка должна добавляться в конец файла. После завершения программы (ввод команды «exit») программа должна вывести полный текст файла.

class addText():
    def __init__(self):
        with open('data.txt', 'a', encoding='utf-8') as f:
            while True:
                data = input('Введите строчку или exit для завершения: ')
                if data != 'exit':
                    f.write(data + '\n')
                else:
                    print('Полный текст')
                    break

            with open('data.txt', 'r', encoding='utf-8') as f:
                print('Содержимое файла: ')
                for line in f:
                    print(line, end='')

programm = addText()