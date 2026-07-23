import random
print("=" * 40)
print("     ROCK PAPER SCISSORS")
print("=" * 40)

user_score = 0
computer_score = 0  

options = ["rock", "paper", "scissors"]

while True: 

    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if user_choice == "quit":

        print("Thanks for playing!")
        break
    
    if user_choice not in options:

        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(options)
    print("Computer chose: " + computer_choice)
    
    if user_choice == computer_choice:

        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors"):

        print("You win!")
        user_score += 1

    elif(user_choice == "paper" and computer_choice == "rock"):

        print("You win!")
        user_score += 1
    elif(user_choice == "scissors" and computer_choice == "paper"):
         
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Final Score - You: " + str(user_score) + ", Computer: " + str(computer_score))