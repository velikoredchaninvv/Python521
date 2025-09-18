
kolichestvo = input('Сколько коров? ')  # 0 #11
kolichestvo = int(kolichestvo)
def cows_form(kolichestvo):
    #if (kolichestvo % 100 > 9) and (kolichestvo % 100 < 21):
    #    return 'коров'  # print(kolichestvo, ' коров')
    #else:
    if (kolichestvo % 100 < 10) or (kolichestvo % 100 > 20):
        if (kolichestvo % 10 == 2) or (kolichestvo % 10 == 3) or (kolichestvo % 10 == 4):
            return 'коровы'  # print(kolichestvo, ' коровы')
        if (kolichestvo % 10 == 1):
            return 'корова'  # print(kolichestvo, ' корова')
        #if (kolichestvo % 10 > 4):
        #    return 'коров' # print(kolichestvo, ' коров')
    return 'коров'

print(kolichestvo, cows_form(kolichestvo))

# Вопросы, на которые можно ответить "да" или "нет" должны 
# превращаться в логические выражения
# чтобы ответить на вопрос"равен" или "нет", надо использовать знак ==
# Ответом на логический вопрос должна быть константа 
# True (истина) или False (ложь)