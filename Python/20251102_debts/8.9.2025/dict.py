# example1 check
# my_dict = {'a':1, 'b':2, 'c':3}
# if 2 in my_dict.values():
#     print('Значение 2 присутствует в словаре')

#example2 iteration
# my_dict = {'a':1, 'b':2, 'c':3}
# for value in my_dict.values():
#     print(value)

#example3 sum, max, min
# my_dict = {'a':1, 'b':2, 'c':3}
# total = sum(my_dict.values())
# print(total)

#example4
my_dict={'name':'Alice', 'age':30, 'city': 'Moscow'}
# Получаем объект view значений
values_view = my_dict.values()
# print(values_view)

# Проверяем наличие значений
# if 'Alice' in values_view:
    # print('Имя Alice присутствует')

# Итерируем по значениям
# for value in values_view:
#     print(value)