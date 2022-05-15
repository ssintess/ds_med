my_f_init = open("task5_4_init.txt", "r")
my_f_new = open("task5_4_new.txt", "w")

dict_ru = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}

for line in my_f_init:
    spl_w = line.split()
    numb = spl_w[2]
    my_f_new.write(f'{dict_ru[numb]} - {numb}\n')

print('All data is written to "task5_4_new.txt"')
my_f_init.close()
my_f_new.close()
