# -------------------- SECTION 1: PATHS, MODULES, DEPENDENCIES ---------------------------------


import tkinter as tk
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
            os.chdir("Python/CONTROL FLOW STRUCTURES (lessons #7 - )/Control Flow bug/Assets")
        except:
            print("Error: \033[91mAssets\033[00m folder not found :c")


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
# change_path_in_foreign_computer()     # This is the code I run at York (yes, I just brute-force the absolute path...).

os.chdir("Assets")
print("current dir:", os.getcwd())


"""
go_to_libraries()

from adaptive_screensize_utils_b import *

go_back()
"""




# -------------------- SECTION 2: TKINTER ---------------------------------

def certificate(name = "Your Name Here", color = "000000"):

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    c = tk.Canvas(root, bg = 'black')

    keyboard.on_press_key("esc", lambda _: root.destroy())


    certificate_raw_img = Image.open("python_certificate.png")

    # resized_for_this_screen: tuple = (int_vertical_position(50), int_vertical_position(50))
    resized_for_this_screen: tuple = (user_screen_width, user_screen_height)

    certificate_img = ImageTk.PhotoImage(certificate_raw_img.resize(resized_for_this_screen))

    canvas = tk.Canvas(root, width = user_screen_width, height = user_screen_height)
    print(int_horizontal_position(50))
    canvas.create_text(int_horizontal_position(50), 40, text = "My Pizza!", font=("Helvetica", 40)) 



    """
    def add_eggs():
        canvas.create_image(int_horizontal_position(25), 80, image=eggs_img, anchor=tk.NW)
        return

    """



    # ------------------------------------------------------------------------------------



    canvas.pack()

    root.mainloop()