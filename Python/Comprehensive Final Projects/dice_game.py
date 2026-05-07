from random import randint
import time

# Throws the dice.
dice = randint(2, 6)

print("Welcome to the Dice Game!")
print("If you get 1, you lose!")
print("\n")

score = 0

while (dice != 1):
    print("Throwing the dice...")
    time.sleep(1.5)
    dice = randint(1, 6)
    print("You got a " + str(dice))
    if dice != 1:
        score = score + dice
    else:
        print("Game Over :c")

print("Final score: " + str(score))



