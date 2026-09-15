# Use custom box volume function 
# That will be used when creating a plotfrom 0 to 10
# with all dimensions being the same (cube)
# PLot : volume as a function of cube side

import matplotlib.pyplot as plt
import math
import numpy as np

length= np.linspace(0,1,100)
volume_of_sphere_list = []
volume_of_box_list = []
volume_of_cube_list = []

def volume_of_cube(length):
    return length ** 3

def volume_of_sphere(radius):   
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def volume_of_box(length):
    return length * 2 * length * 3 * length

# Because the width is twice the length and the height is three times the length

for l in length:
    volume_of_sphere_list.append(volume_of_sphere(l))
    volume_of_box_list.append(volume_of_box(l))
    volume_of_cube_list.append(volume_of_cube(l))

plt.plot(length, volume_of_sphere_list, label = "Volume of Sphere", color = "red")
plt.plot(length, volume_of_box_list, label = "Volume of Box", color = "green")
plt.plot(length, volume_of_cube_list, label = "Volume of Cube", color = "blue")
plt.title("Volume as a function of side length")    
plt.show()
