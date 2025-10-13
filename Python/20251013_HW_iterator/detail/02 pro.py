def create_text():
    with open('text.txt', 'w', encoding='utf-8') as f:
        line = f.write('Строка \n Вторая \n Ну и третья')

create_text = create_text()


def read_text():
    with open('text.txt', 'r', encoding='utf-8') as f:
        line = f.read()
        return line.strip()

read_text = read_text()
print(read_text[1:5])