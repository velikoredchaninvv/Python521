# Использование with:
with open('examle.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content) # Читаем и выводим содержимое файла

# Чтение всего содержимого без with:
file = open('example.txt', 'r', encoding='utf-8')
content = file.read()
print(content)
file.close() # закрываем файл

# Чтение по строкам:
# Используем readline() или readlines() для чтения строки за строкой или получения всех строк в виде списка.
with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip()) # Убираем лишние пробелы

# Запись данных / Перезапись данных
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Привет, мир!\n')
    file.write('Ещё одна строка.')