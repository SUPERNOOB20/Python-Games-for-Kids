# -------------------- SECTION 1: PATHS, MODULES, DEPENDENCIES ---------------------------------


from math import floor
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










def create_teams(team_list):

    team_dict = {}

    for i in range (0, len(team_list)):

        team_dict[team_list[i]] = 0        # {team_ID: (team_name, team_points)}

    return team_dict



def func_a(x):

    y = 1

    if x > 3:
        y = 2
    elif x > 5:
        y = 3

    y += ((x // 7) * 4)     # Round robin for all groups. I don't know how to explain it, but it basically offsets y to account for every single group in group stage.

    return y

def func_b(x):

    y = 1

    if x > 3:
        y = 2
    elif x > 5:
        y = 3

    y += ((x // 7) * 4)     # Round robin for all groups. I don't know how to explain it, but it basically offsets y to account for every single group in group stage.

    return y



def factorial(a):

    product = 1

    while a > 0:
        product *= a
        a -= 1

    return product

def binomial_coefficient(a, b):
    return factorial(a) / (factorial(b) * factorial(a-b))


def team_IDs_to_names(matched_teams: list[tuple[int]], team_list):

    matched_teams_names = matched_teams

    print("\n", "matched_teams_names:", matched_teams_names, "\n")

    for match in range(0, len(matched_teams)):
        for team in range(0, 1):
            current_team = matched_teams[match][team] - 1
            # print("current team:", current_team)
            matched_teams_names[match][team] = team_list[current_team] 

    return matched_teams_names


def arrange_matches(team_list, group_size = 4):
    
    # number_of_matches = binomial_coefficient(group_size, 2)
    number_of_matches = 72                                                                                      # Hard-coded for now - will fix in the future e.e
    # number_of_matches = (int(binomial_coefficient(group_size, 2))) * (int(len(team_list) / group_size))       # Pls fix this D:

    matched_teams_IDs = []

    for match_ID in range(0, number_of_matches):
        team_a = func_a(match_ID)
        team_b = func_b(match_ID)

        matched_teams_IDs.append((team_a, team_b))

    return matched_teams_IDs





# Generates match outcomes at random.
def generate_results(number_of_matches):

    match_results: list = []

    for i in range(0, number_of_matches):
        a = randint(0, 7)
        b = randint(0, 7)
        random_match = (a, b)
        match_results.append(random_match)

    return match_results      # match_results = [(2, 3), (1, 1), (7, 0), ... etc.]


# matched_teams_IDs are the IDs of the teams that played = [(1, 2), (1, 3), (1, 4), (2, 3)... etc.]
def create_matches(team_dict, team_list, match_results: list[tuple[int]] = generate_results(72)):         # 72 = 6 * 12 (6 matches per group, 12 groups total).

    matched_teams_IDs: list[tuple[int]] = arrange_matches(team_list)
    matched_team_names                  = team_IDs_to_names(matched_teams_IDs, team_list)

    print("matched_teams_IDs:",   matched_teams_IDs)
    print("matched_team_names:",  matched_team_names)

    matches = {}

    for i in range(0, len(match_results)):
        match_outcome = (match_results[i][0], match_results[i][1])
        matches[match_outcome] = matched_team_names[i]

    return matches



# Plays Group Stage.
# Declares Group Stage's match results, and adjusts the points accordingly.
# .
# matches: {match_results: teams_that_played}
# for example: {(3, 1): ("Argentina", "Mexico"),
#               (2, 7): ("Argentina", "Canada")}
def play_gs(team_dict, team_list, matches):

    for match in range(0, len(matches)):
        result  = matches[match[0]]
        team_a  = matches[match[1][0]]
        team_b  = matches[match[1][1]]
    
        if result[0] > result[1]:
            team_dict[team_a] += 3      # team 1 wins

        elif result[0] < result[1]:
            team_dict[team_b] += 3      # team 2 wins

        else:                           # result: tie (both teams get 1 point)            
            team_dict[team_a] += 1
            team_dict[team_b] += 1

    return




running          = True
simulation_state = 0

def simulation():

    global running
    global simulation_state
    
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

                if event.key == pygame.K_RETURN:
                    simulation_state += 1

        keyboard.on_press_key("esc", lambda _: stop_running())


        
        screen.blit(field_scaled_surface, (0, 0))

        if simulation_state < 2:
            screen.blit(groups_scaled_surface, (0, 0))



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

        text1 = f"Played {simulation_state} out of 3 games"



        render_text(text1, "pink",  (int_horizontal_position(25), int_vertical_position(5)),  screen, font = bold_handwritten_font)

        x = 2.8
        y = 27.3
        inner_vertical_gap = 6.5

        team_list = ["Mexico",        "South Africa",              "Czechia",          "Corea",
                     "Canada",        "Bosnia\nand Herzegovina",   "Qatar",            "Switzerland",
                     "Brazil",        "Morocco",                   "Haiti",            "Scotland",
                     "USA",           "Paraguay",                  "Australia",        "Türkiye",
                     "Germany",       "Curaçao",                   "Côte d'Ivoire",    "Ecuador",
                     "Netherlands",   "Japan",                     "Sweden",           "Tunisia",
                     "Belgium",       "Egypt",                     "Iran",             "New Zeland",
                     "Spain",         "Cabo Verde",                "Saudi Arabi",      "Uruguay",
                     "France",        "Senegal",                   "Iraq",             "Norway",
                     "Argentina",     "Algeria",                   "Austria",          "Jordan",
                     "Portugal",      "Congo DR",                  "Uzbekistan",       "Colombia",
                     "England",       "Croatia",                   "Ghana",            "Panama"]
        
        team_dict = create_teams(team_list)
        # matches = round_robin(team_dict)

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
                        # print("team_dict:", team_dict)
                        # print("team_list_queue:", team_list_queue)
                        render_text(team_list_queue[0],                 "black",  (int_horizontal_position(x),     int_vertical_position(y)),  screen, font = normal_font)                  # Renders teams
                        render_text(str(team_dict[team_list_queue[0]]), "black",  (int_horizontal_position(x + 11), int_vertical_position(y)),  screen, font = handwritten_font)            # Renders the current score of each team
                        y += inner_vertical_gap
                        team_list_queue.pop(0)
                    
                    y -= inner_vertical_gap * group_size
                    x += 16.3
                
                x = 2.8
                y += inner_vertical_gap * (group_size + 2) - 3

        if (simulation_state > 0) and (simulation_state < 2):
            matches = create_matches(team_dict, team_list)
            play_gs(team_dict, team_list, matches)

        # ------------------------------------------------------------------------------------



        
        pygame.display.flip()
        clock.tick(60)  # Caps the events loop at a 60fps ceiling.
    return




# if main:
#   certificate()



simulation()