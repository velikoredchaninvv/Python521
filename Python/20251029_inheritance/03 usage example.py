class Shape:
    def __init__(self, color="black"):
        self.color = color

    def area(self):
        raise NotImplementedError("Area method must be implemented by subclass")
    
    def __str__(self):
        return f"Shape (color: {self.color})"
    
class Rectangle(Shape):
    def __init__(self, width, height, color="black"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle (widrh: {self.width}, height: {self.height}, color: {self.color})"
    
class Circle(Shape):
    def __init__(self, radius, color="black"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14169*self.radius * self.radius
    
    def __str__(self):
        return f"Circle (radius: {self.radius}, color: j{self.color})"
    
rect = Rectangle(10, 5, "blue")
circle = Circle(7, "red")

print(rect)
print(circle)
print(f"Rectangle area: {rect.area()}")
print(f"Circle area: {circle.area()}")