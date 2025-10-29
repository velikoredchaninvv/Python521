class Student:
    def __init__(self, name):
        self.__name = name
        self.__marks = []
    
    def getMarks (self):
        return self.__marks
    
st = Student('Slava')
print(st.getMarks())