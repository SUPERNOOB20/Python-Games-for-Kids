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





local_print_enabled = True

# -------------------- SECTION 2: PYGAME ---------------------------------

def create_scoreboard(team_list):

    gs_scoreboard = {}

    for i in range (0, len(team_list)):

        gs_scoreboard[team_list[i]] = 0        # {team_ID: (team_name, team_points)}

    return gs_scoreboard

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Splits the team list into groups.
def create_groups(team_list: list[str], group_size = 4) -> list[list[str]]:

    if ((len(team_list)) % group_size) == 1:
        raise NotImplementedError

    group_list: list[list[str]] = []

    current_team: list[str] = []

    for team_index in range (0, len(team_list)):

        current_team.append(team_list[team_index])

        if ((team_index + 1) % 4 == 0) and (team_index > 0):
            group_list.append(current_team)
            current_team = []
                


    global local_print_enabled

    if local_print_enabled == True:
        from pprint import pprint  
        # pprint(group_list)
        local_print_enabled = False

    return group_list

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Hardcoded at 12 groups of 4 teams each, for now.
def elimination(team_tiers):

    qualified_teams = team_tiers.copy()

    qualified_teams.pop(3)      # tier 4 doesn't qualify :c

    tier_3 = []
    for team in team_tiers[2]:  # grabs tier 3
        tier_3.append(team)
    tier_3.sort()
    tier_3.pop(0)
    tier_3.pop(0)

    qualified_teams[2] = tier_3

    return qualified_teams      # qualified_teams = [[GS tier 1], [GS tier 2], [GS tier 3]]


"""
# Provides another way of eliminating groups (going into the brackets)
def alt_elimination(all_teams_in_groups, group_size = 4):

    number_of_qualified_teams = int(group_size / 2)

    qualified_teams = []


    for group in all_teams_in_groups:

        current_group = group.sort()

        for i in range(0, (group_size - number_of_qualified_teams)):
            current_group.pop(0)

        qualified_teams.append(current_group.sort(reverse = True))

        
    return qualified_teams
"""




# Arranges brackets in a way that no two teams of the same group get to play against each other in RO32:
# Qualified teams should be ordered by placement, like this:
# qualified_teams = [[GS tier 1], [GS tier 2], [GS tier 3]]
# .
# WIP e.e
def create_brackets(qualified_teams: list[int], group_list: list[list[str]]):

    print("qualified_teams:", qualified_teams)

    valid_bracket = False

    while valid_bracket == False:
    
        ro16_bracket = []

        tier1 = qualified_teams[0]
        for team in tier1:
            ro16_bracket.append(team)
        


        tier2 = qualified_teams[1]
        for i in range(0, 4):   # repeat 4 times.
            ro16_bracket.append(tier2.pop(0))

        # At this point of the code, we have 12 brackets with tier 1 teams, and 4 brackets with tier 2 teams.
        # Let's fill the rest!

        remaining_teams = []

        tier3 = qualified_teams[2]
        
        for team in tier2:
            remaining_teams.append(team)
        for team in tier3:
            remaining_teams.append(team)
        
        
        assert len(ro16_bracket)    == len(remaining_teams)
        assert len(remaining_teams) == 16
        

        for i in range (0, remaining_teams):
            matched_team = qualified_teams[i]
            ro16_bracket[i] = (matched_team, remaining_teams[i])

        

        for match in ro16_bracket:

            if group_list[match][0] == group_list[match][1]:
                valid_bracket = True


    return ro16_bracket
    

    



def round_robin(group_size = 4, number_of_groups = 12):

    all_groups: list[tuple[int]] =  []

    for group in range(1, number_of_groups + 1):
        
        for team in range (1, group_size + 1):

            for matched_team in range(team, group_size + 1):
                if team != matched_team:
                    all_groups.append((team + ((group - 1) * 4), matched_team + ((group - 1) * 4)))


    return all_groups   # [(1, 2), (1, 3), (1, 4), ...]



def team_IDs_to_names(matched_teams_IDs: list[tuple[int]], team_list):

    # print("team list:", team_list)

    matched_teams_names = matched_teams_IDs

    for match in range(0, len(matched_teams_IDs)):
        first_team  = team_list[matched_teams_IDs[match][0] - 1]        # - 1 to offset the index.
        second_team = team_list[matched_teams_IDs[match][1] - 1]        # - 1 to offset the index.
        matched_teams_names[match] = (first_team, second_team)

    # print("\n", "matched_teams_names:", matched_teams_names, "\n")

    return matched_teams_names








# Generates match outcomes at random.
def generate_results(number_of_matches = 72):

    match_results: list = []

    for i in range(0, number_of_matches):
        a = randint(0, 7)
        b = randint(0, 7)
        random_match = (a, b)
        match_results.append(random_match)

    return match_results      # match_results = [(2, 3), (1, 1), (7, 0), ... etc.]


# returns matches = {result: matched_teams}
# example:
# matches = {(3, 4): ('Mexico', 'Czechia'),
#            (1, 0): ('Mexico', 'Corea'  )}
def arrange_matches(gs_scoreboard, team_list, group_size = 4):
    
    global all_groups

    # ### number_of_matches = binomial_coefficient(group_size, 2)
    # number_of_matches = 72                                                                                        # Hard-coded for now - will fix in the future e.e
    # ### number_of_groups = int(len(team_list) / group_size)
    # ### number_of_matches = (int(binomial_coefficient(group_size, 2))) * number_of_groups                         # Pls fix this D:


    # "quien juega contra quien".
    # len(lineup = 72)
    lineup = team_IDs_to_names(round_robin(), team_list)

    # len(results = 72s)
    results = generate_results()

    gs_matches = {}

    for i in range(0, len(lineup)):
        gs_matches[i] = [results[i], lineup[i]]

    # print("gs_matches:", gs_matches)

    return gs_matches



# Plays Group Stage.
# Declares Group Stage's match results, and adjusts the points accordingly.
# .
# matches: {match_ID: [match_results, teams_that_played]}
# for example: {0: [(3, 1): ("Argentina", "Mexico")],
#               1: [(2, 7): ("Argentina", "Canada")]}
def play_gs(gs_scoreboard, matches):

    for match in range(0, len(matches)):
        result  = matches[match][0]
        team_a  = matches[match][1][0]
        team_b  = matches[match][1][1]
    
        if result[0] > result[1]:
            gs_scoreboard[team_a] += 3      # team 1 wins

        elif result[0] < result[1]:
            gs_scoreboard[team_b] += 3      # team 2 wins

        else:                           # result: tie (both teams get 1 point)            
            gs_scoreboard[team_a] += 1
            gs_scoreboard[team_b] += 1

    return gs_scoreboard


team_list = ["Mexico",        "South Africa",    "Czechia",          "Corea",
             "Canada",        "Bosnia",          "Qatar",            "Switzerland",
             "Brazil",        "Morocco",         "Haiti",            "Scotland",
             "USA",           "Paraguay",        "Australia",        "Türkiye",
             "Germany",       "Curaçao",         "Côte d'Ivoire",    "Ecuador",
             "Netherlands",   "Japan",           "Sweden",           "Tunisia",
             "Belgium",       "Egypt",           "Iran",             "New Zeland",
             "Spain",         "Cabo Verde",      "Saudi Arabi",      "Uruguay",
             "France",        "Senegal",         "Iraq",             "Norway",
             "Argentina",     "Algeria",         "Austria",          "Jordan",
             "Portugal",      "Congo DR",        "Uzbekistan",       "Colombia",
             "England",       "Croatia",         "Ghana",            "Panama"]
        
gs_scoreboard = create_scoreboard(team_list)
group_list = create_groups(team_list)



def render_gs(team_list, gs_scoreboard):
    x = 2.8
    y = 27.3
    inner_vertical_gap = 6.5

    team_list_queue = (team_list).copy()

    group_size = 4               # 4 teams in a group.
    number_of_groups = 12        # 8 groups in the tournament.
    number_of_rows = 2           # 2 rows of groups.

    groups_per_row = int(number_of_groups / number_of_rows)

    # This line of code isn't needed, it's just for extra safety :p
    while len(team_list_queue) > 0:

        for i in range(0, number_of_rows):

            for i in range(0, groups_per_row):

                for i in range(0, group_size):
                    # print("gs_scoreboard:", gs_scoreboard)
                    # print("team_list_queue:", team_list_queue)
                    render_text(team_list_queue[0],                 "black",  (int_horizontal_position(x),     int_vertical_position(y)),  screen, font = normal_font)                  # Renders teams
                    render_text(str(gs_scoreboard[team_list_queue[0]]), "black",  (int_horizontal_position(x + 11), int_vertical_position(y)),  screen, font = handwritten_font)            # Renders the current score of each team
                    y += inner_vertical_gap
                    team_list_queue.pop(0)
                
                y -= inner_vertical_gap * group_size
                x += 16.3
            
            x = 2.8
            y += inner_vertical_gap * (group_size + 2) - 3
    return











pygame.init()       # Yes, initialize pygame twice. Sorry, couldn't find any other workaround "^^
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


SegoeUII_12pt = pygame.font.Font(filename="../Fonts/segoeuii.ttf", size=12)
CCWildWordsI_36pt = pygame.font.Font(filename="../Fonts/CC Wild Words Italic.ttf", size=36)

resized_for_this_screen: tuple = (user_screen_width, user_screen_height)

field_raw_surface = pygame.image.load("field.png").convert_alpha()
field_scaled_surface = pygame.transform.scale(surface = field_raw_surface, size = resized_for_this_screen)

groups_raw_surface = pygame.image.load("groups.png").convert_alpha()
groups_scaled_surface = pygame.transform.scale(surface = groups_raw_surface, size = resized_for_this_screen)

brackets_raw_surface = pygame.image.load("brackets.png").convert_alpha()
brackets_scaled_surface = pygame.transform.scale(surface = brackets_raw_surface, size = resized_for_this_screen)



enable_gs = True


running          = True
simulation_state = 0

def simulation():

    global running
    global simulation_state

    global gs_scoreboard
    global team_list
    
    global enable_gs
    
    global group_list



    clock = pygame.time.Clock()    

    debug_mode = True
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
                    print("gs_scoreboard:", gs_scoreboard)
                    print("\n")

                if event.key == pygame.K_RETURN:
                    simulation_state += 1

        keyboard.on_press_key("esc", lambda _: stop_running())


        screen.blit(field_scaled_surface, (0, 0))

        


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

        text1 = f"Played 0 out of 3 games"

        if (simulation_state < 2):

            screen.blit(groups_scaled_surface, (0, 0))

            # Renders the title.
            text1 = f"Played 3 out of 3 games"
            render_text(text1, "pink",  (int_horizontal_position(25), int_vertical_position(5)),  screen, font = bold_handwritten_font)

            # Renders the standings (the team names and their scores).
            render_gs(team_list, gs_scoreboard)



            if (simulation_state > 0) and (enable_gs == True):
                matches = arrange_matches(gs_scoreboard, team_list)

                # print("arranged_matches:", matches)

                # Updates the scoreboard (hopefully)
                gs_scoreboard = play_gs(gs_scoreboard, matches)

                enable_gs = False

        elif simulation_state >= 2:
            screen.blit(brackets_scaled_surface, (0, 0))


        # ------------------------------------------------------------------------------------
        # ----- Bracket stage

        

        qualified_teams = elimination(team_tiers = group_list)
        brackets: list  = create_brackets(qualified_teams, group_list)

        print(brackets)
        
        pygame.display.flip()
        clock.tick(60)  # Caps the events loop at a 60fps ceiling.
    return




# if main:
#   certificate()



simulation()