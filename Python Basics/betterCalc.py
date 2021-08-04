# Building a better calculater:

num1 = float(input("Enter a number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print( num1 + num2 )
elif op == "-":
    print( num1 - num2 )
elif op == "*":
    print( num1*num2 )
elif op == "/":
    print( num1/num2 )    
else:
    print("Invalid operator")            

# math of raise to power

def raise_to_power(base_num, pow_num):

    result = 1

    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(9,3))