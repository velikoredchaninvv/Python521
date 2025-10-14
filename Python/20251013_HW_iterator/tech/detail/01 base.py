# список
numbers = [1,2,3,4,5]
words = 'Что будет если вызвать слова? \n А дальше напишу ещё предложение \n И потом ещё одно'

# итератор
iterator = iter(numbers)


# вызов итератора через метод next
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# цикл for и и тератор
# for number in numbers:
    # print(number)

# если закончатся итерируемые объекты, а итератор продолжит работу то появится ошибка StopIteration:
# try:
#     # for number in numbers:
#     #     print(number)
#     # print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
# except StopIteration:
#     print('Недостаточно итероаторов')