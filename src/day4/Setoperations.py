friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

#Intersection
shared_interests = friend_a & friend_b

#Union
all_interests = friend_a | friend_b

#Difference
unique_to_a = friend_a - friend_b

print("Shared interests:", shared_interests)
print("All interests:", all_interests)
print("Unique to Friend A:", unique_to_a)
