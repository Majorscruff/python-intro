import random
import string

print(r"""                      | |      
 _ __   __ _ _ __   __| | __ _ 
| '_ \ / _` | '_ \ / _` |/ _` |
| |_) | (_| | | | | (_| | (_| |
| .__/ \__,_|_| |_|\__,_|\__,_|
| |                            
|_|""")



print ("\nWelcome to Panda Password! \n\nLikely the best password genorator in this class room...")

def random_password(stringLength=15):
        password = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password) for i in range (stringLength))

while True:
    answer = input("\nWould you like to generate a new password? \nPlease type Yes or No?")
    if answer == "Yes":
        print("\nYour super panda strength password is... \n","\n",random_password())
    elif answer == "No":
        break
    else:
        print ("\nWhoops! I said 'Yes' or 'No'")