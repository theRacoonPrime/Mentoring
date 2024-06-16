# Variable for number
number = int(input("Enter the number: "))

# If the sum of the first and the last numbers is equal to the difference between the second and the third numbers,
# then the answer is YES; if not, then the answer is NO.
if int(str(number)[0]) + int(str(number)[3]) == int(str(number)[1]) - int(str(number)[2]):
    print("YES")
else:
    print("NO")