hour = int(input("Сколько сейчас времени (в часах)? "))

if hour < 8:
    print('Как насчёт утренней пробежки?')
if hour < 11:
    print('Тебя ждёт завтра')
if hour < 16:
    print('Впереди обед')
if hour < 18:
    print('На полдник пирожные')
if hour < 21:
    print('На ужин гречка')