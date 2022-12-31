# parameterize -> to - ex say hello to -> def hello(to)
# can set default values for parameter (to="world")

def main():
    name = input("What is your name? ")
    # use the value of parameter -> use name as argument
    hello(name)
    #hello()
#def hello(to="world"):


def hello(to="world"):
    print("Hello,", to)
    #print("Hello,", name)


main()

