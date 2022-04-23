a = int(input("Enter your start km: "))
b = int(input("Enter your expect km: "))
day = 1
c = 0
print(f"Day-{day}: {a} km")
while a < b:
    day+= 1
    a = a + a * 0.1
    print(f"Day-{day}: {a:0.2f} km")
print(f"The athlete will reach the goal of {b} km on the day ¹{day}")