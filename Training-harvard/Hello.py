# Ask user for their name
import sys

name = input("What is your name? ")
# Say hello to user
# first argument - hello and second argument variable
print("Hello, ", name)
# one argument - hello + variable  - concatenation
print("Hello, " + name)

# syntax = * any nr of objects
# ,
# sep=''
# end='\n' - new line but if print("Hello, " +  end='') - skips end of line
# print(*object, sep='', end='\n', file=sys.stdout, flush=False)

# Paramaters - positional params
# end - for line ending ; sep - sepatators
print("Hello, ", end="")
print(name)
# print in same line - ignores end of frase at first print
# \ excape character

# f format string - special string + variabile cand add in "" but use {} and before line add f
print(f"Hello, {name}")

# remove white space from str
print("line 28")
name = name.strip()
# Capitalize user name's first letter e.g. Tatiana gavrila => capitalize() function
name = name.capitalize()
# Capitalize user name's every first letter from each word e.g. Tatiana Gavrila => title() function
name = name.title()

#can use more than one function - can combine
name = name.strip().title()

#better and easy to read:
name = input("What is your name? ").strip().title()
print(f"Hello, {name}")