# -------------------- SECTION 1: PATHS, MODULES, DEPENDENCIES ---------------------------------


from math import floor
import os


def current_folder(path: str = os.getcwd()):
    parsed_path = path.split("\\")

    return parsed_path[len(parsed_path) - 1]


if current_folder() != "Programming Games for Kids & Teens":
    error_message = (f"\nERROR: You need to open the  ***\033[91mProgramming Games for Kids & Teens\033[00m***  folder!!!"
                    f"\nYou are currently in the {current_folder()} folder ':3")
    print("\n")
    raise Exception(error_message)


# os.chdir("Python/World Cup")
# os.chdir(os.getcwd())     # Why does this not work...? :c
os.chdir(os.path.dirname(os.path.realpath(__file__)))


import dependencies

this_directory = os.getcwd()
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

running = True


def simulation():

    global running
    
    pygame.init()       # Yes, initialize pygame twice. Sorry, couldn't find any other workaround "^^
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


    SegoeUII_12pt = pygame.font.Font(filename="../Fonts/segoeuii.ttf", size=12)
    CCWildWordsI_36pt = pygame.font.Font(filename="../Fonts/CC Wild Words Italic.ttf", size=36)

    resized_for_this_screen: tuple = (user_screen_width, user_screen_height)

    field_raw_surface = pygame.image.load("field.png").convert_alpha()
    field_scaled_surface = pygame.transform.scale(surface = field_raw_surface, size = resized_for_this_screen)

    groups_raw_surface = pygame.image.load("groups.png").convert_alpha()
    groups_scaled_surface = pygame.transform.scale(surface = groups_raw_surface, size = resized_for_this_screen)



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


        
        screen.blit(field_scaled_surface, (0, 0))
        screen.blit(groups_scaled_surface, (0, 0))



        # ----------- INTERLUDIUM: FONTS ------------------------------------------------------------------------------------

        # normal_font             = tk.font.Font(family = "Segoe UI",         size = 40, slant = "italic")
        # handwritten_font        = tk.font.Font(family = "Bradley Hand ITC", size = 40)
        # italic_handwritten_font = tk.font.Font(family = "Bradley Hand ITC", size = 40, slant = "italic")


        # normal_font             = pygame.font.SysFont('Segoe UI',         30, italic = True)
        # handwritten_font        = pygame.font.SysFont('Bradley Hand ITC', 30)
        # italic_handwritten_font = pygame.font.SysFont('Bradley Hand ITC', 30, italic = True)


        normal_font             = pygame.font.Font('../Fonts/segoeuii.ttf', 18)
        handwritten_font        = pygame.font.Font('../Fonts/BRADHITC.TTF', 30)
        italic_handwritten_font = pygame.font.Font('../Fonts/BRADHITC.TTF', 30)
        bold_handwritten_font   = pygame.font.Font('../Fonts/CC Wild Words Italic.ttf', 48)


        # -------------------------------------------------------------------------------------------------------------------

        text1 = "Played 0 out of 3 games"



        render_text(text1, "pink",  (int_horizontal_position(25), int_vertical_position(5)),  screen, font = bold_handwritten_font)

        x = 3
        y = 27.8
        inner_vertical_gap = 6.5

        team_list = ["Mexico", "South Africa", "Czechia", "Corea",
                     "Canada", "Bosnia\nand Herzegovina", "Qatar", "Switzerland",
                     "Brazil", "Morocco", "Haiti", "Scotland",
                     "USA", "Paraguay", "Australia", "Türkiye",
                     "Germany", "Curaçao", "Côte d'Ivoire", "Ecuador",
                     "Netherlands", "Japan", "Sweden", "Tunisia",
                     "Belgium", "Egypt", "Iran", "New Zeland",
                     "Spain", "Cabo Verde", "Saudi Arabi", "Uruguay",
                     "France", "Senegal", "Iraq", "Norway",
                     "Argentina", "Algeria", "Austria", "Jordan",
                     "Portugal", "Congo DR", "Uzbekistan", "Colombia",
                     "England", "Croatia", "Ghana", "Panama"]
        
        team_list_queue = team_list

        group_size = 4               # 4 teams in a group.
        number_of_groups = 12        # 8 groups in the tournament.
        number_of_rows = 2           # 2 rows of groups.

        groups_per_row = int(number_of_groups / number_of_rows)

        # This line of code isn't needed, it's just for extra safety :p
        while len(team_list_queue) > 0:

            for i in range(0, number_of_rows):

                for i in range(0, groups_per_row):

                    for i in range(0, group_size):
                        render_text(team_list_queue[0], "black",  (int_horizontal_position(x), int_vertical_position(y)),  screen, font = normal_font)
                        y += inner_vertical_gap
                        team_list_queue.pop(0)
                    
                    y -= inner_vertical_gap * group_size
                    x += 16.3
                
                x = 3
                y += inner_vertical_gap * (group_size + 2) - 3
                

        # ------------------------------------------------------------------------------------



        
        pygame.display.flip()
        clock.tick(60)  # Caps the events loop at a 60fps ceiling.
    return




# if main:
#   certificate()



simulation()