my_f = open("task5_6.txt", "r")

my_dict = {}
for line in my_f:
    spl_w = line.split()
    sum_n = 0
    for w in spl_w:
        num = ''
        for char in w:
            try:
                int(char)
                num = num + char
            except ValueError:
                break
        if num.isdigit() is True:
            num = int(num)
            sum_n = sum_n + num
        else:
            continue

    my_dict[spl_w[0]] = sum_n
print(dict)

my_f.close()
