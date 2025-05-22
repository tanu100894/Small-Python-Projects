# This program repeatedly prompts the user to enter to-dos, capitalizes and displays each one, and stores them in a list.

user_prompt = "Enter todo: "
todos= []

while True:
    todo = input("Enter todo: ")
    print(todo.capitalize())
    todos.append(todo)
    print(todos)