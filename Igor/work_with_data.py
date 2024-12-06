import numpy as np
import pandas as pd

#task 1
# a = np.arange(10)
# print(a)

#task_2

# a = np.arange(1, 10).reshape(3, 3)
# print(a)

#task_3

# a = np.array([2,4,6])
# b = np.array([1,3,5])
#
# ans = a + b
# ans_2 = a - b
# ans_3 = a * b
# ans_4 = a // b
#
# print(ans, ans_2, ans_3, ans_4)

# task_4

# a = np.arange(5, 15)
# print(f'{a[0]}, {a[-3:]}, {a[::2]}' )

# task_5

# a = np.random.randint(0,6,5)
# print(a)

# task_6

# bamboo = pd.DataFrame({
#     'Name': ["Igor", "Andrey", "Edward", "Tema"],
#     'Age': [21, 22, 25, 30],
#     'City': ["Prague","London","Paris","Russia"]
# })
#
# print(bamboo)

# task_7

# bamboo = pd.read_csv("C:\\Users\\Игорь\\Desktop\\northwind-SQLite3-main\\northwind-SQLite3-main\\docs\\SCV 100 KB.csv")
# print(bamboo.head(5))

# task_8

# csv_path = "C:\\Users\\Игорь\\PycharmProjects\\KNB\\Igor\\data for work\\archive\\age_gender.csv"
#
# bamboo = pd.read_csv(csv_path)
# age = bamboo[bamboo["age"] > 25]
# print(age)

# task_10

bamboo = pd.DataFrame({
     'Name': ["Igor", "Andrey", "Edward", "Tema"],
     'Age': [21, 22, 25, 30],
     'City': ["Prague","London","Paris","Russia"],
})

bamboo["Salary"] = np.random.randint(10000, 100000, size =len(bamboo))

print(bamboo)