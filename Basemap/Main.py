from TkMap import TkMap
import sys
# import the correct Tk library based on python version
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


window = Tk.Tk()

m = TkMap(window)

# ToDo: read this from csv file
data = [[y*x for x in range(360//5)] for y in range(180//5)]
m.draw_data(data)
m.redraw()


def print_hello():
    print("hello")

button = Tk.Button(window, text="Click me", command=print_hello)
button.pack()

window.mainloop()
