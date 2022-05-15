"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
данные о фирме: название, форма собственности, выручка, издержки.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].


"""

import json

my_f = open("task5_7.txt", "r")

tot_sum = 0
i = 0
my_list = []
dict_f = {}
dict_ap = {}

for line in my_f:
    item = line.split()
    profit = int(item[2]) - int(item[3])
    if profit < 0:
        print(f'No profit for {item[0]}, the loss: {profit}')
        dict_f[item[0]] = profit
    else:
        tot_sum = tot_sum + int(item[2])
        i += 1
        print(f'Profit for {item[0]}: {profit}')
        dict_f[item[0]] = profit

average_profit = tot_sum / i
print(f'\nAverage profit: {average_profit}\n')

dict_ap['average_profit'] = average_profit

my_list.append(dict_f)
my_list.append(dict_ap)

print(my_list)
with open("task5_7.json", "w") as write_json:
    json.dump(my_list, write_json)

print(f'The list saved to json-file "task5_7.json"')

my_f.close()


