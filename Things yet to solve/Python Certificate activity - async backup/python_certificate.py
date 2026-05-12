# -------------------- SECTION 1: PATHS, MODULES, DEPENDENCIES ---------------------------------

import asyncio

import tkinter as tk
from tkinter import font

import keyboard
from PIL import ImageTk, Image
import os
import sys

from random import randint



def check_OS():
    
    user_OS = ""

    # linux
    if sys.platform == ("linux" or "linux2"):
        user_OS = "linux"

    # OS X
    elif sys.platform == "darwin":
        print("Warning: Mac OS not supported! Will attempt to run the game regardless...")
        user_OS = "windows"     # Unimplemented. Just treat it as Windows for the moment being cuz why not.

    # Windows...    
    elif sys.platform == "win32":
        user_OS = "windows"
    

    else:
        raise("Warning: Your Operating System, \033[92m{sys.platform}\033[00m, is not supported :c")

    return user_OS




user_OS = check_OS()

def change_path_to_module_location(current_OS):

    true_path = os.path.dirname(os.path.realpath(__file__))

    new_true_path = os.path.join(true_path, '..')



    if current_OS == "windows":

        new_true_path = os.path.join(true_path, '..')

        sys.path.append(true_path + "/../../..")

        new_true_path = os.path.join(true_path, '..')
        new_true_path = os.path.join(new_true_path, '..')
        new_true_path = os.path.join(new_true_path, 'Libraries')

        sys.path.append(new_true_path)
        # print(sys.path)

        try:
            # os.chdir("Python/CONTROL FLOW STRUCTURES (lessons #7 - )/Control Flow bug/Assets")
            os.chdir("../Functions and Modules/Python Certificate activity/Assets")
        except:
            print(f"Error: \033[91mAssets\033[00m folder not found at {os.getcwd()} :c")


    else:   # Linux    

        sys.path.append(true_path + "/../../../venv_for_linux/lib")



    return




def change_path_in_foreign_computer():
    for i in range(40):     # Just a naive, brute-force approach to absolute paths, pay it no mind.
        os.chdir("/../")
    os.chdir("D:/York 2026/Programming Games for Kids & Teens/Python/CONTROL FLOW STRUCTURES (lessons #7 - )/Control Flow bug/Assets")

    return


print("CURRENT DIR 1:", os.getcwd())

current_path = os.path.dirname(os.path.realpath(__file__))
new_path = os.path.join(current_path, '../../Libraries')
sys.path.append(new_path)
os.chdir(new_path)

print("CURRENT DIR 2:", os.getcwd())


from adaptive_screensize_utils_b import *

change_path_to_module_location(user_OS)

"""
change_path_in_foreign_computer()     # This is the code I run at York (yes, I just brute-force the absolute path...).

os.chdir("Assets")
print("current dir:", os.getcwd())
"""





"""
go_to_libraries()

from adaptive_screensize_utils_b import *

go_back()
"""




# -------------------- SECTION 2: TKINTER ---------------------------------



# Because tkinter offers little-to-no transparency support, I make a semi-transparent window for the blend mode.
# I know. Nasty workaround. It is what it is.
async def certificate(name = "Your Name Here", color = "000000"):
    asyncio.run(blend_mode_window())
    await asyncio.sleep(2)
    asyncio.run(certificate_main(name, color))
    await asyncio.sleep(2)
    return



async def blend_mode_window():
    root2 = tk.Tk()
    root2.attributes('-alpha', 0.2, '-fullscreen', True)
    canvas2 = tk.Canvas(root2, width = user_screen_width, height = user_screen_height)

    keyboard.on_press_key("esc", lambda _: root2.destroy())



    # It's, uh, clockwise order. Starting from the top left corner. Yeah.
    top_left_corner_x = 0
    top_left_corner_y = 0

    top_right_corner_x = user_screen_width
    top_right_corner_y = 0

    bottom_right_corner_x = user_screen_width
    bottom_right_corner_y = user_screen_height

    bottom_left_corner_x = 0
    bottom_left_corner_y = user_screen_height

    canvas2.create_polygon(top_left_corner_x, top_left_corner_y, top_right_corner_x, top_right_corner_y, bottom_right_corner_x, bottom_right_corner_y, bottom_left_corner_x, bottom_left_corner_y, fill="red")



    canvas2.pack()
    root2.mainloop()
    return



async def certificate_main(name = "Your Name Here", color = "000000"):

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    canvas = tk.Canvas(root, width = user_screen_width, height = user_screen_height)




    keyboard.on_press_key("esc", lambda _: root.destroy())
    


    certificate_raw_img = Image.open("python_certificate.png")

    # resized_for_this_screen: tuple = (int_vertical_position(50), int_vertical_position(50))
    resized_for_this_screen: tuple = (user_screen_width, user_screen_height)

    certificate_img = ImageTk.PhotoImage(certificate_raw_img.resize(resized_for_this_screen))

    
    # canvas.create_text(int_horizontal_position(50), 40, text = "My Pizza!", font=("Helvetica", 40)) 

    

    canvas.create_image(0, 0, image=certificate_img, anchor=tk.NW)


    normal_font             = tk.font.Font(family = "Segoe UI",         size=40, slant = "italic")
    handwritten_font        = tk.font.Font(family = "Bradley Hand ITC", size=40)
    italic_handwritten_font = tk.font.Font(family = "Bradley Hand ITC", size=40, slant = "italic")


    


    # Yes I should be using a Frame instead of the Canvas but please have some mercy on me.
    canvas.create_text(int_horizontal_position(30), int_vertical_position(5), text = "Azul Cian", font = normal_font, fill="blue", anchor="center")
    canvas.create_text(int_horizontal_position(60), int_vertical_position(5), text = "hereby grants the title of", font = italic_handwritten_font, anchor="center")

    canvas.create_text(int_horizontal_position(50), int_vertical_position(25), text = "Python Programmer", font = ("Helvetica", 72), anchor="center")

    canvas.create_text(int_horizontal_position(50), int_vertical_position(50), text = "to the student", font = italic_handwritten_font, anchor="center")

    canvas.create_text(int_horizontal_position(50), int_vertical_position(75), text = f"{name}", font = ("Helvetica", 72), anchor="center")


    


    # ------------------------------------------------------------------------------------


    canvas.pack()
    root.mainloop()
    return

# certificate()