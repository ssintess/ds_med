num = int(input("Enter number: "))


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f
        print(f"factorial {i} is {f}")


for el in fact(num):
    print(el)