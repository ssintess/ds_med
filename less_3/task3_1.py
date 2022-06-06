num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))


def my_func(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError as err:
        return err


print(my_func(num_1, num_2))