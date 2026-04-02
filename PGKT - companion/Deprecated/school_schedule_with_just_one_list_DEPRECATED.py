import tkinter as tk
import keyboard
from PIL import ImageTk, Image
import os

import colour_utils

from math import floor

"""
import sys



true_path = os.path.dirname(os.path.realpath(__file__))

new_true_path = os.path.join(true_path, '..')

# print("new_true_path:", new_true_path)

sys.path.append(true_path + "/..")

os.chdir(new_true_path)

"""

# print(os.curdir)
# print(os.getcwd())

from adaptive_screensize_utils import *



print("user_screen_height:", user_screen_height)


root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())

canvas = tk.Canvas(root, width = user_screen_width, height = user_screen_height)
# canvas.create_text(int_horizontal_position(50), 40, text = "School Subjects 2026", font=("Helvetica", 40)) 

os.chdir(os.path.dirname(os.path.realpath(__file__)))
cur_path = os.getcwd()


# Idea: Vary only hue (fixed saturation and value)
def assign_colours(subjects):
    
    hue = 0
    step = 355 / len(subjects)

    saturation = 83
    value = 77

    colour_list = subjects
    
    colour_dict = {}

    while len(colour_list > 0):
        rgb = colour_utils.hsv_to_rgb(floor(hue), saturation, value)
        colour_dict[colour_list[0]] = rgb
        hue + step

    
    return colour_dict




resized_for_this_screen: tuple = (int_vertical_position(50), int_vertical_position(50))

# Will render its contents on screen in ORDER
renderer = []

# argumentos = [str]
def make_schedule_colours(*materias, **argumentos_clave):

    
    list_of_subjects = []

    for materia in materias:
        if materia != "":
            if materia not in list_of_subjects:
                list_of_subjects.append(materia)
    
    set_of_subjects: set = set(list_of_subjects)

    dict_of_colours: dict = assign_colours(set_of_subjects)

    return dict_of_colours



# ------------------------------------------------------------------------------------


# Makes a school schedule.
schedule = ["P.E", "Art", "Maths", "Maths", "Chemistry",                        # Mondays
                "Literature", "Literature", "Art", "English", "",                    # Tuesdays
                "P.E", "I.T", "Geography", "English", "",                            # Wednesdays
                "Chemistry", "I.T", "Geography", "", "",                             # Thursdays
                "Literature", "Literature", "Geography", "English", "Chemistry"]     # Fridays


# ------------------------------------------------------------------------------------


def render(schedule: list[str], colours: dict[str, (int, int, int)]):

    today = 1
    subjects_today = 1

    # Coordinates for the rectangles with the subjects inside of them.
    x_pos = 20
    y_pos = 20

    for item in schedule:
        # if item ==

        # Modulo offset by one to make the coords work with multiplication (starts the multiplication at 1)
        today_cycle = (today % 5) + 1

        canvas.create_rectangle(int_horizontal_position * 30, vh * 15, vw * 40, vh * 25, fill = "black")
        
        today + 1
        
    
    canvas.pack()

    return


render(schedule, make_schedule_colours)

canvas.pack()

root.mainloop()