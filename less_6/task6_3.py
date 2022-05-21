class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(
            f'Full name: {self.name} {self.surname}\nPosition: {self.position}'
        )

    def get_total_income(self):
        print(f'Total income: {self._income["wage"] + self._income["bonus"]}$')


p = Position("Mike", "Fox", "manager", 1000, 500)
p.get_full_name()
p.get_total_income()