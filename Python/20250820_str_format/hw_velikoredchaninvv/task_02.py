def solution(street, house, number):
    answer = 'Дом находится на улице %(street)s, номер дома %(house)i, номер квартиры %(number)i'
    print(answer % {"street":street, "house":house, "number":number})

solution("Главмосстроя", 5900, 123123)
solution("Пупкинкактусовского", 911, 100)
solution("Мерногошага", 815, 168)
