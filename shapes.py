class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectarea = self.length * self.width
        return rectarea

    def perimeter(self):
        rectperimiter = 2 * self.length + 2 * self.width
        return rectperimiter


class square(rectangle):
    def __init__(self, length):
        super().__init__(length, length)


rect = rectangle(5, 10)
print('Area of rectangle - ', rect.area())

print('Perimeter of rectangle - ', rect.perimeter())

sqr = square(5)
print('Are of a square - ', sqr.area())




#
