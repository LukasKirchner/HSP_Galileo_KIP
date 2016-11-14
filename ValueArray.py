# this code assumes the data in the csv-file is given as individual data points
# like they are in the earthquake.csv file
import datetime


class ValuePoint:
    def __init__(self, t, lat, lon, depth, mag):
        self.t = t
        self.lat = lat
        self.lon = lon
        # values
        self.depth = depth
        self.mag = mag


class ValueArray:
    def __init__(self, feature_points):
        # sort feature_points by time
        self.o_list = sorted(feature_points, key=lambda point: point.t)
        return

    # returns a list of all points between t_from and t_to
    def get_points(self, t_from, t_to):
        return [p for p in self.o_list if t_from < p.t < t_to]

    # returns three lists for easy plotting
    # supported values: "depth", "mag"
    def get_values(self, t_from, t_to, value):
        l = self.get_points(t_from, t_to)

        if value == "depth":
            vals = [v.depth for v in l]
        elif value == "mag":
            vals = [v.mag for v in l]
        else:
            return None

        lats = [v.lat for v in l]
        lons = [v.lon for v in l]

        return lats, lons, vals


def load_from_csv(file):
    # UNTESTED sample code for how to create a FeatureArray, likely doesn't work without adjustments
    # currently tuned to the earthquake.csv file
    def string_to_datetime(str):
        # converts string to a datetime object
        # the mask has to be adjusted according to the actual formatting
        # note that strptime does not support milliseconds

        # remove milliseconds
        str = str[:-5]
        return datetime.datetime.strptime(str, "%Y-%m-%dT%H:%M:%S")

    l = []
    for line in file[1:]:
        line.split(";")
        l.append(
            ValuePoint(
                string_to_datetime(line[0]),  # time
                float(line[1]),  # latitude
                float(line[2]),  # longitude
                float(line[3]),  # depth
                float(line[4])  # magnitude
                # other values...
            )
        )
    return ValueArray(l)
