import random
import string

def password_generator(min_length, use_uppercase=True, use_digits=True, use_special_chars=True):
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
  
    characters = letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += digits
    if use_special_chars:
        characters += special_chars

    password = ''.join(random.choice(characters) for _ in range(min_length))
    meets_criteria = False  
    has_uppercase = False
    has_number = False
    has_special_char = False

    while not meets_criteria or len(password) < min_length:
    