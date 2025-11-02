class ParentClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute1
    
    def method(self):
        print("Method 1 from ParentClass")

class ChildClass(ParentClass): # Наследуется от ParentClass
    def __init__(self, attribute1, attribute2, attribute3):
        # Вызываем конструктор родительсого класса для инициализации общих атрибутов
        super().__init__(attribute1, attribute2)
        self.attribute3 = attribute3

    def method2(self):
        print("Method 2 from ChildClass")

    # Переопределине метода родительского класса
    def method(self):
        print("Method 1 from ChildClass (overriden)")


# 03 isinstance() and ossubclass()
# isinstance(object, classinfo): Проверяет, является ли объект экземляром указанного класса или его подкласса.
# issubclass(class, classinfo): Проверят, является ли класс подклассом другого класса

parent = ParentClass("val1", "val2")
child = ChildClass("val1", "val2", "val3")

print(isinstance(child, ChildClass)) # Output: True
print(isinstance(child, ParentClass)) # Output: True (ChildClass является under классом ParentClass)
print(isinstance(parent, ChildClass)) # Ouput: False

print(issubclass(ChildClass, ParentClass)) # Output: True
print(issubclass(ParentClass, ChildClass)) # Output: False

# Преимущества наследования
'''
- Повторное использование кода. Наследование позволяет избежать дублирования кода, повторно используя код родительского класса.
- Расширяемость. Легко добавлять новую функцию добавляя подклассы.
- Организация кода. Наследование позволяет стуктурировать код и создавать иерархии классов, что делает код более понятным и поддерживаемым.
- Полиморфизм. Наследование - одна из основ полиморфизма. Объекты разных классов, имеющих общего родителя, могут быть обработаны единообразно.
'''