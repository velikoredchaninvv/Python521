# Уровень 1: Базовый
# Задача: создайте текстовый файл, в котором будет записано название любимой книги и её автора. Программа должна считать содержимое файла и вывести его на экран.

book = input('Введите название книги: ')
author = input('Введите имя автора книги: ')

class Book():
    def __init__(self, book, author):
        self.book = book
        self.author = author
        with open('books.txt', 'w', encoding='utf-8') as f:
            f.write(f'Название книги: {self.book}' + '\n')
            f.write(f'Имя автора: {self.author}' + '\n')

    def __str__(self):
        return f'Название книги: {self.book}, Имя автора: {self.author}'
    
book = Book(book, author)
print(book)