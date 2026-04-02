import tkinter as tk
import keyboard
from PIL import ImageTk, Image
import os

from adaptive_screensize_utils import *

true_path = os.path.dirname(os.path.realpath(__file__))
print("Current path:", true_path)
os.chdir(true_path)

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

dough_img = ImageTk.PhotoImage(dough_raw_img.resize((90 * int_vh, 90 * int_vh)))
cheese_img = ImageTk.PhotoImage(cheese_raw_img.resize((90 * int_vh, 90 * int_vh)))
tomato_slices_img = ImageTk.PhotoImage(tomato_slices_raw_img.resize((90 * int_vh, 90 * int_vh)))
tomato_sauce_img = ImageTk.PhotoImage(tomato_sauce_raw_img.resize((90 * int_vh, 90 * int_vh)))
eggs_img = ImageTk.PhotoImage(eggs_raw_img.resize((90 * int_vh, 90 * int_vh)))
ham_img = ImageTk.PhotoImage(ham_raw_img.resize((90 * int_vh, 90 * int_vh)))

canvas = tk.Canvas(root, width = 1050, height = 700)
canvas.create_text(600, 20, text = "My Pizza!") 

canvas.create_image(200, 80, image=dough_img, anchor=tk.NW)
canvas.create_image(200, 80, image=cheese_img, anchor=tk.NW)
canvas.create_image(200, 80, image=tomato_sauce_img, anchor=tk.NW)
canvas.create_image(200, 80, image=ham_img, anchor=tk.NW)
canvas.create_image(200, 80, image=tomato_slices_img, anchor=tk.NW)
canvas.create_image(200, 80, image=eggs_img, anchor=tk.NW)



canvas.pack()


root.mainloop()