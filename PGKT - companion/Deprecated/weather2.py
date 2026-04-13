import tkinter as tk
import keyboard
from PIL import ImageTk, Image
import os
import sys

from math import floor

from random import randint

import pygame





def change_path_to_module_location():

    true_path = os.path.dirname(os.path.realpath(__file__))

    new_true_path = os.path.join(true_path, '..')

    sys.path.append(true_path + "/../..")

    os.chdir(new_true_path)

    new_true_path = os.path.join(true_path, '..')
    new_true_path = os.path.join(new_true_path, '..')
    new_true_path = os.path.join(new_true_path, 'Libraries')

    sys.path.append(new_true_path)

    # print("LIBRARIES PATH:", str(sys.path))

    return

change_path_to_module_location()


os.chdir("../")
os.chdir("CONTROL FLOW STRUCTURES (lessons #7 - )")
os.chdir("weather")
os.chdir("Assets")

# print("current_dir: (GETCWD)", os.getcwd())

from adaptive_screensize_utils_b import *
# import colour_utils

asset_height = 3000     # The height of the assets. I exported them at 3000px of height, but feel free to export in a different resolution and change this number if needed :3
scale_factor = asset_height / user_screen_height



pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

sunny_raw_surface = pygame.image.load("sunny.png").convert_alpha()
sunny_scaled_surface = pygame.transform.scale(surface = sunny_raw_surface, size = (user_screen_width / scale_factor, user_screen_height))

rainy_raw_surface = pygame.image.load("rainy.png").convert_alpha()
rainy_scaled_surface = pygame.transform.scale(surface = rainy_raw_surface, size = (user_screen_width / scale_factor, user_screen_height))

sad_face_raw_surface = pygame.image.load("sad_face.png").convert_alpha()
sad_face_scaled_surface = pygame.transform.scale(surface = sad_face_raw_surface, size = (user_screen_width / scale_factor, user_screen_height))

umbrella_face_raw_surface = pygame.image.load("umbrella.png").convert_alpha()
umbrella_scaled_surface = pygame.transform.scale(surface = umbrella_face_raw_surface, size = (user_screen_width / scale_factor, user_screen_height))

base_raw_surface = pygame.image.load("base.png").convert_alpha()
base_scaled_surface = pygame.transform.scale(surface = base_raw_surface, size = (user_screen_width / scale_factor, user_screen_height))



frame_counter = 0               # Times global events (in this case, the weather animation loop :3)

weather = "rainy"     # Just initializes the "weather" variable.


def change_weather():

    global weather

    weather = randint(0, 1)

    match weather:
        case 0:
            weather = "sunny"

        case 1:
            weather = "rainy"
    
    return


draw_umbrella = False   # Oh no! If the kids don't solve the exercise... the guy will get wet! D:
draw_sad_face = True    # Oh no! If the kids don't solve the exercise... the guy will get wet! D:

def take_umbrella():

    # loads umbrella.png
    # loads happy_face.png (?



    global draw_umbrella
    draw_umbrella = True

    global draw_sad_face
    draw_sad_face = False       # If the guy takes the umbrella with him, he won't get wet! So now, he's happy :D    

    return




# .
# .
# .


# Task: We will be simulating a weather forecast in this exercise!
# 
# weather can either be "sunny" or "rainy".
# If the weather is rainy, print a message asking the user to
# take an umbrella!


# ---------------------------------------------------------------------------------------------------
# v  Do the exercise HERE!

if (weather == "rainy"):
    take_umbrella()




# ---------------------------------------------------------------------------------------------------






change_weather_speed = 1        # Time it takes to change the weather (in seconds)
fps = 30

change_weather_speed_in_frames = change_weather_speed * fps         # change_weather_speed_in_frames = 30



running = True


def stop_running():

    global running

    running = False
    return


debug_mode = True       # Switches between "debug mode" and "release mode"


clock = pygame.time.Clock()
pygame.display.set_caption("Weather :)")

def Render_Text(what, color, where):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)

    return

while(running == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard.on_press_key("esc", lambda _: pygame.quit())
    keyboard.on_press_key("esc", lambda _: stop_running())





    screen.fill((255, 255, 255))
    # screen.blit(base_scaled_surface, (0, 0))

    if ((frame_counter % change_weather_speed_in_frames) == 0):
        change_weather()
        frame_counter + 1

        


    if weather == "sunny":
        screen.blit(sunny_scaled_surface, (floor(user_screen_width / 2), 0))

    else:       # weather == "rainy"
        screen.blit(rainy_scaled_surface, (floor(user_screen_width / 2), 0))
        screen.blit(base_scaled_surface, (floor(user_screen_width / 2), 0))     # Draw_base()

        if draw_umbrella == True:
            umbrella_centered_rect = umbrella_scaled_surface.get_rect(center = (floor(user_screen_width / 2), floor(user_screen_height / 2)))
            # screen.blit(sad_face_scaled_surface, (floor(user_screen_width / 2), 0), center)
            screen.blit(umbrella_scaled_surface, umbrella_centered_rect)

            # screen.blit(umbrella_scaled_surface, (floor(user_screen_width / 2), 0))
        else:
            sad_face_centered_rect = sad_face_scaled_surface.get_rect(center = (floor(user_screen_width / 2), floor(user_screen_height / 2)))
            # screen.blit(sad_face_scaled_surface, (floor(user_screen_width / 2), 0), center)
            screen.blit(sad_face_scaled_surface, sad_face_centered_rect)
    


    frame_counter += 1    


    if debug_mode == True:
        pygame.font.init()
        
        Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))    # Show FPS
        # print("FPS:", int(clock.get_fps()))

        Render_Text((str(weather)), (255,0,0), (50,0))    # Show weather status (rainy or sunny)
        Render_Text((str(frame_counter)), (255,0,0), (200,0))    # Show weather status (rainy or sunny)
        

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:    # Checking if a key got pressed or not
                
                if event.key == pygame.K_d:     # Checking if key "D" was pressed
                    print("\n")
                    print("WEATHER:", weather)
                    print("FRAME COUNTER:", frame_counter)
                    print("DRAW SAD FACE:", draw_sad_face)

            


    pygame.display.flip()
    clock.tick(fps)          # Caps the events loop at a (30)fps ceiling. Be careful if the framerate is even lower than that... (oof with delta time)