import tkinter as tk
import keyboard
from PIL import ImageTk, Image
import os

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
canvas.create_text(int_horizontal_position(50), 40, text = "My Pizza!", font=("Helvetica", 40)) 

os.chdir(os.path.dirname(os.path.realpath(__file__)))
cur_path = os.getcwd()





resized_for_this_screen: tuple = (int_vertical_position(50), int_vertical_position(50))

# Will render its contents on screen in ORDER
renderer = []

def add_ingredients(*argumentos, **argumentos_clave):
    for argumento in argumentos:
        
        try:
            # print("Argumento:", argumento)

            raw_img = Image.open(f"{cur_path}/Ingredients/{argumento}.png")
            img = ImageTk.PhotoImage(raw_img.resize(resized_for_this_screen))

            renderer.append(img)
        
        except:
            print("Error creating image: Have you added a valid ingredient?")
            print("Ask your teacher if you need any further help!!! :)")



    return



# ------------------------------------------------------------------------------------

#  v  Solve the exercise here! :)  v


add_ingredients("dough", "cheese", "tomato_sauce", "ham", "tomato_slices", "eggs")


# ------------------------------------------------------------------------------------


def render(renderer: list):
    for img in renderer:
        canvas.create_image(floor(user_screen_width / 2), floor(user_screen_height * 8 / 15), image=img, anchor=tk.CENTER)
    
    canvas.pack()

    return


render(renderer)

canvas.pack()

root.mainloop()