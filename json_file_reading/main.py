import json

with open("questions.json", 'r') as file:
    content = file.read()  #content type is str

data = json.loads(content)  #Type of "data" variable is list

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{(index + 1)}. {alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = (f"{result} for question {index + 1}. Your answer: {question['user_choice']}, "
               f"Correct answer: {question['correct_answer']}")
    print(message)


print('Your Score', score, "/", len(data))
