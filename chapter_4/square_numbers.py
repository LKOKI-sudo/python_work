#chapter_4/square_numbers.py
# Created by: LKOKI-SUDO
# Date: 2024-06-18
# Description: A simple program to demonstrate looping through a list of square numbers and printing messages.

# Creating a list of square numbers using a for loop
squares = []
for value in range (1, 11):
    square = value ** 2
    squares.append(square)
print (squares)

# to write the same program in a shorter way
squares = []
for value in range (1, 11):
    squares.append(value ** 2)
print (squares)


# smiple program to find the minimum, maximum and sum of a list of square numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print (min(digits))
print (max(digits))
print (sum(digits))