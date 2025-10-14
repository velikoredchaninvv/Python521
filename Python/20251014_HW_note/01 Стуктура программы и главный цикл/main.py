while True:
    cmd = input('Введите команду (create|add|view|exit): ').strip().lower()
    
    if cmd == 'create':
        # создаём или очищаем заметку
        with open('notes.txt', 'w', encoding='utf-8') as f:
            f.write()
            print(f"Файл 'notes.txt' создан и очищен")
    
    elif cmd == 'add':
        data = input('Введите текст заметки: ')
        with open('notes.txt', 'a', encoding='utf-8') as f:
            f.write(data + '\n')
            print('Заметка добавлена.')

    elif cmd == 'view':
        try:
            with open('notes.txt', 'r', encoding='utf-8') as f:
                lines = [line.rstrip("\n") for line in f]
            if not lines:
                print('Файл пуст.')
            else:
                for i, line in enumerate(lines, 1):
                    print(f"{i}.{line}")
        except FileNotFoundError:
            print('Файл не найден. Сначала создайте файл.')
        except Exception as e:
            print("Ошибка при чтении файла: ", e)
    
    elif cmd == 'exit':
        print('Программа завершена.')
        break
    
    else:
        print('Неизвестная команда. Попробуйте снова')