words = {'one': 'год', 'few': 'года', 'many': 'лет'}
kolichestvo = 11


def word_form(kolichestvo, words):
    '''Функция получает на вход 2 параметра
    1 параметр - количество
    2 параметр - словарь, содержащий 1, "мало" (2,3,4) и много (5+, 11-19 и т.д.)
    {'one': 'год', 'few': 'года', 'many': 'лет'}
    '''
    if (kolichestvo % 100 < 10) or (kolichestvo % 100 > 20):
        if (kolichestvo % 10 == 2) or (kolichestvo % 10 == 3) or (kolichestvo % 10 == 4):
            return words['few']  # Когда предметов 2, 3 или 4
        if (kolichestvo % 10 == 1):
            return words['one']  # Когда предмет 1
    return words['many']  # Когда предметов много и более 4


print(word_form(kolichestvo,words))