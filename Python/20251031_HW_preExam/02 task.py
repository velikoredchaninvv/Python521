# Потом нужно создать документ где будут названия журналов с 2015 по 2025 год за каждый месяц. Видимо внутри издательство, год, месяц, Название.
# Создать полку на которой будут три разных автора.
# Записать в файл документ с журналами
# Записать в файл полку с книгами

class PrintEdition:
    def __init__(self, name):
        self.name = name
        self.editions = {}

    # def add_editions()

    def __str__(self):
        return f'Список изданий: {self.list}'
        
class Book:
    def __init__(self, author):
        self.author = author

    def __str__(self):
        return f'Автор: {self.author}'

class Journal:
    def __init__(self, name, year, month):
        self.name = name
        self.year = year
        self.month = month
    
    def __str__(self):
        return f'Название: {self.name},год: {self.year}, месяц: {self.month}'
    
# createa Edition
edition = PrintEdition('Дома Лучше')
# edition.name = 'Дома Лучше'
print(edition)