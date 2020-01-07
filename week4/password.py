import random
import string
import shelve

print(r"""                      | |      
 _ __   __ _ _ __   __| | __ _ 
| '_ \ / _` | '_ \ / _` |/ _` |
| |_) | (_| | | | | (_| | (_| |
| .__/ \__,_|_| |_|\__,_|\__,_|
| |                            
|_|""")

'''I have added the import for shelve as i want to expand on this to save the logins. It's just proving a little hard'''

print ("\nWelcome to Panda Password! \n\nLikely the best password genorator in this class room...")

def random_password(stringLength=15):
        password = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password) for i in range (stringLength))

while True:
    answer = input("\nWould you like to generate a new password? \nPlease type Yes or No?")
    if answer == "Yes":
        print("\nYour super panda strength password is... \n","\n",random_password())
    elif answer == "No":
        print("\n Byeeeeeeeeeeee\n")
        break
    else:
        print ("\nWhoops! I said 'Yes' or 'No'")