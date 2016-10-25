from Tkinter import *
from random import randint, choice, randrange
from string import ascii_letters, digits

master = Tk()

canvas_width = 640
canvas_height = 480

point_width = 20
point_height = point_width

number_points = 6

canvas = Canvas(master,
                width=canvas_width,
                height=canvas_height)
canvas.pack()

for i in xrange(number_points):

    color_values = [choice(digits) for n in xrange(6)]
    color_str = "".join(color_values)
    color_str = "#" + color_str

    x = randrange(point_width, canvas_width)
    y = randrange(point_height, canvas_height)

    canvas.create_oval(x, y, x-point_width, y-point_height , fill=color_str)

mainloop()