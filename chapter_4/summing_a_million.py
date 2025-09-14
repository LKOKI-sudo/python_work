# chapter_4 /summing_a_million.py
# Created by: LKOKI-SUDO
# Date: 2024-06-18
# Description: A simple program to generate a list of one million numbers and compute their sum.

one_million = []
for value in range (1, 1_000_001) :
    one_million.append(value)

print (min(one_million))
print (max(one_million))
print (sum(one_million))