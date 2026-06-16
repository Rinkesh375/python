import math

def get_circle_measurements(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = get_circle_measurements(3)

print("Area:", round(area,2))
print("Circumference:", circumference)