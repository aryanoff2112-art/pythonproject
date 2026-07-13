import random
import string

print("=" * 40)
print("          PASSWORD GENERATOR")
print("=" * 40)

def password_generator(min_length, max_length, use_uppercase=True, use_digits=True, use_special_chars=True):
    
    letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
  
    characters = letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += digits
    if use_special_chars:
        characters += special_chars

    password = ""
    meets_criteria = False  
    has_uppercase = False
    has_number = False
    has_special_char = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in string.ascii_uppercase:
            has_uppercase = True
        elif new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special_char = True

        meets_criteria = True
        if use_uppercase :
            meets_criteria = has_uppercase
        if use_digits :
            meets_criteria = meets_criteria and has_number
        if use_special_chars:
            meets_criteria = meets_criteria and has_special_char
        if use_special_chars and not has_special_char:
            meets_criteria = False
    
    return password
while True:
    min_length = int(input("Enter the minimum length of the password: "))
    max_length = int(input("Enter the maximum length of the password: "))
    while max_length < min_length:
        print("Maximum length must be greater than or equal to minimum length.")
        max_length = int(input("Enter the maximum length of the password: "))
    use_special_chars = input("Do you want to include special characters? (yes/no): ").lower() == "yes"
    use_uppercase = input("Do you want to include uppercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Do you want to include numbers? (yes/no): ").lower() == "yes"



    password = password_generator(min_length=min_length,max_length=max_length, use_uppercase=use_uppercase, use_digits=use_digits, use_special_chars=use_special_chars)
    print("Generated Password:", password)
    again = input("\nDo you want to generate another password? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using the Password Generator!")
        break