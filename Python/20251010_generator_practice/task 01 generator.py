# Решение через Generator
# Программа:
def multiplies(limit, divisor):
    for number in range(1, limit+1):
        if number % divisor == 0:
            yield number

# Ввод данных
limit = int(input('Введите лимит: '))
divisor = int(input('Введите кратность: '))

# Вывод результата
print(f'Числа от 1 до {limit}, кратные {divisor}:')
for multiple in multiplies(limit,divisor):
    print(multiple)