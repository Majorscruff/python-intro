import random
import string
import shelve
import time

def random_password(stringLength=15):
        password = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password) for i in range (stringLength))

time.sleep(2)
print(r"""                      | |      
 _ __   __ _ _ __   __| | __ _ 
| '_ \ / _` | '_ \ / _` |/ _` |
| |_) | (_| | | | | (_| | (_| |
| .__/ \__,_|_| |_|\__,_|\__,_|
| |                            
|_|""")

time.sleep(1)

print("\nWelcome to Panda Password! \n\nLikely the best password generator in this class room...")

time.sleep(1)

while True:
    Password_answer = input("\nWould you like to generate a new password?\nPlease type Yes or No?")
    Panswer_yes = "Yes"
    Panswer_no = "No"
    if Password_answer.casefold() == Panswer_yes.casefold():
        time.sleep(.5)
        print("\nYour panda strength password is...\n","\n",random_password())
    elif Password_answer.casefold() == Panswer_no.casefold():
        time.sleep(1)
        print("\nOk, fine.")
        time.sleep(1)
        print("\nByeeeeeeeeeeee\n")

        print(r"""                      | |      
 _ __   __ _ _ __   __| | __ _ 
| '_ \ / _` | '_ \ / _` |/ _` |
| |_) | (_| | | | | (_| | (_| |
| .__/ \__,_|_| |_|\__,_|\__,_|
| |                            
|_|                    
 """)

        break
    else:
        print ("\nWhoops! I said 'Yes' or 'No'")



'''
    account_answer = input("\nWould you like to save this password?")
    Aanswer_yes = "yes"
    Aanswer_no = "no"
    if Aanswer_yes.casefold() == Aanswer_yes.casefold():
        account_name = input("\nEnter Account name:")
        info [account_name] = random_password ()
        print (info)
'''