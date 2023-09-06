import json
import base64



def signup(username, password):

    user_data = {"username": username, "password": password}


    with open("users.json", "a") as user_file:
        user_file.write(json.dumps(user_data) + '\n')
    print("Account created successfully.")




def check_password(username, password):
    with open("users.json", "r") as user_file:
        for line in user_file:
            user_data = json.loads(line)
            #print(user_data)
            if user_data["username"] == username and user_data["password"] == password:
                print("-----------------Welcom Back-------------------")
                return True
    return False



def load_notes(username):
    try:
        with open(f"{username}_notes.json", "r") as notes_file:
            notes_data = json.load(notes_file)
    except FileNotFoundError:
        notes_data = []
    return notes_data



def save_notes(username, notes):
    with open(f"{username}_notes.json", "w") as notes_file:
        json.dump(notes, notes_file)

def login():
    username = input("Username: ")
    password = input("Password: ")
    if check_password(username, password):
        print("Logined successfully.")
        return username
    else:
        print("Login failed. Invalid credentials.")
        return None



def signup_prompt():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    signup(username, password)


while True:
    print("\n1. Login\n2. Signup\n3. Exit")
    choice = input("Select an option: ")
    if choice == "1":
        logged_in_user = login()
        if logged_in_user:

            while True:
                print("\n1. View Notes\n2. Add Note\n3. Logout")
                notes_choice = input("Select an option: ")
                if notes_choice == "1":
                    user_notes = load_notes(logged_in_user)
                    print("----------------Your Notes:-------------------")
                    for idx, note in enumerate(user_notes, start=1):
                        print(f"{idx}. {note}")
                elif notes_choice == "2":
                    new_note = input("--------------------Enter your note: ------------------------\n")
                    user_notes = load_notes(logged_in_user)
                    user_notes.append(new_note)
                    save_notes(logged_in_user, user_notes)
                    print("Note added successfully.")
                elif notes_choice == "3":
                    print("------------------Loged out--------------------")
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == "2":
        signup_prompt()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Please try again.")
