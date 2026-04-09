import tkinter as tk
import keyboard
from PIL import ImageTk, Image
import os
import sys

from math import floor

from random import randint



# sys.path = os.curdir()

root = tk.Tk()
root.attributes('-fullscreen', True)
# c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())

canvas = tk.Canvas(root, width = 1366, height = 768)
canvas.create_text(600, 90, text = "School Subjects 2026", font=("Helvetica", 40))

canvas.create_image(0, 0, image="Assets/sunny.png", anchor=tk.CENTER)
canvas.pack()

root.mainloop()