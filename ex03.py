# inputs

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

adding = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2

message = f"""

-----Calculator----------\n

Add : {num1} + {num2} = {adding}\n
Sub : {num1} - {num2} = {sub}\n
Mult: {num1} x {num2} = {multi}\n
Div : {num1} / {num2} = {div}\n
"""
print(message)