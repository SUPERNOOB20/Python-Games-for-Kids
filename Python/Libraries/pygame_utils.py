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

            if len(value) > 2:
                warnings.warn(f"WARNING: More than 2 values in the image parsing of {given_dict}, in {key}. \nIf you don't know what you're doing, please ask your teacher!")

            handle = value[0]
            image_size = (value[1], value[2])

            key_surf = pygame.image.load(handle).convert_alpha()
            key_scaled_surf = pygame.transform.scale(surface = key_surf, size = image_size)
            created_images[key] = key_scaled_surf


    return created_images



# Input: dict {handle: filename}
# or
# Input: dict {handle: [filename, anchor, x, y]}
#
# anchor to set anchor
# image_size to set size
def creates_images_and_rects(*given_dicts, anchor, image_size):
    
    return



# Raises an exception if the input dict has len() == 0.
# Otherwise, calls "creates_images_and_rects()" (for _ in [])
# Returns a GroupSingle if the input dict has len() == 1.
# Returns a Group if the input dict has len() > 1
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