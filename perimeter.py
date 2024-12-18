import math

def circle_area_perimeter(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

radius = 5
area, perimeter = circle_area_perimeter(radius)
print("Area:", area)
print("Perimeter:", perimeter)
