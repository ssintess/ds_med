my_f = open("task5_5.txt", "w")

nums = input('Enter some numbers separated by spaces: ')
spl_n = nums.split()
sum_n = 0

for n in spl_n:
    n = int(n)
    sum_n = sum_n + n

sum_n = str(sum_n)
my_f.write(f'Set of numbers: {nums}\nSum of numbers: {sum_n}')

print('All data is written to "task5_5.txt"')

my_f.close()
