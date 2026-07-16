master_password = input("Enter your master password: ")
def add():
    website = input("Enter the website: ")
    user_name = input("Enter the Account name: ")
    password = input("Enter the password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{website} | {user_name} | {password}\n")
    print("Password stored successfully!")

def view():
     with open("passwords.txt", "r") as f:
         for line in f:
          print(line.rstrip())
   
while True:
    mode = input("Choose mode (1: Store new Password, 2: View existing Passwords, q: Quit): ")

    if mode == "1":
        add()
    elif mode == "2":
        view()
  

    elif mode.lower() == "q":
        print("Exiting the password manager. ")
        break

    else:
        print("Invalid mode selected.")