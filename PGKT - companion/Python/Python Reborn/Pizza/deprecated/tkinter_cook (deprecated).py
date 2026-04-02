import tkinter as tk
import keyboard
from PIL import ImageTk, Image
import os

# current_path = os.getcwd()
# print("Current path:", current_path)

true_path = os.path.dirname(os.path.realpath(__file__))
print("Current path:", true_path)
os.chdir(true_path)

root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())


dough_img = ImageTk.PhotoImage(Image.open("Ingredients/dough.png"))
cheese_img = ImageTk.PhotoImage(Image.open("Ingredients/cheese.png"))
tomato_slices_img = ImageTk.PhotoImage(Image.open("Ingredients/tomato_slices.png"))
tomato_sauce_img = ImageTk.PhotoImage(Image.open("Ingredients/tomato_sauce.png"))
eggs_img = ImageTk.PhotoImage(Image.open("Ingredients/eggs.png"))
ham_img = ImageTk.PhotoImage(Image.open("Ingredients/ham.png"))


dough_img.resize((400, 100))


canvas = tk.Canvas(root, width = 1050, height = 700)
canvas.create_text(600, 20, text = "My Pizza!") 

canvas.create_image(200, 80, image=dough_img, anchor=tk.NW)
canvas.create_image(200, 80, image=cheese_img, anchor=tk.NW)


canvas.pack()

"""
window_panel = tk.Label(root, text = "My Pizza")
window_panel.pack(side = "top", fill = "both", expand = "yes")


dough_panel = tk.Label(root, image = dough_img)
dough_panel.pack(side = "bottom", fill="none")

cheese_panel = tk.Label(root, image = cheese_img)
cheese_panel.pack(side = "bottom", fill = "both", expand = "yes")

tomato_slices_panel = tk.Label(root, image = tomato_slices_img)
tomato_slices_panel.pack(side = "bottom", fill = "both", expand = "yes")

tomato_sauce_panel = tk.Label(root, image = tomato_sauce_img)
tomato_sauce_panel.pack(side = "bottom", fill = "both", expand = "yes")

ham_panel = tk.Label(root, image = ham_img)
ham_panel.pack(side = "bottom", fill = "both", expand = "yes")

eggs_panel = tk.Label(root, image = eggs_img)
eggs_panel.pack(side = "bottom", fill = "both", expand = "yes")

"""

root.mainloop()