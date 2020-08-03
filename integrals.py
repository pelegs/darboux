#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


def draw_rects(ax, a, b, N, f,
               mode='min', color='red'):
    dx = (b-a)/N
    for i in range(N+1):
        if mode == 'min':
            h = min(f(a+i*dx), f(a+(i+1)*dx))
        elif mode == 'max':
            h = max(f(a+i*dx), f(a+(i+1)*dx))
        else:
            raise ValueError('Bla')
        rect = patches.Rectangle((a+i*dx, 0), dx, h,
                                 color=color)
        ax.add_patch(rect)
    return ax


xmin, xmax = 0, 3.5
x = np.arange(xmin, xmax, 0.01)
f = lambda z: np.sin(z) * (z**2 - 2*z + 3)
y = f(x)

fig = plt.figure()
ax = plt.axes(xlim=(xmin, xmax))

ax = draw_rects(ax, 0.5, 2.5, 5, f,
                mode='max', color='red')
ax = draw_rects(ax, 0.5, 2.5, 5, f,
                mode='min', color='blue')
plt.plot(x, y, color='black')
plt.show()
