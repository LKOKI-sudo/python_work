# first we create a list of guests
guest_list = [ 'albert' , "bach" , 'mandela' ]
# than we print invitation messages for each guest
print (f"Dear {guest_list[0].title()}, you are invited to dinner.")
print (f"Dear {guest_list[1].title()}, you are invited to dinner.")
print (f"Dear {guest_list[2].title()}, you are invited to dinner.")
# now we change the guest list
print ("Unfortunately, Bach can't make it to dinner.")
# we replace Bach with Maradona in the list 
# which is at index 1
guest_list[1] = 'maradona'
# then we print the new set of invitation messages
print (f" Dear {guest_list[0].title()} you are invited to dinner.")
print (f" Dear {guest_list[1].title()} you are invited to dinner instead of bach.")
print (f" Dear {guest_list[2].title()} you are invited to dinner.")
# now lets instert new guests
print ("Good news! We found a bigger dinner table.")
# we use insert() method to add a new guest at the beginning of the list
guest_list.insert(0, "nugzari") 
# we use insert() method to add a new guest in the middle of the list
guest_list.insert(2, "mishku")
# we use append() method to add a new guest at the end of the list
guest_list.append("gigi")
# now we print a new set of invitation messages
print (f" Dear {guest_list[0].title()} you are invited to dinner.")
print (f" Dear {guest_list[1].title()} you are invited to dinner.")
print (f" Dear {guest_list[2].title()} you are invited to dinner.")
print (f" Dear {guest_list[3].title()} you are invited to dinner.")
print (f" Dear {guest_list[4].title()} you are invited to dinner.")
print (f" Dear {guest_list[5].title()} you are invited to dinner.")