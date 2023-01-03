def main():
    x = int(input("Enter a number: "))
    if is_even(x): #put argument x - defined in function below
        print("Even")
    else:
        print("Odd")


def is_even(n):
    #if n % 2 == 0:
    #    return True
    ## only T or F
    #else:
    #    return False
    #all 4 libes above can be substituite with:
    #return True if n % 2 == 0 else False
    #more simple
    return n % 2 == 0
main()
