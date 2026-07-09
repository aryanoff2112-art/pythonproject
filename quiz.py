
print("welcome to my computer quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1      
else:
    print("Incorrect!")    

answer = input("Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which animal is known as the 'King of the Jungle'? ")
if answer.lower() == "lion":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which is the national bird of India? ")
if answer.lower() == "peacock":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the largest ocean on Earth? ")
if answer.lower() == "pacific ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which language is primarily used to create web pages? ")
if answer.lower() == "html":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which festival is known as the Festival of Lights in India? ")
if answer.lower() == "diwali":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which gas do plants absorb from the atmosphere? ")
if answer.lower() == "carbon dioxide":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")    
print("You got " + str((score / 10) * 100) + "%.")
print("Thanks for playing!")