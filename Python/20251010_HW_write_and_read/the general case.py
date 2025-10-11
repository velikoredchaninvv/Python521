lines = ['Срока 1', 'Строка 2', 'Строка 3']
with open('name.txt', 'w') as f:
    f.writelines(line + '\n' for line in lines)