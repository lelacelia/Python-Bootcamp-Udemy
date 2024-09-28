# Day 10: Create a simple calculator

### Goal: practice using function with output and multiple functions

Demo: Link (https://appbrewery.github.io/python-day10-demo/)

*One limitation with the code below is I did not include situation when the inputs entered are not numbers*

```python
from art import logo

# TODO 1: Write out all 4 functions - add, subtract, multiply and divide.
''' Add special case: n2 = 0 --> python has issue with dividing by zero
if n2 == 0 -> result = infinity
and because n1 will be the result of the immediately preceeding calculation
and doing whatever with infinity still result in infinity so, 
if n1 = infinity as a result of a prior calculation
then result will always be infinity
'''

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    return "Infinity"

def infinity_operation(n1,n2, operation):
    if operation == "*" or operation == "/":
        if n2 == 0:
            if operation == "*":
                return 0
        elif n2 < 0:
            if n1 == "Infinity":
                return f"-{n1}"
            else:
                return n1[0].remove() #to remove the - sign
        else:
            return n1

restart = True
continue_calculating = "n"
result = 0.0

while restart == True:
    if continue_calculating == "n":
        print(logo)
        a = float(input("What's the first number?: "))
    else:
        a = result

    print("+\n-\n*\n/")

    operate = input("Pick an operation: ")

    b = float(input("What's the next number?: "))

    # TODO 2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
    operation_dictionary = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide
    }

    if operate in operation_dictionary:
        if result != "Infinity":
            result = operation_dictionary[operate](a,b)
        else:
            result = infinity_operation(a,b,operate)
    else:
        operate = "undefined"

    print(f"{a} {operate} {b} = {result}")

    continue_calculating = input(f"""Type 'y' to continue calculating with {result},
    or type 'n' to start a new calculation: """)

```
