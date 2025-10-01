# def perimeter(x,y):
#     return 2*(x+y)
# print(perimeter(7,2))

# def area(x,y):
#     return x*y
# print(area(4,18))

# perimeter = lambda x,y: 2*(x+y)
# print(perimeter(17,12))

# area = lambda x,y: x*y
# print(area(5,16))

# an = (lambda x,y: x+y)(5,7)
# print(an)

# students = [
#     {'name': 'Alice', 'age': 20},
#     {'name': 'Tolian', 'age': 40},
#     {'name': 'Charlie', 'age': 18}
# ]

# print(students)

# # сортировка по возрасту
# students.sort(key=lambda students: students['age'])
# print(students)


# print(students)
# students.sort(key=lambda students: students['age'])
# print(students)

# def pizza(street, building, flat_number='до подъезда', city='Москва'):
#     return f'Город: {city}, Дом: {building}, Улица: {street}, {flat_number}'

# print(pizza(street='Махровая', building=7, flat_number=199, city='Зелепук'))
# print(pizza(street='Махровая', building=7))
# print(pizza('Махровая', 7))

# temp = []
# def find_phone(name, surname=''):
#     for full_name in phonebook:
#         if name in full_name:
#             temp.append(name)
#             print(temp)
#         # if surname in full_name:
#         #     temp.append(surname)
#         # # return phonebook[full_name]
#         # return temp
    
# print(find_phone(name='Хосе', surname='Плюшевая'))
# # print(find_phone(name='Санта Моника Плюшевая', surname='Моника'))


phonebook = {'Хосе Педро Игнасио': 898765, 'Санта Моника Плюшевая': 7655775}

# def find_phone(name, surname):
name_member = []
for i in phonebook:
    list_split = i.split()
    # name_member.append(list_split)
    print(list_split)
        # return(name_member)
    
# print(find_phone(name='Хосе', surname='Санта'))