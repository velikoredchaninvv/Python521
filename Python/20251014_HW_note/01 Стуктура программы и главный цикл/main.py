while True:
    cmd = input('Введите команду (create|add|view|exit): ').strip().lower()
    
    if cmd == 'create':
        # создаём или очищаем заметку
        with open('notes.txt', 'w', encoding='utf-8') as f:
            f.write()
            print(f"Файл 'notes.txt' создан и очищен")
        # pass
    
    elif cmd == 'add':
        data = input('Введите текст заметки: ')
        with open('notes.txt', 'a', encoding='utf-8') as f:
            f.write(data + '\n')

    elif cmd == 'view':
        # показываем заметки
        pass
    
    elif cmd == 'exit':
        print('Программа завершена.')
        break
    
    else:
        print('Неизвестная команда. Попробуйте снова')