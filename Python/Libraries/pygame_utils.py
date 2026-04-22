# Library with tools for pygame-ce.

import pygame
import adaptive_screensize_utils
import warnings

import os
import sys


pygame.init()

if (getattr(pygame, "IS_CE", False) != True):
    raise Warning("Your version of Pygame isn't CE. Please install pygame-ce with \033[92mpip install pygame-ce\033[00m\033[95m.\033[00m")

def change_path_to_module_location():

    true_path = os.path.dirname(os.path.realpath(__file__))

    new_true_path = os.path.join(true_path, '..')

    sys.path.append(true_path + "/../..")

    os.chdir(new_true_path)


    new_true_path = os.path.join(true_path, '..')
    new_true_path = os.path.join(new_true_path, 'Libraries')

    sys.path.append(new_true_path)

    return



# Input: dict {handle: filename}
#
# anchor to set anchor
# image_size to set size
def creates_images(given_dict: dict):
    

    # change_path_to_module_location()


    created_images: dict = {}

    print("current dict:", given_dict)

    for key, value in given_dict.items():

        # Matches user's screen resolution by default.
        if len(value) == 1:

            key_surf = pygame.image.load(value).convert_alpha()
            key_scaled_surf = pygame.transform.scale(surface = key_surf, size = (user_screen_width, user_screen_height))
            created_images[key] = key_scaled_surf


        else:

            # print("AAAAA")

            if len(value) > 3:
                warnings.warn(f"WARNING: More than 2 values in the image parsing of {given_dict}, in {key}. \nIf you don't know what you're doing, please ask your teacher!")

            handle = value[0]
            image_size = value[2]
            print("Current image_size:", image_size)


            key_surf = pygame.image.load(handle).convert_alpha()
            key_scaled_surf = pygame.transform.scale(surface = key_surf, size = image_size)
            created_images[key] = key_scaled_surf


    return created_images



# Input: dict {handle: filename} (WIP)
# or
# Input: dict {handle: [filename, (anchor, anchorpos), (x, y)]}
#
# anchor to set anchor
# image_size to set size
#
# Returns {handle: (surface, rect)}.
def creates_images_and_rects(given_dict):

    created_images: dict = {}

    for key, value in given_dict.items():
                
        handle = value[0]
        anchor = value[1]
        anchorpos = value[2]
        image_size: tuple = value[3]


        key_surf = pygame.image.load(handle).convert_alpha()
        key_scaled_surf = pygame.transform.scale(surface = key_surf, size = image_size)

        rect_handle = f"{handle} + _rect"

        if anchor == "center":
            rect_handle = key_scaled_surf.get_rect(center = anchorpos)
        else:
            warnings.warn(f"WARNING: Unknown (or yet to be implemented) anchor: {anchor}")

        created_images[key] = [key_scaled_surf, rect_handle]

    print("created images and rects:")

    return created_images



# Raises an exception if the input dict has len() == 0.
# Otherwise, calls "creates_images_and_rects()" (for _ in [])
# Returns a GroupSingle if the input dict has len() == 1.
# Returns a Group if the input dict has len() > 1
#
# THIS FEATURE IS WIP, do not use it yet.
def creates_sprites(*given_dicts, **kwgiven_dicts):
    class MySprite(pygame.sprite.Sprite):
        def __init__(self, type):
            super().__init__()

    match len(given_dicts):
        case 0:
            raise Exception("Please provide an image for the sprite!")
        case 1:
            sprite_instance = pygame.sprite.GroupSingle()
        case 2:
            sprite_instance = pygame.sprite.Group()
    return sprite_instance





# vv  Here's a set of "shortcuts" to screen.blit().
# vv  Might end up deleting or deprecating if it's not convenient.


# vv  images should be a dict of {foo: [bar]}
def draw_with_rect(screen, images, thingy: str):
    draw_this = f"{thingy}_scaled_surface"
    screen.blit(images[draw_this][0], images[draw_this][1])
    return


# Draws without rect.
# images should be a dict of {foo: bar}
def draw(screen, images, thingy: str):
    draw_this = f"{thingy}_scaled_surface"
    screen.blit(images[draw_this], (0, 0))
    return