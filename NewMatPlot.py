from mpl_toolkits.basemap import Basemap, cm
from matplotlib.widgets import Slider
import numpy as np
import matplotlib.pyplot as plt
import csv
import CSVLoad
import matplotlib.cm as cmx
import matplotlib.colors as colors
import ValueGrid as VG

#-----------------------------
#values
filename = 'earthquake.csv'
lats, lons = [], []
mags = []
times = []

xs, ys = [], []

plot_handle = None

#------------------------------
#get values from file
def getValuesFromFile(filename):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)  # skip the headers

        for row in reader:
            if row:
                lats.append(float(row[1]))
                lons.append(float(row[2]))
                mags.append(float(row[4]))
                times.append(row[0])

getValuesFromFile(filename)

#------------------------------
#colorize
def get_marker_color(mags):
    if mags < 3.0:
        return ('go')
    elif mags < 5.0:
        return ('yo')
    else:
        return ('ro')

def redrawMap():
    #global plot_handle, xs, ys
    # When changing the data, change the xdata and ydata and redraw
    #for x,y in xs, ys:
    #plot_handle.remove()

    #plot_handle.set_xdata([])
    #plot_handle.set_ydata([])
    #plot_handle.set_ydata(ys)
    #plot_handle.set_xdata(xs)

    global ax1
    global axSlider
    global fig
    fig.delaxes(ax1)
    ax1 = fig.add_subplot(111)
    axSlider = fig.add_subplot(15,1,15)
    fig.canvas.draw()



#------------------------------
#load file button
def buttonOnClicked(event):
    global filename
    filename = CSVLoad.openFileDialogCsv()
    # clear arrays, so that the old values disappear
    global lats, lons
    lats, lons = [], []
    global mags
    mags = []
    global times
    times = []
    getValuesFromFile(filename)
    redrawMap()
    buildMap(10)

    # code replication because of on_clicked event does not work otherwise
    ax = plt.axes([0, 0.9, 0.1, 0.1])
    b = plt.Button(ax, "Load")
    b.on_clicked(buttonOnClicked)

    plt.show()


#------------------------------
#build map

fig = plt.figure()
title_string = "Earthquakes of Magnitude 2.0 or Greater\n"
title_string += "%s through %s" % (times[-1][:10], times[0][:10])
plt.title(title_string)

ax1 = fig.add_subplot(111)
axSlider = fig.add_subplot(15,1,15)

cbar = None
def buildMap(markerSize):

    map = Basemap(ax=ax1)
    #map = Basemap(projection='robin',lon_0=0,resolution='c') #plt.title("Robinson Projection")

    map.etopo() #'contour'
    #map.bluemarble() #'satellite'

    # draw coastlines, parallels and meridians.
    map.drawcoastlines()
    map.drawparallels(np.arange(-90.,120.,5.))
    map.drawmeridians(np.arange(0.,360.,5.))

    #------------------------------
    #size/color marking points
    msize = markerSize
    global plot_handle

    global xs, ys
    xs, ys = [], []
    for lon, lat, mag in zip(lons, lats, mags):
        x, y = map(lon, lat)
        xs.append(x)
        ys.append(y)
        #msize = mag * min_marker_size
        marker_string = get_marker_color(mag)
        plot_handle,= map.plot(x, y, marker_string, markersize=msize)

    # draw filled contours.

    mag_max = np.amax(mags)
    levels = [0, (mag_max/5)*1, (mag_max/5)*2, (mag_max/5)*3, (mag_max/5)*4, (mag_max/5)*5]

    #global filename
    #grid = VG.load_from_csv(filename)
    #x_new_array, y_new_array, data_new_array = grid.get_values(0, 0)
    # cs = map.contourf(x_new_array, y_new_array, data_new_array, levels,colors = ('r', 'y', 'g', 'c', 'b'))

    # TODO: use real data of csv
    data = [[y * x for x in range(360 // 5)] for y in range(180 // 5)]
    x, y = len(data[0]), len(data)
    X,Y = map.makegrid(x, y)
    cs = map.contourf(X, Y, data, levels, colors=('r', 'y', 'g', 'c', 'b'))

    # add colorbar.
    global cbar
    if cbar:
        fig.delaxes(cbar)
    cbar = map.colorbar(cs, location='bottom', pad="5%")
    #cbar.set_label('mm')

buildMap(9)


#fig.add_subplot(221)   #top left
#fig.add_subplot(222)   #top right
#fig.add_subplot(223)   #bottom left
#fig.add_subplot(224)   #bottom right 



class DiscreteSlider(Slider):
    def __init__(self, *args, **kwargs):
        self.allowed_vals = kwargs.pop('allowed_vals',None)
        self.previous_val = kwargs['valinit']
        Slider.__init__(self, *args, **kwargs)
        if self.allowed_vals==None:
            self.allowed_vals = [self.valmin,self.valmax]

    def set_val(self, val):
        discrete_val = self.allowed_vals[abs(val-self.allowed_vals).argmin()]
        xy = self.poly.xy
        xy[2] = discrete_val, 1
        xy[3] = discrete_val, 0
        self.poly.xy = xy
        self.valtext.set_text(self.valfmt % discrete_val)
        if self.drawon: 
            self.ax.figure.canvas.draw()
        self.val = val
        if self.previous_val!=discrete_val:
            self.previous_val = discrete_val
            if not self.eventson: 
                return
            for cid, func in self.observers.iteritems():
                func(discrete_val)


x = np.arange(0, 61, 5) #61 -> 60 has to be included
sStart = DiscreteSlider(axSlider, 'minute', 0, 60, valfmt='%i',allowed_vals=x, valinit=x[0])



# ------------------------------
# button load file
ax = plt.axes([0,0.9,0.1,0.1])
b = plt.Button(ax, "Load")
b.on_clicked(buttonOnClicked)

plt.show()
