# Function to calculate the volume of a sphere




import math 


def volume_of_sphere(radius):   
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    else:
        volume = (4/3) * math.pi * (radius ** 3)
        return volume

input_radius = float(input("Enter the radius of the sphere: "))

print(f"The volume of the sphere with radius {input_radius} is {volume_of_sphere(input_radius)}")
print(math.pi)