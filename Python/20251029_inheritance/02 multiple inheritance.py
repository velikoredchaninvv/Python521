# python поддерживает множественное наследование, класс может наследовать от нескольких родительских классов.

class Father:
    def fater_method(self):
        print("Father's method")

class Mother:
    def mother_method(self):
        print("Mother's method")

class Child(Father, Mother): # Наследуемся от Father и Mother
    def child_method(self):
        print("Child's method")

child = Child()
child.father_method() # Output: Father's method
child.mother_method() # Output: Mother's method
child.child_method() # Output: Child's method

'''
При множественном наследовании, порядок указания родительских классов важен. Он определяет порядок, в котором Python будет искать методы и атрибуты, если они присутствует в более чем одном родительском классе (Method Resolution Order - MRO). MRO - можно узнать с помощью Child.__mro__
'''