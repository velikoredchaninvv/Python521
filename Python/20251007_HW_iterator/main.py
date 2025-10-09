'''
level 01
Задача: напишите программу, которая использует итератор для последовательного перебора строк текста, разделённого символами перевода строки (\n).
Программа должна по очереди выводить каждую строку.
Если строки закончились, выведите сообщение: «Текст завершён».
'''

class TextIterator:
    def __init__(self, text):
        self.text = text
        self.lines = text.splitlines()
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.lines):
            line = self.lines[self.index]
            self.index += 1
            return line
        else:
            raise StopIteration
        
def process_text(text):
    iterator = TextIterator(text)
    for line in iterator:
        print(line)
    print('Текст завершён')

# Пример использования
text = 'Тут важное сообщение, возможно фраза из фильма, которую все будут цитировать'
process_text(text)