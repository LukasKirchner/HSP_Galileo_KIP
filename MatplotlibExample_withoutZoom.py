from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv
import CSVLoad
import matplotlib.cm as cmx
import matplotlib.colors as colors
import ValueGrid as VG

# -----------------------------
# values
filename = 'TestData.csv'
lats, lons = [], []
mags = []
times = []

xs, ys = [], []

plot_handle = None

grid = VG.load_from_csv(filename)


def redraw_map():
    # global plot_handle, xs, ys
    # When changing the data, change the xdata and ydata and redraw
    # for x,y in xs, ys:
    # plot_handle.remove()

    # plot_handle.set_xdata([])
    # plot_handle.set_ydata([])
    # plot_handle.set_ydata(ys)
    # plot_handle.set_xdata(xs)

    global ax1
    global fig
    fig.delaxes(ax1)
    ax1 = fig.add_subplot(111)
    fig.canvas.draw()


# ------------------------------
# load file button
def button_on_clicked(event):
    global filename
    filename = CSVLoad.openFileDialogCsv()
    # clear arrays, so that the old values disappear
    global lats, lons
    lats, lons = [], []
    global mags
    mags = []
    global times
    times = []
    global grid
    grid = VG.load_from_csv(filename)
    redraw_map()
    build_map(10)

    # code replication because of on_clicked event does not work otherwise
    ax = plt.axes([0, 0.9, 0.1, 0.1])
    b = plt.Button(ax, "Load")
    b.on_clicked(button_on_clicked)

    plt.show()


def build_map(marker_size):
    map = Basemap(ax=ax1)
    # map = Basemap(projection='robin',lon_0=0,resolution='c') #plt.title("Robinson Projection")

    map.etopo()  # 'contour'
    # map.bluemarble() #'satellite'

    # draw coastlines, parallels and meridians.
    map.drawcoastlines()
    map.drawparallels(np.arange(-90., 120., 5.))
    map.drawmeridians(np.arange(0., 360., 5.))

    # ------------------------------
    # size/color marking points
    # msize = marker_size
    # global plot_handle
    #
    # global xs, ys
    # xs, ys = [], []
    # for lon, lat, mag in zip(lons, lats, mags):
    #     x, y = map(lon, lat)
    #     xs.append(x)
    #     ys.append(y)
    #     msize = mag * min_marker_size
    #     marker_string = get_marker_color(mag)
    #     plot_handle, = map.plot(x, y, marker_string, markersize=msize)

    # draw filled contours.


    # global filename
    # grid = VG.load_from_csv(filename)
    # x_new_array, y_new_array, data_new_array = grid.get_values(0, 0)
    # cs = map.contourf(x_new_array, y_new_array, data_new_array, levels,colors = ('r', 'y', 'g', 'c', 'b'))

    x, y, data = grid.get_values(0, 0)

    mag_max = np.amax(data)
    levels = [0, (mag_max / 5) * 1, (mag_max / 5) * 2, (mag_max / 5) * 3, (mag_max / 5) * 4, (mag_max / 5) * 5]

    # colors = ('r', 'y', 'g', 'c', 'b')
    # transparent colors
    cols = colors.colorConverter.to_rgba_array([
        (1, 0, 0, 0.5),
        (1, 1, 0, 0.5),
        (0, 1, 0, 0.5),
        (0, 1, 1, 0.5),
        (0, 0, 1, 0.5)
    ])
    cs = map.contourf(x, y, data, levels, colors=cols)

    # add colorbar.
    global cbar
    if cbar:
        fig.delaxes(cbar)
    cbar = map.colorbar(cs, location='bottom', pad="5%")
    cbar.set_label('mm')

# ------------------------------
# build map

fig = plt.figure()
title_string = "Earthquakes of Magnitude 2.0 or Greater\n"
# title_string += "%s through %s" % (times[-1][:10], times[0][:10])
plt.title(title_string)

ax1 = fig.add_subplot(111)

cbar = None

build_map(9)

#-------------------------------
# save one plot to png
plt.savefig('firstImage.png')

# ------------------------------
# button load file
ax = plt.axes([0, 0.9, 0.1, 0.1])
b = plt.Button(ax, "Load")
b.on_clicked(button_on_clicked)

plt.show()
