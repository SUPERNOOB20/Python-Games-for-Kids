import keyboard
import os
import sys

from random import randint

frame_counter = 0           # Times global events
car_frame_counter = 0       # Times cars' animation loop :3

traffic_lights = "green"      # Lo inicializo en "green". ¿Por qué? Porque sí :p

def cambiar_las_luces_del_semaforo():
    global traffic_lights

    traffic_lights_change = randint(0, 1)

    if (traffic_lights_change == 0):
        traffic_lights = "red"
    else:
        traffic_lights = "green"
    return





def change_path_to_module_location():

    true_path = os.path.dirname(os.path.realpath(__file__))

    new_true_path = os.path.join(true_path, '..')

    sys.path.append(true_path + "/../../..")

    new_true_path = os.path.join(true_path, '..')
    new_true_path = os.path.join(new_true_path, '..')
    new_true_path = os.path.join(new_true_path, 'Libraries')

    sys.path.append(new_true_path)
    print(sys.path)

    return

change_path_to_module_location()


print("current dir:", os.getcwd())
os.chdir("Python/CONTROL FLOW STRUCTURES (lessons #7 - )/Control Flow bug/Assets")



import pygame       # imports pygame-ce

# if pygame not ce... throw an exception or a warning.




import pygame_utils
from adaptive_screensize_utils_b import *


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# User's current screen resolution
user_res = (user_screen_width, user_screen_height)

images: dict = pygame_utils.creates_images({"bg": ["bg.png", user_res]})

images_with_rects: dict = pygame_utils.creates_images_and_rects({"tie_man_1": ["tie_man_1.png", "bottom", user_screen_height / 2, (3 * vw, 8 * vh)],
                                                                 "ground_1": ["ground_1.png", "bottom", user_screen_height, user_res],
                                                                 "ground_2": ["ground_2.png", "bottom", user_screen_height, user_res],
                                                                 "water": ["water.png", "bottom", user_screen_height, user_res],
                                                                 "water_ground": ["water_ground.png", "bottom", user_screen_height, user_res]})

# player_x = images_with_rects["tie_man_1"][0]
# player_y = images_with_rects["tie_man_1"][1]

print("\n")
print("images_with_rects dict:", images_with_rects)
print("\n")



# WIP:  Find a way to assign tie_man_1's rect to tie_man_2 and tie_man_3
# images["tie_man_2"] = "tie_man_2": ["tie_man_2.png", (3 * vw, 8 * vh)]
# images["tie_man_3"] = "tie_man_3": ["tie_man_3.png", (3 * vw, 8 * vh)]

clock = pygame.time.Clock()

pygame.display.set_caption("Tierraria 2 - More ties than the original! :3")







player_gravity = 0
def gravity():
    player_gravity -= 1 * vh
    player_y -= player_gravity
    return

def jump():
    return





def run_the_game():





    # Activity: Tierraria 2.
    # TASK: This is some code for a videogame, Tierraria 2.
    # However, the code has a bug: the little dude jumps even when he is underwater!
    # How do we fix this...?



    """
    if (terrain == "water"):
        action = "swim"

    if (terrain == "ground"):
        action = "jump"
    """









    return
    







def Render_Text(what, color, where):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)

    return



running = True

def stop_running():

    global running

    running = False
    return





# WIP: Tell bottom and left collisions apart with vertices (anchors)


def check_collisions_bottom(player_rect: pygame.Rect, object_rect: pygame.Rect):

    if (player_rect.bottom >= object_rect.top) and (player_rect.bottomleft[0] < object_rect.bottomright[0]):

        player_rect.bottom = object_rect.top - 1      # Snaps the player to the ground.

    return


def check_collisions_left(player_rect: pygame.Rect, object_rect: pygame.Rect):

    if (player_rect.bottom >= object_rect.top) and (player_rect.bottomleft[0] < object_rect.bottomright[0]):

        player_rect.bottom = object_rect.right + 1      # Snaps the player to the ground.


    return


# It's important to check for bottom collisions before the left ones
# (I'm handling bottom-left clips (1 corner clips) as bottom collisions)
def check_collisions():
    
    check_collisions_bottom(images_with_rects["tie_man_1"][0].get_rect(), images_with_rects["ground_1"][0].get_rect())
    check_collisions_bottom(images_with_rects["tie_man_1"][0].get_rect(), images_with_rects["ground_2"][0].get_rect())
    check_collisions_bottom(images_with_rects["tie_man_1"][0].get_rect(), images_with_rects["water_ground"][0].get_rect())

    check_collisions_left(images_with_rects["tie_man_1"][0].get_rect(), images_with_rects["ground_1"][0].get_rect())
    check_collisions_left(images_with_rects["tie_man_1"][0].get_rect(), images_with_rects["ground_2"][0].get_rect())

    return

        



# Initializes player position (sets the "spawn" for the player)
player_x = int_horizontal_position(20)
player_y = int_vertical_position(20)



debug_mode = False

while(running == True):

    screen.fill((255, 255, 255))

    screen.blit(images["bg"], (0, 0))
    screen.blit(images_with_rects["water"][0], (0, 0))
    screen.blit(images_with_rects["ground_2"][0], (0, 0))
    screen.blit(images_with_rects["ground_1"][0], (0, 0))
    screen.blit(images_with_rects["water_ground"][0], (0, 0))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard.on_press_key("esc", lambda _: pygame.quit())
    keyboard.on_press_key("esc", lambda _: stop_running())

    



    player_gravity += 1

    check_collisions()


    screen.blit(images_with_rects["tie_man_1"][0], (player_x, player_y + player_gravity))



    if debug_mode == True:
        pygame.font.init()
        
        Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))    # Show FPS
        Render_Text((str(traffic_lights)), (255,0,0), (100,0))    # Show FPS
        # print("FPS:", int(clock.get_fps()))
        

    
    


    frame_counter     += 1
    # car_frame_counter += 1
    

    pygame.display.flip()
    clock.tick(60)  # Caps the events loop at a 60fps ceiling. Doesn't work at other framerates, for some reason... (oof with delta time)