from mpl_toolkits.basemap import Basemap
from matplotlib.widgets import Slider, Button, RadioButtons
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import csv
import CSVLoad
import matplotlib.cm as cmx
import matplotlib.colors as colors


#-----------------------------
#values
filename = 'earthquake.csv'
lats, lons = [], []
mags = []
times = []


#------------------------------
#get values from file
with open(filename) as f:
    reader = csv.reader(f, delimiter=',')
    next(reader, None)  # skip the headers

    for row in reader:
        if row:
            lats.append(float(row[1]))
            lons.append(float(row[2]))
            mags.append(float(row[4]))
            times.append(row[0])


#------------------------------
#colorize
def get_marker_color(mags):
    if mags < 3.0:
        return ('go')
    elif mags < 5.0:
        return ('yo')
    else:
        return ('ro')

#------------------------------
#load file button
def buttonOnClicked(event):
    CSVLoad.openFileDialogCsv()


# LEFT PART OF WINDOW
#------------------------------
#map
fig = plt.figure(figsize=(12,8))
#fig.subplots_adjust(bottom=0.025, left=0.085, top = 0.995, right=0.925)
title_string = "Earthquakes of Magnitude 1.0 or Greater\n"
title_string += "%s through %s" % (times[-1][:10], times[0][:10])
plt.title(title_string)

axMap = fig.add_subplot(111)
axSlider = fig.add_subplot(15,1,15)


map = Basemap(ax=axMap)
#map.etopo() #'contour'
map.drawcoastlines()
map.drawparallels(np.arange(-90.,120.,5.))
map.drawmeridians(np.arange(0.,360.,5.))
plt.xticks([]), plt.yticks([])


#------------------------------
#size/color marking points
msize = 9
for lon, lat, mag in zip(lons, lats, mags):
    x, y = map(lon, lat)
    #msize = mag * min_marker_size
    marker_string = get_marker_color(mag)
    map.plot(x, y, marker_string, markersize=msize)

class DiscreteSlider(Slider):
    """A matplotlib slider widget with discrete steps."""
    def __init__(self, *args, **kwargs):
        """
        Identical to Slider.__init__, except for the new keyword 'allowed_vals'.
        This keyword specifies the allowed positions of the slider
        """
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


#------------------------------
# Slider for every 5 mins
x = np.arange(0, 61, 5) #61 -> 60 has to be included
sStart = DiscreteSlider(axSlider, 'minute', 0, 60, valfmt='%i',allowed_vals=x, valinit=x[0])





# RIGHT PART OF WINDOW
#------------------------------
#button load file
#axbtnLoad = plt.subplot2grid((6,3),(0,2))
#bLoad = plt.Button(axbtnLoad, "Load", color='0.85', hovercolor='0.975')
#bLoad.on_clicked(buttonOnClicked)

#button refresh map
#axbtnFresh = plt.subplot2grid((6,3),(1,2))
#bFresh = plt.Button(axbtnFresh, "Refresh", color='0.85', hovercolor='0.975')
#b.on_clicked(buttonOnClicked)


plt.show()



