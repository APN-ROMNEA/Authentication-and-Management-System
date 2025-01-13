import os
import sys
import json
import re

sys.path.append(os.path.abspath(r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\File assets"))
from register import UserRegisteration  # Importing the register function from Register.py
from base_register import User
from encryptions import encrypt_data, load_or_generate_key


class UserManager:
    def __init__(self, filename=r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\Main\database.txt"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        users = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    data = json.load(file)
                    for user_data in data:
                        username = user_data["username"]
                        users[username] = user_data
                except json.JSONDecodeError as e:
                    print(f"Error reading the user data: {e}")
        return users

    def is_user_exist(self, identifier):
        for username, data in self.users.items():
            if identifier in (username, data["phone"]):
                return True
        return False

    def set_password(self, identifier):
        attempts = 0
        while attempts < 3:
            new_password = input("Enter a new password: ").strip()
            if self.is_strong_password(new_password):
                confirm_attempts = 0  # Counter for confirm password attempts
                while confirm_attempts < 3:
                    confirm_password = input("Confirm your new password: ").strip()
                    if new_password == confirm_password:
                        for username, data in self.users.items():
                            if identifier in (username, data["phone"]):
                                key = load_or_generate_key()
                                cipher = encrypt_data(key)
                                data["password"] = cipher.encrypt(new_password.encode()).decode()
                                self.save_users()
                                print("Password updated successfully!\n")
                                return
                    else:
                        confirm_attempts += 1
                        print(f"Error: Passwords do not match. Remaining attempts: {3 - confirm_attempts}")
                
                # If confirm password attempts are exhausted
                print("Too many failed confirmation attempts. Returning to the main page.")
                return
            else:
                print("Password is not strong enough. Use a combination of uppercase, lowercase, numbers, and special characters.")
            attempts += 1
            print(f"Remaining attempts: {3 - attempts}")
        
        # If new password attempts are exhausted
        print("Too many failed attempts. Returning to the main page.")

    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[!@#$%^&*()]', password):
            return False
        return True

    def save_users(self):
        with open(self.filename, "w") as file:
            json.dump(list(self.users.values()), file, indent=4)

    def password_recovery(self):
        attempts = 0

        while attempts < 3:
            identifier = input("Enter Username: ").strip()

            if self.is_user_exist(identifier):
                print("User found! You can now reset your password.")
                self.set_password(identifier)
                return
            else:
                print("User not found.")
                choice = input("Would you like to [register], [retype], or [leave]? ").strip().lower()

                if choice == 'leave':
                    print("You have returned to the main page.")
                    return
                elif choice == 'register':
                    user_register_instance = UserRegisteration()
                    user_register_instance.user_register()
                    return
                elif choice == 'retype':
                    attempts += 1
                    print(f"Remaining attempts: {3 - attempts}")
                else:
                    print("Invalid choice. Please enter 'register', 'retype', or 'leave'.")


        print("Too many failed attempts. Returning to the main page.\n")
