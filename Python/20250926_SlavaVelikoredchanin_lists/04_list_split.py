# Задание №4 (вторник, 23 сентября)
# Пусть есть список строк. Сделать два списка:
#  список тех же строк, написанных капсом (заглавными)
#  список тех же строк, написанных строчными (маленькими)
#  Например:
#  ['abc', 'Def', 'GHi']
#  ['ABC', 'DEF', 'GHI']
#  ['abc', 'def', 'ghi']

list_for_work = ['Kukuh', 'TRAITAK', 'grooo']
list_for_upper = []
for i in list_for_work:
    list_for_upper.append(i.upper())
print(list_for_upper)

list_for_lower = []
for i in list_for_work:
    list_for_lower.append(i.lower())
print(list_for_lower)