from itertools import count
from itertools import cycle


#the first

for el in count(3):
    if el == 10:
        break
    else:
        print(el)

      
#the second
      
list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
stop_char = int(input("Enter count of iterations: "))
i = 0

for el in cycle(list):
    if i == stop_char:
        break
    else:
        print(el)
        i += 1