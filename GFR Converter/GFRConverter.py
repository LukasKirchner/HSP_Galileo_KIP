# Converts a file with format "lat, lon, val" into "sat; time; lon; lat; val"
# Assumes the input file ranges from lat = (-85, +85), lon = (-175, +180)
# and converts/pads it to fit range lat = (-90, +90), lon = (-180, +175)
# since the input is a single sat/time pair, sat and time in the output file will noth be 0

import sys


in_file = "E08.csv"
out_file = "E08_conv.csv"

# optional command line usage
if len(sys.argv) == 3:
    in_file = sys.argv[1]
    out_file = sys.argv[2]

data = []

# read input
with open(in_file) as file:
    for line in file:
        sa = line.split(",")
        lat, lon, val = float(sa[0]), float(sa[1]), float(sa[2])
        # rearrange lon == 180
        if lon == 180:
            lon = -180
        data.append((lon, lat, val))
        pass

# insert missing lat = +/- 90
for lon in range(-180, 180, 5):
    data.append((lon, 90, 0))
    data.append((lon, -90, 0))

# resort data by lon>lat
data = sorted(data)

# write to output file
with open(out_file, "w") as file:
    for d in data:
        # write in form "sat; time; lon; lat; val"
        line = "%s;%.1f;%.1f;%.1f;%.1f\n" % ("0", 0, d[0], d[1], d[2])
        file.write(line)
    pass
