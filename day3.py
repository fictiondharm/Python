# import math
# a = float(input("enter the side a :"))
# b = float(input("enter the side b :"))
# c = math.sqrt(pow(a, 2) + pow(b,2))
# print(f"the squareroot of {a}, and {b} is {c}")

print(" today we are buliding a simple  calculator")
operator = (input("enter the operator (+, - , * , /)"))
num1 = float(input(" enter the number 1 "))
num2 = float(input(" enter the number 2 "))

if operator == "" :
     print("select the opertor")
elif operator == "+" :
    result = num1 + num2 
    print(result)

elif operator == "-" :
     result = num1 - num2
     print(result)

elif operator == "*" :
     result = num1 * num2
     print(result)

elif operator == "/" : 
     result == num1 / num2 
     print(result)
else:
     print(f"the entered operator {operator} is invalid")