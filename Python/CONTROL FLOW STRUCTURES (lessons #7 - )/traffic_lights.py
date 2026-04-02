from random import randint

traffic_lights = randint(0, 1)

if (traffic_lights == 0):
    traffic_lights = "red"
else:
    traffic_lights = "green"


# .
# .
# .


# Task: traffic_lights can either be "red" or "green".
# Print a message for cars to stop if the lights are red
# and a message for them to keep going if they are green.


# ---------------------------------------------------------------------------------------------------
# v  Do the exercise HERE!

if (traffic_lights == "red"):
    print("Stop your car! The traffic lights are RED")
else:       # traffic_lights == green
    print("Keep going! The traffic lights are GREEN")