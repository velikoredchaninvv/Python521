# На выполнение заданий по питону студент предполагает потратить ч часов м минут (получить с клавиатуры).
# Во сколько самое позднее ему следует начать, чтобы оставить на дорогу 1 час
# и успеть к 19:00 на занятия?
# Ответ оформить.

def time_for_work():
    hours = input("Введите количество часов: ")
    minutes = input("Введите количество минут: ")
    # print(hours,minute)
    #преобразуем в целые числа
    hours = int(hours)
    minutes = int(minutes)

    return (hours,minutes)

def time_to_make_it(hours,minutes):
    deadline_hours = 19
    deadline_minutes = 0
    #вычисления времени сдачи
    temp_hours = deadline_hours - hours
    temp_minutes = deadline_minutes - minutes
    #работаем с минутами
    if temp_minutes < 0:
        temp_hours -= 1
        temp_minutes += 60
    print(temp_hours,temp_minutes)

#Запуск программ отсюда >>>
time_to_make_it(*time_for_work())