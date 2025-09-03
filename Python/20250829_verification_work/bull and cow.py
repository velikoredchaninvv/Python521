import random

def generate_secret_number(length=4):
    # Генерируем секретное число заданной длины:
    digits = list(range(10))
    random.shuffle(digits)
    secret_number = ''.join(map(str, digits[:length]))
    return secret_number

def get_player_guess(length=4):
    "Получаем попытку игрока и проверяем её на корректность"
    while True:
        guess = input(f'Введите {length} значное число, без повторяющихся цифр: ')
        if not guess.isdigit():
            print('Пожалуйста введите только цифры')
        elif len(guess) != length:
            print(f'Введите {length} символов')
            return False
        # проверка на повторяющиеся символы, записав догадку в множество, а оно не сохраняет одинаковые элементы.
        if len(set(guess)) != len(guess):
            print('Есть повторяющиеся элементы')
        else:
            return guess

def evaluate_guess(secret_number, guess):
    'Оценивает попытку игрока и возвращает количество быков и коров'
    bulls = 0
    cows = 0
    for i in range(len(secret_number)):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

def play_bulls_and_cows():
    'Запускаем игру "Быки и коровы"'
    secret_number = generate_secret_number()
    print('Я загадал число. Попробуйте угадать!')
    attempts = 0
    while True:
        guess = get_player_guess()
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        print(f'Быки: {bulls}, Коровы: {cows}')

        if bulls == len(secret_number):
            print(f'Поздравляю! Вы угадали число {secret_number} за {attempts} попыток')
            break

# Запуск игры
play_bulls_and_cows()