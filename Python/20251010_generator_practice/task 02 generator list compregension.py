'''
Разница между генератором и генератором списка:
Генератор: Это функция, которая использует ключевое слово yield для возврата значений по одному. Генератор не создаёт весь спиок в памяти сразу. Вместо этого он выдаёт значения по требованию, когда вы итерируетесь по нему.
Генератор списка: Это компактный способ создания списка, используя синтаксис, похожий на цикл for внутри квадратных скобок []. Генератор списка создаёт и хранит весь список в памяти сразу.
'''

# Основной синтаксис генератора списка:
# [выражение for элемент in последовательность if условие]

# генератор list comprehension пример
# squares = [x**2 for x in range(10)]
# print(squares)

# через for пример
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

### Через генератор
def multiplies(limit, divisor):
    for number in range(1, limit + 1):
        if number % divisor == 0:
            yield number

## Основная программа
limit = int(input('Введите лимит: '))
divisor = int(input('Введите делитель: '))

print(f'Числа от 1 до {limit}, кратные {divisor}: ')
for multiple in multiplies(limit, divisor):
    print(multiple)

### Генератор списка
def multiples_with_c(limit, divisor):
    return [number for number in range(1, limit+1) if number % divisor == 0]

## Основная программа
limit = int(input('Введите верхний предел: '))
divisor = int(input('Введите делитель: '))

print(f'Числа от 1 до {limit}, кратные {divisor}: ')
print(multiples_with_c(limit, divisor))