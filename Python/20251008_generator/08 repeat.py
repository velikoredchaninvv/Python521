def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield file.split()