def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_file('example_text.txt'):
    print(line)