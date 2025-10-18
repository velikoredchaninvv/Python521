class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return (self.width+self.height)*2
    
rect = Rectangle(5,3)
print("Площадь: ", rect.area())
print("Периметр: ", rect.perimeter())