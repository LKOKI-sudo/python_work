# chapter 4 / looping_through_a_slice.py
# Created by: LKOKI-SUDO
# Date: 2024-06-18
# Description: A simple program to loop through a slice.

players = [ 'charles' , 'martina' , 'michael' , 'florence' , 'eli' ]

print ("Here are the first three players on my team:")
for player in players[:3]:
    print (player.title())