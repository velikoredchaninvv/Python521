# Генераторы список, список можно создать сразу сн ужными элементами
squares = [x**2 for x in range(5)]
print(squares)

# Генераторы словарей
# Создание словаря, где ключи это числа, а значения их квадраты
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)

# Генераторы множеств квадратов чисел
squares_set = {x **2 for x in range(5)}
print(squares_set)
