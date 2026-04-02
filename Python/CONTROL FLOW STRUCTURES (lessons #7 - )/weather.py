

from random import randint


def change_path_to_module_location():

    new_true_path = os.path.join(true_path, '..')
    new_true_path = os.path.join(new_true_path, 'Libraries')

    sys.path.append(new_true_path)

    return






root = tk.Tk()
root.attributes('-fullscreen', True)
# c = tk.Canvas(root, bg = 'black')

keyboard.on_press_key("esc", lambda _: root.destroy())

canvas = tk.Canvas(root, width = user_screen_width, height = user_screen_height)
canvas.create_text(int_horizontal_position(50), 90, text = "School Subjects 2026", font=("Helvetica", 40)) 

os.chdir(os.path.dirname(os.path.realpath(__file__)))
cur_path = os.getcwd()



weather = randint(0, 1)

if (weather == 0):
    weather = "sunny"
else:
    weather = "rainy"


canvas.create_image(user_screen_width / 2, user_screen_height / 2, image=sunny, anchor=tk.CENTER)
canvas.pack()


def take_umbrella():
    canvas.create_image(user_screen_width / 2, user_screen_height / 2, image=rainy, anchor=tk.CENTER)
    canvas.pack()
    return




# .
# .
# .


# Task: We will be simulating a weather forecast in this exercise!
# 
# weather can either be "sunny" or "rainy".
# If the weather is rainy, print a message asking the user to
# take an umbrella!


# ---------------------------------------------------------------------------------------------------
# v  Do the exercise HERE!

if (weather == "rainy"):
    print("The weather is rainy today! Don't forget to take an umbrella wherever you go!")
    take_umbrella()




# ---------------------------------------------------------------------------------------------------












root.mainloop()