import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import colorConverter

__max_width = 15000000
__max_height = 15000000


def __clamp(v, min, max):
    if v<min:
        return min
    if v>max:
        return max
    return v


def __draw_basemap(config, ax):
    cylindrical = config["cylindrical"] == "true"
    zoom = 1 - __clamp(float(config["zoom"]), 0, .9)
    lon = __clamp(float(config["lon"]), -180, 180)
    lat = __clamp(float(config["lat"]), -90, 90)
    if zoom < .6:
        res = "l"
    else:
        res = "c"

    # ToDo: resolution
    if cylindrical:
        # clamp lat to be between -90 and +90
        rect = [lon - zoom*180, lat - zoom*90, lon + zoom*180, lat + zoom*90]
        if rect[1] < -90:
            rect[3] -= rect[1] + 90
            rect[1] = -90
        elif rect[3] > 90:
            rect[1] -= rect[3] - 90
            rect[3] = 90

        params = {
            "projection": "cyl",
            "llcrnrlon": rect[0],
            "llcrnrlat": rect[1],
            "urcrnrlon": rect[2],
            "urcrnrlat": rect[3],
            "resolution": res
        }
    else:
        # ToDo: width/height
        x = zoom * __max_width //2
        y = zoom * __max_height // 2
        params = {
            "projection": "ortho",
            "lon_0": float(config["lon"]),
            "lat_0": float(config["lat"]),
            "llcrnrx" : -x,
            "llcrnry" : -y,
            "urcrnrx" : x,
            "urcrnry" : y,
            "resolution": res
        }

    # ======= Draw Map ========
    m = Basemap(ax=ax, **params)

    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='coral', lake_color='aqua', zorder=0, alpha=0.5)
    m.drawcoastlines()

    # m.etopo()
    # m.bluemarble()
    # m.shadedrelief()
    # m.drawlsmask()

    return m


def __draw_data(m, data, transparency=.5):
    ax = m.ax

    colors = colorConverter.to_rgba_array([
        (1, 0, 0, transparency),
        (1, 1, 0, transparency),
        (0, 1, 0, transparency),
        (0, 1, 1, transparency),
        (0, 0, 1, transparency)
    ])

    lons, lats, data, max_v = data
    lons, lats = m(lons, lats)
    levels = [0, (max_v / 5) * 1, (max_v / 5) * 2, (max_v / 5) * 3, (max_v / 5) * 4, (max_v / 5) * 5]

    contour = m.contourf(lons, lats, data, levels, colors=colors, ax=ax)

    return contour


def draw_one(config, grid, ax, draw_func):
    m = __draw_basemap(config, ax)
    t = float(config["transparency"])

    time = config["time"]
    sat = config["sat"]
    data = grid.get_values(time, sat)

    contour = __draw_data(m, data, t)
    m.colorbar(contour, location='bottom', pad="5%")
    plt.title("Time: %s - Sat: %s" % (time, sat))

    draw_func()


def draw_all(config, grid, ax, draw_func):
    m = __draw_basemap(config, ax)
    t = float(config["transparency"])
    count = 0

    sats = [config["sat"]]
    if sats[0] == "all":
        sats = grid.sats

    times = config["time"]
    if times[0] == "all":
        times = grid.times
    else:
        times = [float(times)]

    for time in times:
        for sat in sats:
            count += 1

            data = grid.get_values(time, sat)

            contour = __draw_data(m, data, t)
            cbar = m.colorbar(contour, location='bottom', pad="5%")
            plt.title("Time: %s - Sat: %s" % (time, sat))

            draw_func()

            # remove contour and colorbar
            for x in contour.collections:
                x.remove()
            cbar.remove()

    return count
