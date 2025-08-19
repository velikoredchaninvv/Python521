# игрок 1 - компьютер, игрок 2 - человек

def hangman(word): # функция в которой хранится игра и принимает один параметр это слово, которое должен отгадать 2ой игрок.
    wrong = 0 # количество ошибок которые допустил 2ой игрок
    stages = [" ", 
                "_________        ",
                "|                ",
                "|        |       ",
                "|        0       ",
                "|       /|\      ",
                "|       / \      ",
                "|                "
                ]
    rletters = list(word) # список, который содержит каждый символ вводимый в word, отслеживает какие символы осталось отгадать
    board = ["_"] * len(word) # board список строк, отслеживает подсказки, которые отображаются для 2го игрока
    win = False # win отслеживает победил ли уже 2ой игрок, по умолчанию False
    print("Добро пожаловать на казнь")

# цикл, обеспечивающий работу игры

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))
    
hangman("кот")