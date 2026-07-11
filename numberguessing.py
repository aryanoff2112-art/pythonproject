import random

while True:

    print("=" * 40)
    print("      NUMBER GUESSING GAME")
    print("=" * 40)

    print("Welcome to the Number Guessing Game!")

    limit = int(input("Enter the upper limit for the number range (greater than 1 and smaller than 100): "))

    while limit <= 1 or limit >= 100:
        print("Please enter a number greater than 1 and smaller than 100.")
        limit = int(input("Enter the upper limit: "))

    if limit <= 10:
        guess = 3
    elif limit <= 30:
        guess = 5
    elif limit <= 50:
        guess = 7
    else:
        guess = 10

    r = random.randint(1, limit)

    print(f"\nI'm thinking of a number between 1 and {limit}.")
    print(f"You have {guess} attempts.")

    while guess > 0:

        try:
            n = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if n < 1 or n > limit:
            print(f"Please enter a number between 1 and {limit}.")
            continue

        if n == r:
            print(f"\n Congratulations! You got it! The answer was {r}")
            break

        guess -= 1

        if guess > 0:
            if n < r:
                print("Too low!")
            else:
                print("Too high!")

            print("Attempts left:", guess)
        else:
            print("\nGame Over!")
            print("The correct number was", r)

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing! Goodbye! ")
        break