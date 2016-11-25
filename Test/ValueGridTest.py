import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import addcyclic

import CommandLine.ValueGrid as VG

grid = VG.load_from_csv("TestData.csv")

lons, lats, data, _ = grid.get_values(0, 0)


print(lons.shape, lats.shape, data.shape)

map = Basemap()
map.drawcoastlines()

map.contourf(lons, lats, data)
plt.show()