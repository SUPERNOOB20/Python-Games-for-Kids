import tkinter as tk
import keyboard

root = tk.Tk()
root.attributes('-fullscreen', True)
c = tk.Canvas(root, bg = 'black')

evento = keyboard.read_event()
    
if evento.event_type == keyboard.KEY_DOWN:
    print(f"Presionaste: {evento.name}")
        
if evento.name == 'esc':
    root.destroy()

# Write your own program here! :3

root.mainloop()