# chapter_4/one_million.py
# Created by: LKOKI-SUDO
# Date: 2024-06-18
# Description: A simple program to generate a list of one million numbers and demonstrate basic list operations

one_million = []
for value in range(1, 1_000_001):
    one_million.append(value)

# Print the value in the list one at the time
for number in one_million :  
    print(number)
