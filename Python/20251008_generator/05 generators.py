# конструкция генератора позволяет комбинировать создание коллекции и условия:
even_numbers = [x for x in range(10) if x%2 == 0]
print(even_numbers)

# словарь только для чётных чисел:
odd_squares_dict = {x: x**2 for x in range(10) if x%2 != 0}
print(odd_squares_dict)
