# This program sorts a list of names alphabetically and prints them with numbering and capitalized formatting.

waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    print(f"{index + 1}.{item.capitalize()}")