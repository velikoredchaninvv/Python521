# Артфиметическое присваивание - не изменение, а замена строки

snachala = 'Было слово '
potom = 'получился текст'

sohramin = snachala
snachala += potom

# Каковы значения переменных? Что случилось с переменной 'snachala'?

print(snachala)
print(sohramin)

print(id(snachala))
print(id(sohramin))