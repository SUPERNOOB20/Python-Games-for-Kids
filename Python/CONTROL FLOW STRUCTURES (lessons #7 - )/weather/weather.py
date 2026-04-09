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

print("current_dir: (GETCWD)", os.getcwd())
# print("current_dir (CURDIR): ", os.curdir)
# print("sys path:", ss)



from adaptive_screensize_utils_b import *
import colour_utils




root = tk.Tk()
root.attributes('-fullscreen', True)
# c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())


# os.chdir(os.path.dirname(os.path.realpath(__file__)))
# cur_path = os.getcwd()

frame_counter = 0               # Times global events
weather_frame_counter = 0       # Times weather animation loop :3

weather = 0     # Just initializes the "weather" variable.

weather = randint(0, 1)

match weather:
    case "sunny":
        weather = 0
    case "rainy":
        weather = 1

draw_sad_face = True    # Oh no! If the kids don't solve the exercise... the guy will get wet! D:

def take_umbrella():
    # load rainy.png
    # load happy_face.png (?

    global draw_sad_face
    draw_sad_face = False
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






change_weather_speed = 2        # Time it takes to change the weather (in seconds)
fps = 30

change_weather_speed_in_frames = change_weather_speed * fps


debug_mode = False

while(running == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard.on_press_key("esc", lambda _: pygame.quit())
    keyboard.on_press_key("esc", lambda _: stop_running())

    screen.fill((255, 255, 255))
    # screen.blit(base_scaled_surface, (0, 0))

    if ((frame_counter % 100) == 0):
        change_weather()
        weather_frame_counter + 1


    if debug_mode == True:
        pygame.font.init()
        
        Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))    # Show FPS
        Render_Text((str(traffic_lights)), (255,0,0), (100,0))    # Show FPS
        # print("FPS:", int(clock.get_fps()))
        

    
    if draw_sad_face == True:
        screen.blit(sad_face_scaled_surface, (0, 0))



    if weather == "sunny":
        screen.blit(sunny_scaled_surface, (0, 0))
    else:       # weather == "rainy"
        screen.blit(rainy_scaled_surface, (0, 0))
    
    

    frame_counter     += 1
    weather_frame_counter += 1
    

    pygame.display.flip()
    clock.tick(fps)          # Caps the events loop at a (30)fps ceiling. Be careful if the framerate is even lower than that... (oof with delta time)