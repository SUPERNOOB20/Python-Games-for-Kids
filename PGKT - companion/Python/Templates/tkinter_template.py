# pip install tkinter
# pip install keyboard input


import tkinter as tk
import keyboard

root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

# root.bind("e", lambda x: root.quit())

close = root.quit()

root.bind('<Escape>', close)


# Write your own program here! :3

root.mainloop()