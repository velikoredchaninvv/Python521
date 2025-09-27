# Задание №5 (среда, 24 сентября)
# Пусть есть строка. Создать список тех её слов, у которых чётная длина
# Например
# 'Мама читала книгу'
# ['Мама', 'читала']

list_for_work = 'тут много слов, каждое из которых несёт какой то смысл, хорошо бы печатать научиться без ошибок'
correct_stroke = list_for_work.replace(',', '')
split_stroke = correct_stroke.split(' ')
# print(split_stroke)

result_list = []
for i in split_stroke:
    if len(i)%2==0:
        result_list.append(i)
    # print(i)
print(result_list)