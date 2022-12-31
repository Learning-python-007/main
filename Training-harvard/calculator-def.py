def main():
    x = int(input("wthat is x? "))
    print("X square is", square(x))


def square(n):
    #return n * n * n
    return pow(n, 2)

main()