#in a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts
# with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

#def starts_with_h(string):
#    if string[0] == "h":
#        return ("$20")

#x = input("Greeting: ")

#if x == "Hello":
#    print("$100")
#elif x == starts_with_h(x):
#    print("$20")
#else:
#    print("0")



def get_greeting_cost(greeting):
    greeting = greeting.lstrip()
    if greeting.startswith('Hello'):
        return "$0"
    elif greeting[0] == 'h' or greeting[0] == 'H':
        return "$20"
    else:
        return "$100"

greeting = input('Enter a greeting: ')
cost = get_greeting_cost(greeting)
print(cost)