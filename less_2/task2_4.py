cust_str = input('Enter some words separated by spaces: ')
list_word = cust_str.split(' ')
count = len(list_word)
i = 0
while i < count:
    a = len(list_word[i])
    b = list_word[i]
    if a > 10:
        print(f'{i + 1}: {b[:10]}')
    else:
        print(f'{i + 1}: {b}')
    i += 1