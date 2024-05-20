import sys

number = input("Enter an integer: ")
try:
    int(number)
except ValueError:
    print("That's not an integer!")
    sys.exit(1)

floatingPoint = input("Enter a floating-point value: ")
try:
    float(number)
except ValueError:
    print("That's not a floating point value!")
    sys.exit(1)

string = input("Enter a string value: ")
try:
    value = eval(string)
    if not isinstance(value, str):
        print("That's not a string value!")
        sys.exit(1)
except ValueError:
    print("That's not a string value!")
    sys.exit(1)
