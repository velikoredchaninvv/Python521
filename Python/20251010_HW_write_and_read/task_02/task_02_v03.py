def write_to_file(filename='data.txt'):
    '''Запись в файл'''
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            while True:
                data = input('Введите тест, для завершения exit: ')
                if data == 'exit':
                    break
                f.write(data + '\n')
    except IOError as e:
        print('Ошбика {e}')
    
def read_from_file(filename='data.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print('Содержимое файла: ')
            for line in f:
                print(line)
    except FileNotFoundError:
        print('')
    except IOError:
        print('')

def main():
    write_to_file()
    read_from_file()

if __name__ == '__main__':
    main()