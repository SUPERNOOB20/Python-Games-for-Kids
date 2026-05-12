# -------------------- SECTION 1: PATHS, MODULES, DEPENDENCIES ---------------------------------


import keyboard

import pygame   # pygame-ce.
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


# Wait, what do you mean this isn't CMake? :p

def add_libraries(expected_filepath = os.getc):
    return

def add_assets(expected_filepath = ):


add_libraries()
add_assets()


"""
go_to_libraries()

from adaptive_screensize_utils_b import *

go_back()
"""




# -------------------- SECTION 2: PYGAME ---------------------------------

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)




SegoeUII_12pt = pygame.font.Font(filename="Fonts/segoeuii.ttf", size=12)
CCWildWordsI_36pt = pygame.font.Font(filename="Fonts/CC Wild Words Italic.ttf", size=36)




resized_for_this_screen: tuple = (user_screen_width, user_screen_height)


certificate_raw_surface = pygame.image.load("python_certificate.png").convert_alpha()
certificate_scaled_surface = pygame.transform.scale(surface = certificate_raw_surface, size = resized_for_this_screen)



certificate_highlighter = pygame.Surface((user_screen_width, user_screen_height), flags=pygame.SRCALPHA)

certificate_highlighter = certificate_highlighter.premul_alpha()

certificate_highlighter.blit(certificate_scaled_surface, (0, 0), special_flags=pygame.BLEND_PREMULTIPLIED)

certificate_highlighter = certificate_highlighter.premul_alpha()

certificate_scaled_surface.blit(certificate_highlighter, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


def Render_Text(what, color, where, screen):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)

    return


clock = pygame.time.Clock()
running = True

def stop_running():

    global running

    running = False
    return





def certificate(name = "Your Name Here", color = "000000"):

    global debug_mode
    global running


    debug_mode = False

    while(running == True):

        screen.fill((255, 255, 255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if (event.key == pygame.K_b) and (debug_mode == True):
                    print("\n")
                    print("Debug mode is active:")
                    print("You can print your logs here")
                    print("\n")

        keyboard.on_press_key("esc", lambda _: root.destroy())





        choose_deck_prompt_surf = pygame.font.Font.render(CCWildWordsI_36pt, "Choose a deck to play with.", True, (255,255,255), None, 0)

        choose_deck_prompt_rect = choose_deck_prompt_surf.get_rect(center = (floor(user_screen_width / 2), floor((user_screen_height / 2) - vh * 11)))
        screen.blit(choose_deck_prompt_surf, choose_deck_prompt_rect)

        screen.blit(certificate_scaled_surface, (0, 0))



        normal_font             = tk.font.Font(family = "Segoe UI",         size = 40, slant = "italic")
        handwritten_font        = tk.font.Font(family = "Bradley Hand ITC", size = 40)
        italic_handwritten_font = tk.font.Font(family = "Bradley Hand ITC", size = 40, slant = "italic")

    
        canvas.create_text(int_horizontal_position(30), int_vertical_position(5), text = "Azul Cian",                  font = normal_font, fill="blue", anchor="center")
        canvas.create_text(int_horizontal_position(60), int_vertical_position(5), text = "hereby grants the title of", font = italic_handwritten_font, anchor="center")

        canvas.create_text(int_horizontal_position(50), int_vertical_position(25), text = "Python Programmer",         font = ("Helvetica", 72), anchor="center")

        canvas.create_text(int_horizontal_position(50), int_vertical_position(50), text = "to the student",            font = italic_handwritten_font, anchor="center")

        canvas.create_text(int_horizontal_position(50), int_vertical_position(75), text = f"{name}",                   font = ("Helvetica", 72), anchor="center")




        # ------------------------------------------------------------------------------------



        
    pygame.display.flip()
    clock.tick(60)  # Caps the events loop at a 60fps ceiling.
    return




# if main:
#   certificate()