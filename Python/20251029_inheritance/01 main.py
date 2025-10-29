from datetime import datetime

class Human:
   
    def __init__(self, name, birthday):
        self.__name = name
        self.__birthday = birthday

    @property
    def age(self):
        return datetime.now(
            ).year - self.__birthday.year