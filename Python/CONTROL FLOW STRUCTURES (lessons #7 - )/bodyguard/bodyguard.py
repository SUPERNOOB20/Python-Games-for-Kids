from random import randint


possible_names = ["Pedro", "Peter", "Frederick", "Ashley", "Ann", "Alan", "Bob", "Joshua", "Elizabeth", "Sam", "Daniel", "David", "Walter", "Jesse"]
possible_surnames = ["García", "Smith", "González", "Brown", "White", "Wilson", "Herrera", "Cook", "Carter", "Jones", "Harris", "Parker"]

random_name    = randint(0, len(possible_names) - 1)
random_surname = randint(0, len(possible_surnames) - 1)

name    = possible_names[random_name]
surname = possible_surnames[random_surname]





age = -1

# Ensures a 50-50 between minors and adults.
match randint(0, 1):
    case 0:
        age = randint(12, 18)
    case 1:
        age = randint(18, 40)

        
age_txt = str(age)      # Text format for printing.

if (age >= 18):
    age_txt = f"\033[92m{age_txt}\033[00m"
else:
    age_txt = f"\033[91m{age_txt}\033[00m"


attendee_message = "\033[96m Hi! \033[00m"

attendee_message1 = f"\033[96m{name} {surname}\033[00m: "
attendee_message2temp = f"Hi! I'm {age_txt} years old. May I come in?"
attendee_message2 = f'"{attendee_message2temp}"'
attendee_message3 = f"{attendee_message1}{attendee_message2}"

for i in range(0, 4):
    print("\n")

print(attendee_message3)

enter = -1

def come_in():
    global enter

    enter = 1
    return

def do_not_come_in():
    global enter

    enter = 0
    return








# ---------------------------------------------------------------------------------------------------

# Exercise: Bodyguard!

# TASK: You are a bodyguard at a disco's entrance.
# age is a variable that stores the age of the next person in line.

# Program a bodyguard that will execute do_not_come_in() if age is less than 18,
# and come_in() if age is equal to or over 18.


# vv  Solve the exercise HERE  vv



if (age < 18):
    do_not_come_in()
else:
    come_in()






# ---------------------------------------------------------------------------------------------------






# print("\n")



message3 = ""

if enter == 1:
    message = '\033[92mCome in.\033[00m'
    message3 = f'"{message}"'

elif enter == 0:
    message = "\033[91mDon't come in.\033[00m"
    message3 = f'"{message}"'

else:   # enter == -1
    message3 = "\033[97m...\033[00m"






print("Bodyguard: " + message3)

for i in range(0, 3):
    print("\n")