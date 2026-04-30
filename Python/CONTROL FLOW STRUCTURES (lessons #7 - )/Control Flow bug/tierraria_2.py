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

    os.chdir(new_true_path)


    new_true_path = os.path.join(true_path, '..')
    new_true_path = os.path.join(new_true_path, 'Libraries')

    sys.path.append(new_true_path)

    return

change_path_to_module_location()



os.chdir("CONTROL FLOW STRUCTURES (lessons #7 - )")
# print("current_dir: ", os.getcwd())
os.chdir("Control Flow Bug")
os.chdir("Assets")



import pygame       # imports pygame-ce

# if pygame not ce... throw an exception or a warning.



import pygame_utils



images: dict = pygame_utils.creates_images({"bg": ["bg.png", (cars_transformed_width * car_scale_factor, cars_transformed_height * car_scale_factor)],
                                            "tie_man_1": ["tie_man_1.png", (user_screen_width, user_screen_height)]})









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


    if (terrain == "water"):
        action = "swim"

    if (terrain == "ground"):
        action = "jump"










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


# Initializes player position (sets the "spawn" for the player)
player_x = int_horizontal_position(20)
player_y = int_vertical_position(60)



debug_mode = False

while(running == True):

    screen.fill((255, 255, 255))

    screen.blit(images["bg"], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard.on_press_key("esc", lambda _: pygame.quit())
    keyboard.on_press_key("esc", lambda _: stop_running())

    



    player_gravity += 1
    screen.blit(images["tie_man_1"], (player_x, player_y + player_gravity))



    if debug_mode == True:
        pygame.font.init()
        
        Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))    # Show FPS
        Render_Text((str(traffic_lights)), (255,0,0), (100,0))    # Show FPS
        # print("FPS:", int(clock.get_fps()))
        

    
    


    frame_counter     += 1
    # car_frame_counter += 1
    

    pygame.display.flip()
    clock.tick(60)  # Caps the events loop at a 60fps ceiling. Doesn't work at other framerates, for some reason... (oof with delta time)