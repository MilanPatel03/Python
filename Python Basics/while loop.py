# While loop

i = 1

while i <= 10:
    print(i)
    i += 1

print("Done with loop")

# simple guessing game 

secret_word = "Home"
guess = ""

while guess != secret_word:
    guess = input("Enter a secret word: ")

print("You win! ")    