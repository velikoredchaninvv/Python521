weather = input("Какая погода? ")
t = int(input('А сколько градусов? '))
decission = ''

if weather == 'sun':
    if t < 10:
        decission = 'оденемся потеплее и '
    decission += 'пойдём гулять'
if weather == 'rain':
    decission = 'Возьмём зонтик'
    if t < 0:
        decission = 'Наденем кросовки с шипами'
print(decission)