# chapter_4 /odd_numbers.py
# Created by: LKOKI-SUDO
# Date: 2024-06-18
# Description: A simple program to generate a list of odd numbers from 1 to 20

odd_numbers = []
for value in range (1, 21, 2) :
    odd_numbers.append(value)

for number in odd_numbers :
    print (number)