import matplotlib
# Set Tk as the backend for basemap drawing (this needs to happen before importing other libraries
matplotlib.use('TkAgg')

from mpl_toolkits.basemap import Basemap
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sys
# import the correct Tk library based on python version
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

import numpy as np
import Zoom

# Default parameters to create the map with
params = {
    'projection': 'cyl',
    'resolution': 'c',
    'llcrnrlon': -180,
    'llcrnrlat': -90,
    'urcrnrlon': 180,
    'urcrnrlat': 90,
}


class TkMap:

    def __init__(self, root):
        self.fig = None
        self.ax1 = None
        self.map = None
        self.canvas = None
        self.tk_canvas = None
        self.zoom = None

        self.fig = Figure()
        # add a grid with one row and one column (= a single graph)
        self.ax1 = self.fig.add_subplot(111)
        # draw a Basemap onto this grid
        self.map = Basemap(ax=self.ax1, **params)
        # link the grid to a Tk.Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.show()
        self.tk_canvas = self.canvas.get_tk_widget()
        self.tk_canvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        # add zoom/pan functions to the grid
        self.zoom = Zoom.ZoomPan()
        self.zoom.zoom_factory(self.ax1)
        self.zoom.pan_factory(self.ax1)

        self.draw_basemap()

    def draw_basemap(self):
        # draw map
        self.map.drawcoastlines()
        self.map.drawmapboundary(fill_color='aqua')
        self.map.fillcontinents(color='coral',lake_color='aqua')
        # draw parallels and meridians.
        # labels = [left,right,top,bottom]
        parallels = np.arange(-80, 81, 20.)
        self.map.drawparallels(parallels,labels=[True,False,False,False])
        meridians = np.arange(-180, 180, 40.)
        self.map.drawmeridians(meridians,labels=[False,False,False,True])

    def draw_data(self, data):
        y, x = len(data), len(data[0])
        X, Y = self.map.makegrid(x, y)
        self.map.contour(X, Y, data)
        # ToDo: Colorbar

    def redraw(self):
        self.canvas.draw()
