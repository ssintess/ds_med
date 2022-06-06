my_f = open("task5_3.txt", "r")

i = 0
all_s = 0

print('The salary less than 20k:')
for line in my_f:
    i += 1
    spl_w = line.split()
    sal = float(spl_w[1])
    all_s = all_s + sal
    if sal < 20000:
        print(f'-- {spl_w[0]} ({sal})')

aver_sal = all_s / i
print(f'average salary is: {round(aver_sal, 2)}')

my_f.close()
