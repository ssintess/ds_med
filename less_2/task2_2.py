list = []
while True:
    a = input('Enter some items. Click empty "Enter" for continue: ')
    len_a = len(a)
    list.append(a)
    if len_a == 0:
        list.pop(-1)
        print(list)
        break

list2 = []
i = 0
count = len(list)
count2 = count
if count % 2 == 1:
    last_el = list[-1]
    count -= 1

while i < count:
    a = list[i]
    b = list[i + 1]
    a, b = b, a
    list2.append(a)
    list2.append(b)
    i += 2

if count2 % 2 == 0:
    print(list2)
else:
    list2.append(last_el)
    print(list2)