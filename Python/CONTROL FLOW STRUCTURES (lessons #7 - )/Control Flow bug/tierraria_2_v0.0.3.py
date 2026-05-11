# -------------------- SECTION 1: PATHS, MODULES, DEPENDENCIES ---------------------------------

import keyboard
import os
import sys

from random import randint


def check_OS():
    
    platform = sys.platform
    user_OS = ""


    # linux
    if platform == ("linux" or "linux2"):
        user_OS = "linux"

    # Macintosh's OS
    elif platform == "darwin":
        print("Warning: macOS not supported! Will attempt to run the game regardless...")
        user_OS = "windows"     # Unimplemented. Just treat it as Windows for the moment being cuz why not.

    # iOS
    elif platform == "ios":
        print("Warning: iOS not supported! Will attempt to run the game regardless...")
        user_OS = "windows"     # Unimplemented. Just treat it as Windows for the moment being cuz why not.

    # Windows...    
    elif platform[:3] == "win":
        user_OS = "windows"
    

    else:
        raise("Warning: Your Operating System, \033[92m{platform}\033[00m, is not supported :c")

    return user_OS




user_OS = check_OS()

def change_path_to_module_location(current_OS):

    if current_OS == "windows":

        true_path = os.path.dirname(os.path.realpath(__file__))

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
        true_path = os.path.dirname(os.path.realpath(__file__))

        new_true_path = os.path.join(true_path, '..')

        sys.path.append(true_path + "/../../../venv_for_linux/lib")


    return


def change_path_in_foreign_computer():
    for i in range(40):     # Just a naive, brute-force approach to absolute paths, pay it no mind.
        os.chdir("/../")
    os.chdir("D:/York 2026/Programming Games for Kids & Teens/Python/CONTROL FLOW STRUCTURES (lessons #7 - )/Control Flow bug/Assets")

    return



change_path_to_module_location(user_OS)
# change_path_in_foreign_computer()     # This is the code I run at York (yes, I just brute-force the absolute path...).

os.chdir("Assets")
print("current dir:", os.getcwd())




import pygame       # imports pygame-ce

# if pygame not ce... throw an exception or a warning.




import pygame_utils
from adaptive_screensize_utils_b import *

# print("IMPORT TEST:", 1 * vw)


# -------------------- SECTION 2: GAME ---------------------------------


# Finally... the game! :D


frame_counter = 0           # Times global events
car_frame_counter = 0       # Times cars' animation loop :3


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# User's current screen resolution
user_res = (user_screen_width, user_screen_height)

images: dict = pygame_utils.creates_images({"bg": ["bg.png", user_res]})

# print("vh and vw:", vh, vw)

#                                                                 handle(key)    filename              anchor          anchorpos                                 size
images_with_rects: dict = pygame_utils.creates_images_and_rects({"tie_man_1":    ["tie_man_1.png",     "bottom",       user_screen_height / 2,                   (3 * vw, 8 * vh)                            ],
                                                                 "ground_1":     ["ground_1.png",      "bottomleft",   (0, user_screen_height),                  (45 * vw, 46.293027361 * vh)                ],
                                                                 "ground_2":     ["ground_2.png",      "bottomleft",   (0, user_screen_height),                  (57.1 * vw, 30.0088261253 * vh)             ],
                                                                 "water":        ["water.png",         "bottomright",  (user_screen_width, user_screen_height),  (60.7 * vw, 42.2771403354 * vh)             ],
                                                                 "water_ground": ["water_ground.png",  "top",          user_screen_height,                       (user_screen_width,   17.9611650485 * vh)   ],
                                                                 "cloud_1":      ["cloud_1.png",       "bottomleft",   (user_screen_width, user_screen_height),  (60.7 * vw, 42.2771403354 * vh)             ],
                                                                 "cloud_67":     ["cloud_67.png",      "bottomleft",   (user_screen_width, user_screen_height),  (60.7 * vw, 42.2771403354 * vh)             ]})



class Cloud:
    # __slots__ = ['anchorpos_x = user_screen_width', 'anchorpos_y = user_screen_height', 'x = 60.7 * vw', 'y = 42.2771403354 * vh']
    def __init__(self, anchorpos_x = user_screen_width, anchorpos_y = user_screen_height * 0.2, x = 60.7 * vw, y = 42.2771403354 * vh):
        images_with_rects[str(self)] = ["cloud_1.png",      "bottomleft",   (anchorpos_x, anchorpos_y),    (x, y)]

    


    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x



    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

    @y.deleter
    def y(self):
        del self._y



    @property
    def xy(self):
        return (self._x, self._y)
    
    @xy.setter
    def y(self, x_value, y_value):
        self._x = x_value
        self._y = y_value

    @xy.deleter
    def y(self):
        del self._x
        del self._y
    






# print("images_with_rects dict:", images_with_rects)



# WIP:  Find a way to assign tie_man_1's rect to tie_man_2 and tie_man_3
# images["tie_man_2"] = "tie_man_2": ["tie_man_2.png", (3 * vw, 8 * vh)]
# images["tie_man_3"] = "tie_man_3": ["tie_man_3.png", (3 * vw, 8 * vh)]

clock = pygame.time.Clock()

pygame.display.set_caption("Tierraria 2 - More ties than the original! :3")



standing_on_ground = False



player_gravity = 0
def gravity():
    player_gravity -= 1 * vh
    player_y -= player_gravity
    return

def jump():

    global standing_on_ground
    if standing_on_ground == True:

        global player_gravity
        player_gravity -= 20

    return





def run_the_game():





    # Activity: Tierraria 2.
    # TASK: This is some code for a videogame, Tierraria 2.
    # However, the code has a bug: Tie Man can't get out of the water!
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

        global standing_on_ground
        standing_on_ground = True

        player_rect.bottom = object_rect.top - 1      # Snaps the player to the ground.

        global player_gravity
        player_gravity = 0
        

    return player_rect


def check_collisions_left(player_rect: pygame.Rect, object_rect: pygame.Rect):

    # print("object top:", object_rect.top)
    # print("player top:", object_rect.top)

    if (player_rect.top > object_rect.top) and (player_rect.bottomleft[0] < object_rect.bottomright[0]):

        player_rect.left = object_rect.right + 1      # Snaps the player outside the wall.


    return player_rect


# It's important to check for bottom collisions before the left ones
# (I'm handling bottom-left clips (1 corner clips) as bottom collisions)
def check_collisions(player_rect):


    player_rect = check_collisions_left(images_with_rects["tie_man_1"][1], images_with_rects["ground_1"][1])
    player_rect = check_collisions_left(images_with_rects["tie_man_1"][1], images_with_rects["ground_2"][1])

    player_rect = check_collisions_bottom(images_with_rects["tie_man_1"][1], images_with_rects["ground_1"][1])
    player_rect = check_collisions_bottom(images_with_rects["tie_man_1"][1], images_with_rects["ground_2"][1])
    player_rect = check_collisions_bottom(images_with_rects["tie_man_1"][1], images_with_rects["water_ground"][1])


    return player_rect

        


def draw_clouds(spawn_timer, screen):

    if (spawn_timer % 200) == 0:

        random_rescale = randint(-10,10)

        current_cloud = Cloud()

        screen.blit(images_with_rects["cloud_1"][0], images_with_rects["cloud_1"][1].scale_by(random_rescale))
        screen.blit(images_with_rects["cloud_67"][0], images_with_rects["cloud_67"][1].scale_by(random_rescale))

    return


# Initializes player position (sets the "spawn" for the player)
# images_with_rects["tie_man_1"][1].bottomleft = int_horizontal_position(20)          # player_x
# images_with_rects["tie_man_1"][1].bottomleft = int_vertical_position(10)            # player_y

images_with_rects["tie_man_1"][1].bottomleft = (int_horizontal_position(20), int_vertical_position(30))            # (player_x, player_y)





# -------------------- SECTION 3: GAME LOOP ---------------------------------

left_key_down = False
right_key_down = False
space_key_down = False

debug_mode = True

while(running == True):

    screen.fill((255, 255, 255))

    screen.blit(images["bg"], (0, 0))
    screen.blit(images_with_rects["water"][0], images_with_rects["water"][1])
    screen.blit(images_with_rects["ground_2"][0], images_with_rects["ground_2"][1])
    screen.blit(images_with_rects["ground_1"][0], images_with_rects["ground_1"][1])
    screen.blit(images_with_rects["water_ground"][0], images_with_rects["water_ground"][1])

    draw_clouds(frame_counter, screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # THANKS TO https://stackoverflow.com/questions/45571647/press-and-hold-for-pygame FOR THIS
            if (event.key == pygame.K_SPACE):
                space_key_down = True
            if (event.key == pygame.K_LEFT):
                left_key_down = True
            if (event.key == pygame.K_RIGHT):
                right_key_down = True

            if (event.key == pygame.K_b) and (debug_mode == True):
                print("\n")
                print("player rect:", images_with_rects["tie_man_1"][1])
                print("player rect - bottom:", images_with_rects["tie_man_1"][1].bottom)
                print("gravity:", player_gravity)
                print("\n")

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_SPACE):
                space_key_down = False
            if (event.key == pygame.K_LEFT):
                left_key_down = False
            if (event.key == pygame.K_RIGHT):
                right_key_down = False


    if space_key_down:
        jump()
    if left_key_down:
        images_with_rects["tie_man_1"][1][0] -= 0.3 * vw
    if right_key_down:
        images_with_rects["tie_man_1"][1][0] += 0.3 * vw


    # keyboard.on_press_key("esc", lambda _: pygame.quit())
    keyboard.on_press_key("esc", lambda _: stop_running())

    



    player_gravity += 1

    standing_on_ground = False
    images_with_rects["tie_man_1"][1] = check_collisions(images_with_rects["tie_man_1"][1])

    # Makes the player fall (when airborne).
    images_with_rects["tie_man_1"][1][1] = images_with_rects["tie_man_1"][1][1] + player_gravity

    screen.blit(images_with_rects["tie_man_1"][0], images_with_rects["tie_man_1"][1])



    if debug_mode == True:
        pygame.font.init()
        
        Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))    # Show FPS
        # print("FPS:", int(clock.get_fps()))


    
    


    frame_counter     += 1
    # car_frame_counter += 1
    

    pygame.display.flip()
    clock.tick(60)      # Caps the events loop at a 60fps ceiling (oof with delta time).