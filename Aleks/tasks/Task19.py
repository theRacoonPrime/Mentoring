# Два числа
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Квадрат суммы
result1 = (number1 + number2) ** 2

# Сумма квадратов
result2 = (number1 ** 2) + (number2 ** 2)

# Результат
print(f"Квадрат суммы {number1} и {number2} равен {result1}")
print(f"Сумма квадратов {number1} и {number2} равна {result2}")