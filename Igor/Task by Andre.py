# task_2
# print('Hello, world !')

# task_3
# print('4 8 15 16 23 42')

# task_4
# task_4 = '\n4 \n8 \n15 \n16 \n23 \n42 \n8 \n15 \n16 \n23 \n42'
# print(task_4)

# task_5
# print('\n \\* \n \\** \n \\*** \n \\**** \n \\***** \n \\****** \n \\*******')

# task_6 = input('What is your name? ')
# print('Hello! ' + task_6)

# task_7 = input('what is your favorite footbal team? ')
# print(task_7 + " - champion!")

# task_8_1, task_8_2, task_8_3 = input(), input(), input()
# print(f'\n{task_8_1}\n{task_8_2}\n{task_8_3}')

# task_9_1, task_9_2, task_9_3  = input(), input(), input()
# print(f'\n{task_9_3}\n{task_9_2}\n{task_9_1}')

# task_10 = ('i', 'like', 'python')
# first, like, python = task_10
# print(task_10[::2])
# print(f"first = {first} like = {like} python = {python} first element = {task_10[0]}")
# print(*task_10, sep='***')

# task_11 = input()
# print("Hello, " + task_11, end='!')

# task_12_1, task_12_2, task_12_3, task_12_4 = input(), input(), input(), input()
# print(task_12_2, task_12_3, task_12_4, sep=task_12_1)

# task_13 = int(input())
# second_number = task_13 + 1
# third_number = second_number + 1
# print(f'\n{task_13}\n{second_number}\n{third_number}')

# task_14 = int(input("Enter first number: "))+int(input("Enter second number: "))+int(input("Enter third number: "))
# print(task_14)

# task_15
# a = int(input())
# v = a**3
# s = 6 * a**2
# print(v, s)

# #task_16
# a = int(input())
# b = int(input())
# f = 3 * (a + b)**3 + 275 * b**2 - 127 * a - 41
# print(f)

# task_17 = int(input("Enter your number:"))
# print(f'next to the number {task_17} number: {task_17 + 1}\nFor number {task_17} last to the number: {task_17 - 1}')
# print(f'')

# task_18
# monitor_value = int(input())
# system_block_value = int(input())
# keyboard_value = int(input())
# mouse_value = int(input())
# print(int(mouse_value + system_block_value + keyboard_value + mouse_value) * 3)

# task 19
# a, b = int(input()), int(input())
# print(f'{a} + {b} = {a+b}', f'{a} - {b} = {a-b}', f'{a} * {b} = {a*b}', sep='\n')


# task_23
# centimeter = int(input())
# metr = centimeter * 100
# print(metr)

# task_21
# number = int(input())
# print(number, number * 2, number * 3, number * 4, number * 5, sep='///')

# task_24 Я БЛЯТЬ ГОЛОВУ СЕБЕ СЛОМАЛ ПОКА ЭТУ ФОРМУЛУ ПРИДУМАЛ...
# mandarins = int(input())
# students = int(input())
# result_1 = mandarins / student
# result_2 = mandarins % student
# print (a, b, sep='\n'

#task_25
# n = int(input())
# if n % 2 == 0:
#     print(n // 2)
# else:
#     print(n // 2 + 1)

#task_20
# a_1, d, n = int(input()), int(input()), int(input())
# print (a_1 + d * (n - 1))

# task_22
# b_1 = int(input('Enter the first term of the progression: '))
# q = int(input('Enter the denominator of progression: '))
# n = int(input('Enter the number of terms of the progression'))
# b_n = b_1 * q ** (n-1) #должно быть в скобках, так как возведение в степень должно быть выполнено до умножения.
# for item in range (b_1, b_n +1, q):
#     print(item)

#task_26
# minute = int(input('write the number of minutes: '))
# hour = minute // 60
# hour_left = minute % 60
# print(f'initial number of minutes {minute} - this {hour} hour {hour_left} minute')

#task_27
# import math
# number = int(input())
# print(math.ceil(number / 4))

#task_28
# number = int(input())
# hundreads = number // 100
# tens = (number // 10) % 10
# units = number % 10
# sum_digits = hundreads + tens + units
# product_digits = hundreads * tens * units
# print(f'\nsum of digits: {sum_digits}\nnumber production: {product_digits}')

#task_29
# number = input()
#
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i != j and j != k and k != i:
#                 print(f"{number[i]}{number[j]}{number[k]}")

# task_32
# a = int(input())
# b = int(input())
# square_of_sum = (a + b) ** 2
# sum_of_squares = a ** 2 + b ** 2
# print(f'The squared sum of {a} and {b} is - {square_of_sum} \nSum of squares of {a} and {b} is - {sum_of_squares}')

# task_33
# a, b, c, d, = int(input()), int(input()), int(input()), int(input())
# print(a ** b + c ** d)

# task_31
# height, width = int(input("ENTER len and width")), int(input())
# for i in range(width): #range создает перебор от 0 до (то число, которые будет вписано) (от 1 до 10 = 0/1/2/3/4/5/6/7/8/9/=)
#     print("*", end="")
# print()
# for i in range(height - 2):
#     print("*", end="")
#     for j in range(width-2):
#         print("/", end="")
#     print("*")
# for i in range(width):
#     print("*", end="")

# task_30
# number = input()
# for i in range(4):
#     for j in range(4):
#         for y in range(4):
#             for x in range(4):
#                 if i != j and j != y and y != x and x != i and x != j and y != i:
#                     print(f"{number[i]}{number[j]}{number[y]}{number[x]}")

# task_34
# number = input()
# print(int(number) + int(number * 2) + int(number *3))

#task_35
# qwerty_1 = input()
# qwerty_2 = input()
# if qwerty_1 == qwerty_2:
#     print('password accepted')
# else: print('password not accepted')

#task 36
# number = int(input())
# if number % 2 == 0:
#     print('even')
# else: print('odd')

#task_37
# number = input()
# first = int(number[0])
# second = int(number[1])
# thirty = int(number[2])
# fourth = int(number[3])
# sum = first + fourth
# diif = second - thirty
# if sum == diif:
#     print('Yes')
# else:print('No')

#task_38
# age = int(input())
# if age >= 18:
#     print('Access allowed')
# else: print('Access denied')

# task_38_2
# n = 4
# for i in range(1, n + 1):
#     print("*" * i)

#task_39
# for i in range(1, 11):
# square = i * i
# cube = i ** 3
# print(f'{i} {square} {cube}')

#task_40 - ХУЙНЯ,ПОНЯТЬ КАК ДЕЛАТЬ.

#task_41
# apple, banana, cherry = 0.50, 0.30, 0.20
# print(f'Item Price: \napple ${apple} \nbanana ${banana} \ncherry ${cherry} \nTotal {apple + banana + cherry} ')

#task_43
# print(f'{'Celsius':<15} {'Fahrenheit':<15}') #Пример того, как писать в два столбика.
# for i in range(0,110,10):
#     j = i * 1.8 + 32
#     print(f'{i:<15} {j:<15}') # ":<15" - указывает, что имя должно быть выровнено по левому краю и занимать 15 символов ширины. Если имя короче 15 символов, оставшееся пространство будет заполнено пробелами.
#task_44 - ЕЩЕ ОДНА ЕБАННАЯ ХУЙНЯ

#task_45
# names = ["Alice", "Bob", "Charlie", "Diana"]
# for name in names:
#     print(f'{name:<10}') #тоже форматирование

#task_46
# text = "hello world hello" #Строка, в которой мы будем считать количество вхождений слова "hello".
# count = text.count('hello') #Метод count подсчитывает количество вхождений подстроки "hello" в строке text.
# print(print(f"'hello' appears {count} times in the text.") #Используем форматированную строку (f-string) для вывода результата

#task_47 #Как создавать календарь
# year, month = 2024, 7
# print(calendar.month(year, month))

#task_48
# name =input('Please tell me your name: ')
# print(f'Nice to meet you: {name}, Let is be friends?!')

#task_49
# print('Please enter two numbers: ')
# first, second = int(input('First: ')), int(input('Second: '))
#print(first + second)

# task_50
# age = int(input('Please enter your age: '))
# print(f"you'll be 100 years old in: {100 - age}")

# task_51
# colour = input("What's your favourite colour")
# print(f'The colour: {color} - is a good colour')

# task_52
# proposal = input()
# print(len(proposal))

# task_53
# while True:
#     num1, num2, operator = float(input()), float(input()), input()
#     if operator == '+':
#         plus = num1 + num2
#         print(f'Your answer: {plus}')
#     elif operator == '-':
#         minus = num1 - num2
#         print(f'Your answer: {minus}')
#     elif operator == '*':
#         multiply = num1 * num2
#         print(f'Your answer: {multiply}')
#     elif operator == '/':
#         if num2 == 0:
#             print("Idiot! It's not divisible by 0")
#         else:
#             division = num1 / num2
#             print(f'Your answer: {division}')
#     else:
#         print("Wrong operator:")
#     again = input('Do you want to perform another calculation? (yes/no): ')
#     if again == 'no':
#         break
##START. check 22/07/24

# #task_56
# print('Attention! Your password must consist of 7 digits, 3 letters of any case, and a minimum of 10 characters.')
# while True:
#     qwerty = input('Please enter your password: ')
#     digits = sum(c.isdigit() for c in qwerty)
#     letters = sum(c.isalpha() for c in qwerty)
#     if len(qwerty) < 10 and digits < 7 and letters < 3:
#         print('Input error! Try again!')
#         continue
#     print('Password accepted')
#     break
#OR
# print('Attention! Your password must consist of 7 digits, 3 letters of any case, and a minimum of 10 characters.')
# while True:
#    qwerty = input('Please enter your password: ')
#    if len(qwerty) <=10:
#        print("Error, password must contain at least 10 characters ")
#        continue
#    digits = sum(c.isdigit() for c in qwerty)
#    letters = sum(c.isalpha() for c in qwerty)
#    if digits < 7:
#        print('Error, password must have at least 7 digits')
#        continue
#    if letters < 3:
#        print('Error, password must have at least 3 letters')
#        continue
#    print('Password accepted')
#    break

#task_57
# while True:
#     num = int(input('Please enter number: '))
#     if num < 0:
#         print('Your number is negative.')
#     elif num == 0:
#         print('Your number is zero.')
#     else:
#         print('Your number is positive ')
#     again = input('Do you want to continue? ')
#     if again == 'yes':
#         continue
#     else:
#         break








