a = 'kuku'
b = """kuku"""
id(a)
2421181381360
id(b)
2421181381360
id(a) == id(b)

print(type(a))
print(type(b))
print(id(a))
print(id(b))

if id(a) == id(b):
    print('Ага, один ID')