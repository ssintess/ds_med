init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [a for b, a in zip(init_list, init_list[1:]) if a > b]

print(new_list)