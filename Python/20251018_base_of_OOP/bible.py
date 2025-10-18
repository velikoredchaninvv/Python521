class Book:
    def __init__(self, title, author, status='В наличии'):
        self.title = title
        self.author = author
        self.status = status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        '''Добавляем новую книгу в библиотеку.'''
        self.books.append(book)
    
    def change_status(self, title, new_status):
        '''Изменяет статус книги по её названию.'''
        for book in self.books:
            if book.title == title:
                book.status = new_status
                return f"Статус книги '{title}' изменён на '{new_status}'"
        return f"Книга '{title}' не найдена"
    
    def show_books(self):
        '''Выводит список вех книг.'''
        if not self.books:
            print('Библиотека пуста.')
        else:
            print('Список книг в библиотеке:')
            for book in self.books:
                print(f"{book.title} ({book.author}) - {book.status}")


library = Library()

while True:
    command = input('Введите команду (add, change, show, exit): ')
    if command == 'add':
        title = input('Введите название книги: ').strip()
        author = input('Введите автора книги: ').strip()
        library.add_book(Book(title, author))
        print(f"Книга '{title}' добавлена в библиотеку.")
    elif command == 'change':
        title = input("Введите название книги: ").strip()
        new_status = input("Введите новый статус (например, 'в наличии' или 'выдана'): ").strip()
        print(library.change_status(title, new_status))
    elif command == "show":
        library.show_books()
    elif command == "exit":
        print("Программа завершена.")
        break
    else:
        print("Неизвестная команда. Попробуйте снова.")