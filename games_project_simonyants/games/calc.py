import random

RULES = "What is the result of the expression?"

def get_question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])

    match operation:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2

    question = f"{num1} {operation} {num2}"
    return question, str(correct_answer)
