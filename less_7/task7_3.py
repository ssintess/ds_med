class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        sub = self.cell - other.cell
        if sub < 0:
            return 'err: less than zero'
        else:
            return sub

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        """��� �������������� ������� ���� __floordiv__,
      �� ��� ��� �� ������� ����� ������������ __truediv__,
      �� ��������� ��������� � ������� round 
      � ���������� ������� ���, 
      ��� ���������� ������ ������������ ���������
      (��������� � ������� �������)"""

        a = round(self.cell / other.cell)
        b = self.cell // other.cell
        if a > b:
            return a - 1
        else:
            return a

    def make_order(self, row):
        full_rows = self.cell // row  #���������� ����� �����
        last_row = self.cell % row  #������� � ��������� ����
        i = 0
        rows = ''

        while i < full_rows:
            k = 0
            while k < row:
                rows = rows + '*'
                k += 1
            rows = rows + '\n'
            i += 1

        b = 0
        while b < last_row:
            rows = rows + '*'
            b += 1
        return rows


cell_1 = Cell(18)
cell_2 = Cell(9)
print(cell_1.cell)
print(cell_2.cell)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_2.make_order(4))
