# this is place.py
# created by LKOKI-SUDO
# this program demonstrates the use of sorted() and reverse() methods


# we create a list of places & then we print the original list
places = [ 'paris', 'new york' , 'tokyo', 'tbilisi', 'sydney']
print(f"\nOriginal list: \n{places}")

# creating sorted list variable using  sorted() method
sorted_places = sorted(places)
print(f"\nSorted list: \n{sorted_places}")

# shows that the original list is unaltered
print(f"\nOriginal list again: \n{places}")

# creating sorted list variable in reverse order or sorted() method with reverse=True argument
sorted_places_reverse = sorted(sorted_places, reverse = True)
print(f"\nSorted list in reverse order: \n {sorted_places_reverse}")

# this shows again that the original list is unaltered
print (f"\nOriginal list again: \n{places}")

# this is the reverse() method which reverses the original list permanently
places.reverse()
print(f"\nReversed list: \n{places}")

# this again reverses the list to its original order
places.reverse()
print(f"\nReversed again to original list order: \n{places}")

# this method sorts the original list permanently in alphabetical order
places.sort()
print(f"\nOriginal list sorted permanently in alphabetical order: \n{places}")

# this method sorts the original list permanently in reverse alphabetical order
places.sort(reverse = True)
print(f"\nOriginal list sorted permanently in reverse alphabetical order: \n{places}")
