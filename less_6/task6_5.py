class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start painting')


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'{self.title} is painting')


class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'{self.title} is painting')


class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'{self.title} is painting')


pen = Pen("Pen")
pen.draw()

pencil = Pencil("Pencil")
pencil.draw()

handle = Handle("Handle")
handle.draw()