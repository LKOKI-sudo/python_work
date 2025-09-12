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
