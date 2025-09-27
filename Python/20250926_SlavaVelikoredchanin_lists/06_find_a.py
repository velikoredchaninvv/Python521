# # Задание №6 (четверг, 25 сентября)
# # Выписать из строки только слова, содержащие букву 'а'

string = 'Очень длинная строка с большим количеством букв, наверно гд ето будет буква а, ато что буду искать пАтом'
deleted_symbols = string.replace(',', '')
split_string = deleted_symbols.split(' ')

find_string = []
for i in split_string:
    if 'а' in i:
        find_string.append(i)
    elif 'А' in i:
        find_string.append(i)
print(find_string)