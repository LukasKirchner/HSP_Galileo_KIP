from mpl_toolkits.basemap import Basemap
from matplotlib.widgets import Slider, Button, RadioButtons
from datetime import datetime
import matplotlib.dates as mdates
import numpy as np
import matplotlib.pyplot as plt
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

#------------------------------
#reset axis
def reset(event):
    sStart.reset()
    sEnd.reset()

# LEFT PART OF WINDOW
#------------------------------
#map
fig = plt.figure()
fig.subplots_adjust(bottom=0.025, left=0.085, top = 0.875, right=0.975)
ax1 = plt.subplot2grid((6,3), (0, 0), colspan=2, rowspan=4)
plt.xticks([]), plt.yticks([])
title_string = "Earthquakes of Magnitude 1.0 or Greater\n"
title_string += "%s through %s" % (times[-1][:10], times[0][:10])
plt.title(title_string)

map = Basemap()
map.etopo() #'contour'
map.drawcoastlines()
map.drawparallels(np.arange(-90.,120.,5.))
map.drawmeridians(np.arange(0.,360.,5.))


#------------------------------
#size/color marking points
msize = 9
for lon, lat, mag in zip(lons, lats, mags):
    x, y = map(lon, lat)
    #msize = mag * min_marker_size
    marker_string = get_marker_color(mag)
    map.plot(x, y, marker_string, markersize=msize)


#------------------------------
# start and endtime axes

#fig.autofmt_xdate()
#axStart.fmt_xdata = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')

a0 = 5 #start datetime
f0 = 3 #end datetime

axStart = plt.subplot2grid((6,3),(4,0), colspan=2)
axEnd = plt.subplot2grid((6,3),(5,0), colspan=2)

sStart = Slider(axStart, 'Start', 0.1, 30.0, valinit=a0)
sEnd = Slider(axEnd, 'End', 0.1, 10.0, valinit=f0)

resetax = plt.axes([0.555, 0.3, 0.095, 0.04])
button = plt.Button(resetax, "Reset", color='0.85', hovercolor='0.975')
button.on_clicked(reset)


# RIGHT PART OF WINDOW
#------------------------------
#button load file
axbtnLoad = plt.subplot2grid((6,3),(0,2))
bLoad = plt.Button(axbtnLoad, "Load", color='0.85', hovercolor='0.975')
bLoad.on_clicked(buttonOnClicked)

#button refresh map
axbtnFresh = plt.subplot2grid((6,3),(1,2))
bFresh = plt.Button(axbtnFresh, "Refresh", color='0.85', hovercolor='0.975')
#b.on_clicked(buttonOnClicked)


plt.show()



