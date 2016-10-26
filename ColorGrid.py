from tkinter import *
import random

width = 500
height = 400

pixel_size = 10


# draws a grid of values onto a canvas
def draw_values(canvas, values):
    def get_pos(x, y):
        return (x     * pixel_size,
                y     * pixel_size,
                (x+1) * pixel_size,
                (y+1) * pixel_size)

    for x, row in enumerate(values):
        for y, value in enumerate(row):
            color = value_to_color(value)
            canvas.create_rectangle(get_pos(x, y), fill=color)

    return


# expects value to be a float between 0 and 1 and turns it into a color representing that value
def value_to_color(value):
    return rgb_to_tk_color(int(value*0xff), 0, int((1-value)*0xff))


# turns seperate rgb values (integer from 0x00 to 0xff each) into a color string for Tk
def rgb_to_tk_color(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


# generates a grid of size (x, y) filled with random values
def random_values(x, y):
    return [[random.random() for i in range(y)] for j in range(x)]


# generates a grid of size (x, y) filled with ordered values
def range_values(x, y):
    return [[(i+j)/(x+y) for i in range(y)] for j in range(x)]


window = Tk()

canvas = Canvas(window, width=width, height=height)
draw_values(canvas, random_values(width//pixel_size, height//pixel_size))
canvas.pack()

window.mainloop()
