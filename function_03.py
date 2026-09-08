# Use custom box volume function 
# That will be used when creating a plotfrom 0 to 10
# with all dimensions being the same (cube)
# PLot : volume as a function of cube side

import matplotlib.pyplot as plt

length= [1,2,3,4,5,6,7,8,9,10]
volume = []

def volume_of_box(length):
    return length ** 3

for l in length:
    volume.append(volume_of_box(l))


plt.plot(length, volume, label = "Volume of Cube", color = "blue")
plt.title("Volume of Cube as a function of side length")    
plt.show()
