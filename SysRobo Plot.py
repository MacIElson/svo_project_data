#!/usr/bin/env python

import numpy as np
from pylab import *
import matplotlib.pyplot as plt

ax=plt.gca()

fig = plt.figure()
ax.clear()

XSqrPts = [2, 16, 16, 2, 2, 16, 16, 2, 2, 19, 19, 1, 0]
YSqrPts = [3, 3, 7, 7, 11, 11, 15, 15, 19, 19, 1, 1, 0]

line = plt.plot(XSqrPts, YSqrPts, 'r-')

fig2 = plt.figure()
ax.clear()
axis('equal')
plt.xlim(0,2)
plt.ylim(0,2)

x = linspace(0,2*pi, 100)

plot (cos(x)+1, sin(x)+1)

plt.show()