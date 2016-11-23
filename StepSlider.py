import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

class ChangingPlot(object):
    def __init__(self):
        self.draw_counter = 0
        x = np.logspace(0, 1, 10)

        self.fig, self.ax = plt.subplots()
        self.sliderax     = self.fig.add_axes([0.2, 0.02, 0.6, 0.03],axisbg='yellow')
        self.slider       = DiscreteSlider(self.sliderax,'Value', 0, 10,\
                                           allowed_vals=x, valinit=x[0])

        self.slider.on_changed(self.update)

        self.ax.plot(x, x, 'ro')
        self.dot, = self.ax.plot(x[0], x[0], 'bo', markersize=18)
        self.text = self.ax.text(2,8,str(self.draw_counter))

    def update(self, value):
        self.draw_counter += 1
        self.dot.set_data([[value],[value]])
        self.text.set_text(str(self.draw_counter)+' draws, value = '+str(value))
        self.fig.canvas.draw() # <--- Add this line

    def show(self):
        plt.show()

class DiscreteSlider(Slider):
    """A matplotlib slider widget with discrete steps."""
    def __init__(self, *args, **kwargs):
        """
        Identical to Slider.__init__, except for the new keyword 'allowed_vals'.
        This keyword specifies the allowed positions of the slider
        """
        self.allowed_vals = kwargs.pop('allowed_vals',None)
        self.previous_val = kwargs['valinit']
        Slider.__init__(self, *args, **kwargs)
        if self.allowed_vals==None:
            self.allowed_vals = [self.valmin,self.valmax]

    def set_val(self, val):
        discrete_val = self.allowed_vals[abs(val-self.allowed_vals).argmin()]
        xy = self.poly.xy
        xy[2] = discrete_val, 1
        xy[3] = discrete_val, 0
        self.poly.xy = xy
        self.valtext.set_text(self.valfmt % discrete_val)
        if self.drawon: 
            self.ax.figure.canvas.draw()
        self.val = val
        if self.previous_val!=discrete_val:
            self.previous_val = discrete_val
            if not self.eventson: 
                return
            for cid, func in self.observers.iteritems():
                func(discrete_val)

p = ChangingPlot()
p.show()
