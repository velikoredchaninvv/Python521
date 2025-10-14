orders = ['Кофе', 'Чай', 'Пирожное', 'Сэндвич']

# преобразуем список в итератор
# order_iterator = iter(orders)

while True:
    try:
        order = next(orders)
        print(f'Обрабатывается заказ: {order}')
    except StopIteration:
        print('Все заказы обработаны')
        break

# код перестал работать, потому что список не является итератором