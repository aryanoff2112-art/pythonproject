import random
import time
from colorama import Fore, Style, init


init(autoreset=True)


operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: round(a / b, 2)
}

print("=" * 40)
print("            MATH QUIZ GAME")
print("=" * 40)

print("\nChoose Difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")

while True:
    difficulty = input("Enter your choice (1-4): ")

    if difficulty == "1":
        min_number = 1
        max_number = 20
        break
    elif difficulty == "2":
        min_number = 21
        max_number = 50
        break
    elif difficulty == "3":
        min_number = 50
        max_number = 100
        break
    elif difficulty == "4":
        min_number = 100
        max_number = 200
        break
    elif difficulty.lower() == "exit":
        print(Fore.CYAN + "Exiting the game. Goodbye!")
        exit()
    else:
        print(Fore.RED + "Invalid choice! Please enter 1, 2, 3 or 4.")

while True:
    try:
        total_questions = int(input("\nEnter total number of questions: "))
        if total_questions > 0:
            break
        else:
            print(Fore.RED + "Number of questions must be greater than 0.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")

def generate_question():
    operation = random.choice(list(operations.keys()))

    if operation == "/":
        num2 = random.randint(1, max_number)
        answer = random.randint(min_number, max_number)
        num1 = answer * num2
        expression = f"{num1} / {num2}"
        return expression, answer

    num1 = random.randint(min_number, max_number)
    num2 = random.randint(min_number, max_number)

    expression = f"{num1} {operation} {num2}"
    answer = operations[operation](num1, num2)

    return expression, answer

score = 0
wrong = 0

quiz_start = time.time()

print("\n" + "=" * 40)
print("              QUIZ STARTS")
print("=" * 40)

for i in range(total_questions):

    print("\n" + "-" * 40)
    print(f"Question {i+1} of {total_questions}")
    print("-" * 40)

    question, correct_answer = generate_question()

    question_start = time.time()

    user_answer = input(f"What is {question}? ")

    question_end = time.time()

    try:
        user_answer = float(user_answer)
        if abs(user_answer - correct_answer) < 0.01:
            print(Fore.GREEN + " Correct!")
            score += 1
        else:
            print(Fore.RED + " Incorrect!")
            print(f"The correct answer is {correct_answer}")
            wrong += 1

    except ValueError:
        print(Fore.RED + "Invalid Input!")
        print(f"The correct answer is {correct_answer}")
        wrong += 1

    print(Fore.CYAN + f"Time taken: {question_end-question_start:.2f} seconds")


quiz_end = time.time()

percentage = (score / total_questions) * 100
total_time = quiz_end - quiz_start

print("\n" + "=" * 45)
print("             QUIZ SUMMARY")
print("=" * 45)

print(f"Questions      : {total_questions}")
print(Fore.GREEN + f"Correct        : {score}")
print(Fore.RED + f"Incorrect      : {wrong}")
print(Style.RESET_ALL + f"Percentage     : {percentage:.2f}%")
print(f"Total Time     : {total_time:.2f} seconds")

print("\nPerformance:")

if percentage == 100:
    print(Fore.GREEN + " Perfect Score! Outstanding!")
elif percentage >= 80:
    print(Fore.GREEN + " Excellent Work!")
elif percentage >= 60:
    print(Fore.YELLOW + " Good Job!")
elif percentage >= 40:
    print(Fore.YELLOW + " Keep Practicing!")
else:
    print(Fore.RED + " Better Luck Next Time!")

print("=" * 45)

while True:
    choice = input("\nDo you want to play again? (Y/N): ").lower()

    if choice == "y":
        print("\nRestart the program to play again.")
        break
    elif choice == "n":
        print(Fore.CYAN + "Thank you for playing!")
        break
    else:
        print(Fore.RED + "Please enter Y or N.")