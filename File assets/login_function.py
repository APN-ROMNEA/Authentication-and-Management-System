import sys
import os
 

# Add the modules folder to sys.path
sys.path.append(os.path.abspath(r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\Code file"))

# Now import the User class from base_register
from login import Login
def login_function():
    user_login = Login()
    user_login.login()
    
    print("="*50)
    print("\n")