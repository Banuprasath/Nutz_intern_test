import json


def encrypt(text, key):
    encrypted_text = []
    for char in text:
        encrypted_char = chr(ord(char) + key)
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

def decrypt(text, key):
    decrypted_text = []
    for char in text:
        decrypted_char = chr(ord(char) - key)
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

def signup(username, password, encryption_key):
    encrypted_username = encrypt(username, encryption_key)
    encrypted_password = encrypt(password, encryption_key)
    user_data = {"username": encrypted_username, "password": encrypted_password}
    with open("users.json", "a") as user_file:
        user_file.write(json.dumps(user_data) + '\n')
    print("Account created successfully.")


def load_notes(username):

    try:
        with open(f"{username}_notes.json", "r") as notes_file:
            notes_data = json.load(notes_file)
    except FileNotFoundError:
        notes_data = []
        print("No Notes Found")
    return notes_data



def save_notes(username, notes):
    with open(f"{username}_notes.json", "w") as notes_file:
        json.dump(notes, notes_file)


def check_password(username, password, encryption_key):
    with open("users.json", "r") as user_file:
        for line in user_file:
            user_data = json.loads(line)
            decrypted_username = decrypt(user_data["username"], encryption_key)
            decrypted_password = decrypt(user_data["password"], encryption_key)
            if decrypted_username == username and decrypted_password == password:
                while True:
                    print("-----------------Welcome Back-------------------")
                    print("\n1. View Notes\n2. Add Note\n3. Logout")
                    notes_choice = input("Select an option: ")
                    if notes_choice == "1":
                        user_notes = load_notes(decrypted_username)
                        print("----------------Your Notes:-------------------")
                        for idx, note in enumerate(user_notes, start=1):
                            print(f"{idx}. {note}")
                        print("----------------------------------------------")
                    elif notes_choice == "2":
                        new_note = input("--------------------Enter your note: ------------------------\n")
                        user_notes = load_notes(decrypted_username)
                        user_notes.append(new_note)
                        save_notes(decrypted_username, user_notes)
                        print("Note added successfully.")
                    elif notes_choice == "3":
                        print("------------------Loged out--------------------")
                        break
                    else:
                        print("Invalid choice. Please try again.")

                    return True
    return False



encryption_key = 3

while True:
    print("*****************************NOTES APP**********************************")
    print("\n1. Login\n2. Signup\n3. Exit")
    choice = input("Select an option: ")
    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        if check_password(username, password, encryption_key):
            pass

        else:
            print("Login failed. Invalid credentials.")
    elif choice == "2":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        signup(username, password, encryption_key)
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Please try again.")


