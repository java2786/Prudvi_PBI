# playlist = ["Vande matram", "Jai ho", "Mera bharat mahan", "Vande matram", "Jai ho"] # 3
# print("Total Songs:",len(playlist))

# friends = ["Ramesh", "Mukesh", "Ramesh"] # 2 people
# print(f"Invited: {len(friends)}")

# Remove duplicate values and does not contain index/sequence 
# use {} instead of [], set instead of list
playlist = {"Vande matram", "Jai ho", "Mera bharat mahan", "Vande matram", "Jai ho"} # 3
print("Total Songs:",len(playlist))

friends = {"Jitesh", "Ramesh", "Mukesh", "Ramesh"} # 2 people
print(f"Invited: {len(friends)}")

dummy_list = []
print("[] type:",{type(dummy_list)})
print("{} type:",type(friends))

print("="*15)

# add new friend to the invitation list
friends.add("Mukesh")
friends.add("Dinesh")
friends.remove("Mukesh")

print(f"Invited: {len(friends)}")
print(friends)



# find difference b/w shallow copy and deep copy
# print all the values stored in set one by one