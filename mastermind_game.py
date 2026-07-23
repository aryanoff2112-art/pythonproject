import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
COLOR_NAMES = {
    "R": "Red",
    "G": "Green",
    "B": "Blue",
    "Y": "Yellow",
    "W": "White",
    "O": "Orange",
}
ANSI_COLORS = {
    "R": "\033[91m",
    "G": "\033[92m",
    "B": "\033[94m",
    "Y": "\033[93m",
    "W": "\033[97m",
    "O": "\033[38;5;208m",
}
RESET = "\033[0m"

TRIES = 10
CODE_LENGTH = 4

BASE_SCORE = 1000
PENALTY_PER_TRY = 80
HINT_PENALTY = 150

def colorize(color):
    """Wrap a color letter in its ANSI color code for terminal output."""
    return f"{ANSI_COLORS.get(color, '')}{color}{RESET}"

def colorize_code(code):
    return " ".join(colorize(c) for c in code)

def print_color_guide():
    print("\n--- Color Guide ---")
    for letter in COLORS:
        print(f"  {colorize(letter)} = {COLOR_NAMES[letter]}")
    print()

def print_instructions():
    print("\n--- How to Play ---")
    print(f"1. The computer secretly picks a code of {CODE_LENGTH} colors (repeats allowed).")
    print(f"2. You have {TRIES} attempts to guess the exact code.")
    print("3. After each guess, you'll see:")
    print("   - Correct Positions: right color, right spot")
    print("   - Incorrect Positions: right color, wrong spot")
    print("4. Type colors separated by spaces, e.g.: R G B Y")
    print("5. Type 'hint' instead of a guess to reveal one correct color (costs points).")
    print("6. Guess the full code correctly before you run out of tries to win!\n")

def print_main_menu():
    print("=" * 40)
    print("           MASTERMIND")
    print("=" * 40)
    print("1. Play Game")
    print("2. Color Guide")
    print("3. Instructions")
    print("4. Quit")

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    """Returns either a list of guessed colors, or the string 'HINT'."""
    while True:
        raw = input("Guess (or type 'hint'): ").strip().upper()

        if raw == "HINT":
            return "HINT"

        guess = raw.split()

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        invalid = False
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                invalid = True
                break
        if invalid:
            continue

        return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if (
            guess_color != real_color
            and color_counts.get(guess_color, 0) > 0
        ):
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def get_hint(code, revealed_positions):

    available = [i for i in range(CODE_LENGTH) if i not in revealed_positions]
    if not available:
        return None
    pos = random.choice(available)
    revealed_positions.add(pos)
    return pos, code[pos]

def winning_message(attempts, score):
    if attempts == 1:
        print("\n INCREDIBLE! You cracked it in a single guess! Pure genius!")
    elif attempts <= 3:
        print(f"\n Outstanding! You guessed the code in just {attempts} tries!")
    elif attempts <= 6:
        print(f"\n Well done! You cracked the code in {attempts} tries.")
    else:
        print(f"\n Phew! You got it in {attempts} tries — cutting it close!")
    print(f"Final Score: {score}")

def game():
    code = generate_code()
    hints_used = 0
    revealed_positions = set()

    print("Welcome to Mastermind!")
    print(f"Available colors: {' '.join(colorize(c) for c in COLORS)}")
    print(f"Enter {CODE_LENGTH} colors separated by spaces.")
    print("Example: R G B Y")
    print("Type 'hint' at any time for a clue (costs points).\n")

    attempt = 1
    while attempt <= TRIES:
        remaining = TRIES - attempt + 1
        print(f"Attempt {attempt}/{TRIES}  (Remaining after this: {remaining - 1})")

        guess = guess_code()

        if guess == "HINT":
            hint = get_hint(code, revealed_positions)
            if hint is None:
                print("No more hints available — all positions already revealed!\n")
            else:
                pos, color = hint
                hints_used += 1
                print(f"💡 Hint: Position {pos + 1} is {colorize(color)} ({COLOR_NAMES[color]})\n")
            continue  

        correct_pos, incorrect_pos = check_code(guess, code)

        print(f"Your guess:  {colorize_code(guess)}")

        if correct_pos == CODE_LENGTH:
            score = max(0, BASE_SCORE - (attempt - 1) * PENALTY_PER_TRY - hints_used * HINT_PENALTY)
            winning_message(attempt, score)
            return

        print(
            f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}"
        )
        print(f"Attempts remaining: {TRIES - attempt}\n")

        attempt += 1

    print("\n❌ You ran out of tries.")
    print("The code was:", colorize_code(code))
    print("Final Score: 0")

def main():
    while True:
        print_main_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            game()
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again != "y":
                print("Thanks for playing Mastermind! Goodbye.")
                break
        elif choice == "2":
            print_color_guide()
        elif choice == "3":
            print_instructions()
        elif choice == "4":
            print("Thanks for playing Mastermind! Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-4.\n")

if __name__ == "__main__":
    main()