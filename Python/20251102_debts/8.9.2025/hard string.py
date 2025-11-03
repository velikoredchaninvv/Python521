# Упражнения:
# [+] Напишите букву а на экране 1980 раз.
# [+] Нарисуйте "ковёр" 10*10 из букв ш, не используя цикл.
# [+] А теперь, используя цикл.
# [+] Нарисуйте "шахматный" ковёр из букв о и точек.
# [+] А теперь, чтоб размер клетки доски был не в один символ, а 3*3.
# [] А теперь, m*n.

# task1
# print('a'*5)

# task2
# print(("aaaaaaaaaa" +'\n')*10)

#task3, try3
# for i in range(1,11):
#     res='ш'*i
# print((res + '\n')*10)

#task4
# [+] Нарисуйте "шахматный" ковёр из букв о и точек.
# for i in range(1,11):
#     print('----------')
#     for d in range(1,11):
#         if d%2==0:
#             print('x', end='')
#         else:
#             print('o', end='')

# for x in range(1,11):
#     print('A')
#     if x%2==0:
#         print('B')

# i=1
# while i<10:
#     if i%10==1:
#         for x in range(1,11):
#             if x%2==0:
#                 print('x', end='')
#             else:
#                 print('o', end='')
#     else:
#         for x in range(1,11):
#             if x%2==0:
#                 print('o', end='')
#             else:
#                 print('x', end='')
#     i+=1


# i=1
# while i<11:
#     if i%2==0:
#         while a<11:
#             if a%2==0:
#                 print('a-a')
#             else:
#                 print('a-b')
#         a+=1
#     else:
#         b=1
#         while b<11:
#             if b%2==1:
#                 print('b-a')
#             else:
#                 print('b-b')
#         b+=1
#     i+=1


# for i in range(1,11):
#     if i%2==1:
#         for x in range(1,11):
#             if x%2==1:
#                 print('x', end='')
#             else:
#                 print('o', end='')
#     else:
#         for x in range(1,11):
#             if i%2==0:
#                 print('o', end='')
#             else:
#                 print('x', end='')

# el1 = 'o.'
# el2 = '.o'
# h=0
# for x in range(1,11):
#     if x%2==1:
#         while h<5:
#             el1+=el1
#             h+=1
#             print(el1)
#     else:
#         while h<5:
#             el2+=el2
#             h+=1
#             print(el2)

# el1 = 'o.'
# el2 = '.o'
# max = 10+1

# for i in range(1,max):
#     if i%2==1:
#         print(el1*5)
#     else:
#         print(el2*5)

# [+] А теперь, чтоб размер клетки доски был не в один символ, а 3*3.

# el1 = '#'
# el2 = '-'

# for x in range(1,5):
#     print((el1+el2)*3+el1)


el1 = ' .o. '
el2 = ' o.o '
stroke = 10+1
column = 5

for i in range(1,stroke):
    if i%2==1:
        print(el1*column)
    else:
        print(el2*column)