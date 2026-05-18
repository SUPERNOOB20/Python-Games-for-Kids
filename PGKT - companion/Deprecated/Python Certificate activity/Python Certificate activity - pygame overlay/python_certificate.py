# -------------------- SECTION 1: PATHS, MODULES, DEPENDENCIES ---------------------------------


from math import floor
import os


def current_folder(path: str = os.getcwd()):
    parsed_path = path.split("\\")

    return parsed_path[len(parsed_path) - 1]


if current_folder() != "Programming Games for Kids & Teens":
    error_message = (f"\nERROR: You need to open the  ***\033[91mProgramming Games for Kids & Teens\033[00m***  folder!!!"
                    "\nYou are currently in the {current_folder()} folder ':3")
    print("\n")
    raise Exception(error_message)

os.chdir("Python/Functions and Modules/Python Certificate activity")


import dependencies

this_directory = os.getcwd()
library_path = os.path.abspath(os.path.join(this_directory, "../../Libraries"))

dependencies.add_libraries(library_path)
dependencies.add_assets("Assets")


import numpy as np
import cv2
import keyboard
from random import randint
from math import floor
from adaptive_screensize_utils_b import user_screen_width, user_screen_height, int_horizontal_position, int_vertical_position, vw, vh

import pygame   # pygame-ce.
pygame.init()

# -------------------- SECTION 1.5: AUXILIARY FUNCTIONS ---------------------------------

def render_text(what, color, where, screen, font = pygame.font.SysFont('Arial', 30)):

    

    text = font.render(what, 1, pygame.Color(color))
    text_rect = text.get_rect()
    text_rect.center = where
    screen.blit(text, text_rect)

    return



def stop_running():

    global running
    running = False

    return





# -------------------- SECTION 2: PYGAME ---------------------------------

running = True


def certificate(name = "Your Name Here", background_color = (240, 115, 196)):

    a = cv2.imread("python_certificate.png", cv2.IMREAD_UNCHANGED)
    b = a

    a = a.astype(float)/255  

    # blue, green, red = cv2.split(b)
    b = cv2.merge(background_color)
    b = b.astype(float)/255

    mask = a >= 0.5 # generate boolean mask of everywhere a > 0.5 
    ab = np.zeros_like(a) # generate an output container for the blended image 

    # now do the blending 
    ab[~mask] = (2*a*b)[~mask] # 2ab everywhere a<0.5
    ab[mask] = (1-2*(1-a)*(1-b))[mask] # else this 






    global running
    
    pygame.init()       # Yes, initialize pygame twice. Sorry, couldn't find any other workaround "^^
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


    SegoeUII_12pt = pygame.font.Font(filename="../Fonts/segoeuii.ttf", size=12)
    CCWildWordsI_36pt = pygame.font.Font(filename="../Fonts/CC Wild Words Italic.ttf", size=36)

    resized_for_this_screen: tuple = (user_screen_width, user_screen_height)

    # certificate_raw_surface = pygame.image.load("python_certificate.png").convert_alpha()
    certificate_raw_surface = pygame.image.frombytes(ab)
    certificate_scaled_surface = pygame.transform.scale(surface = certificate_raw_surface, size = resized_for_this_screen)



    certificate_highlighter = pygame.Surface((user_screen_width, user_screen_height), flags=pygame.SRCALPHA)

    certificate_highlighter = certificate_highlighter.premul_alpha()

    certificate_highlighter.fill(color = (background_color[0],background_color[1], background_color[2], 200))
    

    certificate_highlighter.blit(certificate_scaled_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MAX)

    # certificate_highlighter = certificate_highlighter.premul_alpha()

    # certificate_scaled_surface.blit(certificate_highlighter, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)




    clock = pygame.time.Clock()
    

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

        keyboard.on_press_key("esc", lambda _: stop_running())





        choose_deck_prompt_surf = pygame.font.Font.render(CCWildWordsI_36pt, "Choose a deck to play with.", True, (255,255,255), None, 0)

        choose_deck_prompt_rect = choose_deck_prompt_surf.get_rect(center = (floor(user_screen_width / 2), floor((user_screen_height / 2) - vh * 11)))
        screen.blit(choose_deck_prompt_surf, choose_deck_prompt_rect)

        # screen.blit(certificate_scaled_surface, (0, 0))
        screen.blit(certificate_highlighter, (0, 0))


        # ----------- EPILOGUE: FONTS ------------------------------------------------------------------------------------

        normal_font             = pygame.font.Font('../Fonts/segoeuii.ttf', 30)
        handwritten_font        = pygame.font.Font('../Fonts/BRADHITC.TTF', 30)
        italic_handwritten_font = pygame.font.Font('../Fonts/BRADHITC.TTF', 30)




        text1 = "Azul Cian"
        text2 = "hereby grants the title of"

        text3 = "Python Programmer"

        text4 = "to the student"

        text5 = name



        render_text(text1, "blue",  (int_horizontal_position(40), int_vertical_position(5)),  screen, font = normal_font)
        render_text(text2, "black", (int_horizontal_position(57), int_vertical_position(5)),  screen, font = italic_handwritten_font)
        render_text(text3, "black", (int_horizontal_position(50), int_vertical_position(25)), screen, font = pygame.font.SysFont("Helvetica", 72))
        render_text(text4, "black", (int_horizontal_position(50), int_vertical_position(50)), screen, font = italic_handwritten_font)
        render_text(text5, "black", (int_horizontal_position(50), int_vertical_position(75)), screen, font = pygame.font.SysFont("Helvetica", 72))


        # ------------------------------------------------------------------------------------



        
        pygame.display.flip()
        clock.tick(60)  # Caps the events loop at a 60fps ceiling.
    return




# if main:
#   certificate()