
cubes = [x ** 3 for x in range(10)]
add_cubes1 = filter(lambda x: x % 2 == 0, cubes)

add_cubes2 = (cube for cube in cubes if cube % 2 == 0)

print(list(add_cubes1) == list(add_cubes2))  # prints: True