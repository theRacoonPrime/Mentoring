# Variable for number
number = int(input("Enter the number: "))

# If the remainder is 1 after taking the modulus with 2, the number is odd; if there is no remainder, the number is even.

if number % 2 == 1:
    print(f"{number} is odd number")
else:
    print(f"{number} is even number")

    #  Why do you use () in if conditional ?  Pay attention on PEP8