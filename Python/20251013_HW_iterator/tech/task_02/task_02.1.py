# создание метода
def generator(orders):
    number = 1
    for i in orders:
        yield f'{number}) Обрабатывается: {i}'
        number += 1

# очередь
orders = ['Кофе', 'Чай', 'Пирожное', 'Сэндвич']

# вызов функции
generator = generator(orders)

# запуск
print(next(generator))
print(next(generator))
for i in generator:
    print(i)