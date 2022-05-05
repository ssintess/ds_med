def my_func():
    total_sum = 0
    while True:
        init_list = input(
            "Enter some numbers, separated by spaces: ")
        clear_list = init_list.split()
        for i in clear_list:
            if i == "q":
                return total_sum
            else:
                try:
                    total_sum += int(i)
                except ValueError:
                    print("'q' - exit")
        print(f"Total sum = {total_sum}")

print(my_func())