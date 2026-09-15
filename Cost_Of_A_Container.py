# A tank that holds 100,000
# Shape is cylindrical with hemisphere top
# Cylindrrical part is 500 usd per meter square
# The hemispherical part is 600 usd per meter square

# Hemisphere area = 2 * pi * r^2
# cylindrical_area = 2 * 3.14 * r * h 

# 2 * pi * r^2 + 2 * 3.14 * r * h = 100,000
# pi *r*r *h + 2/3 * pi * r*r*r = 100,000
# pi *r*r(h + 2/3 * r) = 100,000
# h = 100,000/(pi * r * r) - 2/3 * r

# Height is changing from 1 to 10 meters
# radius is changing with the height
# We need to find the cost of the hemispherical part and the cylindrical part as a function of radius and height.





import matplotlib.pyplot as plt
import numpy as np
import math 


height = np.linspace(1, 10, 10)
Hemispherical_area_cost  = []
Cylindrical_area_cost = []
Total_cost = []

radius = []
for h in height:
    
    r = 100000/(math.pi * h * h) - 2/3 * h
    radius.append(r)

for r in radius:
    hemispherical_cost = 2 * math.pi * r * r * 600
    cylindrical_cost = 2 * math.pi * r * height[0] * 500
    total_cost = hemispherical_cost + cylindrical_cost
    Hemispherical_area_cost.append(hemispherical_cost)
    Cylindrical_area_cost.append(cylindrical_cost)
    Total_cost.append(total_cost)





plt.plot(radius, Hemispherical_area_cost, label = "Hemispherical Area Cost", color = "red") #Prompt 1
plt.plot(radius, Cylindrical_area_cost, label = "Cylindrical Area Cost", color = "blue")   # Prompt 2
plt.plot(radius, Total_cost, label = "Total Cost", color = "green") #Prompt 3
plt.title("Cost of a Container as a function of radius")
plt.show()
