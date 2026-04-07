# Note: Used "day_of_the_week.py" as a template :3
# (copypasted that one here, heh)


import keyboard
import os
import sys

from random import randint

frame_counter = 0           # Times global events
kid_frame_counter = 0       # Times cars' animation loop :3

day_of_the_week = "green"      # Lo inicializo en "green". ¿Por qué? Porque sí :p

def cambiar_dia_de_la_semana():
    global dia_de_la_semana

    dia_de_la_semana_change = randint(0, 1)

    if (dia_de_la_semana_change == 0):
        day_of_the_week = "weekend"
    else:
        day_of_the_week = "weekday"
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
os.chdir("Assets")



import pygame       # imports pygame-ce

# if pygame not ce... throw an exception or a warning.


from adaptive_screensize_utils_b import *






pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# scale_factor = (1920 / user_screen_width, 1080 / user_screen_height)

base_raw_surface = pygame.image.load("base.png").convert_alpha()
base_scaled_surface = pygame.transform.scale(surface = base_raw_surface, size = (user_screen_width, user_screen_height))

true_scale_factor_width = 1920 / user_screen_width
true_scale_factor_height = 1080 / user_screen_height





clock = pygame.time.Clock()

pygame.display.set_caption("Traffic Lights :)")

kid_x_pos = 0
kid_y_pos = int_vertical_position(user_screen_height * (7/10))

cars_x_movement = True


def go_to_school():
    global cars_x_movement

    cars_x_movement = True
    return


def go_to_the_park():
    global cars_x_movement

    cars_x_movement = False

    global kid_frame_counter
    kid_frame_counter -= 1
    return











# .
# .
# .


# Task: day_of_the_week can either be "red" or "green".
# Use the stop_cars() function for cars to stop if the lights are red.



def handle_day_of_the_week():


    # ---------------------------------------------------------------------------------------------------
    # v  Do the exercise HERE!

    if (day_of_the_week == "red"):
        stop_cars()




    # ---------------------------------------------------------------------------------------------------


    return






def Render_Text(what, color, where):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)

    return





running = True


def stop_running():

    global running

    running = False
    return


# loop every 120 frames cuz why not
step_func = (11.9270833333 * vw) / 120


debug_mode = False

while(running == True):



    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard.on_press_key("esc", lambda _: pygame.quit())
    keyboard.on_press_key("esc", lambda _: stop_running())

    screen.blit(base_scaled_surface, (0, 0))

    move_cars()

    handle_day_of_the_week()

    if ((frame_counter % 100) == 0):
        cambiar_las_luces_del_semaforo()

    if ((kid_frame_counter % 120) == 0):
        cars_x_pos        -= step_func * 120
        frame_counter     += 1
        kid_frame_counter += 1

    if cars_x_movement == True:
        screen.blit(cars_scaled_surface, (cars_x_pos + step_func, cars_y_pos))
        cars_x_pos += step_func
    else:
        screen.blit(cars_scaled_surface, (cars_x_pos, cars_y_pos))

    if debug_mode == True:
        pygame.font.init()
        
        Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))    # Show FPS
        Render_Text((str(day_of_the_week)), (255,0,0), (100,0))    # Show FPS
        # print("FPS:", int(clock.get_fps()))
        

    
    screen.blit(post_scaled_surface, (int_horizontal_position(20), int_vertical_position(20)))

    if day_of_the_week == "red":
        screen.blit(red_light_scaled_surface, (int_horizontal_position(20), int_vertical_position(19.7)))
    else:       # day_of_the_week == "green"
        screen.blit(green_light_scaled_surface, (int_horizontal_position(20), int_vertical_position(20.3)))
    
    

    frame_counter     += 1
    kid_frame_counter += 1
    

    pygame.display.flip()
    clock.tick(60)  # Caps the events loop at a 60fps ceiling. Doesn't work at other framerates, for some reason... (oof with delta time)