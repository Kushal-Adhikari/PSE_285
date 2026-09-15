# Make a prettty plot of sin(x) from -2pi to +2pi

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-2*math.pi, 2*math.pi, 100)
y = np.sin(x)
z = np.zeros_like(x)  


plt.plot(x, y, label='sin(x)', color='blue')
plt.plot(x, z, label='y=0', color='black', linestyle='--')



tick_positions = [-2*math.pi, -3*math.pi/2, -math.pi, -math.pi/2, 0, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi]
tick_labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']

straight_line_x = np.linspace(-3*math.pi/2, 3*math.pi/2, 100)
straight_line_y = np.linspace(1,-1, 100)

plt.plot(straight_line_x, straight_line_y, label='y=-x', color='red', linestyle='--' , linewidth = 2.25 , markersize = 9)
plt.xticks(tick_positions, tick_labels)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
ax = plt.subplot()
ax.xaxis.set_label_coords(0.5, -1.05)
ax.yaxis.set_label_coords(-0.1, 0.5)
ax.ticklabels.set_fontsize(16.5)

plt.legend()
plt.axis ([-2*math.pi, 2*math.pi, -1.1, 1.1])
plt.title('Plot of sin(x)')
plt.show()
