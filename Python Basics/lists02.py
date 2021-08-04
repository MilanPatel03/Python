#

fav_numbers = [3,93,73,333,31]

fav_actvt = ["learn", "read", "play", "play", "yoga", "exercise"]

# sorting list (.sort)

fav_numbers.sort()
print(fav_numbers)

# Merging 2 lists 1 list (.extend)

fav_actvt.extend(fav_numbers)

print(fav_actvt)

# Add something in list (.append)

fav_actvt.append("meditation")


#

# Add perticuler positon in list (.insert) 

fav_actvt.insert(1, "Fun")

print(fav_actvt)

# For remove element (.remove)

fav_actvt.remove("yoga")
print(fav_actvt)

# For empty list (.clear)

fav_numbers.clear()
print(fav_numbers)

# Know the position no. (.index)

print(fav_actvt.index("play"))

# Know how many time repeat the one word (.count)

print(str(fav_actvt.count("play")) + " time repeat")

# (.reverse)

fav_actvt.reverse()
print(fav_actvt)

# Make a COPY of List (.copy)

my_actvt = fav_actvt.copy()
print(my_actvt)  



