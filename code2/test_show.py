from tkinter import *
from PIL import Image, ImageTk


# create the canvas, size in pixels
canvas = Canvas(width=900, height=220, bg='black')

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

# load the .gif image file
gif1 = PhotoImage(file='box/img1.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(0, 0, image=gif1, anchor=NW)

# run it ...
mainloop()