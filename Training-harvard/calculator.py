# FIRST DRAFT
#    x = input("What's x? ")
#y = input("What's y? ")
## str x = input("What's x? ") -> z = x + y : ex 10 + 2 => then concatenate str = 102
## solution -> add function for int  z = x + y => z = int(x) + int(y)
#z = int(x) + int(y)
#print(z)

# SECOND DRAFT : there is no need of variable z -> nest function
#x = int(input("What's x? "))
#y = int(input("What's y? "))
#print(x+y)
# corect but TOO MUCH: a little too complicated for catchimg up
# print(int(input("What's x? "))+int(input("What's y? ")))

# to support float and round up to nearest int
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x+y)
# print(z)

# not very productive: but: 999 + 1 => 1,000
print(f"{z:,}")

# divdide
#z = x / y
# numbers 4.4 and 2
z = round(x / y, 2)
#=> result 2.2
print("divizion:", z)
#=> result 2.20
print(f"{z:.2f}")
