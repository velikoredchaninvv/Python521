class Room:
    def __init__(self, width, length, height=2.54):
        self.width = width
        self.height = height
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    def __add__(self, other):
        if self.width == other.width:
            return Room(self.width, self.length + other.length)
        if self.length == other.length:
            return Room(self.width + other.width, self.length)
        if self.width == other.length:
            return Room(self.width, self.length + other.width)
        if self.length == other.width:
            return Room(self.width + other.length, self.length)
        
    def __sub__(self, other):
        '''
        Надо реализовать у комнаты метод _ _ sub _ _
        он должен получать на вход комнату и проверять, можно ли такой "кусок" отрезать по прямой, перпендикулярной одной из стен?
        '''
        if self.width >= other.width and self.length >= other.length: # базовая проверка

            if self.width >= other.width:
                if self.length >= other.length:
                    return(self.width - other.width, self.length - other.length)
            
            if self.length >= other.length:
                if self.width >= other.width:
                    return(self.width - other.width, self.length - other.length)
                
            if self.width >= other.length:
                if self.length >= other.width:
                    return(self.width - other.length, self.length - other.width)
                
            if self.length >= other.width:
                if self.width >= other.width:
                    return(self.length-other.width, self.width-other.width)

    def __str__(self):
        return 'Комната с шириной %i, глубиной %i площадью: %i' % (self.width, self.length, self.area())

class Flat:
    def __init__(self, number, stage):
        self.rooms = [
            Room(3, 2),
            Room(4, 5)
        ]
        self.number = number
        self.stage = stage

    def area(self):
        self.area_flat = 0
        for i in self.rooms:
            self.area_flat += i.area()
        return self.area_flat

    def __str__(self):
        result = 'Общее количество комнат: %i \n' % (len(self.rooms))
        # площадь каждой комнаты
        for i in range(len(self.rooms)):
            result += str(self.rooms[i]) + '\n'
        # площадь квартиры
        result += 'Общая площадь квартиры: %i' % (flat.area())
        return result

room1 = Room(5,6)
room2 = Room(4,5)
# print(room)

# print(room1 + room2)
print(room1 - room2)

flat = Flat(17, 17)
# print(flat.area())
# print(flat)