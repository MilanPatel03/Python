# giraffe language (Ignore the words "aeiou" and replace with "g, G")

def translate(phrase):

    translation = ""
    for latter in phrase:
        if latter.lower() in "aeiou":
            if latter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"    
            
        else:
            translation = translation + latter
    return translation

var = input("Enter a phrase: ") 

print(translate(var))