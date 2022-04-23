gain = int(input("Enter your gain: "))
exp = int(input("Enter your expense: "))
profit = gain - exp
if profit <= 0:
    print("Absence profit")
elif profit > 0:
    rent = profit / gain * 100
    print(f"The company is at a profit. Rentability is {rent}% ")
    empl = int(input("Enter the number of employees: "))
    profit_empl = profit / empl
    print(f"Profit per employee is {profit_empl} ")