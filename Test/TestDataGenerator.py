# generates a csv file filled with test data
# ToDo: generate reasonable data (currently fills with random values)

import random

fileName = "TestData.csv"
satellites = [0, 1, 2]
times = [0., 1., 2., 3., 4.]

file = open(fileName, "w")

def one_per_value():
    for s in satellites:
        for t in times:
            for lon in range(-180, 180, 5):
                for lat in range(-90, 91, 5):
                    line = "%s;%.1f;%.1f;%.1f;%.1f\n" % (s, t, lon, lat, random.random())
                    # print(line)
                    file.write(line)


def one_per_satellite_and_time():
    for s in satellites:
        for t in times:
            file.write("%s;%.1f;" % (s, t))
            for lon in range(-180, 180, 5):
                for lat in range(-90, 91, 5):
                    file.write("%f;" % 0.5)
            file.write("\n")

one_per_value()