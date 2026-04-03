import keyboard
import os
import sys

from random import randint

traffic_lights = randint(0, 1)

if (traffic_lights == 0):
    traffic_lights = "red"
else:
    traffic_lights = "green"


def change_path_to_module_location():

    true_path = os.path.dirname(os.path.realpath(__file__))

    new_true_path = os.path.join(true_path, '..')

    sys.path.append(true_path + "/../..")

    os.chdir(new_true_path)


    new_true_path = os.path.join(true_path, '..')
    new_true_path = os.path.join(new_true_path, 'Libraries')

    sys.path.append(new_true_path)

    return

change_path_to_module_location()



os.chdir("CONTROL FLOW STRUCTURES (lessons #7 - )")
print("current_dir: ", os.getcwd())
os.chdir("traffic_lights_assets")

import pygame       # imports pygame-ce

# if pygame not ce... throw an exception or a warning.


from adaptive_screensize_utils import *



pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

cars_raw_surface = pygame.image.load("cars.png").convert_alpha()
cars_scaled_surface = pygame.transform.scale(surface = cars_raw_surface, size = (user_screen_width, user_screen_height))



clock = pygame.time.Clock()

pygame.display.set_caption("Traffic Lights :)")




def stop_cars():
    screen.blit(cars_scaled_surface)
    return













# .
# .
# .


# Task: traffic_lights can either be "red" or "green".
# Print a message for cars to stop if the lights are red
# and a message for them to keep going if they are green.



def handle_traffic_lights():


# ---------------------------------------------------------------------------------------------------
# v  Do the exercise HERE!

    if (traffic_lights == "red"):
        stop_cars()




# ---------------------------------------------------------------------------------------------------


    return










while(True):

    keyboard.on_press_key("esc", lambda _: pygame.quit())

    handle_traffic_lights()



    pygame.display.flip()
    clock.tick(60)  # Caps the events loop at a 60fps ceiling