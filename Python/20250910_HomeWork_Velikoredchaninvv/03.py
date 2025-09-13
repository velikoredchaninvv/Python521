# https://docs.google.com/presentation/d/1h72hyzzi679AA80qJLW67oE-MjxW9gH1lLjG_X3R-TQ

# > С помощью range вывести все нечётные числа от 77 до 777 включительно
# > теперь - используя переменные
# > А теперь, получив диапазон от пользователя


a = int(input('Введите число А: '))
b = int(input('Введите число Б: '))
step = int(input('Введите шаг: '))

for i in range(a,b,step):
    print(i)