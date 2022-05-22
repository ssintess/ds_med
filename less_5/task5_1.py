my_f = open("task5_1.txt", "w")

str = ""

while True:
    ant = input('Enter some items. Click empty "Enter" for exit: ')
    len_a = len(ant)
    if len_a > 0:
        str = str + ant + "\n"
    else:
        my_f.write(str)
        print('All data is written to "task5_1.txt"')
        break

my_f.close()
