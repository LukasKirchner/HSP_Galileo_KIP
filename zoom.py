#
# BaseMap example by geophysique.be
# tutorial 03

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(11.7,8.3))
#Custom adjust of the subplots
plt.subplots_adjust(left=0.05,right=0.95,top=0.90,bottom=0.05,wspace=0.15,hspace=0.05)
ax = plt.subplot(111)
#Let's create a basemap around Belgium
m = Basemap(resolution='i',projection='merc', llcrnrlat=49.0,urcrnrlat=52.0,llcrnrlon=1.,urcrnrlon=8.0,lat_ts=51.0)
m.drawcountries(linewidth=0.5)
m.drawcoastlines(linewidth=0.5)

m.drawparallels(np.arange(49.,53.,1.),labels=[1,0,0,0],color='black',dashes=[1,1],labelstyle='+/-',linewidth=0.2) # draw parallels
m.drawmeridians(np.arange(1.,9.,1.),labels=[0,0,0,1],color='black',dashes=[1,1],labelstyle='+/-',linewidth=0.2) # draw meridians

# Let's add some earthquakes (fake here) :

lon = np.random.random_integers(11,79,1000)/10.
lat = np.random.random_integers(491,519,1000)/10.
depth = np.random.random_integers(0,300,1000)/10.
magnitude = np.random.random_integers(0,100,1000)/10.

# I'm masking the earthquakes present in most of the regions (illustration of masks usage) :
import numpy.ma as ma
Mlon = ma.masked_outside(lon, 5.6, 7.5)
Mlat = ma.masked_outside(lat,49.6,50.6)
lat = ma.array(lat,mask=Mlon.mask+Mlat.mask).compressed()
lon = ma.array(lon,mask=Mlon.mask+Mlat.mask).compressed()
depth =ma.array(depth,mask=Mlon.mask+Mlat.mask).compressed()
magnitude = ma.array(magnitude,mask=Mlon.mask+Mlat.mask).compressed()

x,y = m(lon,lat)
m.scatter(x,y,s=10*magnitude,c=depth)
c = plt.colorbar(orientation='horizontal')
c.set_label("Depth")

# adding a zoom plot :
from mpl_toolkits.axes_grid.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid.inset_locator import mark_inset
from mpl_toolkits.axes_grid.anchored_artists import AnchoredSizeBar

axins = zoomed_inset_axes(ax, 2, loc=2) # zoom = 4
m.scatter(x,y,s=10*magnitude,c=depth)
x,y = m(5.5,50.0)
x2,y2 = m(6.5,50.5)
axins.set_xlim(x,x2)
axins.set_ylim(y,y2)
plt.xticks(visible=False)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.5")
asb = AnchoredSizeBar(axins.transData,
 10000.,
 "10 km",
 loc=4,
 pad=0.1, borderpad=0.25, sep=5,
 frameon=False)
axins.add_artist(asb)

plt.show()
