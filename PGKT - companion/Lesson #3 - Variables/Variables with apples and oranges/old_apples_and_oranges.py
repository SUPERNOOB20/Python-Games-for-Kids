import tkinter as tk
import keyboard
from PIL import ImageTk, Image
import os
import sys
from random import randint

true_path = os.path.dirname(os.path.realpath(__file__))


def change_path_to_module_location():
    """
    true_path = os.path.dirname(os.path.realpath(__file__))
    print("Current path:", true_path)
    os.chdir(true_path)
    os.chdir("..")
    print("Current path:", os.getcwd())
    os.chdir("Libraries")
    print("Current path:", os.getcwd())
    """

    new_true_path = os.path.join(true_path, '..')
    new_true_path = os.path.join(new_true_path, 'Libraries')

    # print("new_true_path:", new_true_path)

    sys.path.append(new_true_path)

    # os.chdir(new_true_path)

    return

change_path_to_module_location()

from adaptive_screensize_utils import *

os.chdir(true_path)

root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())


orange_raw_img = Image.open("orange.png")
apple_raw_img = Image.open("apple.png")

resized_for_this_screen: tuple = (int_vertical_position(10), int_vertical_position(10))

orange_img = ImageTk.PhotoImage(orange_raw_img.resize(resized_for_this_screen))
apple_img = ImageTk.PhotoImage(apple_raw_img.resize(resized_for_this_screen))




canvas = tk.Canvas(root, width = user_screen_width, height = user_screen_height)
canvas.create_text(int_horizontal_position(50), 40, text = "My Variables!", font=("Helvetica", 30)) 

def random_horizontal_location():
    return randint(int_horizontal_position(30), int_horizontal_position(70))

def random_vertical_location():
    return randint(int_vertical_position(10), int_vertical_position(40))


def add_oranges(amount):
    if amount > 50:
        amount = 50
    try:
        while (amount > 0):
            canvas.create_image(random_horizontal_location(), random_vertical_location(), image=orange_img, anchor=tk.NW)
            amount = amount - 1
    except:
        print("ERROR: Ask your teacher!")
    return

def add_apples(amount):
    if amount > 50:
        amount = 50
    try:
        while (amount > 0):
            canvas.create_image(random_horizontal_location(), random_vertical_location(), image=apple_img, anchor=tk.NW)
            amount = amount - 1
    except:
        print("ERROR: Ask your teacher!")
    return

# add_oranges()
# add_apples()






# ------------------------------------------------------------------------------------

#  v  Solve the exercise here! :)  v


apples = 5
oranges = 1

apples = apples - 2

add_apples(apples)          # Draws on screen the given amount of apples
add_oranges(oranges)        # Draws on screen the given amount of oranges



# ------------------------------------------------------------------------------------









canvas.pack()



root.mainloop()