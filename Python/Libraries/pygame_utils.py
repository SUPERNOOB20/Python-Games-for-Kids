import pygame

import adaptive_screensize_utils



# Input: dict {handle: filename}
# Matches user's screen resolution by default.
def creates_images(*args, **kwargs):
    
    created_images: dict = {}

    for key, value in args:

        key_surf = pygame.image.load(value).convert_alpha()
        key_scaled_surf = pygame.transform.scale(surface = key_surf, size = (user_screen_width / scale_factor, user_screen_height))
        created_images[key] = key_scaled_surf


    return created_images



# Input: dict {handle: filename}
# or
# Input: dict {handle: [filename, anchor, x, y]}
def creates_images_and_rects():
    return



# Raises an exception if the input dict has len() == 0.
# Otherwise, calls "creates_images_and_rects()" (for _ in [])
# Returns a GroupSingle if the input dict has len() == 1.
# Returns a Group if the input dict has len() > 1
def creates_sprites():
    return