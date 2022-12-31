#https://cs50.harvard.edu/python/2022/psets/0/einstein/

def main():
    x = int(input("m: "))
    print("E:", einstein(x))
    #E = mc2
    #E  represents energy (measured in Joules),
    # m represents mass (measured in kilograms),
    # c represents the speed of light (measured approximately as 300000000 meters per second),


def einstein(n):
    c = 300000000
    #return (n * c * c)
    #return (n * pow(c, 2))
    return (n * c**2)

main()
