class Road:
    def calc(self, length, width):
        self._length = length
        self._width = width
        print(f'For a road with a length of {self._length} m and a width {self._width} m, {self._length * self._width * 0.025 * 0.05} tons of asphalt are needed')


r = Road()
r.calc(5000, 20)
