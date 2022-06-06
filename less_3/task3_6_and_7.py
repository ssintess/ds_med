words = input('Enter some en-words: ')


def int_func(arg):
    list_init = arg.split()
    list_fin = []
    for i in list_init:
        for let in i:
            let = ord(let)
            if let > 96 and let < 123:
                continue
            else:
                return "Error: only en-words"
        a = i.title()
        list_fin.append(a)
    res = ' '.join(map(str, list_fin))
    return res


print(int_func(words))