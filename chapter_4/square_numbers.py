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