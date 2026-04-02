# This is a library that implements the concepts of
# "vw" (viewport width) and "vh" (viewport hieght) in Python.

# pip install screeninfo
from screeninfo import get_monitors
from math import floor

user_screen_width = get_monitors()[0].width
user_screen_height = get_monitors()[0].height

vw: float = user_screen_width / 100
vh: float = user_screen_height / 100

int_1_vw: int = floor(vw)
int_1_vh: int = floor(vh)



def int_x_vw(width_in_vw):

    invalid_input: bool = (width_in_vw < 0) or (width_in_vw > 100)

    if invalid_input:
        print("ERROR: Please enter a number between 0 and 100 :3")
        return
    
    else:
        return floor(width_in_vw * vw)



def int_x_vh(height_in_vh):

    invalid_input: bool = (height_in_vh < 0) or (height_in_vh > 100)

    if invalid_input:
        print("ERROR: Please enter a number between 0 and 100 :3")
        return
    
    else:
        return floor(height_in_vh * vh)
    


# If given, say, 30 as a parameter, returns float(30vw)
def int_horizontal_size(size_in_vw: int) -> int:         # f(int) = int
    if ((size_in_vw < 0) | (size_in_vw > 100)):
        return -1
    return floor(vw * size_in_vw)



# If given, say, 30 as a parameter, returns float(30vh)
def int_vertical_size(size_in_vh: int) -> int:           # f(int) = int
    if ((size_in_vh < 0) | (size_in_vh > 100)):
        return -1
    return floor(vw * size_in_vh)