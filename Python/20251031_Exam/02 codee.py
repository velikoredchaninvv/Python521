from datetime import datetime, timedelta

class Product:
    def __init__(self, name, price, expiration_date, def_exp_time=1095):
        self.__name = name
        self.expiration_date = expiration_date
        self.now = datetime.now()
        self.def_exp_time = def_exp_time
        self._day_for_expiration = None
        self._price = price
    @property
    def overdue(self):
        if self.now > self.expiration_date:
            return(f'Продукт не свежий')
        else:
            self._day_for_expiration = (self.expiration_date - self.now).days
            return(f'Продукт свежий, до истечения срока годности: {self._day_for_expiration}')
    @property
    def time_for_expiration(self):
        if self._day_for_expiration is not None:
            return(f'Количество дней до завершения срока годности: {self._day_for_expiration}')
        else:
            return(f'Товар просрочен')
        
    @property
    def name(self):
        return self.__name
    def price(self):
        return f'Цена: {self._price}'

class Meat(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price, expiration_date, def_exp_time=1)

class Milk(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price, expiration_date, def_exp_time=3)

class Different(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price, expiration_date, def_exp_time=7)



# Создаём объект, что бы код работал нужно вызывать последоватльно overdue, а потом tile_for_expiration
product = Product('Redis', 100, datetime(2025,12,30))
print(product.overdue)
print(product.time_for_expiration)
print(product.prod_name())
print(product.price())

meat = Meat('Meat', 200, datetime(2026,12,30))
print(meat.overdue)
print(meat.time_for_expiration)
print(meat.prod_name())
print(meat.price())

milk = Milk('Milk', 300, datetime(2025,9,30))
print(milk.overdue)
print(milk.time_for_expiration)
print(milk.prod_name())
print(milk.price())