import sys
import ValueGrid
from ConfigParser import RawConfigParser
import CLBasemap as Map
import GetAxis

# check if called correctly
if len(sys.argv) == 4:
    conf = sys.argv[1]
    csv = sys.argv[2]
    out = sys.argv[3]
else:
    # print("got %i arguments" % len(sys.argv))
    # print(sys.argv)
    # sys.stderr.write("CLMain.py <configfile> <csvfile> <outputfile>\n")
    # sys.exit(2)

    conf = "default.cfg"
    csv = "TestData.csv"
    out = "test.out"


__defaults = {
    "projection": "ortho",
    "lon": "0",
    "lat": "0",
    "width": "15000000",
    "height": "15000000",
    "resolution": "c",

    "time": "0",
    "sat": "all",

    "transparency": ".2",
}

config = RawConfigParser(__defaults)
config.read(conf)

grid = ValueGrid.load_from_csv(csv)

# TEMP
ax = GetAxis.get_axis()

m, contour = Map.draw_basemap(dict(config.items("DEFAULT")), grid, ax)

# TEMP
GetAxis.draw()


