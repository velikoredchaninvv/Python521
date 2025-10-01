# Задача: написать функцию, которая из слов делает предложение
# 
# Между словами вставляются пробелы

def make_text(*words):
    result = words[0][0].upper() + words[0][1:] + ' '
    result += ' '.join(words[1:]) + '.'
    return result

my_story = make_text('мама', 'мыла', 'раму', 'с', 'мылом')
print(my_story)