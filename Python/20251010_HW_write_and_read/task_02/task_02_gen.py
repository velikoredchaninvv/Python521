data = input('Введите строчку: ')

def addtex(self, data):
    n = 0
    while n < data:
        yield n
        n += 1
    
programm = addtex(data)