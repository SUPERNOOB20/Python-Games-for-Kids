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



# print("user_screen_height:", user_screen_height)


root = tk.Tk()
root.attributes('-fullscreen', True)
# c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())

canvas = tk.Canvas(root, width = user_screen_width, height = user_screen_height)
canvas.create_text(int_horizontal_position(50), 90, text = "School Subjects 2026", font=("Helvetica", 40)) 

os.chdir(os.path.dirname(os.path.realpath(__file__)))
cur_path = os.getcwd()








# ------------------------------------------------------------------------------------


# Makes a school schedule.
monday_schedule = []
tuesday_schedule = []
wednesday_schedule = []                            
thursday_schedule = []
friday_schedule = []

schedule = [monday_schedule, tuesday_schedule, wednesday_schedule, thursday_schedule, friday_schedule]
# ------------------------------------------------------------------------------------









# Idea: Vary only hue (fixed saturation and value)
def assign_colours(subjects):

    hue = 0
    step = 355 / len(subjects)

    # saturation = 0.83
    # value = 0.77

    saturation = 0.5
    value = 0.9

    colour_list = list(subjects)
    
    colour_dict = {}

    while len(colour_list) > 0:

        # print("Current hsv:", hue, saturation, value)

        rgb = colour_utils.hsv_to_rgb(floor(hue), saturation, value)
        # print("rgb: ", rgb)
        colour_dict[colour_list[0]] = rgb
        hue += step
        colour_list.pop(0)

    
    return colour_dict




resized_for_this_screen: tuple = (int_vertical_position(50), int_vertical_position(50))


# argumentos = [str]
def make_schedule_colours(*weekdays_wrapped, **argumentos_clave):

    list_of_subjects: list = []
    dict_of_colours: dict = []

    for weekdays in weekdays_wrapped:
        for weekday in weekdays:
            for materia in weekday:
                if materia != "":
                    if materia not in list_of_subjects:
                        list_of_subjects.append(materia)
            
    set_of_subjects: set = set(list_of_subjects)

    if len(set_of_subjects) > 0:
        dict_of_colours: dict = assign_colours(set_of_subjects)

    # print("LIST OF SUBJECTS: ", list_of_subjects)

    if len(dict_of_colours) == 0:
        raise Exception("Error: No subjects found in the schedule! \n Did you do the exercise...? \n Ask your teacher if there's anything you don't understand...!")


    return dict_of_colours

# Translates an rgb tuple of int to a tkinter-friendly colour code.
def rgb_colour_tuple_to_hex(rgb):
    
    # print("PLEASE CHECK THIS CAREFULLY: ", str(rgb))
    # print(type(rgb))

    # print("#%02x%02x%02x" % rgb)

    return "#%02x%02x%02x" % rgb 

def render(schedule: list[list[str]], colours: dict[str, (int, int, int)]):

    # Coordinates for the rectangles with the subjects inside of them.
    x_pos = 25
    # y_pos = 30

    # print("COLOUR: ", colours)


    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    current_week_day_index = 0

    for weekday in schedule:        

        y_pos = 20
        canvas.create_text(int_horizontal_position(x_pos + 5), int_vertical_position(y_pos - 2), text = week_days[current_week_day_index], font=("Arial", 18))

        for subject in weekday:
            
            if subject != "":
                # print("current subject: ", subject)
                # print("current tuple: ", str(tuple(colours[subject])))

                """
                current_colour = rgb_colour_tuple_to_hex(tuple(colours[subject]))
                canvas.create_rectangle(int_horizontal_position(x_pos), int_vertical_position(y_pos), int_horizontal_position(x_pos + 10), int_vertical_position(y_pos + 10), fill = current_colour)
                """

                current_colour = rgb_colour_tuple_to_hex(colours[subject])
                canvas.create_rectangle(int_horizontal_position(x_pos), int_vertical_position(y_pos), int_horizontal_position(x_pos + 10), int_vertical_position(y_pos + 5), fill = current_colour)
                canvas.create_text(int_horizontal_position(x_pos + 5), int_vertical_position(y_pos + 2), text = subject, font=("Helvetica", 14)) 


                # print("x_pos: ", x_pos)
                # print("y_pos: ", y_pos)

                canvas.pack()

            y_pos += 5

        x_pos += 10

        # print("\n")
        current_week_day_index += 1        

    
    # Packages ONLY the schedule
    canvas.pack()
    return

"""
try:
    render(schedule, make_schedule_colours(schedule))
except e:
    print("Error: Did you do the exercise...? :p")
    print("Ask the teacher if you need any help!!!")

    print e
"""
    
render(schedule, make_schedule_colours(schedule))


for weekday in schedule:

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    current_week_day_index = 0

    if len(weekday) > 7:
        print("Error: too many subjects in " + week_days[current_week_day_index] + "!")

    current_week_day_index += 1


times = ["08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00"]
for index in range (0, len(times)):
    canvas.create_text(int_horizontal_position(20), int_vertical_position(22 + index * 5), text = (times[index]), font=("Helvetica", 14))


# Should package ONLY the title and whatnot
canvas.pack()
root.mainloop()