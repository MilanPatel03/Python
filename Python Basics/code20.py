def string_bits(strn):
    result = ""

    for latter in strn:
        if latter.lower() in "aeiou":
            result = latter + result
            return result


var = input("Enter a sting: ")

print(string_bits(var))

