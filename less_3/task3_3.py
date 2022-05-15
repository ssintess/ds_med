num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
num_3 = int(input('Enter the third number: '))


def my_func(arg_1, arg_2, arg_3):
    list = [arg_1, arg_2, arg_3]
    min_num = min(list)
    list.remove(min_num)
    return sum(list)


print(my_func(num_1, num_2, num_3))