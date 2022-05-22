#pls, pre-run 'task5_1.py'

my_f = open("task5_1.txt", "r")

i = 0
for line in my_f:
    i += 1
    spl_w = line.split()
    count_w = len(spl_w)
    print(f"count of words in the str: {count_w}")
print(f"all str: {i}")

my_f.close()
