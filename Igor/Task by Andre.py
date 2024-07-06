# task_2
# print( ('Hello, world !'))


#  Task 2 Ok

# # task_3
# print('4 8 15 16 23 42')
#  Task 3 , Ok


# task_4
# task_4 = '\n4 \n8 \n15 \n16 \n23 \n42 \n8 \n15 \n16 \n23 \n42'
# print(task_4)
#  It is ok

# task_5
# print('\n \\* \n \\** \n \\*** \n \\**** \n \\***** \n \\****** \n \\*******')
# Wrong , a little bit , you have one more slash , slash should be there


# task_6 = input('What is your name? ')
# print('Hello! ' + task_6)
# Nice job


# task_7 = input('what is your favorite footbal team? ')
# print(task_7 + " - champion!")
#  Ok

# task_8_1 = input()
# task_8_2 = input()
# task_8_3 = input()
# print(f'\n{task_8_1}\n{task_8_2}\n{task_8_3}')
#  ok , but you can improve it , try to use more input in one line , like this input(),input(), input()

# task_9_1 = input()
# task_9_2 = input()
# task_9_3 = input()
# print(f'\n{task_9_3}\n{task_9_2}\n{task_9_1}')
#  ok , but the same thing as task 8


# task_10 = ('i', 'like', 'python')  # Разобрать еще раз, не понял.
# first, like, python = task_10
# print(task_10[::2])
# print(f"first = {first} like = {like} python = {python} first element = {task_10[0]}")
# print(*task_10, sep='***')


#  What exactly you do not understand , specify it

# task_11 = input()
# print("Hello, " + task_11, end='!')

# task_12_1, task_12_2, task_12_3, task_12_4 = input(), input(), input(), input()
# print(task_12_2, task_12_3, task_12_4, sep=task_12_1)
#  Ok


# task_13 = int(input())
# second_number = task_13 + 1
# third_number = second_number + 1
# print(f'\n{task_13}\n{second_number}\n{third_number}')
#  Ok


# task_14 = int(input("Enter first number: "))+int(input("Enter second number: "))+int(input("Enter third number: "))
# print (task_14)
#  Pay attention on the spaces , after print


# task_15
# a = int(input())
# v = a**3
# s = 6 * a**2
# print(v, s)
# Well done

 # #task_16
# a = int(input())
# b = int(input())
# f = 3 * (a + b)**3 + 275 * b**2 - 127 * a - 41
# print(f)
# Well done

# task_17 = int(input("Enter your number:"))
# print(f'next to the number {task_17} number: {task_17 + 1}\nFor number {task_17} last to the number: {task_17 - 1}') #я сам не понял, почему без "f" он пишет что это str (разобрать)
# print(f'')
# Describe it what you did not understand


# task_18
# monitor_value = int(input())
# system_block_value = int(input())
# keyboard_value = int(input())
# mouse_value = int(input())
# total_value = (monitor_value + system_block_value + keyboard_value + mouse_value) * 3
# print(total_value)
# It is ok , but you can doi it more shortly for instance  print((int(input()) + int(input()) + int(input()) + int(
# input())) * 3)


# task 19
# first = int(input())
# second = int(input())
# amount = first + second
# difference = first - second
# multiplication = first * second
# print(f'{amount}\n{difference}\n{multiplication}')
# #  A little bit long solution , you can do it better , a,b = int(input()),int(input())
# # print(f'{a} + {b} = {a+b}', f'{a} - {b} = {a-b}', f'{a} * {b} = {a*b}', sep='\n')


# task_23
# centimeter = int(input())
# metr = centimeter * 100
# print(metr)
#  Ok

# task_21
number = int(input())
print(number, number * 2, number * 3, number * 4, number * 5, sep='///')
#  Ok

# task_24 Я БЛЯТЬ ГОЛОВУ СЕБЕ СЛОМАЛ ПОКА ЭТУ ФОРМУЛУ ПРИДУМАЛ...
# mandarins = int(input())
# students = int(input())
# result_1 = mandarins / student
# result_2 = (int(result_1) * students) - mandarins #Эту...
# print(int(result_1))
# print(abs(result_2)) #Я понимаю, что тут другое решение, но я не понимаю, как
#  It is more simple ,  I provide you a few solution how to figure out
# n = int(input())
# k = int(input())
# a = k // n
# b = k % n
# print(a, b, sep="\n")

#  a, b = int(input()), int(input())
# print(b // a, b % a, sep = '\n')

 #task_25
n = int(input())
if n % 2 == 0:
    print(n // 2)
else:
    print(n // 2 + 1)

#      It is ok , but you can do it without conditionals
#      n = int(input()) a = n + 1 print(a // 2 )

# task_20 a_1 = int(input('Enter the first element of the arithmetic progression: ')) d = int(input('Enter the
# difference (step) of the arithmetic progression: ')) n = int(input('Enter the number of elements of the arithmetic
# progression: ')) a_n = a_1 + d * (n - 1) for item in range (a_1, a_n + 1, d): #Я написал сначала самастоятельно,
# но потом решил проверить. несмотря на то, что моя прогрессия работала, нейросеть сказала, что я допустил ошибку. я
# не написал (a_n + 1), написал просто (a_n). Не понимаю,как работает этот +1 print(item) Stop use ChatGPT ,
# the same example as above , you can do it more simple , something like a1, d, n = int(input()), int(input()),
# int(input())
#
# print(a1 + d * (n - 1))
