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

weather = 0

weather = randint(0, 1)

if (weather == 0):
    weather = "sunny"
else:
    weather = "rainy"




def take_umbrella():
    # load rainy.png
    # load happy face.png ?
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
    print("The weather is rainy today! Don't forget to take an umbrella wherever you go!")
    take_umbrella()




# ---------------------------------------------------------------------------------------------------







match weather:
    case "sunny":
        weather = 0
    case "rainy":
        sample = 1




