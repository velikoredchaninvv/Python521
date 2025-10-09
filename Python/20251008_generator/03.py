# def count_up_to(limit):
#     count = 1
#     while count <= limit:
#         yield count
#         count += 1

# for number in count_up_to(5):
#     print(number)  # Вывод: 1 2 3 4 5

# def multiples(limit, divisor):
#     # Число в пределах лимита кратное divisor возможно = limit%divisor==0 # 1ин шаг
#     # tutu = range(limit)%divisor==0 без итератора работать не будет, yield это итератор типа
#     return tutu

# print(multiples(10,3))

divisor = 3
def multiples(limit):
    count = 1 # с какой цифры начинает бегать
    while count <= limit:
        yield count
        # misl = (divisor for divisor in range(limit))
        count += 1

temp = []
for number in multiples(10): # limit - по какую цифру бегает
    temp.append(number)
print(temp[::divisor])
