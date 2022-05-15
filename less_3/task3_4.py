num_1 = float(input('Enter positive number: '))
num_2 = int(input('Enter integer negative number: '))


""" The first solution """


def my_func(x, y):
    res = x**y
    return round(res, 1)


""" The second solution """


def my_func2(x, y):
    i = 1
    z = abs(y)
    res_2 = x
    while i < z:
        res_2 = res_2 * x
        i += 1
    if y < 0:
        return round(1 / res_2, 1)
    else:
        return res_2


print(my_func(num_1, num_2))
print(my_func2(num_1, num_2))