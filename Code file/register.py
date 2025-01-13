import sys
import os
import json
# Add the modules folder to sys.path
sys.path.append(os.path.abspath(r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\File assets"))

# Now import the User class from base_register
from base_register import User
from encryptions import encrypt_data, load_or_generate_key 

#Define about attempts to use in method
Max_Attempts = 3
Attempt = 0
 #Child class that inherited from base class(User)
class UserRegisteration(User):
    def __init__(self):
        super().__init__()
        self.user_date = {}

    #Method for user register
    def user_register(self):
        Max_Attempts = 3
        Attempt = 0

        print("\nPlease follow the instructions to register a new account.\n")

        #Condition for input Firstname and Lastname 
        while True:
            self.firstname = input("First name: ").strip()
            if len(self.firstname) < 2:
                print("First name must have at least 2 characters!!!")
                Attempt += 1
                print(f"Attempts remaining: {Max_Attempts - Attempt}")
                if Attempt >= Max_Attempts:
                    print("Too many attempts for first name. Registration failed.")
                    return False  # Exit if max attempts are reached
                continue  # Continue to prompt for first name again
            else:
                # Reset attempt for first name
                Attempt = 0
                break  # Exit if valid first name is entered

        # Last name input with attempts
        while True:
            self.lastname = input("Last name: ").strip()
            if len(self.lastname) < 2:
                print("Last name must have at least 2 characters!!!")
                Attempt += 1
                print(f"Attempts remaining: {Max_Attempts - Attempt}")
                if Attempt >= Max_Attempts:
                    print("Too many attempts for last name. Registration failed.")
                    return False  # Exit if max attempts are reached
                continue  # Continue to prompt for last name again
            else:
                # Reset attempt for last name
                Attempt = 0
                break  # Exit if valid last name is entered



        #input Username with attempt
        while Attempt < Max_Attempts:
            self.username = input("Username: ").strip()
            if self.check_duplicate_username(self.username):
                Attempt += 1
                print("Username already taken, please choose a different one.")
                print(f"Attempts remaining: {Max_Attempts - Attempt}")
            else:
                print("Username accepted!")
                break
        if Attempt >= Max_Attempts:
                print("\nToo Many Attempts. ")
                return False


        #Reset attempt from username input
        Attempt = 0
        #Password set up and check the condition

        #Input password with attmepts
        while True:
            password = input("Enter your password: ").strip()
            #Check password strenght
            strength = self.Check_Password_strength(password)
            print(f"Password strength: {strength}")

            if strength == "Weak":
                print("Password is not strong enough. Use a combination of uppercase, lowercase, numbers, and special characters.")
                continue

            elif strength == "Moderate":
                print("Password is not strong enough. Use a combination of uppercase, lowercase, numbers, and special characters.")
                continue
            #input password for confirm match or not
            while Attempt < Max_Attempts:
                confirm_password = input("Confirm your password: ").strip()
                if password != confirm_password:
                    Attempt += 1
                    print("Error: Password does not match. Please try again.")
                    print(f"Attempts remaining: {Max_Attempts - Attempt}")
                    if Attempt >= Max_Attempts:
                        print("Too many attempts. Registration Failed.")
                        return
                else:
                    self.set_password(password)
                    print("Password set successfully!")
                    break
            if password == confirm_password:
                break
        
        #Input phone number 8 or 9 digit 
        while True:
            phone = input("Phone number: +855 ").strip()
            hone = phone.replace(" ", "")
            if self.check_phone_number(phone):
                self.phone = "+855 " + phone
                break
            print("Error: Invalid phone number. Please enter 8–9 digits after +855.")

        #Save all the user input to Database.txt file
        self.save_user_data()
        print("Registered Successfully!")

    #Method for checking name duplicate or not
    def check_duplicate_username(self, username):
        try:
            script_directory = os.path.dirname(os.path.abspath(__file__)) # ensure the script always operates relative to its own location
            os.chdir(script_directory)
            file_name = r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\Main\database.txt"
            if os.path.exists(file_name):
                with open(file_name, 'r') as file:
                    try:
                        data = json.load(file)  # Load existing JSON data
                    except json.JSONDecodeError:
                        data = []  # If the file is empty or corrupted, initialize an empty list

            # Check if username already exists in the loaded data
                for existing_user in data:
                    if existing_user['username'] == username:  # Case-insensitive comparison
                        return True  # Username found, duplicate exists
        
            return False  # No duplicate found
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error checking duplicates: {e}")
            return False
    
    #Method for checking password strength or not
    def Check_Password_strength(self, password):
        #initailized
        uppercase = any(char.isupper() for char in password)
        lowercase = any(char.islower() for char in password)
        digit = any(char.isdigit() for char in password)
        special_char = any(char in "!@#$%^&*()" for char in password)

        # Classify the password
        if len(password) >= 8 and uppercase and lowercase and digit and special_char:
            return "Strong"
        elif len(password) >= 8 and ((uppercase and lowercase and digit) or special_char):
            return "Moderate"
        else:
            return "Weak"

    #Method for checking phone number 
    def check_phone_number(self, phone_number):
        phone_number = phone_number.replace(" ", "")
        return phone_number.isdigit() and 8 <= len(phone_number) <= 9
    
    #Method for save user to data file
    def save_user_data(self):

        #Use for remove all the space and phone number store like '+855 11123456'
        formatted_phone = self.phone[4:].replace(" ", "")
        Phone = "+855 " + formatted_phone
        key = load_or_generate_key()
        cipher = encrypt_data(key)
        
        #Format store in file and use it with json library
        user_data = {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'phone': Phone,
            'password': cipher.encrypt(self.get_password().encode()).decode()
        }

        try:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            os.chdir(script_directory)
            file_name = r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\Main\database.txt"
            
            if os.path.exists(file_name):
                with open(file_name, "r") as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []  # If file exists but is empty or corrupted, start with an empty list
            else:
                    data = []

                # Append new user data to the list
            data.append(user_data)

                # Save the updated data back to the file
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
                print(f"User data saved to 'database.txt'")

        except OSError as e:
                print(f"Error saving user data: {e}")
