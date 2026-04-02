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








root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())

"""
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
"""

canvas = tk.Canvas(root, width = 1050, height = 700)
canvas.create_text(600, 20, text = "My Pizza!") 

os.chdir(os.path.dirname(os.path.realpath(__file__)))
cur_path = os.getcwd()

"""
def add_ingredients(*argumentos, **argumentos_clave):
    for argumento in argumentos:
        try:
            print("Argumento:", argumento)

            # imagen_a_abrir: str = f"Ingredients/{argumento}.png"
            # print(imagen_a_abrir)
            # canvas.create_image(200, 80, image=ImageTk.PhotoImage(Image.open(imagen_a_abrir).resize((90 * int_vh, 90 * int_vh))), anchor=tk.NW)

            # canvas.create_image(200, 80, image=ImageTk.PhotoImage((Image.open(f"Ingredients/{argumento}.png")).resize((90 * int_vh, 90 * int_vh))), anchor=tk.NW)
            print(f"Ingredients/{argumento}.png")
            # raw_img = Image.open(f"Ingredients/{argumento}.png")
            raw_img = Image.open("Ingredients/dough.png")
            img = ImageTk.PhotoImage(raw_img.resize((90 * int_vh, 90 * int_vh)))
            canvas.create_image(200, 80, image=img, anchor=tk.NW)

            # print("Argumento:", argumento)
            # print("PATH:", f"{cur_path}/Ingredients/{argumento}.png")
            # canvas.create_image(200, 80, image=ImageTk.PhotoImage((Image.open(f"{cur_path}/Ingredients/{argumento}.png")).resize(resized_for_this_screen)), anchor=tk.NW)


        except:
            print("Error creating image: Have you added a valid ingredient?")
            print("Ask your teacher if you need any further help!!! :)")

    return
"""

resized_for_this_screen: tuple = (int_vertical_position(50), int_vertical_position(50))

# Will render its contents on screen in ORDER
renderer = []

def add_ingredients(*argumentos, **argumentos_clave):
    for argumento in argumentos:
        # print("Argumento:", argumento)

        raw_img = Image.open(f"{cur_path}/Ingredients/{argumento}.png")
        img = ImageTk.PhotoImage(raw_img.resize(resized_for_this_screen))

        renderer.append(img)



    return



"""
canvas.create_image(200, 80, image=dough_img, anchor=tk.NW)
canvas.create_image(200, 80, image=cheese_img, anchor=tk.NW)
canvas.create_image(200, 80, image=tomato_sauce_img, anchor=tk.NW)
canvas.create_image(200, 80, image=ham_img, anchor=tk.NW)
canvas.create_image(200, 80, image=tomato_slices_img, anchor=tk.NW)
canvas.create_image(200, 80, image=eggs_img, anchor=tk.NW)
"""

# ------------------------------------------------------------------------------------

#  v  Solve the exercise here! :)  v


add_ingredients("dough", "cheese")

# canvas.create_image(200, 80, image=ImageTk.PhotoImage((Image.open(f"{cur_path}/Ingredients/dough.png")).resize(resized_for_this_screen)), anchor=tk.NW)


"""
add_dough()
add_cheese()
add_tomato_sauce()
add_ham()
add_tomato_slices()
add_eggs()
"""


# ------------------------------------------------------------------------------------


def render(renderer: list):
    for img in renderer:
        canvas.create_image(200, 80, image=img, anchor=tk.NW)
    
    canvas.pack()

    return


render(renderer)

canvas.pack()

root.mainloop()