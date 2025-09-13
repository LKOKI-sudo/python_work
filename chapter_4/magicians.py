# chapter_4/magicians.py
# Created by: LKOKI-SUDO
# Date: 2024-06-18
# Description: A simple program to demonstrate looping through a list of magicians and printing messages.

# Creating a list of magicians
magicians = ['alice', 'david', 'carolina']
# using a for loop to print each magician's name
for magician in magicians:
    print(f"{magician} \n")

# Printing personalized messages for each magician in the for loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}. \n")

# Printing a final message after the loop
print("Thank you, everyone That was a great magic show!")
