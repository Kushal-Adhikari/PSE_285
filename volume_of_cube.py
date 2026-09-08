length = float(input("Enter the length of the cube: "))
breadth = float(input("Enter the breadth of the cube: "))
height = float(input("Enter the height of the cube: "))
def volume_of_box(length, breadth, height):
    return length * breadth * height
print(f"The volume of the cube with length {length} is {volume_of_box(length, breadth, height)}")
