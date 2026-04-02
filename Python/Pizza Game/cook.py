import tkinter as tk
import keyboard
from PIL import ImageTk, Image
import os
import sys



true_path = os.path.dirname(os.path.realpath(__file__))
module_path = os.path.join(true_path, '..')
sys.path.append(true_path + "/../Libraries")


print("Current path:", true_path)
os.chdir(true_path)

from adaptive_screensize_utils import *

root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())


dough_raw_img = Image.open("Ingredients/dough.png")
cheese_raw_img = Image.open("Ingredients/cheese.png")
tomato_slices_raw_img = Image.open("Ingredients/tomato_slices.png")
tomato_sauce_raw_img = Image.open("Ingredients/tomato_sauce.png")
eggs_raw_img = Image.open("Ingredients/eggs.png")
ham_raw_img = Image.open("Ingredients/ham.png")

resized_for_this_screen: tuple = (int_vertical_position(50), int_vertical_position(50))

dough_img = ImageTk.PhotoImage(dough_raw_img.resize(resized_for_this_screen))
cheese_img = ImageTk.PhotoImage(cheese_raw_img.resize(resized_for_this_screen))
tomato_slices_img = ImageTk.PhotoImage(tomato_slices_raw_img.resize(resized_for_this_screen))
tomato_sauce_img = ImageTk.PhotoImage(tomato_sauce_raw_img.resize(resized_for_this_screen))
eggs_img = ImageTk.PhotoImage(eggs_raw_img.resize(resized_for_this_screen))
ham_img = ImageTk.PhotoImage(ham_raw_img.resize(resized_for_this_screen))

canvas = tk.Canvas(root, width = user_screen_width, height = user_screen_height)
print(int_horizontal_position(50))
canvas.create_text(int_horizontal_position(50), 40, text = "My Pizza!", font=("Helvetica", 40)) 



def add_ham():
    canvas.create_image(int_horizontal_position(25), 80, image=ham_img, anchor=tk.NW)
    return

def add_dough():
    canvas.create_image(int_horizontal_position(25), 80, image=dough_img, anchor=tk.NW)
    return

def add_cheese():
    canvas.create_image(int_horizontal_position(25), 80, image=cheese_img, anchor=tk.NW)
    return

def add_tomato_slices():
    canvas.create_image(int_horizontal_position(25), 80, image=tomato_slices_img, anchor=tk.NW)
    return

def add_tomato_sauce():
    canvas.create_image(int_horizontal_position(25), 80, image=tomato_sauce_img, anchor=tk.NW)
    return

def add_eggs():
    canvas.create_image(int_horizontal_position(25), 80, image=eggs_img, anchor=tk.NW)
    return





# ------------------------------------------------------------------------------------

#  v  Solve the exercise here! :)  v










# ------------------------------------------------------------------------------------











canvas.pack()



root.mainloop()