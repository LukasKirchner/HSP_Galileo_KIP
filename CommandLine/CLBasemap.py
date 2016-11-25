from mpl_toolkits.basemap import Basemap
from matplotlib.colors import colorConverter


def draw_basemap(config, grid, ax):
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

    m.drawcoastlines()
    m.drawmapboundary()
    m.fillcontinents(color='coral', lake_color='aqua')
    m.drawmapboundary(fill_color='aqua')

    # m.etopo()

    time = config["time"]
    sat = config["sat"]
    lons, lats, data, max_v = grid.get_values(time, sat)
    levels = [0, (max_v / 5) * 1, (max_v / 5) * 2, (max_v / 5) * 3, (max_v / 5) * 4, (max_v / 5) * 5]

    # colors = ('r', 'y', 'g', 'c', 'b')
    # transparent colors
    t = float(config["transparency"])
    colors = colorConverter.to_rgba_array([
        (1, 0, 0, t),
        (1, 1, 0, t),
        (0, 1, 0, t),
        (0, 1, 1, t),
        (0, 0, 1, t)
    ])

    lons, lats = m(lons, lats)
    contour = m.contourf(lons, lats, data, levels, colors=colors, ax=ax)

    return m, contour
