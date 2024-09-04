# task_117
#
#import math
#
# class Circle:
#
#    def __init__(self, radius): #1. self создается всегда, он пишется т.к функции всегда передается 1 аргумент, это и есть self. 2.мы можем заменить self, для этого, в аргументе через запитую прописывается тот аргумент, который должен заменить self (в нашем случае radius)
#        self.radius = radius # создаем новое свойство, через "=" прописываем значение, в нашем случае radius
#метод __init__ — это способ задать начальные настройки и значения для нового объекта, чтобы он был готов к использованию сразу после создания.
#    def area(self):
#        return math.pi * (self.radius ** 2) #формула πr²
#
#    def perimetr(self):
#        return 2 * math.pi * self.radius #формула 2πr
#
#circle = Circle(5) #Создание объекта Circle с радиусом 5
#
#print(f"Circle area: {circle.area()}\nCircle perimeter: {circle.perimetr()}")

# task_118
#
# class Student:
#    def __init__(self, name, grade):
#        self.name = name
#        self.grade = grade
#
#   def mean(self):
#        """Calculating grade point average"""
#        return sum(self.grade) / len(self.grade)
#
# student = Student('Igor', [5, 5, 5, 3, 2, 2, 4, 5, 3])
#
# print(f'Student Name: {student.name}\n Average grade: {student.mean()}')