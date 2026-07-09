import random
 
r = random.randint(1, 10)
guess = 3
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("You have 3 attempts to guess the number.")

while guess > 0:
    n = int(input("Make a guess: "))

    if n == r:
        print("You got it! The answer was", r)
        break
    else:
        guess -= 1
        if guess > 0:
            print("Incorrect!")
            print("Attempts left:", guess)
        else:
            print("Game Over!")
            print("The correct number was", r)

