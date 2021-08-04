# Basics of for loop and other

A = [0,1,2,3,4,5] #List
B = (0,1,2,3,4,5) #Tuples
C = {0,1,2,3,4,5} #Set
D = "012345"

E = {
    "name" : "Milan",   # FORM - "keys" : "values"
    "age" : 20
}

# in operator 

print(1 in B)
print(3 in C)

for x in A:
    print(x)

# In a Dictionary

for x in E.keys():
    print(x)

for x in E.values():
    print(x)

for x in E.items():
    print(x)
    