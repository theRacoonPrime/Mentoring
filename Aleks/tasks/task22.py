# Variables for passwords
pass1 = input("Write your password: ")
pass2 = input("Repeat your password: ")

# Check if passwords have the same length if not, write that they are not the same
if(len(pass1) != len(pass2)):
    print("Password are the not same")
else:
    count = 0 
# Check if every char in passwords are the same if not, write that they are not the same
    while count < len(pass1):

        if(pass1[count] != pass2[count]):
            print("Passwords are the not same")
            break
        if(count == len(pass1) - 1):
            print("Passwords are the same") 
        count += 1