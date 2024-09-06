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

#task_119

# class Book:
#    def __init__(self, name, autor, page):
#        self.name = name
#        self.autor = autor
#        self.page = page
#
#    def pull_info(self):
#        """full book details"""
#        info = (f'Title: {self.name}\nAuthor: {self.autor}\nPages: {self.page}')
#        return info
#book = Book('1984', 'George Orwell', 328)
#print(book.pull_info())

# task_120

# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         """two additions"""
#         return self.a + self.b
#
#     def subtract(self):
#         """subtraction"""
#         return self.a - self.b
#
#     def multiply(self):
#         """Multiplication"""
#         return self.a * self.b
#
#     def divide(self,):
#        if self.b == 0:
#            print('Error: Division by zero is not allowed.')
#            return None
#        return  self.a / self.b
#
# calc = Calculator(10,5)
#
# print(f'Addition: {calc.add()}\nSubtraction: {calc.subtract()}\nMultiplication: {calc.multiply()}\nDivision: {calc.divide()}')

# Task_121
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def hello(self):
#         print(f'Hello, my host! My name is {self.name}. i am {self.age} years old')
#
# cat = Cat('Bushy', 9)
#
# cat.hello()

# Task_122

# class BankAccount:
#     def __init__(self, account, balance):
#         self.account = account
#         self.balance = balance
#     def deposit(self):
#         interest = self.balance * 0.05
#         total = self.balance + interest
#         return total
#     def withdraw(self):
#         return self.balance
#
# bankaccount = BankAccount(9876543210, 250000)
#
# print(f'Your information: \nAccount Number: {bankaccount.account}\nBalance: {bankaccount.balance}')
# print(f'Deposit account (balance with interest): {bankaccount.deposit()}')
# print(f'Withdrawal money: {bankaccount.withdraw()}')

#  Task_123
# class Car:
#     def __init__(self, mark, model, year):
#         self.mark = mark
#         self.model = model
#         self.year = year
#     def info(self):
#         """General information about car"""
#         print(f'Car make: {self.mark}\nMachine model: {self.model}\nMachine year: {self.year}')
#
# car = Car('Ram Trucks', 'Pickup', 2020 )
#
# car.info()

# Task_124

# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#     def perimetr(self):
#         """method for calculating the perimeter of a triangle"""
#         return 2 * (self.height + self.width)
#     def area(self):
#         """method for calculating the area of a triangle"""
#         return self.height * self.width
#
# rectangle = Rectangle(5, 10)
#
# print(f'Perimeter is {rectangle.perimetr()}\nArea is: {rectangle.area()} ')
