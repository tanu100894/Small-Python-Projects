# Program to check the password is a strong password using dictionary

password = input("Enter the password: ")
result = {}

# Condition to check if the password length is more than 8

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# Condition to check if the password contains at least 1 digit

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

# Condition to check if the password contains at least 1 upper case character

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

# print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
