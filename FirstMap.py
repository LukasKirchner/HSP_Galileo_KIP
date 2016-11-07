from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv

#------------------------------
#get values from file
with open('earthquake.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader, None)  # skip the headers
    lons = []
    lats = []
    for row in reader:
        if row:
            lat = row[1]
            lon = row[2]
            lons.append(lon)
            lats.append(lat)


#------------------------------
#build map
map = Basemap()
#map = Basemap(projection='robin',lon_0=0,resolution='c') #plt.title("Robinson Projection")

map.etopo() #'contour'
#map.bluemarble() #'satellite'

# draw coastlines, parallels and meridians.
map.drawcoastlines()
map.drawparallels(np.arange(-90.,120.,5.))
map.drawmeridians(np.arange(0.,360.,5.))



x,y = map(lons, lats)

map.plot(x, y, 'bo', markersize=8)    

#v = [[i+j for i in y] for j in x]

#X, Y = map.makegrid(len(v[0]), len(v))

#map.contour(X, Y, v)   

#ax = plt.axes([0.45,0.90,.1,.1])

#def print_hello(event):
#	print("Hello", event)
	#file dialog
	#update map

#b = plt.Button(ax, "Load csv")
#b.on_clicked(print_hello)
plt.show()
