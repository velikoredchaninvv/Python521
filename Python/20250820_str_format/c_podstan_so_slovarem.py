# C подстановка со словарём

v_bazu = "'2025-08-20', 'apple', 20"
# Типизированная подстановка
podstanovka = "'%(data)s','%(fruct)s', %(number)i"
# %s - строка, она же универсльная подстановка
# %f - вещественное число
# %i - целое число
# print(podstanovka)
print(podstanovka % {
                    'data' : '2025-08-20',
                    'fruct' : 'apple',
                    'number' : 20
                    })