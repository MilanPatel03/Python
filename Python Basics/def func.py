def max_num(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:
     return num1
    elif num2 >= num1 and num2 >= num3:
     return num2
    else:
        return num3

maxvar = max_num(33,39,99)

print(maxvar)
    
# code of calculater using def 

var1 = float(input("Enter a num: "))
var2 = float(input("Enter second num: "))

def sum(arg1 , arg2):
    
    print(arg1 + arg2)
    if type(arg1) != type(arg2):
        print("Please enter same type of arg.")
        return
main = sum(var1 , var2)    

print(main)

# A better calculater by using def 

v1 = float(input("Enter a number: "))
o1 = input("Enter operator: ")
v2 = float(input("Enter second number: "))

def calc(num1 , op , num2):

    if op == "+":
        print("summation of given two number is: ", num1 + num2)
    elif op == "-":
        print("subtraction of given two number is: ", num1 - num2)
    elif op == "/":
        print("division of given two number is: ", num1 / num2)
    elif op == "*":
        print("multiplication of given two number is: ", num1 * num2)
    else:
        print("Invalid operator")

var = calc(v1,o1,v2)

print(calc)