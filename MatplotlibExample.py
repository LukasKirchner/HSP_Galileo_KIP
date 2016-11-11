from mpl_toolkits.basemap import Basemap
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
#build map
fig = plt.figure()
title_string = "Earthquakes of Magnitude 1.0 or Greater\n"
title_string += "%s through %s" % (times[-1][:10], times[0][:10])
plt.title(title_string)

map = Basemap()
#map = Basemap(projection='robin',lon_0=0,resolution='c') #plt.title("Robinson Projection")

map.etopo() #'contour'
#map.bluemarble() #'satellite'

# draw coastlines, parallels and meridians.
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

ax = plt.axes([0,0.9,0.1,0.1])

#------------------------------
#button load file
b = plt.Button(ax, "Load")
b.on_clicked(buttonOnClicked)


plt.show()

