# From https://cs.stackexchange.com/a/127918
# ...and https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB_alternative

from math import floor

def whole_min(a: int, b: int) -> int:
    
    min: int = b

    if (a > b):
        min = a
    

    return min

def whole_max(a: int, b: int) -> int:

    max: int = b

    if (whole_min(a, b) == b):
        max = a

    return max


# Separates the calculation into the 6 main cases.
def piecewise_function(n, h, s, v):

    # k = case_function(n, h)
    k: int = (n + (h / 60)) % 6

    arg_3: int = min(k, 4 - k)
    arg_2: int = min(arg_3, 1)
    arg_1: int = max(0, arg_2)

    channel_value: int = v - v * s * arg_1
    return channel_value


# Converts from 0 <= channel_value <= 1 to 0 <= channel_value <= 255
def converted_channel_value(channel):
    return floor(channel * 255)



# int h;     // 0 <= H <= 360
# float s;   // 0 <= S <= 1
# float v;   // 0 <= V <= 1
def hsv_to_rgb(h, s, v):

    r: int = piecewise_function(5, h, s, v)
    g: int = piecewise_function(3, h, s, v)
    b: int = piecewise_function(1, h, s, v)

    # print("converted r: ", converted_channel_value(r))
    # print("converted g: ", converted_channel_value(g))
    # print("converted b: ", converted_channel_value(b))

    rgb = ((converted_channel_value(r), converted_channel_value(g), converted_channel_value(b)))
    return rgb