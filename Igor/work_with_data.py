import numpy as np
import pandas as pd
import pandas as pn

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

bamboo = pd.DataFrame({
    'Name': ["Igor", "Andrey", "Edward", "Tema"],
    'Age': [21, 22, 25, 30],
    'City': ["Prague","London","Paris","Russia"]
})

print(bamboo)