# task_2
# print('Hello, world !')
#  OK
# task_3
# print('4 8 15 16 23 42')
# OK

# task_4
# task_4 = '\n4 \n8 \n15 \n16 \n23 \n42 \n8 \n15 \n16 \n23 \n42'
# print(task_4)
# ok

# task_5
# print('\n \\* \n \\** \n \\*** \n \\**** \n \\***** \n \\****** \n \\*******')
# Wrong , one more slash
# print('\n * \n ** \n *** \n **** \n ***** \n ****** \n ********')
#  How it`s should be

# task_6 = input('What is your name? ')
# print('Hello! ' + task_6)
#  Well done

# task_7 = input('what is your favorite footbal team? ')
# # print(task_7 + " - champion!")
# ok


# task_8_1, task_8_2, task_8_3 = input(), input(), input()
# print(f'\n{task_8_1}\n{task_8_2}\n{task_8_3}')
# Nice

# task_9_1, task_9_2, task_9_3 = input(), input(), input()
# print(f'\n{task_9_3}\n{task_9_2}\n{task_9_1}')
# It`s ok , but there was one more space before equal character

# task_10 = ('i', 'like', 'python')
# first, like, python = task_10
# print(task_10[::2])
# print(f"first = {first} like = {like} python = {python} first element = {task_10[0]}")
# print(*task_10, sep='***')
# I do not understand what you try to do ? Why do you have to more prints here ?
# task_11 = input()
# print("Hello, " + task_11, end='!')
#  Ok

# task_12_1, task_12_2, task_12_3, task_12_4 = input(), input(), input(), input()
# print(task_12_2, task_12_3, task_12_4, sep=task_12_1)
# Ok

# task_13 = int(input())
# second_number = task_13 + 1
# third_number = second_number + 1
# print(f'\n{task_13}\n{second_number}\n{third_number}')
#  OK
# task_14 = int(input("Enter first number: "))+int(input("Enter second number: "))+int(input("Enter third number: "))
# print(task_14)
# Ok
# task_15
# a = int(input())
# v = a**3
# s = 6 * a**2
# print(v, s)
# great job

# # #task_16
# a = int(input())
# b = int(input())
# f = 3 * (a + b)**3 + 275 * b**2 - 127 * a - 41
# print(f)
# great , nice job
# task_17 = int(input("Enter your number:"))
# print(f'next to the number {task_17} number: {task_17 + 1}\nFor number {task_17} last to the number: {task_17 - 1}')
# print(f'')
# nice
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
# print (a, b, sep='\n')

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

#task_41
# apple, banana, cherry = 0.50, 0.30, 0.20
# print(f'Item Price: \napple ${apple} \nbanana ${banana} \ncherry ${cherry} \nTotal {apple + banana + cherry} ')

#task_43
# print(f'{'Celsius':<15} {'Fahrenheit':<15}') #Пример того, как писать в два столбика.
# for i in range(0,110,10):
#     j = i * 1.8 + 32
#     print(f'{i:<15} {j:<15}') # ":<15" - указывает, что имя должно быть выровнено по левому краю и занимать 15 символов ширины. Если имя короче 15 символов, оставшееся пространство будет заполнено пробелами.


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
#    digits = sum(c.isdigit() for c in qwerty) #РАЗОБРАТЬСЯ
#    letters = sum(c.isalpha() for c in qwerty) #РАЗОБРАТЬСЯ
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
#    num = int(input('Please enter number: '))
#    if num < 0:
#        print('Your number is negative.')
#    elif num == 0:
#        print('Your number is zero.')
#    else:
#        print('Your number is positive ')
#    again = input('Do you want to continue? (yes/no):  ').strip().lower() #strip = удаляет пробелы, lower = переводит все в нижний регистр(Независимио от того, в каком регистре будет написано)
#    if again == 'yes':
#        continue
#    else:
#        break

# task_58
# age = int(input('Please enter your age:'))
# if age == 0 or age <= 12:
#     print("Congratulations! You're still a baby")
# elif age >= 13 and age <= 19:
#     print("How's school going? ‘Son.’?")
# elif age >= 20 and age <= 59:
#     print('Adult living is a hard thing')
# else:
#     print('Old age is no joy')

# task_59
# while True:
#     assessment = input('Enter a grade: ').lower()
#     if assessment in ['a', 'b', 'c', 'd']:
#         assessment_up = assessment.upper()
#         print(f'Your grade: {assessment_up}')
#         break
#     else:
#         print('Incorrect estimate.Try again')
#         continue

# task_60
# num = int(input('Please enter a number: '))
# if num % 2 == 0 and num % 3 == 0:
#     print('Your number is divisible by two and three')
# elif num % 2 == 0:
#     print('Your number is divisible by two')
# elif num % 3 == 0:
#     print('Your number is divisible by three')
# else:
#     print('Your number is not divisible by 2 and 3')

#task_61
# num_1, num_2, num_3 = int(input()), int(input()), int(input())
# if num_1 > 0 and num_2 > 0 and num_3 > 0:
#     sum = num_1 + num_2 + num_3
#     print(sum)
# else:
#     print('00')

#task_62/
# while True:
#     num_0 = list(range(0,101))
#     num_1 = int(input())
#     if num_1 in num_0:
#         print('Your number belongs to the interval')
#         break
#     else:
#         print('Your number does not belong to the interval')
#         continue
#OR
# num = int(input())
# if 0 < num <= 100:
#     print('Your number belongs to the interval')
# else:
#     print('Your number does not belong to the interval')


#task_63
# num = int(input())
# if -30 <= num < -7 or 7 < num <= 25:
#     print('Your number belongs to the interval')
# else:
#     print('Your number does not belong to the interval')

#task_64
# num = int(input())
# if 5 <= num < 15 or 20 < num <= 50:
#     print('Your number belongs to the interval')
# else:
#     print('Your number does not belong to the interval')

#task_65
# while True:
#    num_4 = (input('Please enter a four digit number: '))
#    if len(num_4) == 4 and num_4.isdigit():#len = проверяет кол-во символов. .isdigit() = состоит тоько из чисел
#        num_4 = int(num_4) #сразу преобразует строку в число
#        if num_4 % 77 == 0 or num_4 % 1717 == 0: # % = остаток от деления. % возвращает 0б если число делится нацело.
#            print('YES')
#            break
#        else:print('NO')
#        continue
#    else:
#        print('Error! Please enter a four-digit number')
#        continue

#task_66
# a, b, c = int(input()), int(input()), int(input())
# if a + b > c and a + c > b and b + c > a: # длина любой стороны треугольника всегда меньше суммы длин двух его других сторон
#    print('YES')
# else:
#    print('NO')

#task_67
# year = int(input())
# if (year % 44 == 0 and year % 100100 != 0) or year % 400400: # '==' = кратен. '!=' = не кратен
#    print('YES')
# else:
#    print('NO')

#task_68
# x_1, y_1, x_2, y_2 = int(input('Enter the initial column number(1 to 8): ')), int(input('Enter the original line number(1 to 8): ')), int(input("Enter the next column number(let's say a move of 1 square): ")), int(input("Enter the following line number(let's say a move of 1 square): "))
# if 1 <= x_1 <= 8 and 1 <= y_1 <= 8:
#     if (x_2 == x_1 + 1 or x_2 == x_1 - 1) and (y_1 == y_2) or (y_2 == y_1 + 1 or y_2 == y_1 - 1) and (x_1 == x_2):
#         print('YES')
#     else:
#         print('NO')

#task_69
# x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
# if 1 <= x_1 <= 8 and 1 <= y_1 <= 8:
#     if (x_2 == x_1 + 1 or x_2 == x_1 - 1) and (y_2 == y_1 + 1 or y_2 == y_1 - 1):
#         print('YES')
#     else:
#         print('NO')

#task_70
# num_1 = int(input('Enter the zoom speed: '))
# num_2 = int(input('Enter the flash speed: '))
# if num_1 > num_2:
#     print('NO')
# elif num_2 > num_1:
#     print('YES')
# else:
#     print("Don't know")

#task_71
# a, b, c = int(input()), int(input()), int(input())
# if a == b or b ==c or c == a:
#     print('Your triangle is isosceles')
# elif a == 60 and b == 60 and c == 60:
#     print('Your triangle is equilateral')
# elif a != b and b != c and c != a:
#     print('Your triangle is scalene')

#task_72
# num_1, num_2,num_3 = int(input()), int(input()), int(input())
# num_4 = sorted([num_1, num_2, num_3])
# print(num_4[1])

#task_73
# month = int(input())
# if month in (1, 3, 5, 7, 8, 10, 12):
#     print('31')
# elif month in (4, 6, 9, 11):
#     print('30')
# elif month == 2:
#     print('28')

#task_74
# weight = int(input())
# if 0 < weight < 60: print('Light weight')
# elif 60 <= weight < 64: print('Light welterweight')
# elif 64 <= weight < 69: print('Welterweight')
# else:
#     print('Error')

#task_75 УЖЕ ПИСАЛ КАЛЬКУЛЯТОР

#task_76
# a, b = input('please enter colour: yellow, red or blue: '), input('please enter colour: yellow, red or blue: ')
# color = ['yellow', 'red', 'blue' ]
# if a != color and b != color:
#     print('one of the lines is not the right colour!')
# elif a == 'blue' and b == 'red' or b == 'blue' and a == 'red':
#     print('you got a purple colour')
# elif a == 'red' and b == 'yellow' or a =='yellow' and b == 'red':
#     print('you got the colour orange')
# elif a == 'blue' and b == 'yellow' or a == 'yellow' and b == 'blue':
#     print('you got the colour green')
# elif a == b:
#     print(a)

#task_77 (Хороший пример)
# num = int(input('Try your luck! Enter a number: '))
# if num == 0:
#     print('green')
# elif 1 <= num <= 36:
#     if (num % 2 == 0 and 1 <= num <= 10) or (num % 2 == 1 and 11 <= num <= 18) or (num % 2 == 0 and 29 <= num <= 36):
#         print('black')
#     else:
#         print('red')
# else:
#     print('input error')

#task_79
# year = input('Enter the year: ')
# if year.isdigit() and len(year) == 3 or len(year) == 4:
#    if year[-2:] == '00':
#        print('YES')
#    else:
#        print('NO')
# else:
#     print('Error, try again!')

#task_80
# x_1, x_2, y_1, y_2 = int(input()), int(input()), int(input()), int(input())
# if (x_1 + x_2) % 2 == 0 and (y_1 + y_2) % 2 == 0: #черный клетки всегда нечетные (нечетное + нечетное = четное). белые клетки всегда четные (четное + четное= четное). таким образом, если пользователь введет нечетное и четное(разные клетки), то всегда получится "NO"
#    print('YES')
# else:
#    print('NO')

#task_81
# sex, age = input('Who are you today(m or f)? '), int(input('How old are you: '))
# print('Yes' if sex == 'f' and 10 <= age <= 15 else 'No')

# task_82 (Начал изучать словари)
# num = int(input())
# rim_num = {1: 'I', 2: 'II', 3: 'III',4: 'IV',
#            5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII',
#            9: 'IX', 10: 'X'}
# if 1 <= num <= 10:
#     print(rim_num[num])
# else:
#     print('Error')

# Task_83
# num = int(input())
# if num % 2 == 1:
#     print('YES')
# elif 22 <= num <= 55 and num % 2 == 0 or num > 2020 and num % 2 == 0:
#     print("NO")
# elif 66 <= num <= 2020 and num % 2 == 0:
#     print('YES')

# task_87
# a, b = float(input('write 1 length of the cathetus: ')), float(input('write 2 length of the cathetus: '))
# s = 0.5 * a * b
# print(s)

# task_88
# s, v_1, v_2 = float(input('enter a distance between them: ')), float(input('enter the speed of the first old lady: ')), float(input('enter the speed of the second old lady: '))
# v_12 = v_1 + v_2 #Скорость сближения
# ans = s // v_12 #время встречи
# print(f' {ans} hours')

# task_89
# Tf = float(input('enter temperature: '))
# Tc = 5/9 * (Tf - 32)
# print(f'{Tc} in degrees Celsius')

# task_90
# age = int(input('How old is your dog? '))
# if age <= 2:
#     ans = age * 10.5
#     print(ans)
# elif age > 2:
#     ans = ((age-2) * 4) + 21
#     print(ans)

# task_91
# num = float(input('Enter a number: '))
# num_2 = int(num * 10) % 10
# print(num_2)

# task_92
# num = float(input('Enter a number: '))
# num_2 = num - int(num)
# print(num_2)

# task_93
# num_1, num_2, num_3, num_4, num_5 = int(input()), int(input()), int(input()), int(input()), int(input())
# total_sum = (num_1, num_2, num_3, num_4, num_5)
# least = sorted(total_sum)
# print(f'smallest number: {least[0]}\nlargest number: {least[-1]} ')

# task_94
# num_1, num_2, num_3 = int(input()), int(input()), int(input())
# total_num = (num_1, num_2, num_3)
# least = sorted(total_num, reverse=True)
# print(f'{least[0]}\n{least[1]}\n{least[2]}') #либо: for num in least/print(num)

# task_95
# while True:
#     num = (input('Enter a three-digit number(or exit for quit): '))
#     if num.lower() == 'exit':
#         break
#     if num.isdigit() and len(num) == 3:
#         least = sorted(num)
#         if int(least[2]) - int(least[0]) == int(least[1]):
#             print('The number is interesting')
#             continue
#         else:
#             print("The number isn't interesting")
#             continue
#     else:
#         print('Idiot? It says three digits!')

# task_96
# num_1, num_2, num_3, num_4, num_5 = float(input()), float(input()), float(input()), float(input()), float(input())
# numbers = [num_1, num_2, num_3, num_4,num_5]
# sam = 0 #sam = 0 для последующего накопления ссумы модулей
# for num in numbers:
#    sam += abs(num) #abs = убирает знаки, всегда использует '+'. если я ввожу -2.5 он вернут 2.5 (тем самым он убирает знак -, и дает высчитать сумму, а не разнсть.
# print(sam)

# task_97
# print('enter coordinates: ')
# p_1, p_2,q_1, q_2 = int(input()), int(input()), int(input()), int(input())
# man = abs(p_1 - q_1) + abs(p_2 - q_2)
# print('Manhetian distance', man)

#ПРОШЫЕ ТАСКИ, КОТОРЫЕ СОТАВИЛ НА ПОТОМ
# task_40

# num_1 = [0]
# num_2 = [1]
# fib = num_1 + num_2
# for _ in range(8): # при помощи переменной "_" мы показываем, что она не будет использоваться внутри цикла.
#    next_num = fib[-1] + fib[-2] # "fib[-1]" = последний элемент списка fib, "fib[-2]" = предпоследний.
#    fib.append(next_num) # "append" добавляет в "fib" в конец списка элементы из 'next_num'(Добовляет слудющие числа из цикла)
# print(fib)

# task_42 # Я ЕБАЛ...
# n = 5
# for i in range(n):
#     star = '*' * (2 * i + 1)
#     space = ' ' * (n - i - 1)
#     print(space + star)
# for i in range(n - 1, 0, -1):
#     space = ' ' * (n - i)
#     star = '*' * (2 * i - 1)
#     print(space + star)








