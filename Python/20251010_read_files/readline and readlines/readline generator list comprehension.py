f = open('text_readline.txt', encoding='utf-8')
# content = f.readline()
# doc = [line for line in range(len)]
# f.close()
# print(content)

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

for line in read_file('text_readline.txt'):
    print(line)