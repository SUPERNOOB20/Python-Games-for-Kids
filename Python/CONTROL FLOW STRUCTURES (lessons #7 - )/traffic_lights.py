import keyboard
import os
import sys

from random import randint

traffic_lights = 0      # Lo inicializo en 0. ¿Por qué? Porque sí :p

def cambiar_las_luces_del_semaforo():

    traffic_lights = randint(0, 1)

    if (traffic_lights == 0):
        traffic_lights = "red"
    else:
        traffic_lights = "green"
    return





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


from adaptive_screensize_utils_b import *



pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

cars_raw_size = (2332, 31)                                          # <--- CONSTANT
cars_proportion = cars_raw_size[0] / cars_raw_size[1]
cars_inverse_proportion = 1 / cars_proportion

scale_factor = cars_raw_size[0] / 1920

cars_transformed_width = user_screen_width * scale_factor
cars_transformed_height = cars_raw_size[1] / scale_factor

"""
# Scales the size of the "cars" image to adapt to the user's screen resolution (pain).
cars_transformed_width = cars_size[0] / user_screen_width
cars_transformed_height = (cars_transformed_width * 31) / cars_size[0]

print("CAR DIMENSIONS: ", cars_transformed_width, cars_transformed_height)
print("(different) CAR DIMENSIONS: ", user_screen_width / cars_transformed_width, user_screen_height * cars_transformed_height)


cars_raw_surface = pygame.image.load("cars.png").convert_alpha()
cars_scaled_surface = pygame.transform.scale(surface = cars_raw_surface, size = (user_screen_width / cars_transformed_width, user_screen_height * cars_transformed_height))
"""

print("CAR DIMENSIONS: ", cars_transformed_width, cars_transformed_height)


cars_raw_surface = pygame.image.load("cars.png").convert_alpha()
cars_scaled_surface = pygame.transform.scale(surface = cars_raw_surface, size = (cars_transformed_width, cars_transformed_height))



clock = pygame.time.Clock()

pygame.display.set_caption("Traffic Lights :)")



cars_x_pos = 0
cars_y_pos = int_vertical_position(70)

cars_x_movement = True


def move_cars():
    global cars_x_movement

    cars_x_movement = True
    return


def stop_cars():
    global cars_x_movement

    cars_x_movement = False
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








running = True


def stop_running():

    global running

    running = False
    return


# loop every 120 frames cuz why not
step_func = (11.9270833333 * vw) / 120



while(running == True):

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # keyboard.on_press_key("esc", lambda _: pygame.quit())
    keyboard.on_press_key("esc", lambda _: stop_running())

    move_cars()

    handle_traffic_lights()

    cambiar_las_luces_del_semaforo()

    # print("is car moving: ", cars_x_movement)

    # global cars_x_pos
    # global cars_y_pos
    # global cars_x_movement
    if cars_x_movement == True:
        screen.blit(cars_scaled_surface, (cars_x_pos + step_func, cars_y_pos))
        cars_x_pos += step_func
    else:
        screen.blit(cars_scaled_surface, (cars_x_pos, cars_y_pos))
    
    # print("stuff: ", cars_x_pos, cars_y_pos, cars_x_movement)

    pygame.display.flip()
    clock.tick(60)  # Caps the events loop at a 60fps ceiling