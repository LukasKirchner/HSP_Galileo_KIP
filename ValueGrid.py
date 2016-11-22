# this code assumes the data in the csv-file is given as a grid of values
import numpy as np
from itertools import groupby


def _fold_cube(cube, func):
    '''
    # without numpy
    res = []
    for lon in range(len(cube[0])):
        row = []
        for lat in range(len(cube[0, 0])):
            col = []
            for slice in cube:
                col.append(slice[lon, lat])#.val)
            row.append(func(col))
        res.append(row)
    return res
    '''
    return [[func(col) for col in np.rollaxis(m, 1)] for m in np.rollaxis(cube, 1)]


def comb_func(comb):
    if comb == "avg":
        return lambda l: sum(l) / float(len(l))
    elif comb == "min":
        return min
    elif comb == "max":
        return max
    elif comb == "sum":
        return sum
    else:
        # default: identity
        return lambda i: i


def val_func(val):
    if val == "val":
        return lambda v: v.val
    else:
        # default: identity
        return lambda i: i


class ValuePoint:
    def __init__(self, sat, t, lat, lon, val):
        self.sat = sat
        self.t = t
        self.lat = lat
        self.lon = lon
        # values
        self.val = val

    def __repr__(self):
        return "(%.1f, %.1f, %.0f, %.0f, %.2f)" % (self.sat, self.t, self.lat, self.lon, self.val)


class ValueGrid:
    lons, lats = np.arange(-180, 185, 5), np.arange(-90, 95, 5)
    lons, lats = np.meshgrid(lons, lats)

    def __init__(self, feature_points):
        # sort feature_points by time
        l = sorted(feature_points, key=lambda point: (point.t, point.sat, point.lon, point.lat))

        # grid[time][sat] => matrix[lat][lon] => ValuePoint
        # this assumes there's data for every satellite in every timestamp
        self.grid = [[[[point
                      for point in lons]
                      for _, lons in groupby(sat, lambda p: p.lon)]
                      for _, sat in groupby(row, lambda p: p.sat)]
                      for _, row in groupby(l, lambda p: p.t)]

        # extend each grid by 1 using the first element (loop around)
        for c in self.grid:
            for m in c:
                for r in m:
                    r.append(r[0])
                m.append(m[0])

        self.grid = np.array(self.grid)

        # sorted list of every timestamp
        self.times = [t[0, 0, 0].t for t in self.grid]
        # sorted list of every satellite
        self.sats = [s[0, 0].sat for s in self.grid[0]]

        return

    def time_index(self, time):
        # returns the array index of time
        return self.times.index(time)

    def sat_index(self, sat):
        # returns the array index of sat
        return self.sats.index(sat)

    # returns three matrices for easy plotting
    def get_values(self, time, sat="all", val='val', comb='avg'):
        # if sat = "all" , it returns a combination of all satellites, defined by comb
        # otherwise has to be a valid sat identifier
        # val defines which value to get (currently only supports "val")

        tid = self.time_index(time)
        vf = val_func(val)

        if sat == "all":
            a_vals = np.array([[[vf(x) for x in row] for row in grid] for grid in self.grid[tid]])
            vals = np.array(_fold_cube(a_vals, comb_func(comb)))
        else:
            sid = self.sat_index(sat)
            vals = np.array([[vf(x) for x in row] for row in self.grid[tid][sid]])

        return ValueGrid.lons, ValueGrid.lats, vals

    def __str__(self):
        return "ValueGrid: "+str(self.times)+", "+str(self.sats)


def load_from_csv(filename):
    # sample code for how to create a FeatureMatrix
    # currently tuned to the TestData.csv file, so it will need to be rewritten for actual data

    # converts every line into a list of floats and uses these as arguments for creating a new ValuePoint
    with open(filename) as file:
        l = [ValuePoint(*(float(v) for v in line.split(";"))) for line in file]
    return ValueGrid(l)
