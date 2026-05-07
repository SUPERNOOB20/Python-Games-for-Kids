# age = input("How old are you?\n")

print("How old are you?")
age = input()


# age restriction system
# British Airways Policy: If you want to board an airplane alone, you must be over 16 years old.
if (int(age) < 16):
     print("You can't go alone!")
     print("Call your parents!")
else:
     print("You can go. Have a nice trip :3")