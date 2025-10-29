# class Human:
#     def __init__(self, name, mind_type=None, age=None, life=None, qualifai=None):
#         self.name = name
#         self.mind_type = mind_type
#         self.age = age
#         self.life = life
#         self.qualifai = qualifai # компетенции

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def add_grade(self, course, grade):
#         self.course = course
#         self.grade = grade
#         self.grades = []

#         if self.name:
            

# # class Lecturer:
# #     def __init__(self, name, course):
# #         self.name = name
# #         self.course = course
        
# # ТЗ: у человека есть параметры: Возраст, тип (землнин - финансы, марсианин - управление, юпитерианец - воин, венерианец - мыслитель), есть общее время жизни и текущий возраст.
# # Студент являетя человеком, наследует параметры. Проходит науки. За них получает оценки.
# # Учитель ставит оценки студентам, но так же является носителем планеты.

# # выставлени оценки преподавателем студенту. Вопрос где реализовывать функцию выставления оценки преподавателем студенту? У студента
# # оценка типа {student_name:{course:grade}}

# # Проверка
# lecturer = Lecturer('Ivan Petrovish', 'Python')
# # Как выглядит ввод оценки преподавателем студенту?

# student = Student('Slava')
# student.add_grade('Python', 10)
# student.add_grade('Python', 9)
# student.add_grade('Python', 10)