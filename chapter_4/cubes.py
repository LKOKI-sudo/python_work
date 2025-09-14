# chapter 4 / cubes.py
# Created by: LKOKI-SUDO
# Date: 2024-06-18
# Description: A simple program to write comprehensions that generate a list of cubes.

cubes = []
for value in range (1, 11) :
    cube = value ** 3
    cubes.append(cube)

for number in cubes :
    print (number)
