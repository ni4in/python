from manim import *
import numpy as np

class Graph(Scene):
    def construct(self):
        ax = Axes(x_range = [0,10], y_range=[0,50,10], x_length = 6,y_length=6).add_coordinates()
        labels = ax.get_axis_labels(x_label='n', y_label='f(n)')
        log = ax.plot(lambda x:np.log(1+x),color='GREEN')
        self.add(ax,log,labels)
2