cube = lambda a: a**3


print(cube(3))

print(cube(5))

print(cube(7))

print(cube(5))

print(cube(1))




"***********************************************************************************"


numbers = [1, 2, 3, 4]

cubes = list(map(lambda x: x**3, numbers))
print(cubes)