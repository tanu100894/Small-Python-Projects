# Basic ChatBot with chat history storing feature

import datetime

print("Hi! I'm the ChatBot. Type 'bye' to exit.")
conversation_log = []

while True:
    user_input = input("You: ").strip().lower()
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    # Log user input
    conversation_log.append(f"{timestamp} You: {user_input}")

    if user_input in ["hello", "hi", "hey"]:
        response = "Hello there!"
    elif user_input in ["how are you", "how are you doing"]:
        response = "I'm just code, but thanks for asking!"
    elif user_input in ["what's your name", "who are you"]:
        response = "I'm a simple Python ChatBot."
    elif "help" in user_input:
        response = "Try saying 'hello', 'how are you', or 'bye'."
    elif user_input == "bye":
        response = "Goodbye!"
        print(f"ChatBot: {response}")
        conversation_log.append(f"{timestamp} ChatBot: {response}")  # Log final response
        break
    else:
        response = "Sorry, I don't understand that."

    print(f"ChatBot: {response}")
    conversation_log.append(f"{timestamp} ChatBot: {response}")  # Log response

# Save the file
with open("chat_log.txt", 'a') as file:
    file.write("\n--- New Chat Session ---\n")
    for line in conversation_log:
        file.write(line + "\n")

print("Chat log appended to 'chat_log.txt'")