# pip install tkinter
# pip install keyboard input

import tkinter as tk
import keyboard

root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

# root.bind("e", lambda x: root.quit())

# root.bind('<Escape>', close)

"""
def callback(*args, **kwargs):
    print("kwargs:", str(**kwargs))
    print("args:", str(*args))
    return

keyboard.hook(callback, suppress=False, on_remove=print(callback))
"""
# print("keyboard callback:", callback)

# keyboard.on_press(print(keyboard.get_hotkey_name()))

# print(keyboard.record(until='e1lke'))

if keyboard.is_pressed(hotkey='key_pressed'):
    print("key_pressed")
    # keyboard.parse_hotkey_combinations(key_pressed)

if keyboard.is_pressed('e'):
    print("noice")
    root.destroy()

# Write your own program here! :3

root.mainloop()