# Уровень 2: Средний
# Задача: напишите программу, которая моделирует очередь.
# 
# Пользователь может добавлять элементы в конец очереди,
# обслуживать (удалять) элементы из начала
# и просматривать текущую очередь.
# 
# Реализуйте обработку ошибок, если очередь пуста

# Предложите меню. Добавить в конец очереди, Удалить из начала, Просматривать текущую очередь, Выйти

queue = [12,123,51,543,85768,23]

while True:
    msg = input('Выберите действие delete_from_the_end_of_the_queue | delete_from_the_beginning_of_the_queue | view_of_the_queue | exit: ')

    if msg == 'delete_from_the_end_of_the_queue':
        last_element = queue.pop()
        print(f'Последний элемент из очереди {last_element} удлаён.')

    if msg == 'delete_from_the_beginning_of_the_queue':
        ferst_element = queue.pop(0) # да, не эффективно
        print(f'Удалён первый элемент {ferst_element} из стека.')

    if msg == 'view_of_the_queue':
        print(f'Содержимое стека: {queue}')

    if msg == 'exit':
        print('Программа завершена')
        break