n = int(input("Enter number: "))
cur_max = 0
while n > 0:
    i = n % 10
    if i > cur_max:
        cur_max = i
    n = n // 10
print(f"{cur_max}")