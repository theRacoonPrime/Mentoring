# task_2 = 'Здравствуй мир'
# print(task_2)
# # It is more simple , just print("Hello world !")



# task_3 = '''
# 4
# 8
# 15
# 16
# 23
# 424
# 8
# 15
# 16
# 23
# 42
# '''
# print(task_3)

# Task 3 is totally wrong , what is it ?  What does that mean ?  Just use print("4 8 15 16 23 42"), that`s all

#
# task_4 = '\n4 \n8 \n15 \n16 \n23 \424 \n8 \n15 \n16 \n23 \n42'
# print(task_4)

# Task 4 , do you try to run it ?  Did you test it ? If you are run it  is show russian E, somewhere was typed,
# correct answer is provided bellow
# task_4 = '\n4 \n8 \n15 \n16 \n23 \n42 \n8 \n15 \n16 \n23 \n42'
# print(task_4)
#
# # task_5
# i = 1
# num = int(input())
# while i <= num:
#     print('*' * i)
#     i = i + 1
#  Task 5 , try to read one more time the task , you are not understood it , your solution is not work ,
#  only when user type something , it is more simple than you are thinking



# task_6 = input('Как тебя зовут? ')
# print('Привет! ' + task_6)
# # Task 6 is ok , it is wokrk , nice job

# task_7 = input('Твоя футбольная команда? ')
# print(task_7 + " - чемпион!")
# #  Task 7 , nice job , work properly

# task_8_1 = input()
# task_8_2 = input()
# task_8_3 = input()
# answer = (f'\n{task_8_1}\n{task_8_2}\n{task_8_3}')
# print(answer)

# Task 8, basically ok , but you can improve it , pay attention to input method , that`s will be the crucial for you
# task_9_1 = input()
# task_9_2 =input()
# task_9_3 = input()
# answer= (f'\n{task_9_3}\n{task_9_2}\n{task_9_1}')
# print(answer)
#  Task 9 , the same problem as above ,  it is ok , but it could be better , and where are the spaces ? You are not
#  indian guy

# task_10 = ('i', 'like', 'python')
# print(*task_10, sep='***')
# /Не совсем понял, как работает, зачем нужна "*" перед"task_10". Обязательно ли sep писать в "print"

#  the code print(*task_10, sep='***'), the * operator is used to unpack the tuple task_10. This means it takes
#  each element from the tuple and passes them as separate arguments to the print function.
#
# task_10 is a tuple: ('i', 'like', 'python').
# *task_10 unpacks the tuple, so it becomes equivalent to print('i', 'like', 'python').
# sep='***' specifies the separator between the arguments when printing them.
# The sep parameter is optional, and it defines what string should be used to separate
# the values. If you don't specify sep, the default separator (a space) will be used.


# task_11 = input()
# print("Привет, " + task_11, end='!')
# # Task 11 , well done , go ahead


# строка_разделитель = input()
# task_12_2 = input()
# task_12_3 = input()
# task_12_4 = input()
# task_12 = (task_12_2, task_12_3, task_12_4,)
# print(*task_12, sep=строка_разделитель)
#  Holly Molly , Remember ! No russian ! . Next one , you can do it more simple , like this
# a, b, c, d = input(), input(), input(), input()
# print(b, c, d, sep=a)

# task_13 = int(input())
# second_number = task_13 + 1
# third_number = second_number + 1
# print(f'\n{task_13}\n{second_number}\n{third_number}')
# #  Well done , but  I feel Edik here :)

#
# task_14 = int(input())
# task_14_1 = int(input())
# task_14_2 = int(input())
# print(task_14 + task_14_1 + task_14_2)
# # The same  as  in task 12 , could be simple

# # task_15
# a = int(input())
# v = a**3
# s = 6 * a**2
# print(v, s)
# Well done , go ahead

# #task_16
# a = int(input())
# b = int(input())
# f = 3 * (a + b)**3 + 275 * b**2 - 127 * a - 41
# print(f)
# It`s ok too, well done


# task_17 = int(input("Enter your number:"))
# print(f'Следующее за числом {task_17} число: {task_17 + 1}\nДля числа {task_17} предыдущее число: {task_17 - 1}') #я сам не понял, почему без "f" он пишет что это str (разобрать)
# print(f'')

# task_18
# стоимость_монитора = int(input())
# стоимость_системного_блока = int(input())
# стоимость_клавиатуры = int(input())
# стоимость_мыши = int(input())
# общая_стоимость = стоимость_монитора + стоимость_системного_блока + стоимость_клавиатуры + стоимость_мыши
# print(общая_стоимость)

# task 18
# first = int(input())
# second = int(input())
# сумма = first + second
# разность = first - second
# произведение = first * second
# print(сумма)
# print(разность)
# print(произведение)

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
# result_2 = (int(result_1) * students) - mandarins #Эту...
# print(int(result_1))
# print(abs(result_2))

# task_25
# import math
# n = int(input(''))
# if int(n / 2):
#     print(int(n / 2))
# else: print(n / 2 + 1) УЗНАТЬ ПОЧЕМУ НЕ РАБОТАЕТ

# # task_25_1
# import math
# n = int(input(''))
# if n / 2:
#     answer = int(n / 2)
# else:
#     answer = int(n / 2 + 1)
# print(answer)           #Тоже узнать

