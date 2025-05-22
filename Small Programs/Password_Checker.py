# Program to check whether password entered is correct otherwise re-enter it again
# until user entered the correct password.

password = input("Enter the Password: ")

while password != "pass123":
    password = input("Enter the Password: ")

print("Password was correct")