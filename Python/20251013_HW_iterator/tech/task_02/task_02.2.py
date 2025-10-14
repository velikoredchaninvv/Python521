# создание метода
def generator(orders):
    for i, order in enumerate(orders, start=1):
        yield f'{i}) Обрабатывается: {order}'

# очередь
orders = ['Кофе', 'Чай', 'Пирожное', 'Сэндвич']

# вызов функции
generator = generator(orders)

# запуск
print(next(generator))
print(next(generator))
for i in generator:
    print(i)