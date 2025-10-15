while True:
    cmd = input('Введите команду (create|add|view|exit): ').strip().lower()
    
    if cmd == 'create':
        # создаём или очищаем заметку
        with open('notes.txt', 'w', encoding='utf-8') as f:
            pass
        print(f"Файл 'notes.txt' создан и очищен.")
    
    elif cmd == 'add':
        data = input('Введите текст заметки: ').rstrip()

        if data == "":
            print('Пустая заметка не добавлена.')
        else:
            # читаем существующие заметки (если файл есть)
            try:
                with open('notes.txt', 'r', encoding='utf-8') as f:
                    existing = [line.rstrip('\n') for line in f if line.strip() != ""]
            except FileNotFoundError:
                existing = []

            # проверяем совпадение с последней заметкой
            if existing and existing[-1].strip() == data:
                print('Такая заметка уже есть.')
            else:
                with open('notes.txt', 'a', encoding='utf-8') as f:
                    f.write(data + '\n')
                print('Заметка добавлена.')

    elif cmd == 'view':
        try:
            with open('notes.txt', 'r', encoding='utf-8') as f:
                lines = [line.rstrip("\n") for line in f]

            notes = [ln for ln in lines if ln.strip() != ""] # фильтр
            if not notes:
                print('Файл пуст.')
            else:
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
                print(f'Всего заметок: {len(notes)}')
                    
        except FileNotFoundError:
            print('Файл не найден. Сначала создайте файл.')
        except Exception as e:
            print("Ошибка при чтении файла: ", e)
    
    elif cmd == 'exit':
        print('Программа завершена.')
        break
    
    else:
        print('Неизвестная команда. Попробуйте снова.')