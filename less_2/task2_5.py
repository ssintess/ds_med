list = [7, 5, 3, 3, 2]
cur_num = int(input('Enter your number: '))
i = 0
a = len(list)
last_num = list[-1]
if cur_num <= last_num:
    list.append(cur_num)
else:
    while i < a:
        b = list[i]
        if cur_num > b:
            list.insert(i, cur_num)
            break
        i += 1
print(list)



