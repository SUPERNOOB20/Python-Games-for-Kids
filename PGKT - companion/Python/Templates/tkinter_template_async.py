import tkinter as tk
import keyboard

root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())
# keyboard.unhook_all() <--- no work????    https://stackoverflow.com/questions/77460705/how-to-detect-any-key-pressed-without-blocking-execution-in-python


# Write your code here! :3

root.mainloop()