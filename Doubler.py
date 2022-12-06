def Pull():
    x = input("What number are we doubling?")
    if x.isdigit:
        x = int(x)
    else:
        print("Must be a digit.")

    return x


def Doubler():
    while x < 4000:
        x = x * 2
        print(f"doubled is {x}")
    else:
        print(f"We'll land on {x}")

    return x


def Main():
    Doubler(Pull())


Main()
