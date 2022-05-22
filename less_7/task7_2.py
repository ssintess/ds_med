from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cons(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def cons(self):
        cons_coat = self.v / 6.5 + 0.5
        return round(cons_coat, 2)


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cons(self):
        cons_suit = 2 * self.h + 0.3
        return round(cons_suit, 2)


coat = Coat(10)

suit = Suit(5)

print(coat.cons)
print(suit.cons)
print(f'{coat.cons + suit.cons}')
