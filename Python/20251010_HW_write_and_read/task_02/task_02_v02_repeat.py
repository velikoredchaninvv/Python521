class addText():
    def __init__(self):
        with open('data.txt', 'a', encoding='utf-8') as f:
            while True:
                data = input('Введите текст: ')
                if data != 'exit':
                    f.write(data + '\n')
                else:
                    break
            
            with open('data.txt', 'r', encoding='utf-8') as f:
                print('Содержимое файла: ')
                for line in f:
                    print(line, end='')

programm = addText()
