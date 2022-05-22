import time


class TrafficLight:
    def running(self):
        self.__color = 'red'
        print(self.__color, end='\r')
        time.sleep(7)
        print('        ', end='\r')
        self.__color = 'yellow'
        print(self.__color, end='\r')
        time.sleep(2)
        print('        ', end='\r')
        self.__color = 'green'
        print(self.__color, end='\r')
        time.sleep(5)
        print('        ', end='\r')


tl = TrafficLight()
while True:
    tl.running()
