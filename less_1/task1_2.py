sec = int(input("seconds: "))
h = sec // 3600
pre_m = sec % 3600
m = pre_m // 60
s = pre_m % 60
if h < 10:
    h = f"0{h}"
if m < 10:
    m = f"0{m}"
if s < 10:
    s = f"0{s}"
print(f"{h}:{m}:{s}")