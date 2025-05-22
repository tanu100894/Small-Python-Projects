# Read the txt file and write the new member name in the same txt file.

new_member = input("Enter a new member:")

file = open('Files/members.txt', 'r')
members = file.readlines()
file.close()

members.append(new_member + '\n')

file = open('Files/members.txt', 'w')
file.writelines(members)
file.close()