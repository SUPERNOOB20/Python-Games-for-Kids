import keyboard
import os
import sys

from random import randint

frame_counter = 0           # Times global events
car_frame_counter = 0       # Times cars' animation loop :3

traffic_lights = "green"      # Lo inicializo en "green". ¿Por qué? Porque sí :p

def cambiar_las_luces_del_semaforo():
    global traffic_lights

    traffic_lights_change = randint(0, 1)

    if (traffic_lights_change == 0):
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
import pygame_utils





pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

cars_raw_size = (2332, 31)                                          # <--- CONSTANT
cars_proportion = cars_raw_size[0] / cars_raw_size[1]
cars_inverse_proportion = 1 / cars_proportion

scale_factor = cars_raw_size[0] / 1920
car_scale_factor = 3
animation_duration = 120

cars_transformed_width = user_screen_width * scale_factor
cars_transformed_height = cars_raw_size[1] / scale_factor

true_scale_factor_width = 1920 / user_screen_width
true_scale_factor_height = 1080 / user_screen_height

width = user_screen_width / true_scale_factor_width
height = user_screen_height / true_scale_factor_height

images: dict = pygame_utils.creates_images({"cars_scaled_surface": ["cars.png", cars_transformed_width * car_scale_factor, cars_transformed_height * car_scale_factor],
                                            "base_scaled_surface": ["base.png", user_screen_width, user_screen_height],
                                            "red_light_scaled_surface": ["red_light.png", width, height],
                                            "green_light_scaled_surface": ["green_light.png", width, height],
                                            "post_scaled_surface": ["post.png", width, height],
                                            "background_scaled_surface": ["background.png", user_screen_width, user_screen_height]})

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

    global car_frame_counter
    car_frame_counter -= 1
    return











# .
# .
# .


# Task: traffic_lights can either be "red" or "green".
# Use the stop_cars() function for cars to stop if the lights are red.



def handle_traffic_lights():


    # ---------------------------------------------------------------------------------------------------
    # v  Do the exercise HERE!

    
    







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


# loop every "animation_duration" amount of frames
step_func = (11.9270833333 * vw) * car_scale_factor / animation_duration


debug_mode = False

while(running == True):

    screen.fill((255, 255, 255))

    screen.blit(images["background_scaled_surface"], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard.on_press_key("esc", lambda _: pygame.quit())
    keyboard.on_press_key("esc", lambda _: stop_running())

    screen.blit(images["base_scaled_surface"])

    move_cars()

    handle_traffic_lights()

    if ((frame_counter % 100) == 0):
        cambiar_las_luces_del_semaforo()

    if ((car_frame_counter % animation_duration) == 0):
        cars_x_pos        -= step_func * animation_duration
        frame_counter     += 1
        car_frame_counter += 1

    if cars_x_movement == True:
        screen.blit(images["cars_scaled_surface"], (cars_x_pos + step_func, cars_y_pos))
        cars_x_pos += step_func
    else:
        screen.blit(images["cars_scaled_surface"], (cars_x_pos, cars_y_pos))

    if debug_mode == True:
        pygame.font.init()
        
        Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))    # Show FPS
        Render_Text((str(traffic_lights)), (255,0,0), (100,0))    # Show FPS
        # print("FPS:", int(clock.get_fps()))
        

    
    screen.blit(images["post_scaled_surface"], (int_horizontal_position(20), int_vertical_position(20)))

    if traffic_lights == "red":
        screen.blit(images["red_light_scaled_surface"], (int_horizontal_position(20), int_vertical_position(19.7)))
    else:       # traffic_lights == "green"
        screen.blit(images["green_light_scaled_surface"], (int_horizontal_position(20), int_vertical_position(20.3)))
    
    

    frame_counter     += 1
    car_frame_counter += 1
    

    pygame.display.flip()
    clock.tick(60)  # Caps the events loop at a 60fps ceiling. Doesn't work at other framerates, for some reason... (oof with delta time)