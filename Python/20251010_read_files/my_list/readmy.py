f = open('mylist.txt', encoding='utf=8')
content = f.read() # прочесть весь файл
f.close()
print(content)