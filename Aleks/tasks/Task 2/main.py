SepName = input("Напишите строку-разделитель: ")
FirstName = input("Напишите первую строку: ")
SecondName = input("Напишите вторую строку: ")
ThirdName = input("Напишите третью строку: ")
print(FirstName, SecondName, ThirdName, sep=SepName)

#  Line 5 , according PEP8 there are no spaces before and after =
#  It is good answer , but you can do it another way,  check the code bellow
#
# separator = input()
# data = []
# for _ in range(3):
#     data.append(input())
# print(*data, sep=separator)
