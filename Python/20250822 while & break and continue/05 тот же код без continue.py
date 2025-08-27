# [+] Перепишите программу, избежав "continue"
# [+] Посчитайте количество верных и неверных ответов, процент ошибок
# ГОРШОЧЕК, НЕ ВАРИ! Поставьте ограничения:
# [+] По количеству заданий
# [/] По максимуму ошибок
# [] По минимальному проценту ошибок


# получаем случайное число для a и b
from random import randint
a = randint(1,10)
b = randint(1,10)
run = 0
correct = 0
incorrect = 0
error = 2
limit = 4

while run <= limit or error == 0: 
    # вычисление внутри тела условия не влияет на состояние run в данный момент
    result = a+b
    answer = int(input('Сколько будет %(a)i + %(b)i = ' % {"a":a,"b":b}))
    if answer == result:
        print(f'Это правильный ответ {answer}')
        correct += 1 # накопление верных
        run += 1
        print(f'Количество правильных ответов {correct}')
        round = input('Желаете продолжить? Да / Нет ')
        if round == 'Да':
            a = randint(1,10)
            b = randint(1,10)
        else:
            print(f'Количество ответов правильных {correct}, неправильных {incorrect}')
            print(f'Правильных ответов {int(correct/(correct+incorrect)*100)}%')
            exit()
    else:
        print('Попробуй ещё разff')
        incorrect += 1 # накопление неверных
        print(f'Количество неправильных ответов {incorrect}')
        run += 1
        error -= 1
else:
    print(f'Количество ответов правильных {correct}, неправильных {incorrect}')
    print(f'Правильных ответов {int(correct/(correct+incorrect)*100)}%')