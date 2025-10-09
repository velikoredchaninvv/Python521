# Генератор создаётся проще через функцию yield или генераторное выражение

def my_generator(max_num):
    for i in range(max_num):
        yield i

# Использование (Это тоже итераторор!)
gen = my_generator(3)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Или генераторное выражение
gen_expr = (i for i in range(3))
print(next(gen_expr))
print(next(gen_expr))
print(next(gen_expr))