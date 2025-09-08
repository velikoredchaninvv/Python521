# Нарисовать только границу поля и пустую серединку.
s01 = '00000000'
s02 = '0      0'
matrix = 'oxxxxxo'

for i in matrix:
    if i == 'o':
        print(s01)
    else:
        print(s02)