import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import colorConverter


def __draw_basemap(config, ax):
    params = {
        "projection" : config["projection"],

        # get the LONgitude and LATitude of the LowerLeft and UpperRight corners of the area to draw
        # "ll_lon" : float(config["ll_lon"]),
        # "ll_lat" : float(config["ll_lat"]),
        # "ur_lon" : float(config["ur_lon"]),
        # "ur_lat" : float(config["ur_lat"]),

        # get the LONgitude and LATitude of the map center, as well as it's width and height
        "lon_0" : float(config["lon"]),
        "lat_0" : float(config["lat"]),
        "width" : float(config["width"]),
        "height" : float(config["height"]),

        "resolution" : config["resolution"]
    }

    if params["projection"] == "ortho":
        # use width/height as map coordinates
        params.update({
            "llcrnrx" : -params["width"]//2,
            "llcrnry" : -params["height"]//2,
            "urcrnrx" : params["width"]//2,
            "urcrnry" : params["height"]//2,
        })
        del(params["width"])
        del(params["height"])

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

    __draw_data(m, data, t)

    draw_func()


def draw_all(config, grid, ax, draw_func):
    m = __draw_basemap(config, ax)
    t = float(config["transparency"])
    count = 0

    for time in grid.times:
        for sat in grid.sats:
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
