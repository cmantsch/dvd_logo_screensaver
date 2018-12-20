import tkinter as tk
from controller import DvdLogo

def update():
    new_position = ctl.get_next_position()
    canvas.coords(logo, new_position)
    root.after(10, update)

# initialize stuff
root = tk.Tk()
app = tk.Frame(root)
logo_image = tk.PhotoImage(file='res/logo.png')
ctl = DvdLogo(position=(0,0), canvas_size=(1280,720), image_size=(200,200))
# root.logo = logo

# set window properties
root.wm_title('DVD Screensaver')
# todo: geometry

canvas = tk.Canvas(root, bg='black', height=720, width=1280, borderwidth=0, highlightthickness=0)
logo = canvas.create_image(0, 0, image=logo_image, anchor='nw')

canvas.pack()
root.after(10, update)
root.mainloop()