class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num

    def __floordiv__(self, other):
        return self.num // other.num

    def make_order(self, cell):
        a = self.num // cell
        b = self.num % cell
        return '\n'.join(['*' * cell for i in range(self.num // cell)]) + '\n' + '*' * (self.num % cell)

cell = Cell(234)
cell1 = Cell(23)

print(cell / cell1)
print(cell.make_order(10))

