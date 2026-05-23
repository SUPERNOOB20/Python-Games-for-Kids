# -------------------- SECTION 1: PATHS, MODULES, DEPENDENCIES ---------------------------------



import os
import pathlib

this_directory = pathlib.Path(__file__).parent.resolve()

os.chdir(this_directory)


import dependencies

this_directory = pathlib.Path(__file__).parent.resolve()
library_path = os.path.abspath(os.path.join(this_directory, "../Libraries"))

dependencies.add_libraries(library_path)
dependencies.add_assets("Assets")



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

    # text_rect.center = where
    # screen.blit(text, text_rect)

    screen.blit(text, where)

    return



def stop_running():

    global running
    running = False

    return



# -------------------- SECTION 2: PYGAME ---------------------------------

list_of_mouse_pos = []

running          = True
simulation_state = 0

def simulation():

    global list_of_mouse_pos

    global running
    global simulation_state
    
    pygame.init()       # Yes, initialize pygame twice. Sorry, couldn't find any other workaround "^^
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


    SegoeUII_12pt = pygame.font.Font(filename="../Fonts/segoeuii.ttf", size=12)
    CCWildWordsI_36pt = pygame.font.Font(filename="../Fonts/CC Wild Words Italic.ttf", size=36)

    resized_for_this_screen: tuple = (user_screen_width, user_screen_height)

    landscape_raw_surface = pygame.image.load("landscape.png").convert_alpha()
    landscape_scaled_surface = pygame.transform.scale(surface = landscape_raw_surface, size = resized_for_this_screen)

    bunny_raw_surface = pygame.image.load("bunny.png").convert_alpha()
    # bunny_scaled_surface = pygame.transform.scale(surface = bunny_raw_surface, size = resized_for_this_screen)



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

                if event.key == pygame.K_RETURN:
                    simulation_state += 1

        keyboard.on_press_key("esc", lambda _: stop_running())


        
        screen.blit(landscape_scaled_surface, (0, 0))
        screen.blit(bunny_raw_surface, pygame.mouse.get_pos())







        """
        mode = 0


        if mode == 0:
            current_mouse_pos = pygame.mouse.get_pos()
            current_mouse_pos 
            screen.blit(bunny_raw_surface, current_mouse_pos)
        """


        # ----------- INTERLUDIUM: FONTS ------------------------------------------------------------------------------------

        # normal_font             = tk.font.Font(family = "Segoe UI",         size = 40, slant = "italic")
        # handwritten_font        = tk.font.Font(family = "Bradley Hand ITC", size = 40)
        # italic_handwritten_font = tk.font.Font(family = "Bradley Hand ITC", size = 40, slant = "italic")


        # normal_font             = pygame.font.SysFont('Segoe UI',         30, italic = True)
        # handwritten_font        = pygame.font.SysFont('Bradley Hand ITC', 30)
        # italic_handwritten_font = pygame.font.SysFont('Bradley Hand ITC', 30, italic = True)


        normal_font             = pygame.font.Font('../Fonts/segoeuii.ttf', 17)
        handwritten_font        = pygame.font.Font('../Fonts/BRADHITC.TTF', 30)
        italic_handwritten_font = pygame.font.Font('../Fonts/BRADHITC.TTF', 30)
        bold_handwritten_font   = pygame.font.Font('../Fonts/CC Wild Words Italic.ttf', 48)


        # -------------------------------------------------------------------------------------------------------------------

       

        # ------------------------------------------------------------------------------------



        
        pygame.display.flip()
        clock.tick(60)  # Caps the events loop at a 60fps ceiling.
    return




# if main:
#   certificate()



simulation()