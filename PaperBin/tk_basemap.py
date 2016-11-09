import matplotlib
matplotlib.use('TkAgg')
from mpl_toolkits.basemap import Basemap
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
fig = Figure()  ## here
ax1 = fig.add_subplot(111)  ## here

m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.,
            ax=ax1) ## here
m.drawcoastlines()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')

canvas = FigureCanvasTkAgg(fig, master=root)  ## here
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def print_hello():
    print("Hello")

button = Tk.Button(root, text="Click me", command=print_hello)
button.pack()

root.mainloop()