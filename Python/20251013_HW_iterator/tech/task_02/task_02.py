orders = ['Кофе', 'Чай', 'Пирожное', 'Сэндвич']

order_iter = iter(orders)

print(f'Обрабатывается заказ: {next(order_iter)}')
print(f'Обрабатывается заказ: {next(order_iter)}')

for i in order_iter:
    print(f'Обрабатывается заказ: {i}')