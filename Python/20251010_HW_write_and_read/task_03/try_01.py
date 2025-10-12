# Уровень 3: Продвинутый
# Задача: создайте программу, которая позволяет подсчитать количество строк,
# содержащих определённое слово в текстовом файле. Пользователь вводит слово,
# которое нужно найти, и программа выводит количество строк, где оно встречается.

# Создание текста
def create_file():
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write('Напишу ка я тут интересный текст. \nПотому что без интересного текста. \nДа и любого текста. \nТем более не интересного. \nИнтересно не будет.')

write_text = create_file()

# тут будет вводиться слово, но сейчас вводится напрямую
word = 'интерес' 
 
#функция поиска слова в файле
def word_search(filename='file.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            line = f.readline()
            word_index = 0
            while line:
                # print(line.strip())
                if word in line.lower():
                    word_index += 1
                    print(word_index, line.strip())
                line = f.readline()
    finally:
            print(f'Количество слов где встреачется искомое слово: {word_index}')


# запуск программы
read_text = word_search()