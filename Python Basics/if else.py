# if else 

is_male = True
is_tall = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

# elif statement

print("\n")

if is_male and is_tall:
    print("You are a tall male")

elif is_male and not(is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")

else:
    print("You are not male and tall")
