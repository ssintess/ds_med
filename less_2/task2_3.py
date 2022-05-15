list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"]
num_m = int(input('Enter number of month 1-12: '))
if num_m < 1 or num_m > 12:
    print('Incorrect number of month')
else:
    print(list[num_m - 1])