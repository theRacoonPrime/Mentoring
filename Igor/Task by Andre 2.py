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

# Task_125

# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
#
#     def upsurge(self):
#
#         percent = self.salary * 0.15
#         result = self.salary + percent
#         return result
#
# employee = Employee('igor', 'IT specialist', 50000)
#
# print(f'Congratulations {employee.name}!\nYou are doing very good work as a {employee.position}.\nYour new salary: {employee.upsurge()}')

# Task_126

# class Book:
#     def __init__(self, name, autor, pages):
#         self.name = name
#         self.autor = autor
#         self.pages = pages
#
#     def pull_info(self):
#         '''Returns complete information about the book'''
#         info = f'Title: {self.name}\nAuthor: {self.autor}\nPages: {self.pages}'
#         return info
#
# class LibraryBook(Book):
#     def __init__(self, name, autor, pages, availability=True):
#         super().__init__(name, autor, pages)
#         self.availability = availability
#
#     def change_availability(self, status):
#         '''Changes the availability status of the book'''
#         self.availability = status
#
#     def availability_status(self,):
#         '''Returns the current availability status of the book'''
#         if self.availability:
#             return 'Available in the library'
#         else:
#             return 'Checked out'
#
# library_book = LibraryBook('1984', 'George Orwell', 328)
#
# print(f'{library_book.pull_info()}\nStatus: {library_book.availability_status()}')
#
# library_book.change_availability(False)
# print(f'status: {library_book.availability_status()}')

# Task_127

# class Person:
#     def __init__(self, name, age):
#         self.name, self.age = name, age
#
# class Student(Person):
#     def __init__(self,name, age, student_id):
#         super().__init__(name, age)
#         self.student_id, self.courses = student_id, []
#
#     def enroll(self,course):
#         '''Method for enrolling a student in a course'''
#         self.courses.append(course)
#         course.add_student(self)
#
# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#
# class Course:
#     def __init__(self, course_name):
#         self.course_name, self.teacher, self.students = course_name, None, []
#
#     def set_teacher(self, teacher):
#         '''Assigning an instructor to a course'''
#         self.teacher = teacher
#
#     def add_student(self, student):
#         '''Adding a student to a course'''
#         self.students.append(student)
#
#     def get_info(self):
#         '''Method for obtaining course information'''
#         student_names = [student.name for student in self.students]
#         teacher_name = self.teacher.name if self.teacher else 'No teacher assigned'
#         return (f'Course: {self.course_name}\nTeacher: {teacher_name}\nStudents enrolled: {", ".join(student_names) if student_names else 'No students enrolled'}')
#
# student1 = Student('Andrey', 25, 's1001')
# student2 = Student ('Edward', 23, 's1002')
#
# teacher = Teacher('Dr. Smith', 45, 'Mathematics')
#
# course = Course('Algebra')
#
# course.set_teacher(teacher)
#
# student1.enroll(course)
# student2.enroll(course)
#
# print(course.get_info())

#Task_128
# class BankAccount:
#     def __init__(self,account, balance=0, withdrawals_limit=1000):
#         self.account, self.balance,self.withdrawals_limit = account, balance, withdrawals_limit
#
#     def deposit(self, amount):
#         '''Method for depositing funds into the account'''
#         if amount > 0:
#             self.balance + amount
#             print(f'Successfully deposite {amount}. Current balance: {self.balance} ')
#         else:
#             print('Deposit amount must be positive')
#
#     def withdraw(self,amount):
#         '''Method for withdrawal of funds subject to limit'''
#         if amount > self.withdrawals_limit:
#             print(f'Error: Exceeds withdrawal limit of {self.withdrawals_limit}')
#         elif amount > self.balance:
#             print(f'Error: Insufficient balance. Current balance: {self.balance}')
#         elif amount > 0:
#             self.balance -= amount
#             print(f'Successfully withdrew: {amount}. Remaining balance: {self.balance}')
#         else:
#             print('Withdrawal amount must be positive.')
#
#     def get_balance(self):
#         return self.balance
#
# class SavingsAccount(BankAccount):
#     def __init__(self,account, balance, balance_limit=100):
#         super().__init__(account, balance)
#         self.balance_limit = balance_limit
#
#     def apply_interest(self):
#         '''Method for calculating percentage'''
#         if self.balance < self.balance_limit:
#             print(f'Error: your balance {self.balance}. under the limit: {self.balance_limit}')
#         else:
#             interest = self.balance * 0.15
#             self.balance += interest
#             print(f'Your {self.balance} has increased by 15 per cent')
#
# saving = SavingsAccount(12345678, 500, 100)
#
# saving.deposit(150)
#
# saving.apply_interest()
#
# low_balance_account = SavingsAccount(12345678, 50, 100)
# low_balance_account.apply_interest()

# Task_129
#
# class Room: #представляет комнату в отеле, с атрибутами
#     def __init__(self, room_type, price_per_night):
#         self.room_type = room_type #тип комнаты
#         self.price_per_night = price_per_night #цена за ночь
#         self.is_available = True #Логическое значение, доступна комната или нет. По умолчанию True.
#
#     def set_is_available(self, status): #метод для изменения доступности комнаты.
#         '''Establish the accessibility of the room'''
#         self.is_available = status #принимает параметр status, который устанавливает значение 'True'
#
#
# class Booking: #отвечает за управление бронированиями
#     def __init__(self, room, num_of_nights):
#         if room.is_available: #Проверяется, доступна ли комната для бронирования через условие
#             self.room = room #room: ссылка на объект комнаты,
#             self.num_of_nights = num_of_nights #num_of_nights: количество ночей
#             self.total_price = self.calculate_total_price() #total_price: общая стоимость бронирования (рассчитывается с помощью метода calculate_total_price
#             self.is_active = True #is_active: указывает, активно ли бронирование (если бронирование активно, то его нельзя отменить).
#             room.set_is_available(False) #Если комната доступна, она бронируется на заданное количество ночей, и её доступность меняется на False через вызов метода room.set_is_available(False).
#         else:
#             raise ValueError('Room is not available for booking')
#
#     def calculate_total_price(self):
#         '''Method for calculating the total cost of accommodation'''
#         return self.room.price_per_night * self.num_of_nights
#
#     def cancel(self):
#         self.is_active = False #Устанавливает статус бронирования как неактивное
#         self.room.set_is_available(True) #Освобождает комнату, делая её доступной для других бронирований через вызов метода
#
#     def get_details(self): #этот метод возвращает строку с подробностями о бронировании
#         '''Method for obtaining booking details'''
#         return (f'Room type: {self.room.room_type}\nPrice per night: {self.room.price_per_night}\nNights: {self.num_of_nights}\nTotal cost: {self.total_price}')
#
#
# class Hotel: # управляет всеми комнатами и бронированиями в отеле.
#     def __init__(self, name):
#         self.name = name #название отеля.
#         self.rooms = [] #список всех комнат в отеле (список объектов Room)
#         self.bookings = [] # список всех активных бронирований (список объектов Booking).
#
#     def add_room(self, room):
#         self.rooms.append(room) #добавляет объект комнаты в список rooms
#
#     def find_available_room(self, room_type):
#         for room in self.rooms: #проходит по списку всех комнат
#             if room.room_type == room_type and room.is_available: #проверяет, доступна ли комната и соответствует ли её тип заданному
#                 return room
#         return None
#
#     def make_booking(self, room_type, num_of_nights): #метод для создания бронирования
#         room = self.find_available_room(room_type) #Cначала ищет доступную комнату нужного типа через вызов
#         if room:
#             booking = Booking(room, num_of_nights) #Eсли комната найдена, создаёт объект Booking
#             self.bookings.append(booking)#добавляет его в список бронирований self.bookings
#             print(f'Booking successful! Room type: {room_type}, Nights: {num_of_nights}, Total price: {booking.total_price}')
#             return booking
#         else:
#             print(f"No available rooms of type {room_type}") #Если комната не найдена, выводится сообщение о том, что комнаты такого типа нет
#             return None
#
#     def cancel_booking(self, booking):
#         if booking in self.bookings and booking.is_active: #находится ли бронирование в списке активных бронирований и не отменено ли оно уже
#             booking.cancel()#бронирование отменяется
#             self.bookings.remove(booking) #оно удаляется из списка.
#             print('Booking cancelled successfully.')
#         else:
#             print('Booking not found or already cancelled.')
#
#     def show_available_rooms(self):# метод, который выводит все доступные комнаты
#         available_rooms = [room for room in self.rooms if room.is_available]
#         if available_rooms:
#             for room in available_rooms: #те, у которых is_available == True)
#                 print(f"Room type: {room.room_type}, Price per night: {room.price_per_night}")
#         else:
#             print('No available rooms') #сли таких комнат нет, выводится сообщение, что доступных комнат нет.
#
# hotel = Hotel('Grand Hotel')
#
# room1 = Room('Single', 100)
# room2 = Room('Double', 150)
# room3 = Room('Suite', 300)
#
# hotel.add_room(room1)
# hotel.add_room(room2)
# hotel.add_room(room3)
#
# hotel.show_available_rooms()
#
# booking1 = hotel.make_booking('Double', 3)
#
# booking2 = hotel.make_booking('Double', 2)
#
# hotel.cancel_booking(booking1)
#
# hotel.show_available_rooms()






