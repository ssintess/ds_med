gain = int(input("Enter your gain: "))
exp = int(input("Enter your expense: "))
result = gain - exp
if result == 0:
    print("Profit is zero")
elif result > 0:
    print("The company is at a profit")
elif result < 0:
    print("The company is at a loss")