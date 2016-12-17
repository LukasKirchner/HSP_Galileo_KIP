import sys
import ValueGrid
from ConfigParser import RawConfigParser
import CLBasemap as Map
import GetAxis
import os

# check if called correctly
if len(sys.argv) == 4:
    conf = sys.argv[1]
    csv = sys.argv[2]
    out = sys.argv[3]
else:
    # print("got %i arguments" % len(sys.argv))
    # print(sys.argv)
    # sys.stderr.write("CLMain.py <configfile> <csvfile> <outputpath>\n")
    # sys.exit(2)

    conf = "new.cfg"
    csv = "TestData.csv"
    out = "Image"


__defaults = {
    # "projection": "ortho",
    "cylindrical": "true",
    "lon": "0",
    "lat": "0",
    "zoom": "0",
    # "width": "15000000",
    # "height": "15000000",
    # "resolution": "c",

    "time": "all",
    "sat": "all",

    "transparency": ".2",
}

# clear output folder
for file in os.listdir(out):
    filepath = os.path.join(out, file)
    os.unlink(filepath)

config = RawConfigParser(__defaults)
config.read(conf)

time = config.get("DEFAULT", "time")
sat = config.get("DEFAULT", "sat")
grid = ValueGrid.load_from_csv(csv)

ax = GetAxis.get_axis()

# closure to automatically name each file
def __draw():
    class c:
        i = 0

    def draw():
        GetAxis.draw("%s/_%i.png" % (out, c.i))
        c.i += 1
    return draw

# Map.draw_one(dict(config.items("DEFAULT")), grid, ax, __draw())
count = Map.draw_all(dict(config.items("DEFAULT")), grid, ax, __draw())

# return the number of created images
# alternative: jsp:redirect stdout, write count to stdout
# sys.exit(count)




