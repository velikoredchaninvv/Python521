# Уровень 1: Базовый
# Задача: напишите программу, которая моделирует работу стека.
# Пользователь должен уметь добавлять числа в стек,
# удалять верхний элемент
# и просматривать содержимое стека.
# Программа завершает работу по команде exit.


# num = 19

# добавление в конец
# stack.append(num)
# print(stack)

# удаление с конца
# last_element = stack.pop()
# print(stack)
# print(last_element)

# Меню с предложение добавить число в стек
# Меню с предложением удалить последнее число из стека
# Меню что бы показать содержимое стека
# Меню для выхода из программы


stack = [15,123,75,12]

while True:

    message = input('Введите команду add_to_stack | delete_from_stack | view_stack | exit: ').strip().lower()

    if message == 'add_to_stack':
        mes_add = int(input('Введите число, которое хотите добавить в стек: '))
        stack.append(mes_add)

    elif message == 'delete_from_stack':
        last_element = stack.pop()
        print(f'Верхий элемент {last_element} из стека удалён')

    elif message == 'view_stack':
        print(f'Содержимое стека: {stack}')

    elif message == 'exit':
        print('Программа завершена.')
        break