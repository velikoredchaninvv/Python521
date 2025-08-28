# result = 0

znam = int(input('Введите число, я найду обратное: '))
try:
    result = 1/znam
except ZeroDivisionError:
    print('Хехе')
    result = None
if result:
    print('Обратное равно ', result)