# 2. Самостоятельное задание:
# 2.1 создать список [1, -3, 5, -7, 9, -11] с помощью генератора
# 2.2. Создать словарь. Ключи - буквы латинского алфавита, значения -  их коды в текущей кодировке (использовать ord (https://docs.python.org/3/library/functions.html#ord), chr (https://docs.python.org/3/library/functions.html#chr))
# 2.3 Создать множество длин слов всего текста, который представляет собой ваше задание для классной работы

# custom_list = ['hah' if x%2==0 else 'mew' for x in range(5)]
# custom_list = [x**1 for x in range(12)]
# ((-1)**x)* - Это просто множитель через один -1 *0, -1 *1, -1 *2, -1 *3, -1 *4
# ((-1)**x)* - множитель
# x - основание, на что множится
# for x - куда падает
# custom_list = [(-1**x)*x for x in range(1,12)]
# custom_list = [(-1 if x%2==0 else 1) * (x) for x in range(1,12)]

# Решение:
# custom_list = [(x*2+1)*(-1)**x for x in range(6)]
# print(custom_list)

# Решение:
# custom_dict = {chr(97+x):ord(chr(97+x)) for x in range(26)}
# print(custom_dict)

# custom_dict = {chr(97+x):(97+x) for x in range(26)}
# print(custom_dict)


# Решение:
custom_set = {x for x in range(5)}
print(custom_set)