import sys
import os
 

# Add the modules folder to sys.path
sys.path.append(os.path.abspath(r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\File assets"))
from register_function import register_function
from login_function import login_function
from pass_r_function import pass_recovery_function
def main():
    while True:
        print("+_==========================================_+")
        print("||                * * * * *                 ||")
        print("||       A U T H E N T I C A T I O N        ||")
        print("||              S Y S T E M                 ||")
        print("||                  &                       ||")
        print("||           M A N A G E M E N T S          ||")        
        print("||                                          ||")
        print("+_==========================================_+")
        print("\n                   ")
        print("\nPlease choose one of the following options:")
        print("\n 1. Register\n 2. Login\n 3. Password Recovery\n 4. Exit\n")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\n")
            print("======================================================")
            print("|           Welcome To REGISTERATION SYSTEM          |")
            print("======================================================")
            register_function()
            

        elif choice == "2":
            print("\n")
            print("============================================")
            print("|          Welcome To LOGIN SYSTEM         |")
            print("============================================")
            login_function()

        elif choice == "3":
            print("\n")
            print("============================================")
            print("|  Welcome To PASSWORD RECOVERY SYSTEM     |")
            print("============================================")
            
            pass_recovery_function()

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid Choice. Please try again")

if __name__ == "__main__":
    main()
