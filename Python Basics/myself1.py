varr = input("Enter a programming language you know: ")

if varr == "python":
    print("Yess. it is most populer pro lan.")
else:
    print("I dont know about it actually!")   

# Dictionaries

prolan = {

    "python" : "It is most populer programming language",
    "R" : "It is statasctical programming language",
    "java" : "It is oop language",
    "html" : "It is markup language for web devlopment",
    "css" : "It is used for style the website",
    "javascript" : "It is nice programming language",
    "swift" : "It is for IOS devlopers",
    "C" : "It is basic old programming language",
    "C++" : "It is deep language",
    "C#" : "It is game devloping progrmming language",
    "fortran" : "It is very old programming language",
    "Kotlin" : "It is android app devloping language",
    "GO" : "It is programming language by google",

}

var = input("Enter a programming language you know: ")

print(prolan.get(var, "Not a valid key"))

# OR We can use method below

print("\n")
print(prolan["html"])

# Update dictionary

prolanup = {
    "Dart" : "programming lang",
    "Ruby" : "Worst language",
}

prolan.update(prolanup)

print(prolan.get(var, "Not a valid key"))

#print(prolan)