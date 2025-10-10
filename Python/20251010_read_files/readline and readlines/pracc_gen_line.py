f = open('text_readline.txt', encoding='utf-8')

# вывод всех строк
all_str = []
for line in f:
    all_str = all_str.append(line.strip())

print(all_str)
# stroke_length = 0
# for line in f:
#     if stroke_length < len(line):
#         stroke_length = len(line)
# print(stroke_length)
# print(line)

f.close()