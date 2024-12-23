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

# Task_130

# class Dish:
#     '''representing the dish and the price'''
#     def __init__(self, name, price):
#         self.name, self.price = name, price
#
# class Order:
#     ''' ability to add dishes and calculate the total cost.'''
#     def __init__(self):
#         self.dishes = [] #  Список для хранения объектов Dish
#
#
#     def add_dish(self, dish):
#         """Adds a dish"""
#         self.dishes.append(dish)
#
#     def calculate_total_price(self):
#         """Calculates the total cost of the order"""
#         total_price = sum(dish.price for dish in self.dishes) #dish.price - хранит цену конкретного блюдаю. self.dishes -  содержит все добавленные блюда (объекты класса Dish). Цикл проходит по каждому объекту Dish в списке self.dishes. На каждой итерации dish представляет собой объект блюда из заказа.
#         return total_price
#
#     def info(self):
#         """'''Displays information about the order'''"""
#         if self.dishes: # есть ли блюда в списке.
#             print('Your order')
#             for dish in self.dishes:
#                 print(f'- {dish.name}: {dish.price}')
#             print(f'Total cost: {self.calculate_total_price()}')
#         else:
#             print('No dishes in the order')
#
#     def pay(self):
#         """Simulates the payment process"""
#         total_price = self.calculate_total_price()
#         print(f'Order has been paid. Total: {total_price}')
#         self.dishes = []
#
# class Restaurant:
#     def __init__(self):
#         self.orders = [] # список заказов
#
#     def add_order(self, order):
#         """Adds an order to the restaurant"""
#         self.orders.append(order)
#
#     def show_orders(self):
#         """Displays all orders"""
#         if self.orders:
#             for i, order in enumerate(self.orders, 1):
#                 print(f'\nOrder {i}')
#                 order.info() # # Вызываем метод info() для каждого заказа
#         else:
#             print('No orders have been made.')
#
# dish1 = Dish('Big Mak', 100)
# dish2 = Dish('Pizza', 250)
# dish3 = Dish ('salat', 75)
#
# order1 = Order()
# order1.add_dish(dish1)
# order1.add_dish(dish2)
#
# order2 = Order()
# order2.add_dish(dish3)
#
# restaurant = Restaurant()
# restaurant.add_order(order1)
# restaurant.add_order(order2)
#
# restaurant.show_orders()
#
# order1.pay()
#
# restaurant.show_orders()

# Task_131

# class Vehicle:
#     """base class for all vehicles."""
#     def __init__(self, max_speed,num_seats):
#         self.max_speed, self.num_seats = max_speed, num_seats
#
#     def vehicle_info(self):
#         """'Outputs vehicle information"""
#         print(f'Max speed: {self.max_speed} km/h\nSeats: {self.num_seats}')
#
# class Car(Vehicle):
#     def __init__(self, max_speed, num_seats,engine_on=False):
#         super().__init__(max_speed,num_seats)
#         self.engine_on = engine_on
#
#     def on_off(self):
#         if self.engine_on:
#             print('engine running')
#         else:
#             print('engine shut down')
#
# class Bicycle(Vehicle):
#     def __init__(self,max_speed, num_seats, transmissions=0):
#         super().__init__(max_speed, num_seats)
#         self.transmissions = transmissions
#
#     def switching(self, new_gear):
#         if 0 < new_gear <= 8:
#             self.transmissions = new_gear
#             print(f'Gear switched to {self.transmissions}')
#         else:
#             print('Incorrect transmission')
#
# class Airplane(Vehicle):
#     def __init__(self,max_speed, num_seats, flap_type=0):
#         super().__init__(max_speed, num_seats)
#         self.flap_type = flap_type
#
#     def flap_operation(self):
#         if self.flap_type == 1:
#             print('altitude gain')
#         elif self.flap_type == 2:
#             print('take-off')
#         elif self.flap_type == 3:
#             print('approach')
#         elif self.flap_type == 4:
#             print('braking')
#         else:
#             print('mistake! We are going down!')
#
# car = Car(200, 3, False)
# car.vehicle_info()
# car.on_off()
# car.engine_on = True
# car.on_off()
# print('\n')
#
# bike = Bicycle(30, 1,0)
# print('Bisycle information')
# bike.switching(3)
# bike.switching(9)
# print('\n')
#
# plan = Airplane(900, 150,2)
# plan.vehicle_info()
# plan.flap_operation()
# plan.flap_type = 4
# plan.flap_operation()

#task_132

# import random

# def get_user_choice():
#    user_choice = input('Choose: Rock, Scissors, Paper.').lower()
#    if user_choice not in ['rock', 'scissors', 'paper']:
#        print('wrong choice')
#        return get_user_choice()
#    return user_choice

# def get_computer_choice():
#    choices = ['rock', 'scissors', 'paper']
#    return random.choice(choices)

# def winner(user_choice, computer_choice):
#    if user_choice == computer_choice:
#        return 'Tie!'

#    if (user_choice == 'rock' and computer_choice == 'scissors') or \
#            (user_choice == 'scissors' and computer_choice == 'paper' ) or \
#            (user_choice == 'paper' and computer_choice == 'rock'):
#        return "You win"
#    else:
#        return 'You lost'

# def play_game():
#    user_choice = get_user_choice()
#    computer_choice = get_computer_choice()

#    print(f'Your choice: {user_choice.capitalize()}')
#    print(f'computer choice: {computer_choice.capitalize()}')

#    result = winner(user_choice, computer_choice)
#    print(result)

# play_game()

# Task_133

# import random
#
# def computer_choice():
#     return random.randint(1, 10)
#
# def get_user_choice():
#     while True:
#         try:
#             choice = int(input('enter a number between 1 and 10: '))
#             if 1 <= choice <= 10:
#                 return choice
#             else:
#                 print('enter a number between 1 and 10: ')
#         except ValueError:
#             print('You need to enter a number!')
#
# def play_round(user, computer):
#     computer_num = computer_choice()
#     user_num = get_user_choice()
#
#     print(f'the computer chose a number: {computer_num}')
#
#     if user_num == computer_num:
#         print('That is right, +10 points')
#         user += 10
#         computer -= 5
#     else:
#         print('Wrong, -10 points')
#         user -= 10
#         computer += 5
#
#     return user, computer
#
# def check_winner(user, computer):
#     if user >= 150:
#         print('Congratulations, you won!')
#         return  True
#     elif computer >= 150:
#         print('The computer won. Try again!')
#         return  True
#     return False
#
# def game():
#     user_points = 100
#     computer_points = 100
#
#     print('Welcome to the Numerical Battle game. Your task is to guess the number that the computer has guessed.')
#
#     while True:
#         user_points, computer_points = play_round(user_points, computer_points)
#
#         print(f'Your points: {user_points} | Computer points: {computer_points}')
#
#         if check_winner(user_points, computer_points):
#             break
#
#         if input('Would you like to continue? (yes/no): ').lower() != 'yes':
#             break
#
#
# game()

# Task_133(2)
# import random
#
# computer_points, user_points = 100, 100
# while computer_points > 0 and user_points > 0 and computer_points < 150 and user_points < 150:
#     computer_num = random.randint(1,10)
#     try:
#         user_num = int(input('enter a number between 1 and 10: '))
#         if user_num < 1 or user_num > 10:
#             print('Please enter a valid number between 1 and 10.')
#             continue
#     except ValueError:
#         print('Invalid input. Please enter a number.')
#         continue
#     if user_num == computer_num:
#         user_points += 10
#         computer_points -= 5
#         print(f'You won +10 points\nYour points: ({user_points})\nComputer points: ({computer_points})')
#
#     else:
#         user_points -= 10
#         computer_points += 5
#         print(f'Computer won: -10 points\nYour points: ({user_points})\nComputer points: ({computer_points})')
#
# if computer_points <= 0:
#     print('Computer lost')
# elif user_points <= 0:
#     print('You lost')
# elif computer_points >= 150:
#     print('Computer win')
# elif user_points >= 150:
#     print("you won")

# Start work with SQL(task2)
# import sqlite3

# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'
# connection = sqlite3.connect(dp_path)
# cursor = connection.cursor()

# cursor.execute('SELECT * FROM Customers')

# customers = cursor.fetchall()

# for customers in customers:
#    print(customers)

# connection.close()

# Task_3

# import sqlite3 # Подключаем библиотеку
#
# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db' # Создаем переменную, которая содержит путь к файлу, где хранится база данных
# connection = sqlite3.connect(dp_path) # подключение базы данных по указанному пути
# cursor = connection.cursor() # создает обьект cursor, этот обьект позволяет выполнить SQL-запросы к базе данных
#
# cursor.execute('SELECT CompanyName, ContactName FROM Customers') #Выполнение запроса, выбор определнных стобцов из таблицы
#
# customers = cursor.fetchall() # получает все строки, которые были выбраны в результате запроса
#
# for customers in customers: # Проходим покаждой записи customers
#     print(customers)
#
# connection.close()

#Task_4

# import sqlite3

# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'
#connection = sqlite3.connect(dp_path)
#cursor = connection.cursor()

# cursor.execute("SELECT * FROM Customers WHERE Country = 'Germany'")

# customers = cursor.fetchall()

# for customers in customers:
#    print(customers)

#connection.close()

# Task_5

# import sqlite3
#
# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'
# connection = sqlite3.connect(dp_path)
# cursor = connection.cursor()
#
# cursor.execute('SELECT * FROM Customers ORDER BY CompanyName ASC')
#
# customers = cursor.fetchall()
#
# for customers in customers:
#     print(customers)
#
# connection.close()

# Task_6

# import sqlite3
#
# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'
#
# connection = sqlite3.connect(dp_path)
# cursor = connection.cursor()
#
# cursor.execute('SELECT COUNT(*) FROM Customers')
#
# customers = cursor.fetchall()
#
# for customers in customers:
#     print(customers)
#
# connection.close()

# Task_7

# import sqlite3

# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'

# connection = sqlite3.connect(dp_path)
# cursor = connection.cursor()

# cursor.execute('SELECT Country FROM Customers GROUP BY Country')
# unique_countries = cursor.fetchall()

# print("Unique countries: ")
# for country in unique_countries:
#    print(country[0])

# cursor.execute('SELECT Country, COUNT(*) AS CustomerCount FROM Customers GROUP BY Country')
# country_counts = cursor.fetchall()

# for country, count in country_counts:
#    print(f'{country}: {count}')

# connection.close()

# Task_8

# import sqlite3
#
# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'
#
# connection = sqlite3.connect(dp_path)
# cursor = connection.cursor()
#
# cursor.execute('SELECT MIN(UnitPrice), MAX(UnitPrice), AVG(UnitPrice) FROM Products')
# products = cursor.fetchall()
#
# for products in products:
#     print(products)
#
# connection.close()

# Task_9

# import sqlite3
#
# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'
#
# connection = sqlite3.connect(dp_path)
# cursor = connection.cursor()
#
# cursor.execute('SELECT * FROM Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID')
# result = cursor.fetchall()
#
# for i in result:
#     print(i)
#
# connection.close()

# Task_10

# import sqlite3
#
# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'
# connection = sqlite3.connect(dp_path)
# cursor = connection.cursor()
#
# cursor.execute("INSERT INTO Products (ProductName) VALUES ('Vodka')")
# connection.commit()
#
# connection.close()

# Task_11

# import sqlite3
#
# dp_path = r'C:\Users\Игорь\PycharmProjects\KNB\Igor\db\northwind.db'
# connection = sqlite3.connect(dp_path)
# cursor = connection.cursor()
#
# cursor.execute('UPDATE Products SET UnitPrice = UnitPrice * 1.10 WHERE CategoryID = 1')
#
# connection.commit()
#
# connection.close()

#STOP WORK WITH SQL, WILL START USUALLY TASK

#Task_117

# num = [int(input()) for _ in range(5)]
# for i in range(len(num) - 1):
#     for j in range(len(num) - 1 - i):
#         if num[j] > num[j + 1]:
#             num[j], num[j + 1] = num[j +1], num[j]
#             print(num)

# task_118
# total_sum = 0
# total_product = 1
# found_prime = False
# num_1, num_2 = int(input()), int(input())
# for i in range(num_1, num_2 + 1):
#     if i > 1:
#         is_prime = True
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             found_prime = True
#             total_sum += i
#             total_product *= i
# if found_prime:
#     print(f'{total_sum}\n{total_product}')

# task_119

# word = input()
# char_count = {} #Создается пустой словарь, который будет заполняться по мерере обработки строки

# for char in word:
#    if char in char_count:
#        char_count[char] += 1
#    else:
#        char_count[char] = 1

#histogram = '\n'.join([f'{char}: {"*" * count}' for char, count in char_count.items()]) #
#print(histogram)

# Task_120
# import string
# text = input("Please, enter the text: ")
# char_count = {}
# table = str.maketrans("","",string.punctuation)
# new_next_low = text.translate(table).lower().split()
# for char in new_next_low:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# sorted_words = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
# for word, count in sorted_words[:5]:
#     print(f'{word}: {count}')

# Task_121

# num_1,num_2 = list(map(int, input())), list(map(int, input()))
# my_set_1, my_set_2 = set(num_1), set(num_2)
# minus = my_set_1 - my_set_2
# plus = my_set_1 | my_set_2 # | (побитовое ИЛИ)/ Объединение — это множество, содержащее все уникальные элементы, которые присутствуют хотя бы в одном из двух множеств.
# intersection = set(num_1) & set(num_2) # & (побитовое И)/ Пересечение — это множество, содержащее только те элементы, которые присутствуют в обоих множествах.
# result = (intersection, plus, minus) #Кортеж
# print(result)

# Task_122

# num_students = int(input('Enter the number of students: '))
# students = {}
#
# for i in range(num_students):
#     print(f"\nStudents: {i + 1}:")
#     name = input("Enter the name of student: ")
#     age = int(input('Enter the age of student: '))
#     grades = list(map(int, input("Enter the student's grades through the space: ")))
#
#     students[name] = {'Age': age, 'Grades': grades}
#
# searh_name = input('Enter the name of student to search:')
#
# if searh_name in students:
#     print(f'Name: {searh_name}\nAge: {students[searh_name]['Age']}\nGrades: {students[searh_name]['Grades']}')
# else:
#     print('Student not found')

# Task_123

# mylist = []
# n = int(input('How many elements do you want to add? '))
# for i in range(n):
#     element = input(f'Enter an element {i + 1}: ')
#     low_element = element.lower()
#     mylist.append(low_element)
#
# unigue_elements = set(mylist)
# slovar = {}
# for j in mylist:
#     if j in slovar:
#         slovar[j] += 1
#     else:
#         slovar[j] = 1
#
# sorted_slovar = sorted(slovar.items(), key=lambda item: item[1],reverse=True)
# print(sorted_slovar)

# Task_124

# list1 = input('Enter the items in the first list separated by a space: ').split()
# list2 = input('Enter the items in the second list separated by a space:').split()
#
# unique_list1, unique_list2 = set(map(int, list1)), set(map(int, list2))
# sym_dif = unique_list1.symmetric_difference(unique_list2)
#
# print('Symmetric difference:', sym_dif)

# Task_125

# num = int(input('enter the number: '))
# sum_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_digits += digit
#     num //= 10
# print('Sum of the Numbers:', sum_digits)

# Task_84 (ЕБАННЫЙ СЛОН)

# x_1, y_1, x_2, y_2 = int(input('column number: ')), int(input('line number: ')), int(input('column number: ')), int(input('line number: '))
# if 1 <= x_1 <= 8 and 1 <= x_2 <= 8 and 1 <= y_1 <= 8 and 1 <= y_2 <= 8:
#    if x_2 - x_1 == y_2 - y_1:
#        print('Yes')
#    else:
#        print('No')
# else:
#     print('The number must be between 1 and 8')

# Task_85 85 (ЕБАННЫЙ КОНЬ)

# x_1, y_1, x_2, y_2 = int(input('column number: ')), int(input('line number: ')), int(input('column number: ')), int(input('line number: '))
# if all(1 <= i <= 8 for i in [x_1,x_2,y_1,y_2]):
#     if (x_2 == x_1 + 2 or x_2 == x_1 - 2) and (y_2 == y_1 + 1 or y_2 == y_1 - 1):
#         print('YES')
#     elif (y_2 == y_1 + 2 or y_2 == y_1 - 2) and (x_2 == x_1 + 1 or x_2 == x_1 - 1):
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('The number must be between 1 and 8')

# Task_86 (ЕБАННЫЙ ФЕРЗЬ)
# x_1, y_1, x_2, y_2 = int(input('column number: ')), int(input('line number: ')), int(input('column number: ')), int(input('line number: '))
# if all(1 <= i <= 8 for i in [x_1,x_2,y_1,y_2]):
#     if x_1 == x_2 or y_1 == y_2:
#         print('Yes')
#     elif x_2 - x_1 == y_2 - y_1:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('The number must be between 1 and 8')