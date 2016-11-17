import ValueGrid as VG
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

file = open("TestData.csv")
grid = VG.load_from_csv(file)

data = grid.get_values(0, 0)

map = Basemap()
map.drawcoastlines()
map.contourf(*data)
plt.show()