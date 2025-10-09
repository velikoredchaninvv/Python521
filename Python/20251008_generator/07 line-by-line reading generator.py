# Пример 2: Генератор для построчного чтения файлов
# Генератор экномит память, загружая строки файла только по мере необходимости:

def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip() # вместо return возвращает yield для generator

for line in read_file("example.txt"):
    print(line) # построчный вывод содержимого файла

