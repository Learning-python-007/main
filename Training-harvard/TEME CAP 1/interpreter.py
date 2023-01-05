# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression
# and then calculates and outputs the result as a floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space
# between y and z, wherein:
#
# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /,
# then z will not be 0.
#
# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an
# interpreter for math!

def interpreter():
    # Prompt the user for input
    user_input = input("Enter an arithmetic expression: ")

    # Split the input into three parts: x, y, and z
    x, y, z = user_input.split()

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Initialize the result to 0
    result = 0

    # Use a dictionary to map y to the corresponding operation
    operations = {
        "+": x + z,
        "-": x - z,
        "*": x * z,
        "/": x / z
    }

    # Calculate the result
    result = operations[y]

    # Output the result, formatted to one decimal place
    print("Result: {:.1f}".format(result))

# Run the interpreter
interpreter()