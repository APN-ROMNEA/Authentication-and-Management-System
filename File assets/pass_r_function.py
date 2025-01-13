import sys
import os
 
# Add the modules folder to sys.path
sys.path.append(os.path.abspath(r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\Code file"))

# Now import the User class from base_register
from passwordrecovery import UserManager

def pass_recovery_function():
    user_manager = UserManager(r"C:\Users\User\OneDrive\CADT SChool\CADT_Year-2\Python\Week-10\G2_T3_Project\Main\database.txt")
    user_manager.password_recovery()