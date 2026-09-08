import math

import numpy as np
import matplotlib.pyplot as plt
import math
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])


plt.xlim(0,4 )
plt.ylim(0,100 )
plt.plot(x,y , label = "x^2" , color = "red")
plt.plot(x,y**2 , label = "x^4" , color = "blue")
plt.legend()
plt.title("Simple Plot")
plt.xlabel("x-axis -Axis Powers")
plt.ylabel("y-axis - Axis Powers")
plt.show()