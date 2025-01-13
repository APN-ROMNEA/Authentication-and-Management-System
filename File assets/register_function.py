import sys
import os
 
# Add the modules folder to sys.path
sys.path.append(os.path.abspath(r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\Code file"))
from register import UserRegisteration
def register_function():
    user_registeration = UserRegisteration()
    if user_registeration.user_register():
        print("\nRegistration Complete!")
        print("Thank you for joining our system!\n")
    
    print("="*50)
    print("\n")

