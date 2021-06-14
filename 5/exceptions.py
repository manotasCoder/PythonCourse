import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("we need a number to operate")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("Division by zero is not supported in this app")
    sys.exit(1)



print(f"{x} / {y} is {result}")